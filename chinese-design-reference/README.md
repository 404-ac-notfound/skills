# chinese-design-reference

An evidence-labelled reference library for informed Chinese visual design, packaged as a portable **Agent Skill** (SKILL.md format) with all reference material included. Built for a Chinese–English Malaysian Chinese family-history book (Qi/Chee 齊 family, roots in Qi'an Village, Fuzhou), reusable for any Chinese design work.

Covers: character structure & variants · calligraphy & brushwork (篆隸楷行草) · composition & style-matching · painting & visual language · seals & symbolism · Chinese book arts & bilingual typography · Fuzhou/Malaysian Chinese context · print production & licensing · a dedicated 齊/齐 character dossier.

## Repository layout

```
chinese-design-reference/
├── SKILL.md                    ← entry point: routing table, evidence labels, standing rules
├── references/                 ← loaded on demand, never all at once
│   ├── 01_character_structure.md … 08_production_assets.md
│   ├── qi_character_dossier.md
│   ├── qi_family_book_brief.md
│   ├── evaluation_sheet.md
│   └── assets_register.csv     ← 44 sources/exemplars: URLs, object IDs, licences
└── assets/
    ├── visual_atlas.pdf        ← 16 annotated plates + 28 link-only exemplars
    └── images/                 ← licence-cleared images (CC0 / PD / CC BY 4.0)
```

Every claim in the reference files is labelled **(A)** documented fact, **(B)** visual observation, **(C)** scholarly interpretation, or **(D)** proposed design application. Respect these labels when quoting.

## Use in Claude

**Option A — as a Skill (Claude.ai Skills / Claude Code / API):**
Upload `chinese-design-reference.skill` (the packaged zip) where your Claude environment accepts skills, or place the folder in your skills directory. Claude auto-triggers on relevant tasks.

**Option B — as Project knowledge (any Claude.ai project):**
1. Project files: upload `SKILL.md` plus everything in `references/` (the 12 markdown files + CSV). Skip `assets/` — images and the atlas add size without helping text retrieval; open the atlas locally when you need to see the works.
2. Project instructions — paste this block:

```
This project includes a Chinese design reference library (SKILL.md + reference files).

Rules:
1. Before any Chinese design, typography, calligraphy, seal, or cultural-content task, read SKILL.md and follow its routing table to load at most two relevant reference files. Never load the whole library.
2. Respect the evidence labels: (A) documented fact, (B) visual observation, (C) scholarly interpretation, (D) design application. Never present C or D as documented fact, and never present the client's design preferences as historical precedent.
3. Follow the eight standing rules in SKILL.md (attested character forms only; no stroke-order reconstruction from appearance; no decorative "squiggles"; no universal symbolism claims; display lettering ≠ body typography; regional over generic; check image licences; read each module's Gaps section).
4. For anything involving the surname 齊/齐, always read references/qi_character_dossier.md first.
5. Before delivering design output, run the relevant checks in references/evaluation_sheet.md.
```

## Use in ChatGPT

ChatGPT does not auto-trigger skills. Two workable setups:

- **Custom GPT:** create a GPT, paste the SKILL.md body (minus the frontmatter) into its Instructions, and upload the files in `references/` as Knowledge. Retrieval works, though less predictably than Claude Projects.
- **Any chat:** paste the SKILL.md body at the start of the conversation, then attach only the one or two reference files relevant to the current task. Re-attach in new chats — knowledge is not persistent.

## Use in Grok

Grok has no persistent file-knowledge or skill mechanism. Per conversation: paste the SKILL.md body (or the short "Rules" block above) into the first message or Custom Instructions, then attach the relevant reference file(s). Keep attachments to one or two modules per task — that is how the library is designed to be used.

## Licensing

- **Text of this library:** free to share and adapt with attribution.
- **Images in `assets/images/`:** individually licensed — public domain, CC0, or NPM Open Data CC BY 4.0. The licence and required attribution for each file are in `references/assets_register.csv` (match by item ID = filename). Museum possession of an object does not by itself grant reproduction rights; the register records reuse conditions per item.
- **Fonts referenced** (Source Han, Noto, LXGW WenKai) are SIL OFL; see module 08 for the verified table.

## Status and gaps

First edition, compiled 2026-11-07. Known gaps are listed in SKILL.md and in each module's "Gaps and limitations" section. Contributions of documented, licensed material are welcome — preserve the evidence labels and never fabricate provenance.
