# Anki for VSCode：VS Code 内直接制卡的完美插件

你是否厌倦了在 Anki 的编辑器中缓慢地敲字？是否希望能在 VS Code 的舒适环境中直接创建卡片？

**Anki for VSCode** 插件让你直接在 VS Code 中编写 Markdown，一键发送到 Anki。无需脚本，无需配置，开箱即用。

## 一、Anki for VSCode 简介

[Anki for VSCode](https://marketplace.visualstudio.com/items?itemName=jasew.anki) 是 VS Code 的官方扩展，通过 AnkiConnect 与 Anki 通信，让你在 VS Code 中直接创建和发送卡片到 Anki。

**核心特点**：
- 一键发送 Markdown 内容到 Anki
- 自动识别卡片分割符
- 支持 Cloze 完形填空
- 支持图片插入
- 自动生成标签

**安装量**：10,000+（热门插件）

## 二、安装与环境要求

### 前置条件

1. **Anki >= 2.1.21**
2. **AnkiConnect >= 2020-07-13**（插件代码：`2055492159`）
3. **VSCode >= 1.66**

### 安装步骤

1. 在 VS Code 中按 `Ctrl+P`，输入：
   ```
   ext install jasew.anki
   ```
2. 在 Anki 中安装 AnkiConnect 插件
3. 确保 Anki 正在运行

## 三、快速开始

### 基础用法

在 Markdown 文件中编写内容，用 `##` 标题分割卡片：

```markdown
## What's Markdown?

Markdown is a lightweight markup language with plain-text-formatting syntax.

## Who created Markdown?

John Gruber created the Markdown language in 2004 in collaboration with
Aaron Swartz on the syntax.
```

**操作**：
1. 按 `Ctrl+Shift+P` 打开命令面板
2. 输入 `Anki: Send To Deck`
3. 卡片自动发送到 Anki 的 "notes" 牌组

**效果**：
- 标题作为正面（Front）
- 内容作为背面（Back）
- 自动添加文档标题作为标签

### 前后面分割

使用 `%` 符号分割正反面：

```markdown
## YAGNI

Describe this acronym and why it's so important.

%

"You aren't gonna need it" (YAGNI) is a principle of extreme programming
(XP) that states a programmer should not add functionality until deemed
necessary.
```

这会创建一张卡片：
- **正面**：YAGNI / Describe this acronym and why it's so important.
- **背面**：You aren't gonna need it" (YAGNI) is a principle...

## 四、发送方式详解

### 1. 发送到默认牌组

命令：`Anki: Send To Deck`

所有卡片发送到 "notes" 牌组（可在设置中修改默认牌组）。

### 2. 发送到自定义牌组

命令：`Anki: Send To Own Deck`

根据文档中的 `#` 标题创建牌组。例如文档标题为 `# Python`，卡片会发送到 "Python" 牌组。

```markdown
# Python

## What's a list comprehension?

A concise way to create lists in Python using a single line of code.

## How do you handle exceptions?

Use try-except blocks to catch and handle runtime errors gracefully.
```

卡片发送到 "Python" 牌组。

### 3. 按目录结构发送

命令：`Anki: Send To DirName Deck`

根据文件路径创建牌组层级。例如文件路径：
```
/workspace/programming/python/notes.md
```

卡片发送到 `programming::python` 牌组。

### 4. 更新已发送的卡片（Beta）

在设置中启用：
```json
{
  "anki.md.updateCards": true,
  "anki.md.insertNewCardID": true
}
```

卡片会携带 NoteID，更新时自动同步。

## 五、Cloze 完形填空

在标题中使用 `{{c1::}}` 语法创建 Cloze 卡片：

```markdown
## A bit like {{c1::this}}

This is a test of cloze deletion
```

**注意**：
- Cloze 卡片的标题内容作为问题
- 正文内容不会使用（因为 Cloze 卡片只有一面）
- 不支持与 `%` 分割符同时使用

**多挖空示例**：
```markdown
## {{c1::Ephemeral}} means {{c2::temporary or short-lived}}
```

生成一张卡片，挖空两个部分。

## 六、图片支持

在 Markdown 中直接插入图片：

```markdown
## Describe this diagram

![image](https://example.com/diagram.png)

The diagram shows the architecture of a web application.
```

图片会自动上传到 Anki。

## 七、标签系统

在 Markdown 中添加标签：

```markdown
## Question 1

Answer to question 1

[tags]: #python #basics

---

## Question 2

Answer to question 2

[tags]: #python #advanced
```

**规则**：
- 标签必须在新行中
- 每个卡片只能有一行标签
- 使用 `#标签名` 格式

## 八、Explorer 浏览器

插件提供侧边栏浏览器，可以：
- 查看所有牌组
- 浏览卡片内容
- 查看模板 CSS（只读）

打开方式：点击 VS Code 左侧活动栏的双星图标 ⭐⭐

## 九、VS Code 配置优化

在 `settings.json` 中添加推荐配置：

```json
{
  // 默认牌组名称
  "anki.deck": "我的牌组",
  
  // 自动发送时使用文件路径作为牌组名
  "anki.useDirStructure": true,
  
  // 启用卡片更新功能
  "anki.md.updateCards": true,
  "anki.md.insertNewCardID": true,
  
  // Markdown 最佳配置
  "markdown.preview.enableWikiLinkSyntax": true,
  "editor.wordWrap": "on",
  "editor.fontSize": 16,
  "editor.lineHeight": 1.8
}
```

## 十、快捷键

| 快捷键 | 功能 |
|-------|------|
| `Ctrl+Shift+P` | 打开命令面板 |
| `Ctrl+Shift+A` | 发送到默认牌组 |
| `Ctrl+Shift+D` | 按文档标题发送到牌组 |

自定义快捷键（`keybindings.json`）：

```json
[
  {
    "key": "ctrl+shift+a",
    "command": "anki.sendToDeck"
  },
  {
    "key": "ctrl+shift+d", 
    "command": "anki.sendToOwnDeck"
  }
]
```

## 十一、工作流示例

### 示例 1：学习编程概念

创建文件 `python-basics.md`：

```markdown
# Python Basics

## What is a list comprehension?

A concise way to create lists in Python using a single line of code.

[tags]: #python #basics

---

## How do you define a function?

Use the `def` keyword followed by the function name and parameters.

[tags]: #python #functions

---

## What is the difference between `==` and `is`?

- `==` compares values (equality)
- `is` compares identity (same object in memory)

[tags]: #python #comparison
```

发送到 "Python Basics" 牌组，自动添加标签。

### 示例 2：学习医学知识

创建文件 `anatomy-heart.md`：

```markdown
# Heart Anatomy

## What is the sinoatrial node?

The SA node is the heart's natural pacemaker, located in the right atrium.

[tags]: #medicine #cardiology #anatomy

---

## Describe the blood flow through the heart

{{c1::Deoxygenated blood}} enters the {{c2::right atrium}} through the 
{{c1::superior and inferior vena cava}}.

[tags]: #medicine #cardiology #bloodflow
```

### 示例 3：学习英语词汇

创建文件 `toefl-vocab.md`：

```markdown
# TOEFL Vocabulary

## ephemeral

adj. lasting for a very short time

Usage: Fame is ephemeral - it can disappear overnight.

[tags]: #toefl #adjectives

---

## ubiquitous

adj. existing or appearing everywhere

Usage: Smartphones have become ubiquitous in modern society.

[tags]: #toefl #adjectives
```

## 十二、注意事项

### 1. Anki 必须运行

发送卡片时，Anki 必须处于运行状态。关闭 Anki 会导致发送失败。

### 2. 字段名称

确保你的笔记类型包含 "Front" 和 "Back" 字段，或者在设置中指定正确的字段名。

### 3. 牌组命名

牌组名称区分大小写，确保与 Anki 中的名称完全匹配。

### 4. 备份

由于插件直接修改 Anki 数据库，建议：
- 定期备份 Anki 集合
- 在使用新功能前创建备份

## 十三、与其他插件对比

| 插件 | 特点 | 适用场景 |
|-----|------|---------|
| **Anki for VSCode** | 开箱即用，Markdown 友好 | 快速制卡 |
| **Anki Editor** | 编辑模板，语法高亮 | 模板开发 |
| **Anki Sidebar** | VS Code 内复习 | 边编码边复习 |

## 十四、常见问题

**Q: 发送失败，显示 "AnkiConnect is not running"？**
- 确认 Anki 已启动
- 确认 AnkiConnect 插件已安装
- 重启 Anki 和 VS Code

**Q: Cloze 卡片没有生效？**
- 检查语法：`{{c1::答案}}`
- 确保标题中有 cloze 标记
- 不要与 `%` 分割符同时使用

**Q: 如何更改默认牌组？**
- 打开设置 `Ctrl+,`
- 搜索 `anki.deck`
- 修改为你的牌组名称

**Q: 可以批量发送吗？**
- 是的，只需在命令面板中选择发送整个文件
- 每张 `##` 标题会生成一张卡片

## 总结

Anki for VSCode 让制卡变得前所未有的简单：

| 优势 | 说明 |
|-----|------|
| 开箱即用 | 无需配置脚本 |
| Markdown 友好 | 熟悉的编辑体验 |
| 多种发送方式 | 灵活适应不同场景 |
| 自动标签 | 省去手动添加的麻烦 |
| Cloze 支持 | 一键创建挖空卡片 |

---

**相关资源**：
- [AnkiConnect 教程](08-anki-connect.md) - API 详细用法
- [Anki 基础卡片创建教程](04-anki-basic-cards.md) - 卡片创建基础
- [Anki Cloze 完形填空教程](05-anki-cloze.md) - Cloze 语法详解