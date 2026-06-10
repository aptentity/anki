# 让 AI 直接操作你的 Anki：anki-connect-skill 让卡片自动化起飞

> 配合 Anki Skill 使用，一个负责"教 AI 怎么做"，一个负责"让 AI 真做"。从此告别手动点击

## 前言

上一篇我分享了 [Anki Skill](https://juejin.cn/post/xxx)：一个教会 AI **怎么设计好卡片** 的方法论。

但光会"教"还不够。**真正能解放双手的，是让 AI 直接动手**。

比如：

- 📝 我刚整理完 50 张英语单词笔记 → 让 AI 一次性导入 Anki，而不是手动复制粘贴
- 🔍 我想找"所有标记红色且本月失败的卡片" → 让 AI 帮我筛
- ✏️ 发现某张卡的字段名拼错了 → 让 AI 批量改 200 张
- 📊 看统计时想分析最近 30 天的复习表现 → 让 AI 自动拉数据

**这些事，靠 UI 点鼠标累死，靠 anki-connect-skill 一句话搞定**。

今天来拆解这个能"动手"的 Skill 👇

---

## 一、anki-connect-skill 是什么？

```
anki-connect-skill/
└── SKILL.md    # 核心：让 AI 通过 AnkiConnect API 操作 Anki
```

它跟上一篇的 anki skill **完全不同**：

| 维度 | anki skill | anki-connect-skill |
|------|-----------|-------------------|
| **能力** | 教 AI 怎么做好卡片 | 让 AI 直接操作 Anki |
| **类比** | 写作课的讲义 | 数据库的客户端 |
| **输入** | 你给素材 | API 调用 |
| **输出** | 卡片设计建议 | 真实创建/修改/删除 |
| **依赖** | 无 | Anki 桌面端 + AnkiConnect 插件 |

**一句话总结**：anki skill 是**军师**，anki-connect-skill 是**士兵**。

---

## 二、什么是 AnkiConnect？

anki-connect-skill 的技术核心是 [AnkiConnect](https://foosoft.net/projects/anki-connect/) —— Anki 的一个官方插件，给 Anki 暴露了 **REST API**。

```
┌──────────┐         HTTP          ┌──────────┐         ┌──────────┐
│   AI     │ ──────JSON-RPC─────→ │ AnkiConnect │ ──────→ │   Anki   │
│  Agent   │                       │  (Port 8765)  │         │   数据库  │
└──────────┘                       └──────────┘         └──────────┘
```

开启后，Anki 会监听 `localhost:8765`。任何能发 HTTP 请求的程序都能操作 Anki。

**这意味着**：
- 任何编程语言（Python、JS、Go、Shell...）都能调用
- 任何工具（curl、Postman、Alfred、Zapier...）都能触发
- 任何 LLM Agent（Trae、Cursor、Claude Code...）都能操作

**真正做到"万物皆可触发 Anki"**。

---

## 三、5 分钟快速接入

### Step 1：安装 AnkiConnect 插件

1. 打开 Anki → 工具 → 插件 → 获取插件
2. 输入代码：`2055492159`
3. 重启 Anki

### Step 2：验证 API 是否通

```bash
curl -s -X POST http://localhost:8765 \
  -d '{"action": "deckNames", "version": 6}'
```

如果返回一堆牌组名（如 `["英语", "医学", "default"]`），恭喜通了 ✅

### Step 3：把 skill 放进项目

```bash
cp -r anki-connect-skill /your-project/.trae/skills/
```

搞定。AI Agent 现在**自动**会用它。

---

## 四、5 大核心能力

### 4.1 创建笔记（addNote）

**最常用**。一条命令创建一张卡片。

```json
{
  "action": "addNote",
  "version": 6,
  "params": {
    "note": {
      "deckName": "英语",
      "modelName": "Basic",
      "fields": {
        "Front": "ephemeral",
        "Back": "adj. 短暂的；瞬息的"
      }
    }
  }
}
```

返回 note ID（`1780985523176`）。可以用这个 ID 后续修改、删除。

### 4.2 查找笔记（findNotes）

按条件筛卡片。AnkiConnect 支持 **Anki 的全部搜索语法**。

```json
// 找所有包含 "ephemeral" 的笔记
{"action": "findNotes", "params": {"query": "ephemeral"}}

// 找英语牌组中最近 7 天失败的卡片
{"action": "findNotes", "params": {"query": "deck:英语 rated:7:1"}}

// 找红色标记且有 leech 标签的
{"action": "findNotes", "params": {"query": "flag:1 tag:leech"}}
```

### 4.3 更新笔记（updateNoteFields）

批量改字段值。

```json
{
  "action": "updateNoteFields",
  "params": {
    "note": {
      "id": 1780985523176,
      "fields": {"Back": "adj. 短暂的（修正版）"}
    }
  }
}
```

### 4.4 删除笔记（deleteNotes）

```json
{
  "action": "deleteNotes",
  "params": {"notes": [1780985523176, 1780985527699]}
}
```

⚠️ **不可恢复**，慎用。

### 4.5 查询统计（getDeckStats）

```json
{"action": "getDeckStats", "params": {"decks": ["英语"]}}
```

返回新卡数、复习数、间隔均值等。

---

## 五、4 个杀手级应用场景

### 5.1 批量导入英语单词

> 痛点：手动逐条复制粘贴 100 个单词到 Anki 至少 1 小时

**解决**：让 AI 自动读文件 + 自动创建。

```
用户：把 /Users/admin/vocab.txt 里的所有单词导入英语牌组
AI：正在读取文件并通过 AnkiConnect 导入...

[30 秒后]
AI：成功导入 100 张卡片，耗时 28 秒
```

**实际就是**：
1. AI 读文件，按行解析
2. 调用 `addNote` 100 次
3. 返回结果汇总

### 5.2 一键找"水蛭卡"

> 痛点：水蛭卡藏在大牌组里，UI 找起来很麻烦

```
用户：帮我找出英语牌组所有 leech 标签的卡片，并显示它们的失败次数
AI：正在查询...

找到 8 张 leech 卡：
- ephemeral (失败 12 次)
- ubiquitous (失败 9 次)
- ...
```

**背后是**：
```bash
curl -X POST http://localhost:8765 \
  -d '{"action": "findNotes", "params": {"query": "deck:英语 tag:leech"}}'
```

### 5.3 批量重命名/重组牌组

> 痛点：旧牌组结构乱了，想批量迁移

```
用户：把所有 "英语::GRE" 下的卡片移到 "考试::GRE" 牌组
AI：正在查询并移动...

[完成]
移动了 1234 张卡片
```

### 5.4 自动化复习提醒

> 痛点：每天手动看 Anki 才知道要复习什么

**配合 macOS 自动化（Keyboard Maestro / cron）**：

```bash
# 每天早上 9 点运行
COUNT=$(curl -s -X POST http://localhost:8765 \
  -d '{"action": "getNumCardsToReview", "params": {"daysAhead": 1}}')
osascript -e "display notification \"今天要复习 $COUNT 张卡\""
```

---

## 六、跟 LLM Agent 怎么配合？

**重点来了**。这个 skill 单独用就是 API 客户端，**但配合 LLM 才发挥威力**。

### 工作流程

```
┌─────────────────────────────────────────────────┐
│  用户：把这段话做成 Anki 卡片                    │
└────────────────────┬────────────────────────────┘
                     ↓
        ┌────────────────────────────┐
        │  LLM Agent 加载 anki skill  │ ← 第一步：用方法论
        │  (cards.md 决策格式)        │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │  LLM 调用 AnkiConnect API   │ ← 第二步：执行
        │  (anki-connect-skill 动手)  │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │  Anki 真的创建卡片           │
        └────────────────────────────┘
```

### 实战对比

**没用 skill 的 AI**：
> "我建议你这样创建卡片：Front: 'ephemeral', Back: '短暂的'..."
> （然后用户还得自己复制粘贴）

**用了两个 skill 的 AI**：
> "我已为你创建了 1 张卡片到'英语'牌组，note ID 是 1780985523176"
> （用户看到 Anki 里真的多了一张卡）

---

## 七、常见问题

### Q1：Anki 必须一直开着吗？

**是的**。AnkiConnect 是 Anki 的插件，Anki 关了 API 就不响应。

**解决方案**：
- 让 Anki 开机自启
- 用脚本定时检查并提示

### Q2：API 调用的速率限制？

官方建议每 50-100ms 一次请求。批量操作记得加延时。

```python
import time
for word in words:
    add_note(word)
    time.sleep(0.1)  # 100ms 间隔
```

### Q3：能不能远程调用？

**默认不行**（只监听 localhost）。要远程访问需要在 AnkiConnect 配置里改 `webBindAddress` 和 `webPort`，但有安全风险。

**推荐**：用反向代理（frp / ssh tunnel）。

### Q4：跟插件（如 AnkiHub、Image Occlusion Enhanced）冲突吗？

一般不冲突，因为都是 Anki 内部 API。但同时调用多个 API 时要小心竞态。

---

## 八、两个 skill 怎么配合？

| 场景 | 用 anki skill | 用 anki-connect-skill |
|------|:----------:|:-------------------:|
| 设计卡片结构 | ✅ | ❌ |
| 重写病卡 | ✅ | ❌ |
| 真的创建卡片 | ❌ | ✅ |
| 真的删除/修改 | ❌ | ✅ |
| 统计诊断 | ✅ (分析建议) | ✅ (拉数据) |
| 批量操作 | ❌ | ✅ |
| 质量检查 | ✅ | ❌ |

**最佳实践**：
- **设计阶段**：用 anki skill 思考"怎么做好这张卡"
- **执行阶段**：用 anki-connect-skill 让 AI 真的去做
- **诊断阶段**：用 anki skill 分析统计 + 用 anki-connect-skill 拉数据

---

## 九、写在最后

**AI 时代的工作流正在被重塑**。

过去我们用 Anki：
- 手动创建 → 手动复习 → 手动统计 → 手动优化

**现在**：
- 让 AI 设计 → 让 AI 创建 → AI 帮我复习（复习时 AI 给解释）→ AI 帮我分析

这不是未来，是**已经能做到的事**。

**两个 Skill 配合使用的效果**：

- ✅ 5 分钟导入 100 张卡片
- ✅ 一句话找出所有水蛭
- ✅ 自动诊断 + 自动重写
- ✅ 学习数据可视化

### 📌 行动清单

1. **安装 AnkiConnect**：5 分钟搞定
2. **验证 API**：跑一次 `deckNames` 命令
3. **把两个 skill 都放进项目**：让 AI 兼顾问+士兵
4. **试试一句话创建卡片**：感受"AI 真的动了 Anki"的快乐

