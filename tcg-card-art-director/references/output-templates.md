# 输出模板

Use Chinese for Zone War project deliverables unless the user asks otherwise.

## OC Worldbuilding Prompt File

Use this as the default full-file shape when the user provides worldbuilding, faction, deck, or character direction and mainly wants AI image prompts.

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
- 一句话幻想：
- 力量/技术来源：
- 核心冲突：
- 画面基调：

## 2. 主题视觉 DNA
- 主体轮廓：头身比例、发型/冠饰/披风/机体外形等最大识别块
- 服饰/身体结构：衣服、甲胄、自然覆盖物、纹样或身体特征
- 道具/武器/工具：手持物、交通工具、仪式物、机械装置
- 场景语言：这个世界常见的地貌、建筑、能量舞台或战场
- 色彩与光：主色、辅助色、边缘光、眼睛/核心高光
- 必须放大的识别块：卡面缩小后仍要看清的形状
- 禁止偏移：容易跑偏的题材、时代、质感、情绪

## 3. AI Prompt 总规则
- 英文 prompt 顺序：主体 → 特征 → 道具 → 动作 → 场景 → 构图 → 镜头 → 光线 → 色彩 → 卡面可读性
- 中文释义：每条英文 prompt 下方必须有 `中文释义：`
- 背景简化：
- 卡面可读性：

## 4. 单卡/角色 Prompt
### {卡名或角色名}
- 设计判断：
- 识别点：
- 动作与场景：
- 色彩与高光：

```text
{clean English prompt}
```
中文释义：

- 看图重点：
  - 主体是否准确：
  - 轮廓是否清楚：
  - 动作是否像卡牌登场/发动瞬间：
  - 背景是否过碎：
  - 颜色和高光是否能一眼识别：
````

## Series Visual Bible

```markdown
# 《域·维度战争》系列视觉圣经：{系列名}

## 1. 系列定位
- 一句话幻想：
- 游戏身份：
- 情绪承诺：
- 适用卡牌类型：
- 不适用范围：

## 2. 视觉支柱
1. 
2. 
3. 

## 3. 统一风格规则
- 色彩：
- 材质：
- 轮廓：
- 光影：
- 背景/场景：
- 共鸣/域能表现：

## 4. 稀有度升级
- 普通：
- 稀有：
- 高稀有/签名：

## 5. 禁止事项
- 

## 6. 代表卡图方向
| 卡名/概念 | 卡牌类型 | 画面核心 | 视觉风险 |
| --- | --- | --- | --- |
| | | | |
```

## Single Card Art Design Document

```markdown
# 卡图设计文档：{卡名或概念}

## 1. 基本信息
- 所属项目：《域·维度战争》
- 系列/主题：
- 卡牌类型：
- 属性：
- 稀有度目标：
- 游戏角色：
- 当前生产状态：Concept / Sketch / Prompt / Outsource / Review / Final

## 2. 美术总监摘要
{用 2-4 句话说明这张图必须让玩家看见什么。}

## 3. 画面核心叙事
- 主体：
- 动作：
- 冲突/转折：
- 观众第一眼应该读到：
- 不能误读成：

## 4. 构图方案
- 镜头：
- 主体位置：
- 动势：
- 前景/中景/背景：
- 卡框安全区：
- 缩略图识别点：

## 5. 视觉语言
- 色彩：
- 材质：
- 光影：
- 符号/纹样：
- 域能/共鸣表现：
- 背景世界观：

## 6. 与规则的绑定
- 这张图服务的体验：
- 图中必须体现的规则身份：
- 不能暗示的规则：
- 如果卡牌效果改变，需要重画/微调的部分：

## 7. AI 绘图 Prompt
### 构思与推导
- [风格定位]：
- [主体特征]：
- [服饰/纹样/物品]：
- [动作事件]：
- [场景搭建]：
- [视角构图]：
- [色调光影]：
- [轮廓高光]：
- [卡框安全]：

### Prompt Strategy
- 媒介选择：
- 主体识别优先级：
- 必须出现的外观特征：
- 必须出现的服饰/纹样/物品：
- 必须出现的动作：
- 登场/发动瞬间：
- 场景与规则绑定：
- 背景简化规则：
- 视角与构图：
- 主色调与光线：
- 外轮廓/边缘光/眼睛或核心高光：
- 参考图转译：
- 生成模型注意事项：

### 通用 Positive Prompt
```text

```
中文释义：

### 通用 Negative Prompt
```text

```

### Midjourney Prompt Package
#### MJ 版本 A：Faithful Production
- 意图：
- Prompt：
```text
{plain subject identity}, {body shape and face/head details with large readable shape blocks}, {clothing, armor, motif or pattern}, {held objects or props}, {summoning, activation, attack, defense, or transformation action}, {simplified energy stage or clean domain platform}, {composition and subject position}, {camera angle and motion path}, {light direction, strong outer contour, rim light, bright eyes or core highlight}, {high-saturation high-contrast color palette}, {card-size readability cue}
```
中文释义：
- 参数建议：
- Watch-outs：

#### MJ 版本 B：High-Rarity Drama
- 意图：
- Prompt：
```text

```
中文释义：
- 参数建议：
- Watch-outs：

#### MJ 版本 C：Exploration
- 意图：
- Prompt：
```text

```
中文释义：
- 参数建议：
- Watch-outs：

#### MJ 参考图策略
- 是否需要 `--sref`：
- 建议 `--sw`：
- 是否需要 `--oref`：
- 建议 `--ow`：
- 是否需要 image prompt / `--iw`：

#### MJ 迭代记录
| 轮次 | 问题 | 修改动作 | 下一版 Prompt 调整 |
| --- | --- | --- | --- |
| 1 | | | |

## 8. 外包画师 Brief
- 交付内容：
- 尺寸/比例：
- 必须保留：
- 可自由发挥：
- 禁止事项：
- 参考方向：
- 需要提交的阶段稿：

## 9. 美术总监审核表
| 项目 | 通过标准 | 状态 | 备注 |
| --- | --- | --- | --- |
| 主体识别 | 缩略图能看清主角/事件 | 待审 | |
| 卡牌类型 | 不读文字也能猜到类型 | 待审 | |
| 系列一致性 | 符合系列视觉支柱 | 待审 | |
| 规则一致性 | 不暗示不存在的效果 | 待审 | |
| 卡框安全 | 关键信息不被遮挡 | 待审 | |
| 印刷可读 | 明暗和边缘足够清楚 | 待审 | |
| 原创安全 | 无第三方 IP/商标/真人肖像风险 | 待审 | |

## 10. 返修建议
- 优先级 P0：
- 优先级 P1：
- 优先级 P2：
```

## Review Pass

```markdown
# 卡图审核意见：{卡名或概念}

## 结论
- 状态：通过 / 小修 / 大修 / 暂停
- 最大风险：

## 主要问题
1. 
2. 
3. 

## 返修指令
- 构图：
- 角色/主体：
- 色彩/光影：
- 规则可读性：
- 系列一致性：

## 下一版验收标准
- 
```

## Generated Image Review

Use this when the user provides generated images and asks what drifted or how to revise prompts.

````markdown
# 生成图复盘：{卡名或主题}

## 美术总监结论
- 状态：保留 / 小修 / 大修 / 重跑
- 是否守住主题灵魂：
- 最大偏移：

## 偏移诊断
- 缺失：
- 错误：
- 意外：
- 可能原因：

## 修改方向
- 视觉设定要改：
- Prompt 要改：
- 负向提示要加：
- 下一轮只测试：

## 修订 Prompt
```text
{clean revised English prompt}
```
中文释义：

## 下一轮看图重点
- 
````
