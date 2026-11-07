---
name: chinese-design-reference
description: Evidence-based reference library for informed Chinese visual design — character structure and variants (異體字), calligraphy and brushwork across the five scripts (篆隸楷行草), composition and style-matching, Chinese painting visual language, seals (印章) and symbolism, Chinese book arts and Chinese–English bilingual typography, Fuzhou/Fujian and Malaysian Chinese cultural context, and print production with verified font/image licensing. Use when designing, typesetting, illustrating, evaluating, or advising on Chinese-language visual materials — book covers, family-history books, bilingual layouts, seal design, calligraphic titles, character-correctness checks, matching a new character to existing calligraphy, choosing CJK fonts, checking image reuse rights, or judging cultural appropriateness. Includes a dedicated dossier for the surname character 齊/齐 and an application brief for a Qi/Chee family-history book.
---

# Chinese Design Reference Library

A modular, evidence-labelled reference library. Its first application is a Chinese–English family-history book for the Qi/Chee 齊 family (roots in Qi'an Village, Fuzhou), but all modules are reusable.

**What it is not:** it does not certify expertise or replace a trained calligrapher's assessment. It improves evidence, visual vocabulary, and judgment.

## Workflow

1. Consult the routing table below and read **at most two** relevant reference files. Do not load the whole library.
2. Respect the evidence labels in every file (below).
3. Apply the standing rules (below) to any output.
4. Before delivering design work, run the relevant tests in `references/evaluation_sheet.md`.

## Routing table

| Task involves… | Read |
|---|---|
| Character correctness, traditional/simplified, variants 異體字 | `references/01_character_structure.md` |
| Brushwork, five scripts 篆隸楷行草, judging calligraphy | `references/02_calligraphy_brushwork.md` |
| Matching a new character to existing lettering; spacing, composition 章法 | `references/03_composition.md` |
| Ink painting, landscape, 留白, 詩書畫印 | `references/04_painting_visual_language.md` |
| Seals 印章, 朱文/白文, auspicious motifs and their ambiguity | `references/05_seals_inscriptions.md` |
| Chinese–English typesetting, fonts, punctuation, binding, family trees | `references/06_book_arts_bilingual_typography.md` |
| Fuzhou/Fujian or Malaysian Chinese naming, migration, ancestral halls | `references/07_fuzhou_malaysian_context.md` |
| Print specs, DPI, font licences, image reuse rights | `references/08_production_assets.md` |
| The character 齊/齐 — history, calligraphic forms, client's preferred design | `references/qi_character_dossier.md` |
| The Qi family book specifically (titles, bilingual pages, photos, cover) | `references/qi_family_book_brief.md` |
| Pre-delivery checks | `references/evaluation_sheet.md` |
| Image provenance, licences, stable links | `references/assets_register.csv` |

Visual assets: `assets/visual_atlas.pdf` (16 annotated plates + 28 link-only exemplars); `assets/images/` holds licence-cleared image files keyed by the item IDs in the register.

## Evidence labels — never blur them

- **(A)** Documented fact / primary statement, traceable to a cited source.
- **(B)** Visual observation of a specific work.
- **(C)** Scholarly interpretation — attributed, contestable.
- **(D)** Proposed contemporary design application — advice, not history.

Never present (C) or (D) as (A). Never upgrade a client's design preference into a historical claim (`references/qi_character_dossier.md` §5 is the canonical example of keeping them apart).

## Standing rules

1. Verify non-standard character forms against 漢典 / 教育部異體字字典 / 說文解字 before drawing or approving them. A cursive form must be attested, not plausible (module 01 §6 workflow).
2. Stroke order and artist intent cannot be reconstructed from appearance alone; describe what is visible and label inference (module 02 §4).
3. Style-matching means matching brush mechanics — entry, pressure rhythm, turns, joins, density — never decorative "squiggles" (module 03 §5 checklist).
4. No universal symbolism claims ("this colour always means X"); state period/region/occasion scope (module 05 §7).
5. Calligraphic display lettering ≠ body typography; keep expressive titles character-correct and set body text per W3C CLREQ (module 06 §7).
6. Prefer documented Fuzhou/regional practice over generic "Chinese culture"; never infer a real person's identity or ancestry from a romanised spelling (module 07 §6).
7. Museum ownership ≠ reproduction permission; check the licence column of `references/assets_register.csv` before reusing any image.
8. Each module ends with "Gaps and limitations" — read it before acting on that module.

## Known gaps (library-level)

- "Qi'an Village" characters unconfirmed (homophone clash with historical 齊安郡); family must supply.
- No client artwork of the preferred 齊 form was supplied; dossier §5 assessment is analytic only.
- Malaysian Chinese print/ephemera conventions are thin in the literature.
- 王漢宗 font licensing is disputed — avoid; use OFL fonts (Noto/Source Han, LXGW).
