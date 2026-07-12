# Director-Led Agents

Use this when the card art department needs stronger internal collaboration, more taste, better series consistency, or generation-result diagnosis. This is an internal operating model, not a user-facing meeting transcript.

## Principle

The department is director-led, not committee-led.

The Creative Director Agent owns taste and final coherence. Other agents may explore, translate, and check, but they do not override the theme soul, aesthetic declaration, exaggeration/restraint rules, or rejected bland direction.

## Agent Chain

Use this chain for full deck, faction, worldbuilding, or generated-image review work:

1. **Creative Director Agent**
   - Input: user lore, card list, character direction, reference images, user taste feedback.
   - Output: theme soul, charming contradiction, aesthetic declaration, exaggerate, restrain, memory hook, rejected bland direction.
   - Gate: if this is generic, stop and sharpen it before continuing.

2. **Worldbuilding Agent**
   - Input: Creative Director judgment plus user lore.
   - Output: visual-world rules: power source, faction belief, habitat, body logic, social structure, props, repeated symbols, taboos.
   - Gate: keep only worldbuilding that changes the image.

3. **Visual DNA Agent**
   - Input: Creative Director judgment and visual-world rules.
   - Output: silhouette language, costume/body structure, motif system, palette, lighting, background rule, large readable blocks.
   - Gate: every deck needs 3-6 recurring visual rules and 3-6 prohibited drift directions.

4. **Single Card Director Agent**
   - Input: card name, role, rules text, theme DNA.
   - Output: one visual event per card: subject, action, prop, camera, background, card-size priority.
   - Gate: adjacent cards must not have the same pose, same camera, same prop emphasis, and same background logic unless intentionally paired.

5. **Prompt Engineer Agent**
   - Input: locked visual direction.
   - Output: one clean English AI prompt plus Chinese translation.
   - Gate: prompt must use concrete visual words, no field labels, no model parameters, no project-internal proper nouns, no unreadable text dependence.

6. **Generation Review Agent**
   - Input: generated image or failed prompt result.
   - Output: missing, wrong, unexpected, likely cause, revision action.
   - Gate: diagnose before rewriting. Do not blindly add adjectives.

7. **Final Creative Director Pass**
   - Input: all prompts or image-review revisions.
   - Output: keep, revise, or reject.
   - Gate: each card must still serve the theme soul and memory hook.

## Default User-Facing Output

Do not show internal agent dialogue. Collapse the chain into:

```markdown
## 0. 美术总监判断
## 1. 世界观图像核心
## 2. 主题视觉 DNA
## 3. 单卡/角色 Prompt
## 4. 统一负向提示词
## 5. 生成后看图重点
```

For generated-image review, use:

```markdown
## 美术总监结论
## 偏移诊断
- 缺失：
- 错误：
- 意外：
- 可能原因：
## 修改方向
## 修订 Prompt
```

## Difference Checks

Before finalizing a deck, scan for sameness:

- Same subject pose repeated too often.
- Same camera angle repeated too often.
- Same "glowing circle behind character" solution repeated too often.
- Same color accent used without card-specific reason.
- Same background stage for cards that should have different events.
- Prompts that only swap animal/weapon names but keep the same sentence structure.

If sameness is found, revise at the Single Card Director stage, not by adding adjectives at the Prompt Engineer stage.

## When To Use Real Parallel Subagents

Use real subagents only for large or high-risk work:

- 30+ cards.
- Multiple factions in one request.
- A full world bible plus prompts.
- Reviewing many generated images.
- Forward-testing skill behavior.

Do not use parallel subagents for normal single-deck prompt files unless the user asks. Parallel agents can improve coverage but can also fragment taste. The main agent must always run the final Creative Director pass.

## Review Rubric

Score each deck or generated-image batch mentally:

- Soul: does the deck have a memorable fantasy beyond category labels?
- Coherence: do all cards belong to the same visual world?
- Differentiation: can neighboring cards be told apart at thumbnail size?
- Card action: does each image feel like a card appearing or activating?
- Prompt cleanliness: can an image model follow the prompt without internal jargon?
- Drift resistance: are the most likely wrong outputs explicitly blocked?

If two or more answers are weak, revise before final delivery.
