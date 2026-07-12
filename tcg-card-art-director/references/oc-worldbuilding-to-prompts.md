# OC Fantasy Worldbuilding To AI Prompts

Use this when the user gives worldbuilding, factions, card decks, character concepts, or story fragments and expects the card art department to help build a coherent original fantasy/OC visual world before writing AI prompts.

## Core Position

The department is not only formatting card briefs. It should translate story material into a usable visual world:

- what kind of world this is
- what powers or technology shape it
- what factions believe and build
- what characters look like because of that world
- what recurring symbols, costumes, tools, bodies, colors, and environments make the setting recognizable
- how those decisions become clean AI prompts

The final deliverable may be a complete file, but the user's main reading target is usually the AI prompt. Keep worldbuilding concise and directly useful for image generation.

## Prompt-First Document Shape

For full card/deck/character requests, use this order:

0. **美术总监判断**
   - Define theme soul, charming contradiction, aesthetic declaration, what to exaggerate, what to restrain, memory hook, and rejected bland direction.
   - This section should be short but decisive. It gives the work taste before it becomes a prompt list.

1. **世界观图像核心**
   - One paragraph that defines the fantasy, era, power source, conflict, and image tone.
   - Keep it short; do not write lore prose unless asked.

2. **阵营/主题视觉 DNA**
   - 3-5 visible rules: silhouette, clothing/armor, motifs, tools/weapons, body features, environment language.
   - State what to enlarge for card readability.
   - State what to avoid.

3. **角色/卡图识别点**
   - For each important subject: identity, body/face, outfit, motif, props, action, scene, colors, highlights.
   - Mention only elements that should affect the image.

4. **AI 绘图提示词**
   - Put the English prompt near the card/character direction, not buried after long briefs.
   - Add `中文释义：` directly below.
   - Use the simplified prompt hierarchy from `midjourney-prompting.md`.

5. **生成后看图重点**
   - 3-6 short checks: subject, silhouette, action, prop, background, color.
   - This replaces long default outsourcing sections unless the user asks for a painter brief.

## Worldbuilding Compression

Convert lore into image rules:

| Lore Question | Visual Translation |
| --- | --- |
| What is the power source? | glowing core, crystal color, ritual node, engine, fungus network, wind trail |
| What is the faction's social structure? | uniform, rank mark, luxury level, tool quality, body posture |
| What do they build? | architecture, vehicles, armor, weapons, everyday objects |
| What do they fear or desire? | defensive posture, hidden parasite, overgrown lab, broken border, watchful eyes |
| What is their environment? | sky deck, root shelterbelt, imperial greenhouse, palace workshop, border island |
| What should repeat across cards? | silhouette block, color accent, emblem shape, light source, recurring prop |

Do not include worldbuilding that does not change the image.

## Default Full File Sections

Use this compact structure for deck or faction work:

````markdown
# {主题名} 卡图与 AI Prompt 设计

## 0. 美术总监判断
- 主题灵魂：
- 最迷人的矛盾：
- 审美宣言：
- 必须夸张：
- 必须克制：
- 一眼记忆点：
- 本次拒绝的平庸方向：

## 1. 世界观图像核心

## 2. 主题视觉 DNA
- 主体轮廓：
- 服饰/身体结构：
- 道具/武器/工具：
- 场景语言：
- 色彩与光：
- 禁止偏移：

## 3. AI Prompt 总规则
- 英文 prompt 顺序：
- 中文释义规则：
- 背景简化规则：
- 卡面可读性：

## 4. 单卡/角色 Prompt
### {卡名或角色名}
- 设计判断：
- 识别点：
- 动作与场景：
- 色彩与高光：

```text
English prompt...
```
中文释义：...

- 看图重点：
  - 主体是否准确：
  - 轮廓是否清楚：
  - 动作是否像卡牌登场/发动瞬间：
  - 背景是否过碎：
  - 颜色和高光是否能一眼识别：
````

Only add artist brief, review tables, or iteration logs when the user asks for them or when reviewing generated images.

## What To Avoid

- Do not make the user read a long production document before reaching prompts.
- Do not default to outsourced artist brief.
- Do not over-explain rules text.
- Do not turn every card into a mini essay.
- Do not make prompts generic by stripping out all world-specific visual decisions.
