# Composition Engine — Layout, Formats, Seals

Rules distilled from the reference library (Modules 03, 05, 06, 08). compose.py implements
these as parameters; read this before patching or overriding it.

## 1. Formats

| Format | Aspect (w:h) | Orientation | Typical use | Column rule |
|---|---|---|---|---|
| hanging-scroll 立軸 | 1:2 to 1:3 | Vertical text | Wall display, single phrase | Columns right→left, top→bottom |
| banner 橫披 | 2:1 to 4:1 | Vertical text (or single horizontal row for ≤4 chars) | Over-door, modern walls | Right→left |
| square 斗方 | 1:1 | Vertical text | Single character or 4-char phrase | 1–2 columns |
| fan 扇面 | Arc, ~2:1 bounding | Radiating short columns | Gift, album | Alternate long/short columns to follow the arc |
| album-leaf 冊頁 | 4:3 | Vertical text | Book-adjacent art, gift | Classical leaf conventions (Module 06 §1) |

## 2. Column math & rhythm (行氣)

- Columns read top→bottom, ordered right→left. compose.py defaults to this; horizontal rows
  are allowed only for banner format with ≤ 4 characters.
- **Never end with a single orphan character** on the final column (孤行). Balance columns so
  the last carries ≥ 2 characters; redistribute rather than squeeze.
- Column axis: characters may drift off-axis ≤ 3% of column width for hand-feel; systematic
  drift (all one direction) reads as an error, not rhythm.
- Size variance between characters: ±8% max within one work. 避就 — when a character repeats,
  vary its form only if an attested variant exists (Module 01 §6); never distort to differ.
- Line spacing (行距) ≥ 40% of character size for running/cursive, ≥ 25% for regular/clerical.

## 3. 留白 (empty paper) ratios

- 天頭 (head) > 地腳 (foot): head margin ≈ 1.5× foot margin in hanging scrolls.
- Minimum total margin: 12% of the short edge on all sides; 18%+ for heavy styles (KAI-YAN-01).
- Empty paper is a compositional element, not leftover (Module 04 §4) — when in doubt, enlarge
  margins rather than enlarge characters.

## 4. Seals and colophon (Module 05)

- **Name seal (姓名章):** below or left of the signature/last column, size ≈ 1/2 to 2/3 of a
  text character. 白文 for weight, 朱文 for lightness; one red total.
- **Leisure seal (引首章):** optional, upper right of first column, smaller than the name seal.
- **Never** scatter seals decoratively; never overlay seals on harvested master glyphs
  (the Qianlong caution — SI-02).
- Colophon (落款): smaller characters (50–65% of main text size), same or lighter style,
  final (leftmost) column area. Contents: date (干支 or Western), place, "name + 書/敬書".
- Seal paste red: single accent red only; no blue/purple paste without documented reason.

## 5. Ink, paper, palette

- Paper: warm off-white (#F5F0E4 to #F8F4E9) or aged (#EFE6D0); subtle fibre texture allowed
  (synthetic texture is fine — only glyphs must be attested).
- Ink: near-black with warmth (#1A1815 … #26221C); harvested rubbing glyphs may stay
  white-on-black if the whole work commits to the rubbing aesthetic (Module 02: negative is the
  native medium of stele calligraphy).
- Accent red (seal): vermilion 朱砂 #C03A2B … #D64A35. Only red in the work.
- No "Chinese red and gold" ornament (anti-cliché, Module 04 §6).

## 6. Harmonization when glyphs come from different masters

1. Unify ink tone first (curves/levels), then scale, then baseline.
2. If one glyph's texture clashes (crisp rubbing vs soft ink), add uniform grain — do not
   sharpen or blur individual glyphs into each other.
3. Step back test: at 25% zoom the work should read as one hand. If not, swap the offending
   glyph for another attested source before adjusting further.

## 7. Output & print floors (Module 08)

- Deliver PNG at ≥ 300 dpi at intended display size; keep a layered/vector intermediate.
- Stroke floors at final size: ≥ 0.25 pt positive, ≥ 0.5 pt reversed (white-on-black).
- Rich black C60 M40 Y40 K100 only for areas ≥ 5 mm; total ink ≤ 300%.
- Register every output in `gallery/index.json` with: file, text, style code, format, glyph
  sources (asset IDs), evaluation status, date.