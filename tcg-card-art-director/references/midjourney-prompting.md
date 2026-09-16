# Midjourney Prompting For Zone War Card Art

This reference distills transferable Midjourney prompt practices from `justinperea/midjourney-cc-skill` and Midjourney's official prompt/parameter guidance, then adapts them to TCG card illustration production.

Sources:
- Midjourney prompt basics and parameters: https://docs.midjourney.com
- Midjourney prompt engineering skill source: https://github.com/JustinPerea/midjourney-cc-skill

## Core Rule

Midjourney is not an art brief reader. It responds best to a short, front-loaded visual prompt with concrete nouns and actions. Keep the full art direction in the card brief, then compress only the visible decisions into the prompt.

Use "clear subject description" as the first rule. The prompt should state what is on screen before it states how impressive it feels. Avoid adjective piles. One precise feature is better than three vague style words.

## Visual Reasoning Before Prompting

Before writing the final prompt, use this structure internally to select visible content. Ordinary delivery is only one English prompt and its Chinese translation. Show the Chinese reasoning block only when the user requests an explanation or full brief.

1. 用户管理的情绪板与风格参考
   - Do not set medium, rendering treatment, art style, or mood inside the ordinary prompt. The user controls them with their own Midjourney moodboard.
   - Translate only the card's visible content into the prompt: subject, anatomy or shape, costume or natural covering, props, action, scene hierarchy, camera, lighting, color relationships, and card-frame readability.
   - If the user provides a moodboard and explicitly asks for a full MJ command, keep its reference parameter separate from the content prompt. Do not describe it as another game's style or copy characters, poses, costumes, logos, or signature motifs.

2. 画面主体深度刻画
   - Specify visible identity: body shape, face, eyes, hairstyle or equivalent creature features, costume or natural covering, held objects, and large readable design blocks.
   - Tie every important design choice to the card name, faction, gameplay role, and species/object source.
   - Replace vague words like "cute", "cool", "forest warrior" with visible features such as "round glowing seed eyes", "layered leaf cloak", "slender twig limbs", "pinecone backpack".
   - Describe clothing and equipment in plain parts: helmet, collar, cloak, sleeves, belt, armor plates, skirt, boots, gloves, shield, rifle, staff, backpack, pouch.
   - Describe motifs as visible marks: leaf-shaped embroidery, red flow lines, hollow diamond halo marks, bark cracks, sand-dune stripes, gear teeth, root knots.
   - Describe action as a verb plus object: raising a shield, loading a rifle, pulling a wounded ally up, planting roots, swapping positions, firing a flare.
   - Push subject readability through large shape blocks: bigger hair mass, larger leaf crown, larger cloak, larger shoulder armor, bigger weapon head, brighter core, larger eye highlights, or a cleaner head silhouette.
   - For cute or mascot-like subjects, make the silhouette toy-like: compact body, oversized head or crown, simple limb shapes, large eyes, one clear prop, and a single readable pose.
   - Do not use identity-comparison shortcuts to describe gender, temperament, or social reading. These phrases pollute generation and are less controllable than visible features. Rewrite them as drawable traits: soft facial lines, narrow jaw, slim frame, narrow shoulders, flat chest, long hair, loose collar, wide sleeves, bare feet, reserved expression, precise hand pose.

3. 环境构建与氛围
   - Describe a concrete place, not a generic background.
   - Include at least one gameplay-relevant environment cue: battlefield lane, resonance nodes, domain energy, shelterbelt rows, root tunnels, aircraft deck, classroom, ruins, etc.
   - Define light and palette: warm afternoon sand light, cyan-green root glow, dusty backlight, muted sage green and copper bark, high-rarity dramatic rim light.
   - Keep atmosphere practical: time of day, weather, main light direction, and 2-4 dominant colors.
   - When the subject has many small details, simplify the background into a colored energy stage, clean domain platform, circular summoning field, or broad color gradient. Do not average-fill the image with small branches, leaves, wires, rubble, spores, or particles.
   - For green or forest themes, use a green energy stage or simple root platform behind the subject instead of dense tree-branch detail unless the card specifically needs a forest environment.

4. 专业摄影语言 / 构图镜头
   - Prefer medium-wide or wide compositions. For character cards, describe a full-body view with feet, key props and open action space inside the frame. For trace cards, describe the distance between participants, event and setting so the story remains legible. Choose the camera angle independently; a low angle does not require a close crop.
   - State card-frame readability as physical composition, not a vague request: "main face and weapon in upper half", "lower quarter low-detail", "formation nodes not behind text area".
   - Use direct framing words such as "medium-wide full-body view", "wide side view", "entire figure inside the frame", and "open space ahead of the leap". Avoid contradictory instructions such as "full body" together with "waist-up", or "wide shot" together with "face fills the frame". Use close-ups only for a specific visual need or user request.
   - Prefer card-entry or activation moments over quiet illustration moments: the subject appears, lands, raises a weapon, releases energy, blocks, fires, commands, transforms, or activates a core.
   - Require visible separation: strong outer contour line, rim light on shoulders/head/weapon, bright eyes or core highlights, and a background value that does not merge with the subject.

Optional reasoning output for a requested explanation or full brief:

```markdown
### 构思与推导
- [画面任务]：
- [主体特征]：
- [服饰/纹样/物品]：
- [动作事件]：
- [场景搭建]：
- [视角构图]：
- [色调光影]：
- [轮廓高光]：
- [卡框安全]：
```

## Simplified TCG Prompt Shape

Use this structure by default. It follows the common AI image prompt hierarchy while removing fixed Material, Style, and Quality layers.

```text
{main subject}, {body shape and face/head details}, {clothing, armor, natural covering, motif or pattern}, {held objects or props}, {card-entry or activation action}, {specific environment or simplified energy stage}, {composition}, {camera angle}, {light direction, rim light, eye/core highlight}, {high-saturation high-contrast color palette}, {output/readability cue}
```

Recommended order:
1. Subject.
2. Body and face/head details.
3. Clothing, armor, natural covering, motif, or pattern.
4. Held objects or props.
5. Action.
6. Environment or simplified energy stage.
7. Composition.
8. Camera angle.
9. Lighting, rim light, eye/core highlight.
10. Color palette and contrast.
11. Output/readability cue.

Do not add separate Material, Style, or Quality layers by default:
- Material: include only when it is a required visible identity cue, such as white ceramic armor, bark skin, glass vial, bronze gear, or paper wing.
- Style: omit by default. The user controls style through their own moodboard; include a reference parameter only when they explicitly request a full MJ command.
- Quality: do not use prestige words such as `masterpiece`, `best quality`, or `ultra-detailed`.

For TCG card art, never rely on tiny text inside the image. A brief "no readable text" cue may be used; provide a separate negative prompt only when requested.

## Card-Type Framing Rules

Use these as prompt-composition instructions, not as a request to reproduce another game's style or visual identity.

Apply "Single-Card Picture Control" in `zone-war-art-bible.md` before encoding the composition. Front-load the character's concrete appearance and one visible action. Give necessary effect cues a subordinate position and contrast; leave out secondary rules clauses that introduce another time, action, or focal subject. Translate mechanics into visible shapes and spatial relationships, not terms such as "resonance spirit" or "extra energy cost" alone. Do not depict a tax as a complete stop or a hand return as revival.

- For **域主、普通域灵、共鸣域灵**, front-load the character or creature. Describe one dominant figure, its face/head, large silhouette block, prop, and active action before the setting. Ask for a clean energy stage or only one to three supporting domain cues; keep the background lower-detail and lower-contrast than the subject.
- For **共鸣域灵**, describe nodes and formation geometry as framing or orbiting evidence around the figure. Do not make a floating diagram the main read.
- For **通常域痕、结界域痕**, front-load the event and its consequence. Prompt a visible trigger, central change, and affected place or secondary reaction, so the image reads as a small story. The scene can contain more environment than a character card, but must retain one decisive focal action.

## Natural Zone War Prompt Shape

For production prompts, do the structure in the reasoning, not in the final prompt text. The final prompt should read like one polished visual instruction line, not a form with labels.

```text
{plain subject identity}, {visible body shape, face or head design with large readable shape blocks}, {clothing, armor, natural covering, motif or pattern}, {held objects and important props}, {one summoning, activation, attack, defense, or transformation action}, {simplified energy stage or clean domain platform with only a few background objects}, {composition and subject position}, {camera angle and motion path}, {light direction, outer contour line, rim light, bright eyes or core highlight}, {2-4 high-saturation colors with strong value contrast}, {face, action, weapon or symbol readable at card size, no readable text}
```

Use this structure when the user asks for "高级", "结构性", "MJ", "Midjourney", "V8.1", "完整 prompt", "AI 绘图提示词", or production-ready card art prompts.

Do not put label words such as `SUBJECT:`, `GAMEPLAY EVENT:`, `ENVIRONMENT:`, `COMPOSITION CAMERA:`, `STYLE MEDIUM:`, `PALETTE MATERIAL LIGHT:`, `CARD READABILITY:`, or `QUALITY:` into the final prompt.

Do not put model parameters such as `--ar`, `--raw`, `--s`, `--c`, `--v`, `--style`, `--no`, `--sref`, `--oref`, `--iw`, or their numeric values into the final prompt unless the user explicitly asks for a parameterized MJ command. If parameters are useful, provide them in a separate "参数建议" line.

Do not put project-internal proper nouns, card names, character names, faction names, weapon form names, or rules keywords into the final prompt when they are not broadly understandable visual words. Translate them into visible generic descriptors instead.

Do not put social-comparison labels into the final prompt. Write the visual evidence instead: `young adult male with soft facial lines, narrow jaw, slim flat chest, narrow shoulders, long black hair, loose robe collar, wide sleeves, bare feet`.

Examples:
- Use "white armored mechanical angelic vanguard with two yellow energy wings" instead of a character name.
- Use "paired compact six-flanged mace weapons that unfold into light blades" instead of an internal weapon name.
- Use "flintlock-shaped energy rifle" instead of an internal rifle name.
- Use "built-in yellow-white force-field generator" instead of an internal shield name.
- Use "three-point triangular deployment nodes" instead of a numbered game formation name.

Do not use Midjourney multi-prompts or text weights such as `::` when the user's client rejects multiple text prompts. Prefer one single natural-language prompt line.

Do not automatically include `Photorealistic` or `8k` for TCG prompts. Use them only when the requested medium is photography or photoreal CG.

Do not automatically include vague quality words such as `masterpiece`, `best quality`, `ultra-detailed`, `epic`, `stunning`, or `gorgeous`. Physical surface descriptions may clarify identity; linework, shading, medium, and other rendering treatments remain controlled by the user's moodboard unless requested.

## Chinese Translation Under Prompts

After every final English AI prompt, add a Chinese translation line outside the code block:

````markdown
```text
English prompt line...
```
中文释义：中文翻译这里要逐项对应英文 prompt 的主体、外观、服饰/纹样/物品、动作、场景、构图、镜头、光线、色彩、轮廓高光和卡面可读性。
````

Rules:
- The Chinese translation is for human checking, not for AI generation.
- Keep it concise but complete enough to verify the visual intent.
- Do not add new visual elements in the Chinese translation that are absent from the English prompt.
- Do not translate internal lore names back into the English prompt. Internal names may appear in the Chinese explanation if useful for the user, but the English prompt must stay generic and visual.

## Clear Prompt Test

Before finalizing a prompt, check whether it answers these questions:

- Who or what is the subject?
- What is the subject's body shape, face/head, clothing/armor/natural covering?
- What motif, pattern, or faction feature appears on the subject?
- What object is the subject holding or interacting with?
- What exact action is happening?
- Where is the scene?
- From what camera angle is it seen?
- What are the main colors, light direction, and contrast relationship?
- Is the subject separated by strong outline, rim light, eye highlight, or core highlight?
- Is the background simpler than the subject?
- Does the pose feel like a card summoning, activation, attack, defense, or transformation moment?

If the prompt mostly answers with mood words, rewrite it.
If the prompt produces gray-pink, beige, old-paper, or low-contrast output by default, rewrite the palette with higher saturation and stronger value separation.
If the prompt uses a gender-comparison phrase to do the job of actual design description, rewrite it into body shape, facial structure, clothing, hair, posture, and props.

## Zone War Defaults

| Use Case | Parameter Baseline |
| --- | --- |
| Standard card illustration | `--ar 2:3 --style raw --s 150` |
| Strict art-director control | `--ar 2:3 --style raw --s 75-125` |
| High-rarity dramatic art | `--ar 2:3 --style raw --s 200-300 --c 10-25` |
| Early exploration | `--ar 2:3 --draft --s 150 --c 25-40` |
| Series consistency | `--ar 2:3 --style raw --s 150 --sref [style_ref] --sw 150-300` |
| Character/object consistency | `--ar 2:3 --style raw --s 125 --oref [ref] --ow 100-250` |

Use `--q 2` for final detail tests only. Do not use `--q 4` with `--oref`.

## Reference Strategy

### Style Reference

Use `--sref` only when the user has an approved moodboard reference and explicitly asks for a full MJ command. It transfers visual style more than content; it is not part of the ordinary content prompt.

Guidance:
- `--sw 50-100`: subtle influence.
- `--sw 150-300`: useful production range.
- `--sw 400+`: strong influence, higher risk of overriding card-specific identity.

### Omni Reference

Use `--oref` for recurring characters, creatures, artifacts, emblems, or vehicles. It replaces old `--cref` usage in V7-style workflows.

Guidance:
- `--ow 100`: balanced preservation.
- `--ow 200-300`: strong preservation.
- Avoid `--ow 400+` unless identity must dominate the prompt.
- Lower `--s` when `--oref` is important.

### Image Prompt

Use an uploaded image prompt when the user wants similar layout, subject, or colors, not just style. Use `--iw` only when needed:
- `--iw 0.5`: light influence.
- `--iw 1`: balanced.
- `--iw 1.5-2`: strong.

When using a user-provided reference image:
- Translate it into prompt language such as "clean expressive dark ink linework", "layered leaf cloak", "muted sage green palette", "slender twig limbs".
- Add safety negatives if needed: `--no copied mask, identical reference character, copied pose, watermark, signature`.
- Prefer describing the desired design principles instead of saying "same style as this image" inside the production brief.

## Prompt Variants

Provide one clean MJ prompt by default. Provide three controlled variants only when the user explicitly asks for variants, exploration, or a generation batch.

When variants are requested, preserve the same fixed subject anchors across the batch and state the one primary variable each version tests. Once a candidate is selected, use that candidate's seed or reference asset when available and revise only named failures.

1. Faithful Production
   - Lower stylize, clear subject, safer composition.
   - Best for cards that already have a locked role.

2. High-Rarity Drama
   - More dramatic lighting, stronger atmosphere, moderate chaos.
   - Best for 域主, signature cards, boss units, promos.

3. Exploration
   - Uses draft or chaos to search composition and motif options.
   - Best before final art direction is locked.

## TCG Composition Notes

Describe required card-frame clearance as physical empty or low-detail regions, using the actual illustration window when known. The following are optional examples, not a requirement to darken or empty the bottom of every image:

- "main subject centered above the lower third, lower quarter kept low-detail and darker"
- "face and weapon in the upper half, clean atmospheric gradient behind lower text area"
- "large uncluttered negative space along the bottom edge"
- "formation nodes visible around the subject, not behind the card text area"
- "simple green energy stage behind the subject, no dense branch texture"
- "large leaf crown and cloak form two clear silhouette blocks"
- "thick dark outer contour, bright rim light on head and shoulders, glowing eyes and chest core"

For 共鸣域灵, prompt spatial logic directly:

```text
resonance creature as the central array anchor, glowing formation points orbiting on the floor plane, readable tactical geometry, completed pattern implied by linked nodes
```

## Negative Prompt Defaults

Use as a separate negative prompt or exclusion note, not appended to the final prompt line unless the user asks for a full MJ command:

```text
text, words, letters, watermark, signature, logo, UI, border, card frame
```

Add only specific exclusions that matter. Avoid negative phrasing that can be misread as separate unsafe or unwanted words. Prefer saying what should appear instead of relying on `--no`.

## Iteration Framework

After a generation, diagnose before rewriting:

- Missing: what required element did not appear?
- Wrong: what appeared but in the wrong way?
- Unexpected: what appeared that should not be there?
- Hypothesis: which phrase or parameter likely caused it?

Record the selected image, seed, or reference asset when the tool supports it. This is the reproducibility record for the next pass, not a claim that the image is final.

Action guide:

| Problem | Next Action |
| --- | --- |
| All four images miss the concept | Rewrite prompt, front-load the missed subject |
| All four are too busy | Lower `--s`, add `--style raw`, simplify environment |
| One image is close | Use variation or keep its seed/reference direction |
| Style is inconsistent across a series | Add or adjust `--sref` and `--sw` |
| Recurring character/object drifts | Add or adjust `--oref` and `--ow` |
| Composition is too tight | Re-prompt with wider shot or use Zoom Out/editor |
| Card text area is cluttered | Prompt physical low-detail area, not "leave space" |

Soft limit: if three prompt attempts do not converge, return to the art brief and simplify the concept.

## Output Format

By default, deliver only one clean English prompt and its Chinese translation. The fields below apply only to a requested expanded brief or iteration report; parameters require an explicit request:

- Visual Reasoning: the Chinese `构思与推导` block above.
- Intent: what this variant tests.
- Prompt: one clean natural-language prompt line, without label words or numeric model parameters.
- 中文释义: a concise Chinese translation below the English prompt, outside the code block.
- 参数建议: optional, separate from the prompt, only when useful.
- Watch-outs: likely failures and how to iterate.
