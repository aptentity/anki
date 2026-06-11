# 搜索

- [简单搜索](#简单搜索)
- [限定字段](#限定字段)
- [标签、牌组、卡片和笔记](#标签牌组卡片和笔记)
- [忽略重音 / 组合字符](#忽略重音--组合字符)
- [搜索完形填空](#搜索完形填空)
- [正则表达式](#正则表达式)
- [卡片状态](#卡片状态)
- [标记](#标记)
- [卡片属性](#卡片属性)
- [近期事件](#近期事件)
  - [添加](#添加)
  - [编辑](#编辑)
  - [答题](#答题)
  - [首次答题](#首次答题)
- [匹配特殊字符](#匹配特殊字符)
  - [原始输入](#原始输入)
- [对象 ID](#对象-id)
- [自定义数据](#自定义数据)
- [其他搜索](#其他搜索)

Anki 的浏览界面和筛选牌组功能使用一套通用的搜索语法来定位特定卡片 / 笔记。此语法也可用于调整 FSRS 优化的范围。

## 简单搜索

在搜索框中输入文本时，Anki 会查找匹配的笔记并显示其卡片。Anki 会在笔记的所有字段中搜索，但**不会搜索标签**（搜索标签的方法见[后文](#标签牌组卡片和笔记)）。

**示例：**

- `dog` — 搜索"dog"，会匹配"doggy"、"underdog"等
- `dog cat` — 查找同时包含"dog"和"cat"的笔记，如"raining cats and dogs"
- `dog or cat` — 查找包含"dog"或"cat"的笔记
- `dog (cat or mouse)` — 查找包含"dog"和"cat"，或包含"dog"和"mouse"的笔记
- `-cat` — 查找不含"cat"的笔记
- `-cat -mouse` — 查找既不含"cat"也不含"mouse"的笔记
- `-(cat or mouse)` — 与上面效果相同
- `"a dog"` — 查找精确包含"a dog"序列的笔记，如"atta dog"，但不包括"dog a"或"adog"
- `-"a dog"` — 查找不含精确"a dog"序列的笔记
- `d_g` — 匹配 d + 一个字符 + g，如 dog、dig、dug
- `d*g` — 匹配 d + 零个或多个字符 + g，如 dg、dog、dung
- `w:dog` — 按单词而非字符序列搜索，会匹配"dog"但不匹配"doggy"或"underdog"（需要 Anki 2.1.24+）。注意：格式变化可能被视为单词边界，例如搜索 `w:exam` 会匹配 **exam**ple（因为 example 中的"exam"部分被加粗格式化）
- `w:dog*` — 会匹配"dog"和"doggy"，但不匹配"underdog"
- `w:*dog` — 会匹配"dog"和"underdog"，但不匹配"doggy"

**注意事项：**

- 搜索词用空格分隔
- 多个搜索词默认是 **AND** 关系（即同时满足）。Anki 2.1.24+ 可显式使用 `and`（`dog and cat` 等同于 `dog cat`），但旧版会把 `and` 当作普通词搜索
- 用 `or` 只需匹配其中一个词
- 词前加 `-` 表示取反
- 用括号分组，如 `dog (cat or mouse)` — 有括号时匹配"dog cat"或"dog mouse"；无括号则匹配"dog"和"cat"，或单独匹配"mouse"
- Anki 只能在[排序字段](https://docs.ankiweb.net/editing.html#customizing-fields)中搜索带格式的文本。如果某个词的一部分被格式化了（如 "<strong>exa</strong>mple"），搜索 `example` 不会匹配，除非该字段是排序字段。如果格式不在词中间，Anki 可以在任何字段中找到该词
- 标准搜索对拉丁字符不区分大小写（a-z 匹配 A-Z）。其他字符（如西里尔字母）标准搜索时区分大小写，但可以用单词边界或正则表达式（`w:`、`re:`）搜索来做到不区分大小写

## 限定字段

你也可以让 Anki 只在特定字段中匹配内容。与上面的搜索不同，字段内搜索**默认需要精确匹配**。

- `front:dog` — 查找 Front 字段恰好是"dog"的笔记。字段内容是"a dog"不会匹配
- `"animal front:a dog"` — 查找"Animal Front"字段恰好是"a dog"的笔记。必须用双引号
- `front:*dog*` — 查找 Front 字段任意位置包含"dog"的笔记
- `front:` — 查找 Front 字段为空的笔记
- `front:_*` — 查找 Front 字段非空的笔记
- `front:*` — 查找有 Front 字段的笔记（无论是否为空）
- `fr*:text` — 查找字段名以"fr"开头的字段（需要 Anki 2.1.24+）

## 标签、牌组、卡片和笔记

- `tag:animal` — 查找带有"animal"标签或其子标签（如"animal::mammal"）的笔记
- `tag:none` — 查找没有标签的笔记
- `tag:ani*` — 查找以"ani"开头的标签
- `deck:french` — 在名为"French"的顶级牌组或其子牌组（如"French::Words"）中查找卡片。**不会**匹配其他同级牌组中的子牌组，如"Languages::French"
- `deck:french::words` — 在"French::Words"子牌组中查找
- `deck:french -deck:french::*` — 查找"French"牌组中的卡片，**但不包括**其子牌组
- `deck:"french words"` — 牌组名包含空格时的搜索方式
- `"deck:french words"` — 同上
- `deck:filtered` — 仅筛选牌组
- `-deck:filtered` — 仅普通牌组
- `preset:"Default"` — 在使用"Default"牌组选项预设的所有牌组中查找卡片（需要 Anki 23.10+）
- `card:forward` — 查找由名为"Forward"的卡片类型创建的卡片
- `card:1` — 按卡片类型编号搜索，例如查找第二条完形填空删除用 `card:2`
- `note:basic` — 搜索使用名为"Basic"的笔记类型创建的卡片

## 忽略重音 / 组合字符

> 需要 Anki 2.1.24+、AnkiMobile 2.0.60+ 或 AnkiDroid 2.17+。

用 `nc:`（no combining）可以让 Anki 忽略组合字符：

- `nc:uber` — 匹配"uber"、"über"、"Über"等
- `nc:は` — 匹配"は"、"ば"、"ぱ"
- `nc:heisen` 或 `nc:heißen` — 匹配包含"heißen"和"heisen"的笔记（ß 被视为 s，s 也被视为 ß）

> ⚠️ 忽略组合字符的搜索比普通搜索慢。

## 搜索完形填空

> 需要 Anki 25.07+。

用 `sc:`（strip clozes）可以搜索包含完形填空删除的笔记的完整文本，自动忽略完形填空标记：

- `sc:mnemonic` — 匹配包含 `{{c1::mn}}{{c2::e}}monic` 的笔记
- `sc:capital of France` — 匹配包含 `The {{c1::capital}} of {{c2::France}}` 的笔记

> ⚠️ 去除完形填空的搜索比普通搜索慢。

## 正则表达式

> 需要 Anki 2.1.24+、AnkiMobile 2.0.60+ 或 AnkiDroid 2.17+。

用 `re:` 开头可以使用正则表达式搜索。Anki 会把后面的内容当作[原始输入](#原始输入)处理。

**示例：**

- `"re:(some|another).*thing"` — 匹配包含"some"或"another"、后面跟零个或多个字符、再跟"thing"的笔记
- `re:\d{3}` — 匹配包含连续 3 位数字的笔记

正则表达式也可以限定到特定字段。与普通字段搜索不同，正则表达式搜索**不需要精确匹配**：

- `front:re:[a-c]1` — 匹配 Front 字段中任意位置出现的 a1、B1 或 c1
- `front:re:^[a-c]1$` — 同上，但要求字段内容**正好是** a1/b1/c1，前后不能有其他字符

Anki 2.1.50+ 支持标签的正则表达式：

- `tag:re:^parent$` — 查找标签恰好是"parent"的笔记，不包括"parent::child"等子标签
- `"tag:re:lesson-(1[7-9]|2[0-5])"` — 查找"lesson-17"到"lesson-25"的标签

更多信息请参考 [regexone.com 入门教程](https://regexone.com/lesson/introduction_abcs)。

**注意事项：**

- 搜索默认不区分大小写；在开头加 `(?-i)` 可以开启大小写敏感
- 某些文本（如空格和换行符）在 HTML 中表示方式可能不同——可以用编辑界面的 HTML 编辑器查看底层 HTML 内容
- Anki 正则表达式的具体支持情况请参见 [regex crate 文档](https://docs.rs/regex/1.3.9/regex/#syntax)

## 卡片状态

- `is:due` — 到期复习卡片和学习中卡片
- `is:new` — 新卡片
- `is:learn` — 学习中的卡片
- `is:review` — 复习（到期和未到期的）以及失误卡片
- `is:suspended` — 被[自动](https://docs.ankiweb.net/leeches.html)或手动暂停的卡片
- `is:buried` — 被[自动或手动](https://docs.ankiweb.net/studying.html#siblings-and-burying)埋葬的卡片
- `is:buried-sibling` — 被自动埋葬的卡片
- `is:buried-manually` — 被手动埋葬的卡片

失误卡片会同时属于多个状态，结合搜索词可以获得更精确的结果：

- `is:learn is:review` — 已失误、等待重新学习的卡片
- `-is:learn is:review` — 复习卡片，不包括失误卡片
- `is:learn -is:review` — 首次进入学习的卡片

## 标记

- `flag:0` — 无标记的卡片
- `flag:1` — 红色标记
- `flag:2` — 橙色标记
- `flag:3` — 绿色标记
- `flag:4` — 蓝色标记
- `flag:5` — 粉色标记
- `flag:6` — 青色标记
- `flag:7` — 紫色标记

## 卡片属性

- `prop:ivl>=10` — 间隔 10 天或以上的卡片
- `prop:due=1` — 明天到期的卡片
- `prop:due=-1` — 昨天到期的卡片
- `prop:due>=1` — 所有未来到期的卡片（包括明天）
- `prop:due<=-1` — 所有逾期卡片
- `prop:due>=-1 prop:due<=1` — 昨天、今天和明天到期的卡片
- `prop:reps<10` — 答题次数少于 10 次的卡片
- `prop:lapses>3` — 失误超过 3 次的卡片
- `prop:ease!=2.5` — 容易度不等于 2.5 的卡片
- `prop:pos<=100` — 新卡片队列中位置小于等于 100 的卡片

以下搜索需要 Anki 23.10+ 且启用 FSRS：

- `prop:s>21` — 稳定性大于 21 天的卡片
- `prop:d>0.3` — 难度大于 0.3 的卡片
- `prop:r<0.9` — 可检索性（retrievability）小于 0.9 的卡片

## 近期事件

### 添加

- `added:1` — 今天添加的卡片
- `added:7` — 最近 7 天添加的卡片

> 检查是基于卡片创建时间而非笔记创建时间，所以即使笔记是很久以前添加的，只要卡片是在时间范围内生成的，都会包含在内。

### 编辑

- `edited:n` — 笔记文本在最近 n 天内有添加 / 编辑的卡片

> 需要 Anki 2.1.28+ 或 AnkiMobile 2.0.64+。

### 答题

- `rated:1` — 今天答题的卡片
- `rated:1:2` — 今天答 Hard（2）的卡片
- `rated:7:1` — 最近 7 天内答 Again（1）的卡片
- `rated:31:4` — 最近 31 天内答 Easy（4）的卡片

> Anki 2.1.39+ 支持超过 31 天的答题搜索。

注意：要搜索某一天答题的卡片，`rated:n -rated:(n-1)` 可能不总是有效，请改用：

- `prop:rated=0` — 今天答题的卡片
- `prop:rated=-1` — 昨天答题的卡片
- `prop:rated=-7` — 7 天前答题的卡片

### 首次答题

> 需要 Anki 2.1.45+。

- `introduced:1` — 今天首次答题的卡片
- `introduced:365` — 最近 365 天内首次答题的卡片

## 匹配特殊字符

> 以下搜索需要 Anki 2.1.36+。

前面章节展示了 `*`、`_` 和 `"` 等字符在搜索中有特殊含义。如果要搜索这些字符本身，需要告诉 Anki 不要特殊处理它们。这称为"转义字符"，主要通过双引号和反斜杠实现。

- **空格**：用双引号包住整个搜索词 `"entire term"`。如果是冒号搜索，也可以只引用冒号后的部分 `part:"after the colon"`
- **`and` / `or`**：用双引号包住，如 `dog "and" cat`。如果把整个搜索词都用引号包住，不需要单独转义 `and` 或 `or`
- **`"`、`*` 和 `_`**：前面加反斜杠，如 `\_` 匹配真实的下划线（不匹配任意单字符）
- **`\`**：反斜杠本身也要转义，搜索真实的反斜杠用 `\\`
- **`(` 和 `)`**：用双引号包住整个词、用反斜杠、或两者都用。例如 `"(text)"`、`\(text\)` 和 `"\(text\)"` 都等价于搜索 `(text)`
- **`-`**：词首的 `-` 通常表示取反。如果要搜索真实的连字符，用反斜杠或引号，如 `\-free` 或 `"-free"` 会匹配"guilt-free"和"cruelty-free"
- **`:`**：冒号必须用反斜杠转义，除非前面有另一个未转义的冒号。例如 `w:3:30` 搜索"3:30"作为单词，不需要反斜杠；但不用冒号搜索时需要这样写：`3\:30`
- **`::`**：两个连续冒号不需要转义
- **`&`、`<` 和 `>`**：这些字符在搜索时会被当作 HTML 处理，直接搜索不会按预期工作。需要用 HTML 实体名称：`&amp;`（对应 `&`）、`&lt;`（对应 `<`）、`&gt;`（对应 `>`）。例如搜索 `&amp;text` 可以找到字段中包含 `&text` 的笔记

### 原始输入

某些关键字（如 `re:`）后面的文本会被当作原始输入处理。上面的特殊字符在这种情况下大多会失去特殊含义，但仍需注意：

- 双引号 `"` 必须转义
- 空格和未转义的括号需要将搜索词用引号包住
- 搜索词不能以奇数个反斜杠结尾

## 对象 ID

- `nid:123` — 笔记 ID 为 123 的笔记
- `cid:123,456,789` — 卡片 ID 为 123、456 或 789 的所有卡片

笔记和卡片 ID 可以在浏览器的[卡片信息](https://docs.ankiweb.net/stats.html)对话框中找到。这些搜索在进行插件开发或数据库相关工作时也很有用。

## 自定义数据

Anki 允许在卡片上存储少量自定义数据，支持自定义调度等高级用例。该功能的一个著名应用是早期 FSRS 的实现。在 Anki 23.10+ 中有以下搜索方式：

- `has-cd:v` — 自定义数据中有属性 `v` 的卡片
- `prop:cdn:d>5` — 自定义数据中 `d` 的值（通常指 FSRS 中的难度）大于 5 的卡片
- `prop:cds:v=reschedule` — 自定义数据中字符串 `v` 等于 `reschedule` 的卡片

## 其他搜索

- `prop:due=1 is:learn` — 跨日学习卡片，明天到期
- `prop:due=0 is:learn -introduced:1` — 今天到期的跨日学习卡片
- `prop:resched=0` — 今天被重新调度的卡片（通过"设置到期日"或"更改时重新调度卡片"）