# TCG Card Art Director

Director-led Codex skill for TCG card illustration direction, OC/faction visual worldbuilding, and clean AI image prompts.

This repository packages the skill as a reusable folder:

```text
tcg-card-art-director/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
```

## What It Does

- Turns card lists, factions, characters, and story concepts into card art direction.
- Builds a compact visual world before writing prompts.
- Uses an internal creative-director-led workflow instead of a mechanical prompt template.
- Writes clean English AI image prompts with Chinese explanations below each prompt.
- Checks prompts for common pollution such as model parameters, field labels, internal proper nouns, and vague quality words.

## Typical Triggers

```text
卡图设计部设计这个卡组
卡图设计部用总监制 agents 设计这个角色
用 tcg-card-art-director 给这张卡做 AI 绘图 prompt
审核这张生成图哪里偏了，并改 prompt
优化卡图设计部的提示词规则
```

## Install Locally

Copy the `tcg-card-art-director` folder into your Codex skills directory:

```text
C:\Users\<you>\.codex\skills\tcg-card-art-director
```

Restart Codex or open a new task so the skill metadata is refreshed.

## Validate

Run the prompt hygiene checker against any generated Markdown card-art document:

```powershell
python .\tcg-card-art-director\scripts\validate_card_art_prompts.py .\path\to\card-art-doc.md
```

Run Codex skill validation after changing the skill:

```powershell
python <codex-skill-creator>\scripts\quick_validate.py .\tcg-card-art-director
```

## Publishing Notes

Keep private card lists, unpublished worldbuilding, local screenshots, `.docx` files, and absolute machine paths out of this repository unless you intentionally want to publish them.
