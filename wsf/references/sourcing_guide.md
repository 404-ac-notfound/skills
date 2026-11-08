# Sourcing Guide — Where Glyphs May Come From

Every character in a composed work must resolve through this hierarchy. Record the source
(asset ID or URL) per glyph for the gallery registry. If the chinese-design-reference library
is available, its `assets_register.csv` is the master list; module numbers below refer to it.

## Priority ladder

1. **Harvested master glyphs** — cropped from licence-cleared images in the register:
   - Met Open Access **CC0** (no attribution needed): CB-04 石鼓文, CO-03 黃庭堅, CO-04 米芾,
     PA-01 袁袠扇面, SI-01/SI-03/SI-04, BT-01 芥子園, PV-04 郭熙.
   - NPM Open Data **CC BY 4.0** (attribute: 國立故宮博物院 National Palace Museum): CB-03
     自敘帖, CB-05 曹全碑, QI-07 蜀素帖, QI-08 爭坐位帖, SI-02, CO-01/CO-02.
   - Wikimedia Commons **PD / PD-art**: CB-01 蘭亭序(神龍), CB-02 祭姪文稿, PV-01 早春圖,
     PV-02 富春山居圖, PV-03 千里江山圖, QI-04 曹全碑齊.
   - **Avoid or verify first**: CC BY-SA items (CS-03, FM-01, FM-04 — share-alike obligations);
     items marked reference-only / rights unresolved (CS-04, QI-05, QI-06, QI-09, QI-10, BT-04).
2. **Paleography SVGs** — ACC project (PD) glyph series: QI-01 oracle, QI-02 bronze, QI-03
   small-seal. Ideal starting points for seal/emblem work; redrawn, so cite as redrawn.
3. **OFL font fallback** — LXGW WenKai (kai flavour), Source Han Serif/Sans TC (structure
   reference). Label any output using font glyphs as **draft** until replaced by harvested
   forms, unless the font's own aesthetic is the stated intent.
4. **System fonts (macOS Kaiti/Xingkai etc.)** — layout mock-ups only; never deliver.

## Never

- AI-image-generated characters (pseudo-glyphs; fail accuracy tests).
- Scraped images from rights-unresolved sites (e.g. QI-09's source page).
- 王漢宗 fonts (licence problems, Module 08 §6).
- "Cleaning up" a master's corrections/dry-brush into synthetic smoothness (Module 02: the
  process marks are the authenticity).

## Harvest workflow (per glyph)

1. Locate the character in the source image (register `annotation` often names the line —
   e.g. QI-07: 齊 in 龜鶴年壽齊羽介所託殊; QI-08: 以齊桓公之盛業).
2. Crop generously, then threshold: rubbings → keep white strokes on transparent; ink-on-paper
   → keep dark strokes on transparent. Remove background paper tone, keep stroke texture.
3. Denoise conservatively — erosion and 飛白 are data, not noise (Module 02, CB-04 lesson:
   separate stone-erosion from brush line before keeping either).
4. Export PNG with alpha, ≥ 1000 px on the long side, named `<char>.png` (e.g. `齊.png`) into
   the work's `--glyphs` directory. Log: char, asset ID, page/crop region, licence.

## Finding a character that isn't in the register

- Dictionaries for form verification (not images): 漢典 zdic.net, 教育部異體字字典 — confirm
  standard form, stroke count, attested variants (Module 01 §6 workflow).
- Then search the same cleared collections (Met, NPM Open Data, Commons) for works containing
  the character; the register's module pages document search patterns per institution.
- Cursive forms: check attestation against 草訣百韻歌 / 標準草書 logic (QI-09 lesson — cursive
  齊 merges with 齋/高/馬 unless its differentiating cues survive).

## The 齊 shortcut

Ten attested 齊 forms are already documented (QI-01…QI-10): oracle, bronze, small-seal,
clerical (曹全碑), regular (顏勤禮碑 — text evidence only), running (蜀素帖, 爭坐位帖),
cursive warnings (草訣), and Qi Baishi seal precedent. For 齊-family work, harvesting from
QI-07/QI-08 (NPM CC BY 4.0) or QI-04 (Commons) covers most needs immediately.