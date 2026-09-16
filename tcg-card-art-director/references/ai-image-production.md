# 《域·维度战争》AI 生图生产闭环

Use this only when the user explicitly asks for multi-round AI generation, prompt batches, candidate selection, image review, targeted editing, or production records. It is model-agnostic: adapt the final command to the user's chosen image tool, but keep the production logic unchanged.

## Core Principle

An AI prompt is not the art brief. First lock a short visual contract, then use generation to test one visual decision at a time. Do not ask one image generation to solve identity, pose, camera, story, palette, material, and background density all at once.

## 1. Visual Contract Before Generation

Every card needs these fields before its first batch:

- **Rules snapshot and status:** design ID, version, complete card text, card type, attribute, role, and whether the card is Draft/Test or safe for final-art production.
- **Fixed anchors:** three to five visible facts that must survive every variation, such as the subject silhouette, core prop, action, attribute cue, and card-type composition control.
- **One-batch variable:** the single primary decision being explored now: silhouette, action, camera, story beat, or environment. Do not vary all of them together.
- **No-go list:** wrong type reading, forbidden world drift, obscured face/body/prop, readable text, frame conflict, and any rule implication the card does not have.
- **Acceptance checks:** what must be readable at thumbnail size and what makes an image eligible to become the reference for the next pass.

If rules, type, or attribute are unknown, label the batch as concept exploration. Do not call the result final or use it as evidence for a fixed setting.

## 2. Three-Pass AI Workflow

### Pass A: Explore

Generate a small batch of composition thumbnails. Each route has one job:

- **Route 1 — identity/silhouette:** tests the subject's large shape blocks and key prop.
- **Route 2 — action/camera:** tests the strongest card-entry, attack, defense, command, or activation moment.
- **Route 3 — story/field:** for 域痕, tests trigger → change → consequence; for 域主/域灵, tests the cleanest supporting domain stage.

Keep the fixed anchors identical across routes. State each route's test in Chinese before its prompt. A batch is successful when at least one image proves the intended visual idea, not when all four images look polished.

### Pass B: Lock and Refine

Select one candidate for its composition and readability, not merely because it has the most texture or dramatic effects. Record the selected image or seed/reference ID when the tool supports it.

Use the selected candidate as a composition or character reference only after it passes the visual contract. In each refinement pass, change one or two named failures: for example, "make the staff readable" or "clear the lower text area." Do not rewrite the entire prompt after a near miss.

### Pass C: Finish and Card QA

Use local editing, inpainting, outpainting, or a targeted re-generation only to solve remaining named defects. Then check the actual crop/template, not an imagined frame.

Required checks:

- thumbnail: first read is the intended character or event;
- crop: face, action, key prop, resonance geometry, and card-type cue avoid frame/text zones;
- hierarchy: character cards retain clean supporting stages; trace cards retain one decisive event;
- consistency: palette, material, and motif fit the series without becoming a copied external style;
- production record: model/tool, final prompt, reference asset or seed when available, and export filename are retained with the approved image.

## 3. AI-First Output Package

For a normal single-card request, produce the smallest package that enables the next image pass:

1. **Visual contract** — fixed anchors, one-batch variable, no-go list, acceptance checks.
2. **Explore routes** — three compact Chinese test intents and their clean English prompts with Chinese translations.
3. **Selection rule** — what makes a candidate eligible for Pass B.
4. **Production prompt** — one locked prompt after a candidate is chosen; do not pretend it is already approved if no image exists.
5. **Repair prompts** — only when a generated image is supplied; each repair names the defect and the precise change.

For a full deck, add a batch plan that distributes silhouette, camera, action, and background logic before any image is generated. Do not make every card use the same three routes.

## 4. Diagnosis Rules

Diagnose before changing prompts:

- **Missing:** a fixed anchor never appears. Front-load it and remove competing nouns.
- **Wrong:** an anchor appears in the wrong form. Describe its drawable geometry, scale, placement, and material more concretely.
- **Unexpected:** the model adds clutter, a second subject, text, or imported visual language. Simplify the background and state what the image should prioritize instead.
- **Composition failure:** the subject is small or card text areas are busy. Change camera, physical subject placement, or low-detail region; do not add quality words.
- **Three failed passes:** return to the visual contract and reduce the number of fixed anchors. Do not keep stacking exclusions.

## 5. Boundaries

- AI exploration does not authorize changes to card text, attribute, type, or setting.
- Never claim a visual direction is locked without a selected image or explicit user approval.
- Do not use an external game's style, characters, frames, symbols, or named visual identity as an AI reference shortcut.
