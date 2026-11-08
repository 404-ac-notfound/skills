#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compose.py — Chinese calligraphy composition engine (集字成篇).

Composes vertical-column calligraphy artwork on a paper-toned canvas with
optional 白文 seal and colophon, in several classical formats
(hanging-scroll / banner / square / fan / album-leaf).

Glyphs come from per-character PNG overrides (--glyphs DIR/<char>.png, alpha
channel required) when available, otherwise from a discovered CJK font
(labelled as draft in the gallery registry).

Dependencies: Python 3.9+ stdlib + Pillow only.
"""

import argparse
import hashlib
import json
import math
import os
import random
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent

# --------------------------------------------------------------------------
# Style profiles
# --------------------------------------------------------------------------

PAPER = (245, 240, 228)          # #F5F0E4
SEAL_RED = (192, 58, 43)         # #C03A2B
SEAL_BORDER = (143, 42, 30)      # darker red
DRAFT_GREY = (138, 131, 120)     # #8A8378
FAN_GUIDE = (205, 195, 168)      # subtle fan-arc guide tone

# Font-search groups: substrings matched (case-insensitive) against font file
# basenames found in FONT_DIRS.  Order inside a group is priority order.
FONT_DIRS = [
    "/System/Library/Fonts",
    "/System/Library/Fonts/Supplemental",
    "/Library/Fonts",
    os.path.expanduser("~/Library/Fonts"),
]
FONT_GROUPS = {
    "xingkai": ["xingkai", "stxingkai", "行楷", "slidexiaxing",
                "bailufeiyunshouxieti"],
    "kai":     ["kaiti", "stkaiti", "楷體", "楷体", "楷", "zikutang"],
    "lishu":   ["lishu", "隸書", "隶书", "baoli"],
    "song":    ["songti", "stsong", "noto serif cjk", "source han serif"],
    "zhuanshu": ["zhuanshu", "篆書", "篆书", "zhuan"],
    "heiti":   ["stheiti", "heiti", "hiragino sans gb", "pingfang"],
    "anycjk":  ["arial unicode", "hiragino sans gb"],
}
# Fonts whose names collide with group substrings but are NOT that script.
FONT_EXCLUDE = ["notosanslisu", "kailasa"]


def _profile(prefer, variance, drift, ink, margin=1.0, rotate=None,
             spacing="loose"):
    return {
        "prefer": prefer,          # ordered font-group fallback chain
        "variance": variance,      # ± relative glyph-size variance
        "drift": drift,            # ± relative horizontal axis drift
        "ink": ink,
        "margin": margin,          # 留白 multiplier
        "rotate": rotate,          # (min_deg, max_deg) per-glyph rotation
        "spacing": spacing,        # "loose" (≥40% gap) or "tight" (≥25%)
    }


STYLE_PROFILES = {
    "KAI-YAN-01":  _profile(["kai", "song", "heiti", "anycjk"], 0.04, 0.02,
                            "#1A1815", margin=1.18, spacing="tight"),
    "KAI-MU-01":   _profile(["song", "kai", "heiti", "anycjk"], 0.02, 0.0,
                            "#26221C", spacing="tight"),
    "XING-MI-01":  _profile(["xingkai", "kai", "song", "anycjk"], 0.08, 0.03,
                            "#1A1815", rotate=(-1.0, 3.0)),   # mean lean +1°
    "XING-YUAN-01": _profile(["xingkai", "kai", "song", "anycjk"], 0.06, 0.025,
                             "#201D18"),
    "XING-YAN-01": _profile(["xingkai", "kai", "song", "anycjk"], 0.08, 0.03,
                            "#231F1A"),
    "CAO-HUANG-01": _profile(["xingkai", "kai", "song", "anycjk"], 0.08, 0.03,
                             "#1A1815"),
    "CAO-HUAI-01": _profile(["xingkai", "kai", "song", "anycjk"], 0.08, 0.03,
                            "#1A1815"),
    "LI-CAO-01":   _profile(["lishu", "kai", "song", "anycjk"], 0.03, 0.01,
                            "#1A1815", spacing="tight"),
    "ZHUAN-SG-01": _profile(["zhuanshu", "kai", "song", "anycjk"], 0.02, 0.0,
                            "#1A1815", spacing="tight"),
    "ZHUAN-SM-01": _profile(["zhuanshu", "kai", "song", "anycjk"], 0.02, 0.0,
                            "#1A1815", spacing="tight"),
    # Hybrids inherit the profile of their structure donor.
    "HYB-QZM-01":  dict(_profile(["zhuanshu", "kai", "song", "anycjk"], 0.02,
                                 0.0, "#1A1815", spacing="tight")),
    "HYB-MI-YAN-01": dict(_profile(["xingkai", "kai", "song", "anycjk"], 0.08,
                                   0.03, "#1A1815", rotate=(-1.0, 3.0))),
    "HYB-KAI-LI-01": dict(_profile(["song", "kai", "heiti", "anycjk"], 0.02,
                                   0.0, "#26221C", spacing="tight")),
    "HYB-CAO-KAI-01": dict(_profile(["kai", "song", "heiti", "anycjk"], 0.04,
                                    0.02, "#1A1815", margin=1.18,
                                    spacing="tight")),
}

FORMATS = {
    # name: (w:h ratio as h/w multiplier, default width)
    "hanging-scroll": (2.4, 1200),
    "banner": (1 / 2.6, 2400),
    "square": (1.0, 1600),
    "fan": (0.5, 2000),
    "album-leaf": (0.75, 1600),
}


# --------------------------------------------------------------------------
# Font discovery
# --------------------------------------------------------------------------

class FontChoice(object):
    def __init__(self, path, index, family, style):
        self.path = path
        self.index = index
        self.family = family
        self.style = style
        self._cache = {}

    def at(self, size):
        size = max(8, int(size))
        if size not in self._cache:
            self._cache[size] = ImageFont.truetype(self.path, size,
                                                   index=self.index)
        return self._cache[size]

    @property
    def label(self):
        return self.family + ((" " + self.style)
                              if self.style and self.style != "Regular" else "")


def _list_font_files():
    files = []
    for d in FONT_DIRS:
        if not os.path.isdir(d):
            continue
        for root, _dirs, names in os.walk(d):
            for n in names:
                if n.lower().endswith((".ttf", ".ttc", ".otf")):
                    files.append(os.path.join(root, n))
    return files


def _probe_font(path, index, chars):
    """Return fraction of `chars` this font (path,index) renders genuinely.

    A glyph counts as missing when it renders empty OR when its bitmap is
    identical to a bitmap shared by >=3 distinct probe characters (the classic
    .notdef-box signature).
    """
    try:
        font = ImageFont.truetype(path, 48, index=index)
    except Exception:
        return 0.0, None

    def render(ch):
        im = Image.new("L", (96, 96), 0)
        ImageDraw.Draw(im).text((48, 48), ch, font=font, fill=255,
                                anchor="mm")
        return im

    # Reference .notdef bitmaps: characters essentially no font contains.
    # Any probe char rendering the same bitmap is silently missing.
    refs = set()
    for ref in ("\uE000", "\uF8FF", "\U0002A6A5"):
        im = render(ref)
        if im.getbbox():
            refs.add(im.tobytes())

    bitmaps = {}
    empty = set()
    for ch in chars:
        im = render(ch)
        if not im.getbbox():
            empty.add(ch)
            continue
        data = im.tobytes()
        if data in refs:
            empty.add(ch)
            continue
        bitmaps.setdefault(data, []).append(ch)
    notdef = set()
    for _data, group in bitmaps.items():
        if len(group) >= 3:
            notdef.update(group)
    covered = [c for c in chars if c not in empty and c not in notdef]
    frac = len(covered) / max(1, len(chars))
    try:
        fam, sty = font.getname()
    except Exception:
        fam, sty = os.path.basename(path), ""
    return frac, (fam, sty)


def find_font(prefer_groups, probe_chars, weight_pref_bold=False,
              verbose=False):
    """Find the first font in the group fallback chain rendering ALL probe
    characters.  Returns FontChoice or None."""
    files = _list_font_files()
    for group in prefer_groups:
        subs = FONT_GROUPS.get(group, [])
        cands = []
        for f in files:
            base = os.path.basename(f).lower()
            if any(x in base for x in FONT_EXCLUDE):
                continue
            if any(s.lower() in base for s in subs):
                cands.append(f)
        variants = []
        for f in sorted(cands):
            for idx in range(4):
                frac, name = _probe_font(f, idx, probe_chars)
                if name is None:
                    break
                if frac >= 1.0:
                    variants.append((f, idx, name[0], name[1]))
        if variants:
            if weight_pref_bold:
                variants.sort(
                    key=lambda v: 0 if any(
                        w in (v[3] or "").lower()
                        for w in ("bold", "black", "heavy")) else 1)
            f, idx, fam, sty = variants[0]
            if verbose:
                print("[font] group=%s -> %s (index %d) %s %s"
                      % (group, os.path.basename(f), idx, fam, sty),
                      file=sys.stderr)
            return FontChoice(f, idx, fam, sty)
    return None


# --------------------------------------------------------------------------
# Paper
# --------------------------------------------------------------------------

def make_paper(w, h, rng):
    img = Image.new("RGB", (w, h), PAPER)
    # Low-amplitude per-pixel noise blended at <=4% opacity.
    noise = Image.effect_noise((w, h), 22).convert("RGB")
    img = Image.blend(img, noise, 0.035)
    # Faint fibre streaks.
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for _ in range(max(12, w * h // 90000)):
        x = rng.uniform(0, w)
        y = rng.uniform(0, h)
        ln = rng.uniform(w * 0.01, w * 0.06)
        ang = rng.uniform(-0.12, 0.12)
        tone = rng.choice([(210, 200, 175, 10), (255, 252, 244, 10)])
        d.line([x, y, x + ln * math.cos(ang), y + ln * math.sin(ang)],
               fill=tone, width=1)
    img = Image.alpha_composite(img.convert("RGBA"), overlay)
    return img


# --------------------------------------------------------------------------
# Glyph rendering
# --------------------------------------------------------------------------

def paste_font_glyph(canvas, ch, font_choice, ink, cx, cy, size, angle=0.0):
    """Render one glyph centred at (cx, cy); tile is 2x glyph size so small
    rotations never clip."""
    gsize = max(8, int(size))
    tile_side = gsize * 2
    tile = Image.new("RGBA", (tile_side, tile_side), (0, 0, 0, 0))
    d = ImageDraw.Draw(tile)
    d.text((tile_side // 2, tile_side // 2), ch,
           font=font_choice.at(gsize), fill=ink + (255,), anchor="mm")
    if angle:
        tile = tile.rotate(angle, resample=Image.BICUBIC,
                           center=(tile_side // 2, tile_side // 2))
    canvas.paste(tile, (int(cx - tile_side // 2), int(cy - tile_side // 2)),
                 tile)


def paste_harvested_glyph(canvas, img, cx, cy, cell):
    """Scale a harvested PNG (alpha) into the grid cell, preserving aspect."""
    w, h = img.size
    scale = min(cell * 0.96 / w, cell * 0.96 / h)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    g = img.resize((nw, nh), Image.LANCZOS)
    canvas.paste(g, (int(cx - nw / 2), int(cy - nh / 2)), g)


# --------------------------------------------------------------------------
# Seal (白文)
# --------------------------------------------------------------------------

def render_seal(chars, side, kai_font, seed):
    side = int(side)
    img = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    radius = max(3, side // 12)
    d.rounded_rectangle([0, 0, side - 1, side - 1], radius=radius,
                        fill=SEAL_RED + (255,),
                        outline=SEAL_BORDER + (255,),
                        width=max(2, side // 80))
    cell = side / 2.0
    fsize = cell * 0.80
    if len(chars) == 4:
        # Traditional 回讀 order: top-right, bottom-right, top-left, bottom-left.
        pos = [(0.75, 0.25), (0.75, 0.75), (0.25, 0.25), (0.25, 0.75)]
    else:  # 2 chars: single column on the right, top then bottom.
        pos = [(0.72, 0.25), (0.72, 0.75)]
    for ch, (fx, fy) in zip(chars, pos):
        d.text((side * fx, side * fy), ch, font=kai_font.at(fsize),
               fill=PAPER + (255,), anchor="mm")
    # Carved feel: erode the alpha mask 1px, then nibble the border with
    # seeded random bites.
    alpha = img.split()[3].filter(ImageFilter.MinFilter(3))
    img.putalpha(alpha)
    rng = random.Random(seed)
    bite = Image.new("L", (side, side), 0)
    bd = ImageDraw.Draw(bite)
    for _ in range(max(6, side // 6)):
        ex = rng.choice([rng.uniform(0, side * 0.06),
                         rng.uniform(side * 0.94, side)])
        ey = rng.uniform(0, side)
        r = rng.uniform(1, max(2, side * 0.02))
        bd.ellipse([ex - r, ey - r, ex + r, ey + r], fill=200)
        bd.ellipse([ey - r, ex - r, ey + r, ex + r], fill=200)
    img.putalpha(ImageChops.subtract(img.split()[3], bite))
    return img


# --------------------------------------------------------------------------
# Layout helpers
# --------------------------------------------------------------------------

def distribute_columns(n, cols):
    """Balanced char counts per column; last column carries >=2 chars."""
    base, rem = divmod(n, cols)
    counts = [base + (1 if i < rem else 0) for i in range(cols)]
    if cols > 1 and counts[-1] == 1:
        counts[-2] -= 1          # move one char from the previous column
        counts[-1] += 1
        counts = [c for c in counts if c > 0]
    return counts


def choose_columns(n, avail_w, avail_h, gap_ratio, pitch_y=1.06):
    """Pick the column count maximising character size."""
    best = None
    for cols in range(1, n + 1):
        counts = distribute_columns(n, cols)
        per_col = max(counts)
        cs_w = avail_w / (cols + (cols - 1) * gap_ratio)
        cs_h = avail_h / (per_col * pitch_y)
        cs = min(cs_w, cs_h)
        if best is None or cs > best[0] + 0.5:
            best = (cs, cols, counts)
    return best  # (char_size, cols, counts)


def gap_ratio_for(profile):
    return 0.25 if profile["spacing"] == "tight" else 0.40


# --------------------------------------------------------------------------
# Composition
# --------------------------------------------------------------------------

def compose_vertical_columns(canvas, text, counts, char_size, right_edge,
                             top_margin, profile, font_choice, glyphs,
                             glyph_src, rng):
    """Lay out vertical columns right->left, top->bottom."""
    gr = gap_ratio_for(profile)
    pitch_x = char_size * (1 + gr)
    pitch_y = char_size * 1.06
    idx = 0
    last_col_bottom = top_margin
    last_col_left = right_edge
    for ci, cnt in enumerate(counts):
        col_right = right_edge - ci * pitch_x
        col_cx = col_right - char_size / 2
        for j in range(cnt):
            ch = text[idx]
            idx += 1
            scale = 1 + rng.uniform(-profile["variance"],
                                    profile["variance"])
            dx = rng.uniform(-profile["drift"], profile["drift"]) * char_size
            cy = top_margin + j * pitch_y + char_size / 2
            if ch in glyphs:
                paste_harvested_glyph(canvas, glyphs[ch][0], col_cx + dx, cy,
                                      char_size)
                glyph_src[ch] = "harvested:" + glyphs[ch][1]
            else:
                angle = (rng.uniform(*profile["rotate"])
                         if profile["rotate"] else 0.0)
                paste_font_glyph(canvas, ch, font_choice, profile["ink"],
                                 col_cx + dx, cy, char_size * scale, angle)
                glyph_src.setdefault(ch, "font:" + font_choice.label)
            last_col_bottom = max(last_col_bottom, cy + char_size / 2)
        last_col_left = col_right - char_size
    return last_col_left, last_col_bottom


def compose_fan(canvas, text, avail, profile, font_choice, glyphs,
                glyph_src, rng):
    """Fan format.

    APPROXIMATION: a true 扇面 wraps columns along the fan arc with
    alternating long/short columns.  Here columns stay straight (two-tier:
    alternating long/short) and each column's TOP follows the inner fan arc
    (a circular arc from the fan apex), which reads convincingly while
    avoiding per-glyph arc-warping.
    """
    x0, y0, avail_w, avail_h = avail
    W, H = canvas.size
    n = len(text)
    gr = gap_ratio_for(profile)

    # Fan guide: apex below the paper centre, two arcs + radial ribs.
    apex = (W / 2.0, H - y0 * 0.8)
    r_out = avail_h * 1.28
    r_in = r_out * 0.52
    guide = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(guide)
    for r in (r_out, r_in):
        gd.arc([apex[0] - r, apex[1] - r, apex[0] + r, apex[1] + r],
               start=200, end=340, fill=FAN_GUIDE + (110,), width=2)
    for k in range(8):
        a = math.radians(200 + k * 20)
        gd.line([apex[0] + r_in * math.cos(a), apex[1] + r_in * math.sin(a),
                 apex[0] + r_out * math.cos(a), apex[1] + r_out * math.sin(a)],
                fill=FAN_GUIDE + (70,), width=1)
    canvas.alpha_composite(guide)

    # Choose cols / long-count L / short delta d maximising char size.
    # Column tops follow a parabolic stand-in for the fan's inner arc, so
    # the usable height is discounted by the arc amplitude (30%).
    arc_amp = avail_h * 0.30
    best = None
    for cols in range(1, n + 1):
        for L in range(1, n + 1):
            for d in range(1, L):
                counts = [L if i % 2 == 0 else L - d for i in range(cols)]
                if sum(counts) != n:
                    continue
                if cols > 1 and counts[-1] < 2:
                    continue
                cs = min(avail_w / (cols + (cols - 1) * gr),
                         (avail_h - arc_amp) / (L * 1.06 + 0.9))
                if best is None or cs > best[0] + 0.5:
                    best = (cs, cols, counts)
    if best is None:                       # fallback: single column
        best = (min(avail_w, avail_h / (n * 1.06)), 1, [n])
    char_size, _cols, counts = best

    pitch_x = char_size * (1 + gr)
    pitch_y = char_size * 1.06
    right_edge = x0 + avail_w
    center_x = x0 + avail_w / 2.0
    bottom_limit = y0 + avail_h
    idx = 0
    last_col_bottom, last_col_left = y0, right_edge
    for ci, cnt in enumerate(counts):
        col_right = right_edge - ci * pitch_x
        col_cx = col_right - char_size / 2
        # Column top follows the (parabolic) inner arc of the fan: higher in
        # the middle, lower towards the edges.
        t = (col_cx - center_x) / max(1.0, avail_w / 2.0)
        top = y0 + arc_amp * t * t
        # Keep the whole column on the paper.
        top = min(top, bottom_limit - cnt * pitch_y)
        top = max(y0, top)
        for j in range(cnt):
            ch = text[idx]
            idx += 1
            scale = 1 + rng.uniform(-profile["variance"],
                                    profile["variance"])
            dx = rng.uniform(-profile["drift"], profile["drift"]) * char_size
            cy = top + j * pitch_y + char_size / 2
            if ch in glyphs:
                paste_harvested_glyph(canvas, glyphs[ch][0], col_cx + dx, cy,
                                      char_size)
                glyph_src[ch] = "harvested:" + glyphs[ch][1]
            else:
                angle = (rng.uniform(*profile["rotate"])
                         if profile["rotate"] else 0.0)
                paste_font_glyph(canvas, ch, font_choice, profile["ink"],
                                 col_cx + dx, cy, char_size * scale, angle)
                glyph_src.setdefault(ch, "font:" + font_choice.label)
            last_col_bottom = max(last_col_bottom, cy + char_size / 2)
        last_col_left = col_right - char_size
    return char_size, last_col_left, last_col_bottom


def compose_banner_row(canvas, text, avail, profile, font_choice, glyphs,
                       glyph_src, rng):
    """Banner with <=4 chars: ONE horizontal row, read right->left."""
    x0, y0, avail_w, avail_h = avail
    n = len(text)
    pitch = 1.15
    char_size = min(avail_h * 0.62, avail_w / (n * pitch))
    cy = y0 + avail_h / 2
    right_edge = x0 + avail_w
    for i, ch in enumerate(text):
        cx = right_edge - char_size / 2 - i * char_size * pitch
        scale = 1 + rng.uniform(-profile["variance"], profile["variance"])
        if ch in glyphs:
            paste_harvested_glyph(canvas, glyphs[ch][0], cx, cy, char_size)
            glyph_src[ch] = "harvested:" + glyphs[ch][1]
        else:
            paste_font_glyph(canvas, ch, font_choice, profile["ink"],
                             cx, cy, char_size * scale)
            glyph_src.setdefault(ch, "font:" + font_choice.label)
    row_bottom = cy + char_size / 2
    row_left = right_edge - n * char_size * pitch
    return char_size, row_left, row_bottom


# --------------------------------------------------------------------------
# Registry
# --------------------------------------------------------------------------

def update_registry(out_dir, entry):
    path = os.path.join(out_dir, "index.json")
    works = []
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                works = json.load(f)
            if not isinstance(works, list):
                works = []
        except Exception:
            works = []
    works = [w for w in works if w.get("file") != entry["file"]]
    works.append(entry)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(works, f, ensure_ascii=False, indent=2)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Compose Chinese calligraphy artwork (集字成篇).")
    p.add_argument("--text", required=True)
    p.add_argument("--style", required=True, choices=sorted(STYLE_PROFILES))
    p.add_argument("--format", default="hanging-scroll",
                   choices=sorted(FORMATS))
    p.add_argument("--seal", default=None)
    p.add_argument("--colophon", default=None)
    p.add_argument("--glyphs", default=None,
                   help="directory of <char>.png harvested glyph overrides")
    p.add_argument("--out", default=str(SCRIPT_DIR / "gallery"))
    p.add_argument("--name", default=None)
    p.add_argument("--width", type=int, default=None)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--draft", action="store_true")
    args = p.parse_args(argv)

    text = "".join(args.text.split())
    if not text:
        p.error("--text is empty after stripping whitespace")
    profile = dict(STYLE_PROFILES[args.style])
    profile["ink"] = hex_to_rgb(profile["ink"])

    seal_chars = None
    if args.seal:
        seal_chars = "".join(args.seal.split())
        if len(seal_chars) not in (2, 4):
            p.error("--seal must be 2 or 4 characters (got %d)"
                    % len(seal_chars))
    colophon = "".join(args.colophon.split()) if args.colophon else None

    seed = args.seed
    if seed is None:
        seed = int(hashlib.sha256(
            (text + "|" + args.style).encode("utf-8")).hexdigest()[:8], 16)
    rng = random.Random(seed)

    # Canvas geometry.
    hw, def_w = FORMATS[args.format]
    W = args.width or def_w
    H = int(round(W * hw))
    base_margin = max(0.12 * min(W, H), 60) * profile["margin"]
    if args.format == "hanging-scroll":
        head, foot = base_margin * 1.5, base_margin
    else:
        head = foot = base_margin
    left_m = right_m = base_margin

    # Fonts: probe with every character we must render.
    probe = sorted(set(text + (seal_chars or "") + (colophon or "")))
    bold_pref = args.style in ("KAI-YAN-01", "HYB-CAO-KAI-01")
    main_font = find_font(profile["prefer"], probe, weight_pref_bold=bold_pref,
                          verbose=True)
    if main_font is None:
        sys.exit(
            "ERROR: no usable CJK font found.\nSearched dirs:\n  "
            + "\n  ".join(FONT_DIRS)
            + "\nInstall a CJK font (Kaiti/Xingkai/Songti) and retry.")
    kai_font = find_font(["kai", "song", "heiti", "anycjk"], probe,
                         verbose=True) or main_font

    # Harvested glyph overrides.
    glyphs = {}
    if args.glyphs:
        gdir = Path(args.glyphs)
        for ch in set(text):
            fp = gdir / (ch + ".png")
            if fp.is_file():
                im = Image.open(str(fp)).convert("RGBA")
                glyphs[ch] = (im, fp.name)

    canvas = make_paper(W, H, rng)

    # Two-pass layout: estimate char size, reserve colophon strip, recompute.
    avail_w0 = W - left_m - right_m
    avail_h = H - head - foot
    gr = gap_ratio_for(profile)
    colophon_reserve = 0.0
    if colophon and args.format != "fan":
        est = min(avail_h / (math.ceil(len(text) / 2) * 1.06),
                  avail_w0 / 2)
        colophon_reserve = est * 0.55 * 1.7
    avail_w = avail_w0 - colophon_reserve

    glyph_src = {}
    n = len(text)
    if args.format == "banner" and n <= 4:
        char_size, last_left, last_bottom = compose_banner_row(
            canvas, text, (left_m + colophon_reserve, head, avail_w, avail_h),
            profile, main_font, glyphs, glyph_src, rng)
    elif args.format == "fan":
        # Reserve lower band for the seal when one is requested.
        fan_h = avail_h * (0.78 if seal_chars else 1.0)
        char_size, last_left, last_bottom = compose_fan(
            canvas, text, (left_m, head, avail_w0, fan_h),
            profile, main_font, glyphs, glyph_src, rng)
    else:
        _cs, _cols, counts = choose_columns(n, avail_w, avail_h, gr)
        if seal_chars:
            # Reserve vertical room for the seal (side 0.6 + clearance 0.5
            # of a char) so it never overlaps the last glyph.
            avail_h2 = max(avail_h * 0.5, avail_h - _cs * 1.25)
            _cs, _cols, counts = choose_columns(n, avail_w, avail_h2, gr)
        right_edge = W - right_m
        char_size = _cs
        last_left, last_bottom = compose_vertical_columns(
            canvas, text, counts, char_size, right_edge, head,
            profile, main_font, glyphs, glyph_src, rng)

    # Colophon: vertical, 55% of main char size, kai font, left of the final
    # text column.
    if colophon:
        cs = char_size * 0.55
        pitch = cs * 1.18
        if args.format == "banner" and n <= 4:
            col_right = left_m + colophon_reserve + cs
        else:
            col_right = last_left - char_size * 0.45
        per = max(1, int((H - head - foot * 0.5) // pitch))
        x = col_right - cs / 2
        y_start = head
        for k, ch in enumerate(colophon):
            col = k // per
            row = k % per
            cx = x - col * pitch * 1.4
            cy = y_start + row * pitch + cs / 2
            paste_font_glyph(canvas, ch, kai_font, profile["ink"], cx, cy, cs)

    # Seal: below-left of the signature/last column, clearance >= half char.
    if seal_chars:
        side = char_size * 0.6
        seal_img = render_seal(seal_chars, side, kai_font, seed ^ 0x5EA1)
        if args.format == "banner" and n <= 4:
            sx = left_m + colophon_reserve
            sy = last_bottom + char_size * 0.5
        else:
            sx = last_left + (char_size - side) / 2 - char_size * 0.1
            sy = last_bottom + char_size * 0.5
        # Keep the seal on the paper.
        sx = max(left_m * 0.5, min(sx, W - right_m * 0.5 - side))
        sy = min(sy, H - foot * 0.35 - side)
        canvas.paste(seal_img, (int(sx), int(sy)), seal_img)

    # Draft footer.
    harvested_used = bool(set(text) & set(glyphs.keys()))
    draft = args.draft or not harvested_used
    if draft:
        fsize = max(12, W // 60)
        d = ImageDraw.Draw(canvas)
        d.text((max(20, left_m * 0.5), H - max(30, foot * 0.4)),
               "DRAFT — font glyphs pending harvested masters · 集字草稿",
               font=kai_font.at(fsize), fill=DRAFT_GREY + (255,), anchor="ls")

    # Save + registry.
    os.makedirs(args.out, exist_ok=True)
    if not args.name:
        h = hashlib.sha1((text + args.style).encode("utf-8")).hexdigest()[:6]
        name = "%s-%s-%s" % (args.style.lower(),
                             datetime.now().strftime("%Y%m%d"), h)
    else:
        name = args.name
    fname = name + ".png"
    fpath = os.path.join(args.out, fname)
    canvas.convert("RGB").save(fpath, "PNG")

    entry = {
        "file": fname,
        "name": name,
        "text": text,
        "style": args.style,
        "format": args.format,
        "seal": seal_chars,
        "colophon": colophon,
        "glyph_sources": {ch: glyph_src.get(ch, "font:" + main_font.label)
                          for ch in text},
        "draft": draft,
        "created": datetime.now().isoformat(timespec="seconds"),
    }
    update_registry(args.out, entry)

    print(fpath)
    print(" ".join("%s:%s" % (ch, glyph_src.get(ch, "font:" + main_font.label))
                   for ch in text))
    return 0


if __name__ == "__main__":
    sys.exit(main())