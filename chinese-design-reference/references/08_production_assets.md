# Module 08 — Production and Reusable Assets

**Scope.** Practical print-production constraints for a Chinese–English family-history book (fine brushwork, small CJK text, dark backgrounds, archival photographs, wide family trees), plus a verified register of reusable font and image assets with exact licensing.

**Evidence labels:** (A) documented fact / primary statement; (B) visual observation; (C) scholarly/technical interpretation; (D) proposed contemporary design application.

**Standing rule.** For every asset this module separates **publication-cleared** material from **reference-only** material, and it bears repeating: **a museum's ownership of a physical object does NOT automatically grant anyone reproduction permission** — image rights follow the institution's stated licence for the specific digital file, not custody of the object (A).[^1^]

---

## 1. Print constraints on fine brushwork

Chinese calligraphy and brush-drawn artwork contain hairline strokes, tapered entries/exits (起筆/收筆), and dry-brush (飛白) textures. These interact with hard print floors.

### 1.1 Minimum stroke/line widths (offset and digital CMYK)

A working print specification matrix (house spec of a trade printer, 2026 edition) gives for 4-colour process printing (A):[^2^]

| Element | Positive (ink on paper) | Reversed (paper showing through ink) |
|---|---|---|
| Line / rule | 0.1 mm (0.25 pt) | 0.2 mm (0.5 pt) |
| Type (Latin reference) | 6 pt | 8 pt; 9 pt on uncoated stock |
| Lightest printable tint | 8 % | — |
| Registration tolerance | ±0.15–0.25 mm between colour impressions | — |

Two mechanisms drive these floors (A, technical explanation):[^2^]

- **Misregistration.** C, M, Y and K are separate impressions that never land exactly together. Fine lines or small glyphs built from multiple inks show coloured fringes. Therefore: build fine strokes and small text in **a single ink (K100)**.
- **Dot gain.** Ink spreads on contact with paper, more on uncoated than coated stock. A positive stroke prints slightly *heavier*; a reversed (white) stroke is eaten from both sides and can fill in. This is why reversed minimums are larger.

**Application to brushwork (D).**

1. Reproduce calligraphy as **grayscale or single-plate black** wherever possible, at 300 ppi effective resolution or better (see §4); a 4-colour build of a hairline guarantees fringing.
2. Measure the thinnest strokes of any scanned artwork at final reproduction size: keep them ≥ 0.1 mm on coated stock; treat 0.15 mm as a safer target.
3. Dry-brush textures print as stochastic tint noise; if the lightest flecks matter, raise the floor rather than letting the RIP clip everything below ~8 %.
4. For foil-stamped calligraphy (covers, title devices), the floors rise sharply: positive line target 0.15 mm (floor 0.1 mm), reversed gap 0.25 mm, and high-contrast (fine-hairline) letterforms need **12 pt minimum** in foil (A).[^2^]

## 2. Small Chinese text: minimum sizes and why CJK needs more

The W3C's *Requirements for Chinese Text Layout* (CLREQ) documents the traditional Chinese type-size system and its legibility floor (A):[^3^]

| Traditional size | Points | ≈ mm | Use |
|---|---|---|---|
| 五號 (Size 5) | 10.5 pt | ≈ 3.7 mm | standard body text |
| 新五號 (New Size 5) | 9 pt | ≈ 3.2 mm | newspapers, magazines |
| 六號 (Size 6) | 7.875 pt | ≈ 2.8 mm | **minimum acceptable for content text** |
| 七號 (Size 7) | 5.25 pt | ≈ 1.9 mm | below legibility floor for reading matter |

CLREQ's rationale: below roughly 六號, "the complex structure of Han characters" makes text difficult to read (A).[^3^] Chinese glyphs fill a square em and pack many strokes into it, so the *stroke gap* — not the nominal point size — is what fails first; a 7 pt Chinese character can be denser than a 7 pt Latin word and needs a larger effective size for the same readability (C, from the CLREQ size table and character-frame model).[^3^]

Related CLREQ parameters for book work (A):[^3^]

- Type-area line gap is commonly **50–100 % of the font size** (i.e., line height ≈ 1.5–2× font size); line length should be a whole multiple of the font size, with line ends aligned (justified grid).
- Han–Western inter-script spacing: up to **1/4 em** between Han characters and Latin/digits (none at line start/end; none adjacent to Chinese punctuation).
- Chinese composition tradition: "an orphan does not make a line, nor a widow a page" (孤字不成行、孤行不成頁).

**Application (D).**

- Set bilingual body at ≥ 10.5 pt for Chinese (五號), with English one step smaller visually matched; captions no smaller than 8 pt Chinese / 六號 absolute floor 7.875 pt.
- Names in small sizes (family-tree labels, photo credits) should use a sans or a low-contrast song/serif weight, because fine serif horizontals (宋體橫畫) thin below the stroke floor at small sizes (D, consequence of §1).

## 3. Dark backgrounds: reverse type and rich black for CJK

Dark full-bleed pages (mourning bands, memorial plates, section dividers) are attractive for a family history but are the highest-risk pages in the book.

- **Rich black.** For large dark areas use a rich black such as **C60 M40 Y40 K100**, but only for areas **at least ~5 mm across**; keep **total ink coverage ≤ 300 %** (A).[^2^] Small elements and all small text on dark grounds stay **single-ink K** builds.
- **Reverse (white) type floors.** Reversed type needs 8 pt minimum (9 pt on uncoated) for Latin; CJK needs more because stroke gaps fill in from all sides under dot gain — practical guidance: reversed Chinese at **≥ 9–10 pt**, medium or bold weight, low-contrast (sans or demibold song) faces (D, extrapolated from the documented reversed floors and dot-gain mechanism).[^2^]
- **Knockout text over photographs** (portraits behind memorial text) compounds the problem: the background is not a flat solid, so fill-in is uneven. Prefer a solid or vignetted panel behind reversed text (D).
- Reversed rules/family-tree connector lines: ≥ 0.5 pt (0.2 mm) (A).[^2^]

## 4. Archival photographs: scanning standards and restoration ethics

### 4.1 Capture standards

The US Federal Agencies Digital Guidelines Initiative (FADGI), *Technical Guidelines for Digitizing Cultural Heritage Materials* (3rd ed., 2023), sets measurable star levels. For reflective photographic/print material the 4-star level is ≈ **400 ppi** capture (≥ 396 ppi after reproduction-scale accuracy), 16-bit, in a wide colour space (Adobe RGB 1998 / ProPhoto / ECI); lower star levels step down through 300/250/200 ppi (A).[^4^] FADGI also notes that very fine detail (e.g., engravings) may warrant 800 ppi or higher, and that originals must not be pressed under glass without approval — potential harm to the object overrides the schedule (A).[^4^]

Practical rules consistent with these standards (C, common archival practice):[^5^]

| Material | Working capture |
|---|---|
| Documents/letters | 300 ppi minimum; 400–600 ppi for small handwriting |
| Photographic prints | **600 ppi** (headroom for cropping/enlargement) |
| 35 mm slides/negatives | dedicated film scan at much higher effective ppi (2400–4000 ppi) |
| Master format | TIFF (uncompressed or lossless), 16-bit where possible; JPEG/PNG only for access copies |

**Application (D).** Scan family photographs at 600 ppi TIFF even if the book will use them at 300 ppi; the extra resolution is the family's archive, not the book's. Record scanner, date, and settings per file — treat each scan like an accession record.

### 4.2 Restoration ethics

(A) FADGI's masters discipline — a master file is a faithful capture; adjustments belong in derivative "production masters" (A).[^4^] For a family history, translate this into policy (D):

1. Keep an untouched scan as master; all retouching (tear repair, spot removal, tone) happens on copies.
2. Document every substantive alteration in the caption or credits ("digitally restored, 2026"); never silently alter faces, dates, or inscriptions.
3. Cropping for layout is acceptable; compositing people into groups they were not photographed in is a factual alteration and must be disclosed or avoided.

## 5. Family trees in print: layout strategies for wide 世系 diagrams

Traditional genealogies solved the width problem structurally: the 歐蘇式 convention breaks the chart into **five-generation blocks (五世一提)** that restart on each page/section (A, see Module 07, §3.2).[^6^] Modern print strategies (D):

1. **Modular five-generation blocks** — heritage-true and page-friendly; each block cites the block it continues from/to ("續上頁第X世").
2. **Fold-out (gatefold) plates** for the full descent chart; keep the block version in the text for readability.
3. **90°-rotated landscape spreads** for wide charts; acceptable for plates, poor for reading matter.
4. **Typographic floors inside charts:** names ≥ 六號 (7.875 pt) and ideally ≥ 8 pt; connector rules ≥ 0.25 pt positive / 0.5 pt reversed; single-ink K for all fine rules (A floors from §1).[^2^][^3^]
5. **Bilingual labels:** characters primary, registered/pinyin name secondary at one size down, generation number (第X世 / Gen. X) as a running marginal marker so any page is self-locating (D).

## 6. Font resources with verified licensing

Licence texts and terms below were checked against primary sources (GitHub licence files, foundry statements, licence full texts) on 2026-11-07. **Re-verify before publication; licence terms change.**

### 6.1 Font licensing table

| Font | Source | Licence (verified) | Commercial use | Embedding in a printed/PDF book | Modification | Key conditions / cautions |
|---|---|---|---|---|---|---|
| **Noto Serif SC / TC, Noto Sans SC / TC** | Google / notofonts | SIL OFL 1.1 (A)[^7^] | Yes | Yes | Yes (derivatives under OFL, no Reserved Names) | Do not sell font files alone; keep copyright notice + OFL text when redistributing |
| **Source Han Serif / Source Han Sans (思源宋體/黑體)** | Adobe + Google, adobe-fonts GitHub | SIL OFL 1.1 (A)[^8^] | Yes | Yes | Yes | Reserved Font Name "Source": derivatives must not use "Source" in the name (A)[^9^] |
| **LXGW WenKai 霞鹜文楷** (kai/fangsong style, from Fontworks Klee One) | github.com/lxgw/LxgwWenKai | SIL OFL 1.1 (A)[^10^] | Yes, no fee, no attribution required | Yes | Yes; derivatives must stay OFL and must NOT use reserved names 「霞鹜」「LXGW」 (A)[^11^] | Font files must not be sold standalone |
| **Google Fonts calligraphy faces: Ma Shan Zheng 馬善政, Zhi Mang Xing 鐘齊志莽行書, Liu Jian Mao Cao 柳建毛草, Long Cang 龍藏** | Google Fonts | SIL OFL 1.1 (A)[^12^] | Yes | Yes | Yes (OFL terms) | Display/書法-flavour faces; fine for titles, too mannered for body text (D) |
| **Klee One (Fontworks)** | fontworks-fonts GitHub | SIL OFL 1.1 (A)[^11^] | Yes | Yes | Yes | Basis of LXGW WenKai; Japanese glyph preferences |
| **AR PL fonts (文鼎公眾授權字型, 1999: PL中楷/PL細上海宋/PL簡報宋/PL簡中楷)** | Arphic donation to open source, 1999 | **Arphic Public License 1999** — free copying/distribution/modification with licence file retained; not explicitly restricted to non-commercial use (A)[^13^][^14^] | Generally yes under the 1999 text; see caution | Yes | Yes, with prominent change notices and same-terms redistribution | **Caution:** the 2010 releases (AR PL MingU20-L, AR PL BaoSong2 GBK) use a *revised* licence restricted to **non-profit distribution only** (A)[^14^] — do not mix the two generations |
| **王漢宗自由字型 (Dr. Wang Hannzong)** | Originally GNU GPL (2000/2004 donations) (A)[^15^] | GNU GPL (as released) | **Disputed — avoid** | — | — | 2004 copyright dispute with Arphic (文鼎); justfont's review cleared 18 faces but later **withdrew them**; Chinese free-font archivists (貓啃網) now advise against commercial use due to unresolved provenance risk (A)[^15^] |
| **Zpix 最像素** | SolidZORO GitHub | **Proprietary** (A)[^16^] | **No (paid: US$1,000 per single commercial product)**; free only for personal and education projects | Paid licence only | Explicitly forbidden (no modification/decompilation/conversion/splitting) (A)[^16^] | Pixel style is evocative for "archival/ledger" aesthetics, but for a publication either buy the licence or use an OFL pixel font (Fusion Pixel / Ark Pixel, OFL 1.1) (A)[^17^] |
| **Cubic 11 俐方體11號** | ACh (Taiwan) | Custom permissive licence; derivative works must carry the same licence (copyleft-like) (A)[^17^] | Yes | Yes | Yes (same-licence condition) | Traditional-Chinese-first 11×11 pixel face |
| **全字庫正楷體/正宋體 (Taiwan CNS)** | Taiwan National Development Council | Open Government Data License v1.0 (attribution) (A)[^18^] | Yes, with attribution | Yes | Limited | Standard 楷書 useful for a "textbook kai" voice |

### 6.2 OFL essentials (from the licence text itself)

The SIL Open Font License 1.1 permits use, study, copying, merging, embedding, modification, redistribution, and sale *of documents/products made with the font*; conditions: font software may not be sold **by itself**; redistributions must include the copyright notice and licence; modified versions may not use **Reserved Font Names**; derivatives must remain under OFL; and — crucially for book production — **the licence's font-side obligations do not apply to documents created using the font** (A).[^7^] A printed book or PDF with embedded OFL fonts is a "document", not a font redistribution; you need only archive the licence text in the project (C).

### 6.3 Recommended working set for the family-history book (D)

- **Chinese body (traditional)**: Noto Serif TC or Source Han Serif TC; **(simplified, if needed)**: SC variants of the same.
- **Chinese display / heritage voice**: LXGW WenKai (kai warmth) for quotes and captions; an OFL calligraphy face (Ma Shan Zheng or Zhi Mang Xing) strictly for cover/chapter titles.
- **Latin companion**: any OFL serif matched in x-height; check BUC diacritics (ŏ, ĕ̤, ṳ̄, à̤) render — test with actual Foochow Romanized strings before committing (see Module 07, §2.2).
- **Avoid**: 王漢宗 faces (provenance dispute), Zpix (paid for commercial), any "free download" font without a licence file. System-bundled fonts (e.g., macOS/Windows CJK fonts) are licensed for use *within the OS*, which does not automatically cover embedding in commercial print files — treat as unverified unless the EULA is checked (C).[^19^]

## 7. Image resources with verified licensing

### 7.1 Institutional open-access sources

| Source | Scale (as stated) | Licence of released files | Attribution | Verified notes (2026-11-07) |
|---|---|---|---|---|
| **Metropolitan Museum of Art — Open Access** | > 406,000 hi-res images (museum's standing figure) (A)[^20^] | **CC0** for images of works the Met believes to be public domain; only items with the Open Access icon (A)[^20^][^21^] | Not required; courtesy credit "The Metropolitan Museum of Art, New York" requested | Restricted works go through Art Resource for a fee. **Photographs you take yourself in the museum may not be published or commercially exploited** — use the OA file, not your own photo (A)[^20^]. Free API, no key, ≤ 80 req/s (A)[^22^] |
| **Smithsonian Open Access** | 2.8 M items at Feb-2020 launch; > 5.1 M 2D/3D items now stated (A)[^23^] | **CC0** for items carrying the CC0 designation (A)[^23^] | Not required | Smithsonian disclaims guarantee that CC0 items are free of *third-party* rights (publicity/privacy, trademarks); check per item (A)[^23^] |
| **國立故宮博物院 (NPM, Taipei) Open Data** | ~410,000+ object images released in tiers (A)[^24^] | **Low-res images (~1 MP): CC0** — no attribution needed. **Mid-res images (~6 MP) and site text: CC BY 4.0 / 政府資料開放授權條款-第1版** (A)[^24^][^25^] | CC BY tier: display e.g. 「品名 國立故宮博物院，臺北，CC BY 4.0 @www.npm.gov.tw」 (A)[^24^] | **High-res images are NOT open** — licensed for a fee under the museum's digital-asset rules; NPM has terminated licences of infringing users (A)[^25^]. Open Data excludes patent/trademark rights; don't make products implying NPM manufacture (A)[^25^] |
| **Wikimedia Commons** | Millions, aggregated | **Per-file**: CC0 / CC BY / CC BY-SA / public domain; faithful 2-D reproductions of public-domain works are treated as PD by Commons policy (A)[^26^] | Per file licence | Read each file page; prefer institutional uploads; uploader-supplied licences are community-asserted, not warranted (C) |
| **Getty Open Content / Art Institute of Chicago / Rijksmuseum / Cleveland / NGA Washington / Paris Musées** | Tens of thousands each | CC0 for designated public-domain images (A, directory verified against terms pages 2026-09)[^27^] | Varies (AIC requests caption credit) | Useful corroborating sources for Chinese art |
| **British Museum** | ~1.9 M images | **CC BY-NC-SA 4.0 — non-commercial only** (A)[^27^] | Required | Contrast case: NOT usable in a commercial publication |

### 7.2 Reference-only vs publication-cleared — working classification

- **Publication-cleared (given stated conditions):** Met OA (CC0); Smithsonian OA CC0 items; NPM Open Data low-res (CC0) and mid-res (CC BY 4.0 with attribution line); Wikimedia Commons files whose file page shows CC0/PD/CC BY (with attribution) — verify each file page on the download date and archive a copy of the licence statement.
- **Reference-only (do NOT publish without separate licence):** anything on a museum site *without* the open-access mark; British Museum images (NC); NPM high-res; images from books, auction catalogues, commercial archives, and general web search; photographs taken by visitors inside museums (Met explicitly prohibits publishing these) (A).[^20^]
- **The core principle (A):** custody ≠ copyright. A museum that owns a Ming fan owns paper and ink, not necessarily the rights in a photograph of it; and a CC0 dedication covers only the file the institution itself released. Conversely, CC0 does not clear *third-party* rights (privacy, publicity, trademarks) — the Smithsonian and Met both say so in their terms (A).[^20^][^23^]

## 8. Visual exemplars

See `assets_register.csv`, items PA-01…PA-04:

1. **PA-01** — Yuan Zhi (袁袛), *Calligraphy* (明, folding fan mounted as album leaf, ink on paper), Met object 13.100.82, CC0: a publication-cleared master for studying how fine brushwork survives reproduction; hairlines and dry-brush make it a live test of §1 floors (B).[^28^]
2. **PA-02** — LXGW WenKai specimen sheet (project documentation image; SIL OFL 1.1): the kai/fangsong display voice recommended in §6.3 (B).[^10^]
3. **PA-03** — Source Han Serif repository & LICENSE.txt (SIL OFL 1.1): canonical reference for the OFL + Reserved Font Name regime (A).[^8^][^9^]
4. **PA-04** — FADGI *Technical Guidelines for Digitizing Cultural Heritage Materials*, 3rd ed. (2023): the scanning-standard reference behind §4 (A).[^4^]

## 9. Gaps and limitations

1. **Printer-specific tolerances.** §1–3 figures come from one trade printer's published house matrix plus CLREQ; the actual print vendor's spec sheet supersedes them — request it before finalising artwork (especially rich-black recipe, ink limit, and reversed minimums, which vary by press and stock).
2. **王漢宗 licence status** remains genuinely unresolved publicly (GPL release vs. the Arphic dispute); the conservative position — avoid for publication — is documented, but no court outcome was located.
3. **Zpix pricing** is as published on the author's GitHub page; terms may be negotiable per product.
4. **NPM CC BY 4.0 attribution wording** should be copied from the NPM Open Data page at time of use; tier pixel thresholds (≈1 MP / ≈6 MP) are as stated by secondary descriptions of the policy.
5. **BUC (Foochow Romanized) font coverage** not yet tested against the candidate fonts; requires a rendering test (see §6.3).
6. No Malaysian print-vendor-specific guidance was obtained; all print figures are general offset/digital floors.

---

[^1^]: https://www.metmuseum.org/about-the-met/policies-and-documents/open-access
[^2^]: https://www.printpeppermint.com/guides/file-setup/minimum-line-weight-and-type-size
[^3^]: https://www.w3.org/TR/clreq/
[^4^]: https://www.digitizationguidelines.gov/guidelines/FADGI%20Technical%20Guidelines%20for%20Digitizing%20Cultural%20Heritage%20Materials_3rd%20Edition_05092023.pdf
[^5^]: https://heirloom.cloud/blogs/blog/best-dpi-for-scanning-photos-why-600-dpi-is-ideal
[^6^]: https://upload.wikimedia.org/wikipedia/commons/7/76/Shanghai_%E5%A4%AA%E6%9C%AB%E5%BE%90%E6%B0%8F%E5%AE%97%E8%AD%9C.pdf
[^7^]: https://fontsource.org/fonts/noto-serif-sc/about
[^8^]: https://github.com/adobe-fonts/source-han-serif/tree/release/
[^9^]: https://github.com/adobe-fonts/source-han-serif/blob/master/LICENSE.txt
[^10^]: https://github.com/lxgw/LxgwWenKai
[^11^]: https://font.doany.cn/f/lxgw-wenkai?weight=Bold
[^12^]: https://colorwander.bryantchen.cc/terms
[^13^]: https://www.maoken.com/arp
[^14^]: https://en.wikipedia.org/wiki/Arphic_Technology
[^15^]: https://www.maoken.com/zhengyi/1923.html
[^16^]: https://github.com/SolidZORO/zpix-pixel-font
[^17^]: https://github.com/liyupi/ai-model-world/blob/main/docs/pixel-character-pipeline-research.md
[^18^]: https://github.com/jeffreyxuan/toneoz-font-zhuyin
[^19^]: https://hkdesignpro.com/blog/chinese-font-licensing/
[^20^]: https://metropolitan.museum/the-museum/open-access-free-images/
[^21^]: https://github.com/metmuseum/openaccess
[^22^]: https://metmuseum.github.io/
[^23^]: https://www.si.edu/openaccess (see also https://dnacreative.notion.site/Smithsonian-Open-Access-2-8-million-digital-assets-dedicated-to-public-domain-20e998cd1e1c80fc818afbde9d940b93)
[^24^]: https://www.evergreentw.com.tw/npm
[^25^]: https://www.ly.gov.tw/Pages/ashx/File.ashx?FilePath=~/File/Attach/244893/File_19840466.pdf
[^26^]: https://commons.wikimedia.org/wiki/Category:Ancestral_halls_in_Fujian
[^27^]: https://umberlore.com/open-license-art-image-directory/
[^28^]: https://www.metmuseum.org/art/collection/search/35993
