# Style Menu — Codes, Samples, Recommendations, Hybrids

All evidence claims below trace to the chinese-design-reference library (module numbers in
parentheses; asset IDs reference `assets_register.csv`). Sample images live in
`../assets/samples/`; IDs without a local file are displayed in the menu via their register URL.

## 1. Base styles

| Code | Name | Script | Anchor work (source ID) | Sample file | Stroke signature | Best for | Caution |
|---|---|---|---|---|---|---|---|
| KAI-YAN-01 | 顏體楷書 Yan-style regular | 楷書 | 顏勤禮碑 779 CE (QI-06); 爭坐位帖 (QI-08) | — (register link) | Weighty verticals, emphatic level 二 base, monumental dignity | Book covers, formal titles, the family surname | Heavy forms need generous 留白; cramped layouts kill it |
| KAI-MU-01 | 刻本楷書 Woodblock regular | 楷書 | 說文解字 汲古閣本 (CS-01); 康熙字典 1827 (CS-02) | CS-01.jpg, CS-02.jpg | Carved regularity, knife-crisp terminals, vertical-column authority | Classical book-title pages, dictionary styling | Reads as print, not hand — pair with a hand element (seal) |
| XING-MI-01 | 米芾行書 Mi Fu running | 行書 | 蜀素帖 1088 (QI-07); 吳江舟中詩 (CO-04) | — (register link) | Elongated right-leaning silhouette, swift connected diagonals, strategic imbalance | Energetic titles, modern-feeling classical work | Distortion is strategic atop correct structure — never freestyle it |
| XING-YUAN-01 | 明人扇面行書 Ming fan running | 行書 | 袁袠 行書金陵懷古詩 (PA-01, Met CC0) | PA-01.jpg | Hairline strokes + dry-brush passages, refined literati small scale | Album leaves, elegant short phrases, gift pieces | Fine strokes hit print floors fast — keep ≥ 0.25 pt at final size |
| XING-YAN-01 | 顏真卿草稿行書 Draft running | 行書 | 祭姪文稿 758 (CB-02/CO-01) | — (register link) | Visible pressure rhythm, corrections kept, documentary rawness | Emotive inscriptions, memorial texts | Draft aesthetic suits grief/sincerity registers only — wrong for festive uses |
| CAO-HUANG-01 | 黃庭堅草書 Huang cursive | 草書 | 廉頗藺相如傳 c. 1095 (CO-03, Met CC0) | CO-03.jpg | Sustained column energy, long-range 避就 across repeats | Medium-length texts where some legibility survives | Cursive merges look-alikes (齊≈齋/高/馬) — verify each form is attested |
| CAO-HUAI-01 | 懷素狂草 Wild cursive | 草書 | 自敘帖 777 (CB-03, NPM CC BY 4.0) | CB-03.jpg | Thin-but-continuous centreline, natural 飛白, visible re-dip rhythm | Single-character art, dramatic display | Illegible to most readers; never for informational text; authenticity debated — cite tradition |
| LI-CAO-01 | 曹全隸書 Cao Quan clerical | 隸書 | 曹全碑 185 CE rubbing album (CB-05, NPM CC BY 4.0) | — (register link) | Silkworm-head entries 蠶頭, swallow-tail exits 雁尾, flattened 八分 spread | Baseline-stable titles; suits 齊's two-level base | One 雁尾 per character — repeating it is a beginner error |
| ZHUAN-SG-01 | 石鼓文大篆 Stone-drum great seal | 大篆 | 石鼓文 rubbings (CB-04, Met CC0) | CB-04.jpg | Even-weight concealed-tip line, stone-erosion texture separable from brush | Archaic-feeling emblems, seals' companion calligraphy | Dating unsettled; describe as "attributed Eastern Zhou/Qin" |
| ZHUAN-SM-01 | 小篆 Small seal | 小篆 | 說文解字 齊部 (QI-03); ACC SVGs | QI-03.png | Maximum symmetry, even line, emblem-ready | Logotypes, seal faces, single-character marks | Redrawn SVGs ≠ woodblock scans — fine for design, cite as redrawn |
| SEAL-BAI-01 | 白文方印 Intaglio square seal | 印 | Song jade square seal (SI-03, Met CC0) | SI-03.jpg | White characters on red ground, square format ~9 cm class | The 齊氏之印 family seal | Test legibility at 12 mm and 18 mm before committing (Module 05 §3) |
| SEAL-ZHU-01 | 朱文印 Relief seal | 印 | Module 05 §§1–2 conventions; imperial jade (SI-01) | SI-01.jpg | Red characters on white, single-character 齊 mark | Accent seal under a title | One red accent only — no decorative scattering (Qianlong caution) |

## 2. Recommendation matrix (use case → codes)

| Use case | First choice | Alternatives | Why |
|---|---|---|---|
| Family-history book cover title | KAI-YAN-01 | XING-MI-01, LI-CAO-01 | Monumental, formal, matches the documented 顏體 cousin (QI-06) |
| 齊 family emblem / logotype | HYB-QZM-01 (§3) | ZHUAN-SM-01 | Symmetric seal-script skeleton + monumental stroke weight |
| Square name seal 齊氏之印 | SEAL-BAI-01 | SEAL-ZHU-01 | Documented conventions (Module 05 §§1–2) |
| Hanging scroll, living room | XING-YUAN-01 | XING-MI-01 | Refined at viewing distance, fine-brush elegance |
| Single dramatic character (齊) | ZHUAN-SM-01 | CAO-HUAI-01 | Symmetry for contemplation; wild cursive for drama |
| Memorial / solemn inscription | XING-YAN-01 | KAI-YAN-01 | Documentary sincerity of the draft tradition |
| Festive couplet (婚/壽) | KAI-YAN-01 | LI-CAO-01 | Legible dignity; verify motif/occasion scope (Module 05 §7) |
| Bilingual book (Chinese dominant) | KAI-MU-01 + Latin small caps | XING-YUAN-01 | Print-hand hybrid pairs cleanly with Latin serif (Module 06 §2) |
| Modern-art statement | CAO-HUAI-01 | CAO-HUANG-01 | Continuous-line energy; label tradition, not autograph |

## 3. Hybrids

A hybrid = **structure donor** (skeleton/proportions) + **manner donor** (stroke pressure,
entries/exits, rhythm). Document both donors and the ratio; pass evaluation-sheet B-tests;
assign code HYB-<X>-<NN>. Uniqueness lives in the combination + text + layout, not in
invented strokes.

| Code | Name | Structure donor | Manner donor | Rationale / intended use |
|---|---|---|---|---|
| HYB-QZM-01 | 齊篆顏骨 Qi emblem hybrid | ZHUAN-SM-01 (symmetric 齊 skeleton, QI-03) | KAI-YAN-01 (weighty verticals, level base) | The recommended route for a 齊 family mark — dossier §5 preferences honoured (two lower levels, left-leg up, right-leg down) |
| HYB-MI-YAN-01 | 米骨顏肉 | XING-MI-01 (right-leaning skeleton) | KAI-YAN-01 (pressure/weight) | Energetic but grounded titles for large formats |
| HYB-KAI-LI-01 | 楷骨隸波 | KAI-MU-01 (regular structure) | LI-CAO-01 (蠶頭雁尾 on horizontals only) | Print-legible title with clerical grace; flatters 齊's base levels |
| HYB-CAO-KAI-01 | 草意楷足 | KAI-YAN-01 (legible feet/structure) | XING-YAN-01 (draft rhythm, connective hints) | Running flavour readable by non-specialists — safe for bilingual family audiences |

Rules for new hybrids: (a) both donors must be base styles in this menu or documented additions;
(b) state a ratio (e.g. "70% structure / 30% manner"); (c) generate a sample and pass the
evaluation gate before adding to the menu; (d) record in the Custom styles section below.

## 4. Custom styles (user-added)

Styles saved via the menu page are stored in the browser; record durable additions here as well.

| Code | Name | Donors / source | Sample | Added | Notes |
|---|---|---|---|---|---|
| HYB-SGC-01 | 石鼓草意 Stone-drum × wild-cursive | Structure: ZHUAN-SG-01 / attested ACC seal-script forms (齊-seal, 家-seal, PD); Manner: CAO-HUAI-01 (continuous line, 飛白 dry-brush, carved erosion — synthetic texture only) | 齊家 family seal, 朱文 + 白文 double-rail rounded frame (gallery, 2026-11-08) | 2026-11-08 | Created for the 齊家 vertical family seal; glyph forms attested, manner is a (D) design treatment |

## 5. Naming & code conventions

- Script prefix: KAI 楷 / XING 行 / CAO 草 / LI 隸 / ZHUAN 篆 / SEAL 印; hybrids HYB.
- Codes are stable identifiers — never reuse a retired code; increment the -NN suffix.
- A style code in a gallery registry entry is the permanent record of how a work was made.