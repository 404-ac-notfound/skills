# Evaluation Sheet — Pre-Delivery Tests for Claude

**How to use:** run the relevant section before delivering any design or page involving Chinese content. Each test is marked:

- **[proposed]** — a test defined here but **not yet performed** on real output.
- **[performed]** — a test actually executed, with date and target recorded by the tester.

At first release, **all tests below are [proposed]** unless a tester fills in the record line.

---

## A. Character accuracy

| # | Test | Pass standard | Status / record |
|---|---|---|---|
| A1 | Every non-standard or calligraphic character form on the page is checked against 漢典 / 教育部異體字字典 / an attested work (Module 01 §6 workflow) | Each form either matches the standard glyph or cites a documented variant/attested cursive source | [proposed] |
| A2 | Traditional/simplified consistency within each text block | No mixed-script sentence unless deliberately quoting; deliberate cases are annotated | [proposed] |
| A3 | Stroke-count spot check on display characters (esp. 齊 = 14 strokes traditional, 齐 = 6) | Counts match dictionary record | [proposed] |
| A4 | No invented glyph presented as historical | Any client-specific form (e.g., preferred 齊) is labelled "family design choice" | [proposed] |
| A5 | Cursive abbreviation test: any abbreviated form appears in 草訣百韻歌 / 標準草書 / a documented masterwork | Attestation cited, or form replaced | [proposed] |

## B. Style matching (new lettering vs existing)

| # | Test | Pass standard | Status / record |
|---|---|---|---|
| B1 | Stroke-thickness range of the new character falls inside the source lettering's measured range | Max/min stroke width within source band (Module 03 §5 checklist) | [proposed] |
| B2 | Pressure rhythm: tapered entries/exits match the source's brush behaviour (藏鋒/露鋒, 提按) | Entry/exit shapes visually consistent under 400% zoom | [proposed] |
| B3 | Turns and joins: angular vs rounded turns match source; joins show same connective logic | No mismatched corner vocabulary | [proposed] |
| B4 | Visual density: black-to-white ratio of the new character within ±10% of neighbours | Measured on a rasterised proof | [proposed] |
| B5 | The "squiggle" test: no decorative stroke was added to simulate hand-writing | Every stroke traceable to a structural or attested-abbreviation role | [proposed] |
| B6 | Honesty rule: output describes only what is visible; no claims of reconstructed stroke order or intent | Labels (B)/(C) used in any annotation | [proposed] |

## C. Cultural appropriateness

| # | Test | Pass standard | Status / record |
|---|---|---|---|
| C1 | No universal symbolism claim ("red always means…") anywhere in copy | Every symbolic claim carries period/region/occasion scope (Module 05 §7) | [proposed] |
| C2 | Motif audit: any bat/crane/peach/dragon/如意 usage checked for funerary, imperial, religious, or political associations that clash with context | Associations documented and appropriate | [proposed] |
| C3 | Seal audit: seal type (name/studio/閒章), 朱文/白文 choice, and placement follow Module 05 conventions | Placement and colour purposeful, single red | [proposed] |
| C4 | Regional check: Fuzhou/Fujian or Malaysian Chinese content relies on regional sources, not generic "Chinese culture" claims | Module 07 cited for each regional claim | [proposed] |
| C5 | No identity inference: nothing infers a person's ancestry/relationship from a romanised spelling | Explicit coexistence note present where spellings vary | [proposed] |
| C6 | No synthetic image presented as a historical example | Every historical image traceable in assets_register.csv | [proposed] |

## D. Bilingual legibility

| # | Test | Pass standard | Status / record |
|---|---|---|---|
| D1 | Hierarchy: a reader can identify the primary language and navigate within 3 seconds per spread | Hierarchy rule stated per page type (Module 06 §2) | [proposed] |
| D2 | Chinese body ≥ 10.5 pt; captions ≥ 7.875 pt | Measured in the layout file | [proposed] |
| D3 | Punctuation per GB/T 15834-2011; 避頭尾 prohibitions honoured (no line-initial 。、」etc.) | Passes a CLREQ checklist pass | [proposed] |
| D4 | Font licence audit: every embedded font is OFL or otherwise cleared (Module 08 §6 table); 王漢宗 fonts absent | Licence column filled for each font | [proposed] |
| D5 | Calligraphic titles remain character-correct (A-tests applied to display lettering) | Display forms pass A1–A5 | [proposed] |

## E. Rendered-page quality (print)

| # | Test | Pass standard | Status / record |
|---|---|---|---|
| E1 | Fine brushwork survives print: strokes ≥ 0.25 pt positive / ≥ 0.5 pt reversed at final size (Module 08 §1, §3) | Verified on a printed proof at 100% | [proposed] |
| E2 | Dark backgrounds: rich black C60 M40 Y40 K100 only ≥ 5 mm; total ink ≤ 300% | Preflight report clean | [proposed] |
| E3 | Archival photos scanned ≥ 600 dpi; restoration log exists | Log attached to project files | [proposed] |
| E4 | Family tree: generations unambiguous at arm's length; three name forms legible | Tested with one non-designer reader | [proposed] |
| E5 | Image rights: every reproduced image is publication-cleared per assets_register.csv (not "reference-only") | Licence column re-checked at press time | [proposed] |
| E6 | Soft-proof review of one full spread by a native-literate Chinese reader and one English-only reader | Both complete navigation tasks | [proposed] |

---

**Tester record template** (copy per test run):

```
Test ID: __  Date: ____-__-__  Target (file/page): ______
Result: PASS / FAIL  Evidence: ______  Tester initials: __
```