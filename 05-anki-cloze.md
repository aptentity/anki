# Anki Cloze 完形填空教程：高效学习短语和固定搭配

Cloze（完形填空）是 Anki 中非常强大的卡片类型，特别适合学习短语、固定搭配和上下文关联的场景。

## 一、什么是 Cloze

Cloze 源自"cloze test"（完形测试），核心思想是在文本中挖空，让学习者主动回忆缺失的内容。

**与基本卡片的区别**：
- 基本卡片：正面一个问题，背面一个答案
- Cloze 卡片：在同一段文本中挖空，自动生成问题

## 二、基本语法

Cloze 使用双花括号 `{{c1::答案}}` 语法：

```markdown
{{c1::Ephemeral}} means temporary or short-lived.
```

**显示效果**：
```
[...] means temporary or short-lived.
```

复习时，挖空部分显示为省略号 `[...]`。

## 三、单挖空与多挖空

### 单挖空

```markdown
The {{c1::path}} to success is paved with hard work.
```

生成卡片：
```
The [___] to success is paved with hard work.
```

### 多挖空（同一编号）

```markdown
{{c1::Ephemeral}} means {{c1::temporary}}.
```

生成卡片：
```
[___] means [___].
```

两张卡片相同知识点，可以加强记忆。

### 多挖空（不同编号）

```markdown
{{c1::Ephemeral}} means {{c2::temporary or short-lived}}.
```

生成两张卡片：
- 卡片1：`[___] means temporary or short-lived.`
- 卡片2：`Ephemeral means [___].`

## 四、实用场景

### 场景1：学习固定搭配

```markdown
{{c1::Bear}} in mind that practice makes perfect.
```

适合学习介词搭配、动词短语等。

### 场景2：学习语法

```markdown
The boy {{c1::who}} I met yesterday was very friendly.
```

适合学习从句、关系词等语法点。

### 场景3：学习专业术语

```markdown
{{c1::Photosynthesis}} is the process by which plants convert sunlight into energy.
```

适合医学、法律等需要记忆复杂定义的学科。

### 场景4：学习代码语法

```markdown
Use {{c1::git commit}} to save your changes to the local repository.
```

适合程序员学习命令行和代码语法。

## 五、Cloze 模板的高级用法

### 1. 添加提示

```markdown
{{c1::Ephemeral}} means {{c2::temporary}} - think of something that disappears quickly.
```

背面显示完整提示。

### 2. 限制显示

使用 `::` 分隔正面和背面内容：

```markdown
{{c1::Ephemeral::adj. 短暂的}} means temporary or short-lived.
```

显示效果：
- 正面：`[___] means temporary or short-lived.`
- 背面：`Ephemeral (adj. 短暂的) means temporary or short-lived.`

### 3. 多行文本

```markdown
{{c1::Ephemeral}} means temporary or short-lived.

例句：Fame is ephemeral - it can disappear overnight.
```

## 六、常见问题

### Q: Cloze 和基本卡片哪个更好？

A: 根据场景选择：
- 需要精确记忆某个知识点 → 基本卡片
- 需要学习上下文、固定搭配 → Cloze

### Q: 挖空太多会影响理解吗？

A: 不会。Cloze 的设计正是通过主动回忆来增强理解。

### Q: 如何快速创建 Cloze 卡片？

A: 选中一段文本，按 `Alt+Shift+C`（Windows）或 `Cmd+Shift+C`（macOS）。

## 七、示例卡片

### 英语词汇

```
卡片1:
{{c1::Ubiquitous}} means existing everywhere.

卡片2:
The {{c1::serendipity}} of finding this book changed my life.

卡片3:
{{c1::Paradigm}} shift refers to a fundamental change in assumptions.
```

### 医学术语

```
卡片1:
{{c1::Myocardial infarction}} is commonly known as a heart attack.

卡片2:
The {{c1::ventricle}} is a chamber of the heart that receives and pumps blood.
```

### 编程知识

```
卡片1:
Use {{c1::git push}} to upload local repository changes to a remote repository.

卡片2:
{{c1::API}} stands for Application Programming Interface.
```

## 总结

| 要点 | 说明 |
|-----|------|
| 语法 | `{{c1::答案}}` |
| 单挖空 | `{{c1::A}}` 生成一张卡片 |
| 多挖空同编号 | `{{c1::A}}{{c1::B}}` 生成一张卡片，AB都被挖空 |
| 多挖空不同编号 | `{{c1::A}}{{c2::B}}` 生成两张卡片 |

---

**相关资源**：
- [Anki 基础卡片创建教程](04-anki-basic-cards.md)
- [Anki 优质卡片制作原则](07-anki-card-principles.md)