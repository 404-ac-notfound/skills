# The revision handoff

Give the recipient one brief they can act on without the review chat. “Rage” is the name of the handoff. The voice can be dry. The instructions must be precise. Every imperative should change the work or protect a choice that matters.

## Establish the toolchain

1. **Find the origin.** Read the production notes, file metadata if visible, version history, source files, and recorded generation prompts or export history. Name the originating platform, model, and mode at the level the evidence supports. An export application may identify the exporter alone. Visual or prose mannerisms cannot identify the generator. Mark unknown origin when it remains unknown.
2. **Identify where the revision happens.** Distinguish the tool that made the draft, the app reading it now, and the app or person who will make the repair. Use the project-approved route and the actual available source files. An image generator, a native layout app, and a text model need different handoffs.
3. **Verify current capabilities before prescribing tool-specific steps.** Open the current official documentation or release notes for the relevant surface, version, and model. Check the active mode when visible. Verify only what affects the repair, such as whether the reviewer sees embedded images, which input supports region editing, whether a layer can be preserved, what output is actually editable, or whether an upload is visible outside the project. If origin and revision use different platforms, check the originating tool's constraints where they affect the source you can recover. Cite the relevant official page and verification date in the review notes. If current capability or version cannot be verified, give a tool-neutral handoff or a documented route. Ask about the platform only if the repair depends on the answer.

### Where to check

These are starting points. Reopen the relevant page at review time. Confirm the UI, plan, or API that the recipient can actually use.

| Surface | What to verify |
| --- | --- |
| Claude Projects or Claude Code | Project instructions and knowledge visible to this chat. Verify whether the uploaded file exposes rendered pages or only text. For a layout review, use the actual PDF pages or image exports the selected surface can see. [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), [Claude file upload and visual processing](https://support.claude.com/en/articles/8241126-upload-files-to-claude). |
| Kimi | Verify the selected mode's file understanding and editable output for the necessary format. [Kimi model selection and file handling](https://www.kimi.com/en/help/new-user-guide/agentic-chat). |
| ChatGPT or ChatGPT Images | Verify visual PDF retrieval for the actual upload location and plan. For image edits, verify selection support and request a comparison of the returned image with protected regions. [Visual Retrieval with PDFs](https://help.openai.com/en/articles/10416312), [ChatGPT Images editor](https://help.openai.com/en/articles/11084440-chatgpt-image-libraryopenai). |
| Midjourney, Gemini, or Grok Imagine | Verify reference image, region, layer, and export support for the exact surface. A consumer editor and an API may have different controls or privacy behavior. [Midjourney Editor](https://docs.midjourney.com/hc/en-us/articles/32764383466893-Editor), [Gemini image capabilities](https://ai.google.dev/gemini-api/docs/image-generation), [xAI image editing API](https://docs.x.ai/developers/model-capabilities/images/editing). |
| InDesign or other native layout | Check the native source, existing image links, page and spread behavior, and the printer's preflight requirements. [Adobe print-ready PDF workflow](https://helpx.adobe.com/indesign/desktop/print/print-production-and-file-creation/produce-print-ready-pdf-files.html). |

## Decide where to take control

- **Specify the exact change** when the acceptable result is narrow or a downstream dependency needs it. Give a locator, replacement, and outcome for a fact, quote, name, glyph, date, term, heading, consequential page turn, repeatable layout rule, or technical specification. Use measurements from the project. For an image that must retain exact lettering, geometry, or a protected region, use editable type, a linked asset, or another verified controlled method when generation cannot guarantee it.
- **Set the effect and give latitude** when several good solutions exist. State what the reader should notice, know, or feel, what must be preserved, and where creative judgment is welcome. For pacing, image selection, shot direction, or voice, a testable effect gives the maker room to solve the real problem.
- **Combine them** where needed. “Move the portrait to the reveal spread. Keep the verified date and names. Choose the crop that makes her hesitation readable at page size.” Exact page, exact facts, creative crop. Check the neighboring spreads after the move.

## Write one paste-ready block

Open with the asset, exact revision, audience or destination, and assignment. Put changes in working order. Include the project rules the recipient needs, stable locators, concrete replacements where available, and the choices the recipient can make. Close with the requested return artifact and a check which demonstrates the work fits as a whole. Name unresolved evidence or scope when it affects what can be delivered. Use only references and project material the recipient is authorized to receive. Keep any sourcing commentary outside the block unless the recipient needs a source to execute the change.

For a human, use production vocabulary they recognize. For an AI, specify the input files or attached references and the verified surface's controls, only as relevant. For a new render, ask to see the consequential edit in context. For a local fix, ask for the affected area and enough of its surroundings to confirm the repair. When the verdict is KILL, give the stop order and the evidence or change of premise that would justify recommissioning. A PUBLISH judgment needs no handoff.

The following handoff repairs a premature image reveal in a fictional print chapter.

```text
Revise the print proof for Chapter 6, revision 4. The school portrait has given away the one thing the reader came to discover.

1. Move the portrait from the opening spread to the spread where Mina identifies the girl. Anchor it after “I knew that ribbon.” Use the existing cleared portrait file and its approved caption.
2. Let the opening build toward recognition. Keep the narrator's short sentences and the original first-person point of view. Choose the crop on the new spread so the ribbon registers before the caption. Preserve a clear gutter using the printer's spec.
3. Return the revised chapter proof with the opening spread, the reveal spread, and the following spread in sequence. Check that a first-time reader meets Mina before seeing the portrait and that the next spread still reads cleanly after the move.
```
