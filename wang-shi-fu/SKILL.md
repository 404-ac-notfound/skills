---
name: wang-shi-fu
description: Compose original, high-quality Chinese calligraphy artwork using the 集字 (jízì, "gathered characters") method — assembling attested glyphs from licence-cleared historical masters into new compositions. Provides a browsable style menu with codes and sample images, style recommendation and hybrid-style design, vertical-column layout in hanging-scroll / album-leaf / fan / square formats, seal (印章) placement, and a gallery of generated works. Use when the user wants to generate, create, or design Chinese calligraphy art, a calligraphic book title or cover treatment, brush-style lettering, a 齊 family emblem or seal, wall scrolls, couplets; when they ask for a style menu, style codes, or style combinations; or when they want to add hybrid styles to the menu or manage a gallery of generated calligraphy designs. Depends on the chinese-design-reference library for evidence, glyph sources, and the pre-delivery evaluation gate.
---

# Wang Shi Fu — Chinese Calligraphy Composer

Create new calligraphy artwork by **composing attested historical glyphs** — never by inventing
or AI-generating character forms. Precedent: 懷仁's 集王羲之行書聖教序, a canon-defining work
assembled character-by-character from Wang Xizhi's writing.

## Hard rules (never violate)

1. **No invented glyphs.** Every character must be attested (a documented historical form), or
   explicitly labelled "family design choice / contemporary design" per the reference library's
   Module 01 §6 workflow.
2. **No AI-image-generated characters.** Image models produce pseudo-characters that fail
   character-accuracy tests. Texture and paper effects may be synthetic; glyphs may not.
3. **Licence discipline.** Harvest glyphs only from sources marked cleared in the reference
   library's `assets_register.csv` (Met CC0, NPM Open Data CC BY 4.0, Commons PD, ACC project PD,
   OFL fonts). Record the source of every harvested glyph.
4. **Evaluation gate.** Before delivery, run the relevant tests from the reference library's
   `references/evaluation_sheet.md` (A: character accuracy, B: style matching, C: cultural
   appropriateness, E: print quality) and report results.

## Workflow 1 — Help the user choose a style

- If the user wants to browse visually: open `menu/index.html` (style cards with sample images,
  codes, filters, hybrids, gallery). A static page — open directly in a browser.
- If working headless: read `references/style_menu.md` and recommend from its use-case matrix.
- Always present the **style code** (e.g. `XING-MI-01`) plus one-line character description and
  best-use note. Recommend 2–3 candidates with trade-offs rather than one flat answer.

## Workflow 2 — Compose an artwork

1. Collect: **text** (exact characters; confirm traditional/simplified), **style code**,
   **format** (hanging-scroll / banner / square / fan / album-leaf), optional **seal text** and
   **colophon (落款)**.
2. Read `references/composition_engine.md` for the format's layout rules (column math, 留白
   ratios, seal positions).
3. Resolve glyphs per `references/sourcing_guide.md` — priority: harvested master glyphs >
   paleography SVGs > OFL font fallback (label fallback outputs as drafts).
4. Compose with `scripts/compose.py`, e.g.:
   ```bash
   python scripts/compose.py --text "齊氏家乘" --style XING-YUAN-01 \
       --format hanging-scroll --seal "齊氏之印" --out gallery/
   ```
   Per-character harvested-glyph overrides: place `<char>.png` files in a directory and pass
   `--glyphs <dir>`.
5. Run the evaluation gate (Hard rule 4). Fix failures before delivery.
6. Save the final PNG into `gallery/` and register it in `gallery/index.json` (compose.py does
   this automatically); the menu page's Gallery tab reads the same folder.

## Workflow 3 — Design a hybrid style

1. Hybrid = **structure donor** + **brush-manner donor** (e.g. Mi Fu skeleton + Yan Zhenqing
   pressure). Read `references/style_menu.md` § Hybrids for documented combos and rules.
2. Assign a code `HYB-<X>-<NN>`, document donors, ratio, and intended use.
3. Generate a sample, pass the evaluation gate, then add it to the menu (the page's "Add style"
   feature, persisted in browser storage) and append it to the Custom styles section of
   `references/style_menu.md`.

## Workflow 4 — Gallery management

- Generated works live in `gallery/` with `gallery/index.json` as the registry (file, style
  code, text, sources, evaluation status, date).
- The menu page's Gallery tab lets the user browse, favourite, and prune works.

## Bundled resources

| Path | When to use |
|---|---|
| `references/style_menu.md` | Choosing/recommending styles, designing hybrids — read whenever a style code is involved |
| `references/composition_engine.md` | Any composition task — read before running compose.py |
| `references/sourcing_guide.md` | Whenever a glyph must be sourced — read before harvesting |
| `scripts/compose.py` | The composition engine; run it, patch it if a format needs extending |
| `menu/index.html` | Visual style browsing, hybrid saving, gallery — point the user to it |
| `assets/samples/` | Sample images displayed by the menu page |

## Dependency

This skill assumes access to the **chinese-design-reference** library (modules 01–08, the 齊
dossier, the evaluation sheet, and `assets_register.csv`). If it is not installed, work from the
bundled references alone and mark all evidence claims as unverified.