# Platform Notes

Last refreshed: 2026-09-04.  
These are working baselines, not law. Re-verify official docs or the live UI when a limit is load-bearing. If a number here disagrees with the field in front of the user, the field wins — update this file.

How to use: pick the destination section, confirm the cap/surface, then write. Do not treat this as an Imagine-only manual.

---

## ChatGPT

- **Custom Instructions (paid: Plus/Pro/Business/Enterprise/Edu):** 5,000 characters as of 15 Jul 2026 (was 1,500). Two-field setups still appear in older writeups at 1,500 each — check the live Personalization screen.
- **Custom Instructions (Free/Go):** ~1,500 characters.
- **Project instructions:** OpenAI does not publish a hard number. Practical working target ~8,000 characters. Overflow goes in project files. Project instructions override global custom instructions inside that project.
- **Project files:** Free 5 / Go+Plus 25 / Edu-Pro-Business-Enterprise 40 per project (help center). Upload 10 at a time.
- Compress instructions. Files hold corpus.

## Claude

- **Profile / account instructions:** ~1,500–2,000 characters (third-party; confirm on claude.ai).
- **Project instructions:** ~8,000 characters practical. Anthropic does not always publish a hard cap. Keep them short anyway — they tax every turn.
- **Project knowledge:** files; paid plans can flip to RAG when the project fills. Free: max 5 projects.
- **CLAUDE.md (Claude Code):** no hard cap. Aim 1k–2.5k words. Loaded at session start.
- Context windows vary by model (200K default; paid chats on current flagships much larger). Instructions still should stay tight.

## Gemini

- **Gem instructions:** often cited ~2,000 characters; Google does not always publish a hard cap. Shorter Gems follow more consistently. Structure as Persona / Task / Context / Format.
- **Gem knowledge files:** 10 files, 100 MB each (Google upload limits).
- Gems cannot be used with Gemini Live (as of latest help text).
- Tight beats long. If it will not stick, split into two Gems rather than one essay.

## Kimi

- **Project instructions:** exist as plain text per project. Official help says the character cap scales with plan — check the membership page at write time. Do not invent a number.
- **Project files:** max 50 files, 100 MB each; read on demand, not fully preloaded.
- **Project quotas:** Free 2 projects / 500 MB; Go+Pro 20 / 20 GB; Max+Ultra 100 / 50 GB (help center 2026-09).
- **Agent context:** documented as 256K characters on the Agent limits page.

### Kimi Agent Swarm (verified 2026-09-27)

- **Surface:** https://www.kimi.com/agent-swarm or Kimi App model switch → **K3 Swarm**. Not the same product as regular Agent or Deep Research.
- **Model:** Help Center says Swarm is powered by Kimi K3 (product label: K3 Swarm). Architecture claim: up to 300 sub-agents, 4,000+ tool calls, main agent ~15 oversight steps. The 4.5× claim is for parallelizable search/batch work, not every task.
- **Membership:** Moderato includes Swarm; Kimi Claw does not start at Moderato. Swarm credits cost several times a regular Agent task. Moderato list: ~25 Swarm uses, 2 concurrent Swarm subtasks.
- **Write for it like a CEO brief, not a chat turn:** one clear outcome, work that actually splits, source-ranking, success criteria, output file list, stop rules. Independent specialists + forced reconciliation.
- **Good:** wide retrieval, batch collection, multi-file packs, long-form compilation, parallel coding/review, office file dumps.
- **Bad:** single-thread judgment, tiny questions, fiction, tasks that cannot split. Ambiguous briefs collapse into fake parallelism.
- **Outputs:** real files (md/docx/pptx/xlsx/code folders), not just a chat essay.

## Grok Chat / Projects / Agents

- **Custom instructions:** reported range 4,000–12,000 depending on layer and date (cut to ~4k with Custom Agents, some sources say 12k restored). Verify in Settings → Customize before writing a block that must fit.
- **Custom Agents:** 4 slots; instructions often cited at ~4,000 characters each.
- **Grok Projects / Workspaces:** instruction field + files. No stable public cap found — keep instructions short, put corpus in files. Do not dump a constitution into Imagine Agent just because a Grok Project exists.
- **Grok Build / AGENTS.md:** no character cap; loaded in full; keep focused.

## Grok Imagine (image & video)

Two consumer surfaces. Do not mix them up.

### Quality / Fast bench (`grok.com/imagine` generator)

- Image 2.0 is Quality Mode (Aug 2026). Stronger instruction following, typography, edits.
- Set **aspect** and **Quality/Fast** and **variation count (2 / 4 / 8 / 12)** while the box is empty when those toggles are visible.
- Attaching a reference often switches the path toward edit and can hide Quality/Fast toggles. Decide toggles first, refs second — or text-only for shape hunts.
- Up to 5 reference images on Image 2.0 consumer edits.
- Remove Background exists on the post/edit path. Prefer a clean silhouette on the shell color, then cut out. Do not bet the file on the model inventing real alpha from the words "transparent background."
- Prompt shape: subject → environment → camera/light → style → short avoids.
- Over-negating a famous logo makes the model clone it. Describe the object you want.

### Imagine Agent / New Project canvas

- Different product: producer on an open canvas. Template chips include Historical Stories, Create Worlds, Short Film, UGC Product Stories, Brand Identity.
- Good for a locked visual system across many frames after a keeper exists.
- Bad first door for a single PWA mark — it will build a world.
- No Quality toggle once a ref is attached (field-confirmed 2026-09-04). You can ask for N variations in the prompt text; that is count, not Quality Mode.
- Do not tap template chips for icon/mark work. Empty canvas + factory rules ("one 1:1 mark per run, no pages").

### Video

- Video 1.5: ~1–15s; name one camera move; add a Sound: line when it matters. Native 1080p on supported T2V/I2V paths; reference-to-video often capped lower.

## Grok Build Mode

- Consumer builder inside Grok: websites, apps, games, dashboards; preview in-chat; publish to grok.me.
- Prompt: type + core function + screens + usage context (mobile-first, palette). Stage large apps.
- Phone apps: test pass + iOS/Android Add to Home Screen steps + icons/manifest.
- Not the same tool as Imagine Agent.

## General

When a field is tight: cut fluff, examples, and decorative markdown. Short imperatives. Corpus lives in files. Behavior lives in instructions.

If this file is missing a destination the user named, research it that turn and add a dated stub here.
