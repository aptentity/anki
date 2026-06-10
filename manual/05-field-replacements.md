# 字段替换

- [基础替换](#基础替换)
- [换行](#换行)
- [单个字段的语音合成](#单个字段的语音合成)
- [多字段与静态文本的语音合成](#多字段与静态文本的语音合成)
- [特殊字段](#特殊字段)
- [提示字段](#提示字段)
- [词典链接](#词典链接)
- [去除 HTML](#去除-html)
- [从右到左文本](#从右到左文本)
- [注音字符（Ruby）](#注音字符ruby)
  - [附加的注音字符过滤器](#附加的注音字符过滤器)
- [媒体与 LaTeX](#媒体与-latex)
  - [静态声音/图片](#静态声音图片)
  - [字段引用](#字段引用)
- [检查答案](#检查答案)
  - [忽略变音符号](#忽略变音符号)

## 基础替换

最基本的模板类似这样：

```
{{Front}}
```

当你把文本放在花括号中时，Anki 会按名称查找对应字段，并将该文本替换为该字段的实际内容。

**字段名区分大小写**。如果你的字段名为 `Front`，写成 `{{front}}` 将无法正常工作。

你的模板不限于只放字段列表。你还可以在模板中加入任意文本。例如，如果你正在学习首都城市，并创建了一个带"国家"字段的笔记类型，你可以创建如下正面模板：

```
What's the capital city of {{Country}}?
```

默认的背面模板看起来类似这样：

```
{{FrontSide}}

<hr id=answer>

{{Back}}
```

这表示"先显示卡片正面的文本，然后是一条分隔线，再显示 Back 字段"。

`id=answer` 部分告诉 Anki 问题和答案之间的分隔位置。这让 Anki 在你按"显示答案"时能**自动滚动到答案开始的位置**——在长卡片上特别有用（尤其是在屏幕较小的移动设备上）。如果你不想在答案开头显示水平线，也可以改用其他 HTML 元素（如 `<p>` 或 `<div>`）。

## 换行

卡片模板类似网页，因此换行需要使用特殊命令。例如，如果你在模板中写：

```
one
two
```

在预览中你实际会看到：

```
one two
```

要换行，你需要在行末添加一个 `<br>` 代码，像这样：

```
one<br>
two<br>
```

`br` 是 "(line) br(eak)"（换行）的缩写。

字段同理。如果你想让两个字段各占一行显示，可以这样写：

```
{{Field 1}}<br>
{{Field 2}}<br>
```

## 单个字段的语音合成

> 此功能需要 Anki 2.1.20、AnkiMobile 2.0.56 或 AnkiDroid 2.17。

要让 Anki 用美式英语朗读 Front 字段，你可以在模板中放：

```
{{tts en_US:Front}}
```

在 Windows、macOS 和 iOS 上，Anki 会使用操作系统内置的语音。Linux 上没有内置语音，但可以通过插件提供，例如[这个](https://ankiweb.net/shared/info/391644525)。

要查看所有可用的语言/语音列表，在模板中放：

```
{{tts-voices:}}
```

如果所选语言有多个可用语音，你可以在列表中指定偏好语音，Anki 会选用第一个可用的。例如：

```
{{tts ja_JP voices=Apple_Otoya,Microsoft_Haruka:Field}}
```

这表示在 Apple 设备上使用 Otoya，在 Windows PC 上使用 Haruka。

某些 TTS 实现支持指定不同的语速：

```
{{tts fr_FR speed=0.8:SomeField}}
```

`speed` 和 `voices` 都是可选的，但**语言必须指定**。

在 Mac 上，你可以自定义可用语音：

- 打开"系统偏好设置"
- 点击"辅助功能"
- 点击"语音"
- 点击系统语音下拉框，选择"自定义"

不同语音效果不同，多试几个选你喜欢的。注意 Siri 语音只能被 Apple 自家应用使用。安装新语音后，需要重启 Anki 才能使用。

在 Windows 上，某些语音（如 Cortana）无法选择，因为微软不允许其他应用使用。

在完形填空（Cloze）笔记类型上，你可以用 `cloze-only` 过滤器让 Anki 只朗读被遮蔽的部分：

```
{{tts en_US:cloze-only:Text}}
```

`cloze-only` 过滤器在 Anki 2.1.29+、AnkiMobile 2.0.65+ 和 AnkiDroid 2.17+ 中支持。

## 多字段与静态文本的语音合成

> 此功能需要 Anki 2.1.50+、AnkiMobile 2.0.84+ 或 AnkiDroid 2.17+。

如果想让 TTS 朗读多个字段或模板中的静态文本，可以使用：

```
[anki:tts lang=en_US] This text should be read. Here is {{Field1}} and {{Field2}}[/anki:tts]

This is other text on the template. It is outside of the tags so it should not be read.
```

## 特殊字段

你可以在模板中包含一些特殊字段：

```
笔记的标签：{{Tags}}

笔记类型：{{Type}}

卡片所在牌组：{{Deck}}

卡片所在子牌组：{{Subdeck}}

卡片的标记（flag）：{{CardFlag}}

卡片类型（如"Forward"等）：{{Card}}

正面模板的内容
（仅在背面模板中有效）：{{FrontSide}}
```

`FrontSide` 不会自动播放卡片正面的音频。如果你希望同一段音频在正面和背面都自动播放，你需要**手动把音频字段也加到背面**。

与其他字段一样，特殊字段名也**区分大小写**——必须用 `{{Tags}}` 而非 `{{tags}}`，以此类推。

## 提示字段

你可以把一个字段加到卡片的正面或背面，但**默认隐藏**，需要主动点开才显示。这称为**提示字段**（hint field）。在添加提示前请注意：在 Anki 中让一道题越容易回答，你在现实中遇到时记住它的可能性就越低。请先阅读 [https://super-memory.com/articles/20rules.htm](https://super-memory.com/articles/20rules.htm) 上的"最小信息原则"。

首先，你需要在笔记中添加一个字段来存放提示（如果还没有的话）。如果不知道怎么做，请参考[字段](https://docs.ankiweb.net/editing.html#customizing-fields)章节。

假设你已经创建了一个名为 MyField 的字段，你可以在模板中加上下面的内容，让 Anki 在卡片上包含该字段但默认隐藏：

```
{{hint:MyField}}
```

这会显示一个标为"显示提示"的链接；点击后该字段的内容会显示在卡片上。（如果 MyField 为空，则什么也不显示。）

如果你在问题侧显示了提示，然后揭示了答案，提示会再次隐藏。如果你希望提示在显示答案时**始终可见**，你需要从背面模板中移除 `{{FrontSide}}`，并手动添加你想显示的字段。

**目前提示字段不支持音频**——音频会无视你是否点击了提示链接而直接播放。

如果你想自定义外观或行为，需要自己实现提示字段。我们无法提供相关支持，但以下代码可作为起点：

```html
{{#Back}}
<a class=hint href="#"
onclick="this.style.display='none';document.getElementById('hint4753594160').style.display='inline-block';return false;">
Show Back</a><div id="hint4753594160" class=hint style="display: none">{{Back}}</div>
{{/Back}}
```

## 词典链接

你也可以用字段替换来创建词典链接。假设你在学一门语言，你常用的在线词典支持用如下 URL 搜索：

```
http://example.com/search?q=myword
```

你可以在模板中这样写，自动生成一个链接：

```
{{Expression}}

<a href="http://example.com/search?q={{Expression}}">在词典中查询</a>
```

上面的模板让你在复习时点击链接就能搜索该笔记的词条。不过有个注意事项，请看下一节。

## 去除 HTML

与模板一样，字段以 HTML 形式存储。在上面的词典链接示例中，如果 Expression 字段中的词是"myword"且没有格式，HTML 就是"myword"。但当你在字段中加入格式时，会包含额外的 HTML。比如 "myword" 加了粗体，实际 HTML 就是 `<b>myword</b>`。

这会给词典链接之类的东西带来问题。在上面的例子里，词典链接会变成：

```html
<a href="http://example.com/search?q=<b>myword</b>">在词典中查询</a>
```

链接里多出来的字符很可能会让词典网站困惑，导致你搜不到任何结果。

为解决这个问题，Anki 提供了在字段替换时**去除格式**的功能。如果在字段名前加 `text:`，Anki 不会包含任何格式。于是即使字段带格式也能正常工作的词典链接就变成：

```html
<a href="http://example.com/search?q={{text:Expression}}">在词典中查询</a>
```

## 从右到左文本

如果你学的是从右到左阅读的语言，需要这样调整模板：

```html
<div dir=rtl>{{FieldThatHasRTLTextInIt}}</div>
```

## 注音字符（Ruby）

某些语言常用在文字上方的注释来标注读音。这些注释称为[注音字符（Ruby character）](https://en.wikipedia.org/wiki/Ruby_character)。在日语中称为[振假名（furigana）](https://en.wikipedia.org/wiki/Furigana)。

在 Anki 中，你可以用下面的语法显示注音字符：

```
Text[Ruby]
```

假设上面的文本写在 MyField 字段中。默认情况下，如果你直接用 `{{Myfield}}`，字段会原样显示。要让注音字符正确显示在文字上方，在模板中使用 `furigana` 过滤器：

```
{{furigana:MyField}}
```

下面是一些例子：

| 原始文本 | 渲染效果 |
|---|---|
| `Text[Ruby]` | Text<sup>Ruby</sup> |
| `日本語[にほんご]` | 日本語<sup>にほんご</sup> |
| `世[よ]の 中[なか]` | 世<sup>よ</sup>の 中<sup>なか</sup> |
| `世[よ]の中[なか]` | 世<sup>よ</sup>の中<sup>なか</sup> *(错误！)* |

注意第三个例子中"中"字符前有一个空格。这是必需的，用来指定注音只作用于该字符。如果没有空格，注音会错误地显示在"的"字符上方，如第四个例子所示。

### 附加的注音字符过滤器

除 `furigana` 过滤器外，你还可以用 `kana` 和 `kanji` 过滤器只显示注音文本的某些部分。`kana` 过滤器只显示注音文本，`kanji` 过滤器则完全去除注音文本。

| 原始文本 | 字段过滤器 | 渲染效果 |
|---|---|---|
| `日本語[にほんご]` | `{{furigana:MyField}}` | 日本語<sup>にほんご</sup> |
| `日本語[にほんご]` | `{{kana:MyField}}` | にほんご |
| `日本語[にほんご]` | `{{kanji:MyField}}` | 日本語 |

这些名字同样借自日语：[kana](https://en.wikipedia.org/wiki/Kana) 表示描述单词读音的音节系统，而 [kanji](https://en.wikipedia.org/wiki/Kanji) 表示其中的汉字。

## 媒体与 LaTeX

Anki 不会扫描模板中的媒体引用，因为这样做很慢。这对在模板中包含媒体有影响。

### 静态声音/图片

如果你想在每张卡片上都包含**相同的**图片或声音（例如每张卡片顶部一个公司 logo）：

1. 把文件重命名，让它以下划线开头，例如 `_logo.jpg`。下划线告诉 Anki 该文件是被模板引用的，共享牌组时应一并导出。
2. 在正面或背面模板中引用该媒体，例如：

```html
<img src="_logo.jpg">
```

### 字段引用

**不支持**在媒体引用中使用字段。复习时可能能显示也可能不能显示，而且在"检查未使用的媒体"、导入/导出等功能中无法正常工作。以下写法**无效**：

```html
<img src="{{Expression}}.jpg">

[sound:{{Word}}]

[latex]{{Field 1}}[/latex]
```

你应该在字段中直接包含媒体引用。更多信息请参考[导入章节](https://docs.ankiweb.net/importing/text-files.html#importing-media)。

## 检查答案

你可以在 YouTube 上观看[介绍此功能的视频](http://www.youtube.com/watch?v=5tYObQ3ocrw&yt:cc=on)。

检查答案最简单的方法是：在添加笔记窗口左上角点击"Basic"，选择"Basic (type in the answer)"（基本-输入答案）。

如果你下载了共享牌组，想用输入答案的方式复习它，可以修改该牌组的卡片模板。如果模板像这样：

```
{{Native Word}}

{{FrontSide}}

<hr id=answer>

{{Foreign Word}}
```

要想输入外语单词并核对正误，需要把正面模板改为：

```
{{Native Word}}
{{type:Foreign Word}}
```

这里我们在想要比对的字段前加了 `type:`。因为 `FrontSide` 出现在背面，所以输入框也会出现在背面。

复习时，Anki 会显示一个文本框让你输入答案；按回车或显示答案后，Anki 会标出你答对和答错的部分。文本框的字号就是你在"字段"对话框中为该字段配置的字号（编辑笔记时可见）。

> 注意：输入答案的文本框**不会**出现在预览对话框或 AnkiWeb 中。

此功能**不会改变卡片如何被回答**——你仍然需要自己判断记得是否清楚。

一张卡片上**只能用一个输入比对**。如果你把上面那段加多次，不会生效。它也**只支持单行**，因此不适合比对包含多行的字段。

Anki 用等宽字体显示答案比对，以便"你的输入"和"正确答案"两栏能对齐。如果你想自定义比对的字体，可以在样式部分的底部加：

```css
code#typeans { font-family: "myfontname"; }
```

这会影响以下答案比对的 HTML：

```html
<code id=typeans>...</code>
```

高级用户可以用 CSS 类 `typeGood`、`typeBad` 和 `typeMissed` 自定义输入答案的默认颜色。AnkiMobile 支持 `typeGood` 和 `typeBad`，但不支持 `typeMissed`。

如果你想覆盖输入框的大小而不想改字段对话框里的字体，可以用 `!important` 覆盖默认的内联样式：

```css
#typeans { font-size: 50px !important; }
```

完形填空卡片也可以输入答案。方法是在正面和背面模板都加 `{{type:cloze:Text}}`，让背面类似：

```
{{cloze:Text}}
{{type:cloze:Text}}
{{Extra}}
```

如果有多个被遮蔽的部分，可以在文本框中用逗号分隔多个答案。

### 忽略变音符号

如果你不想让 Anki 在比对输入时计较**变音符号**（重音等）的差异，可以用 `type:nc`：

```
{{type:nc:Front}}
```

这样可以确保重音的差异不会被判错。例如 `بطيخ` 与 `بَطِّيخ`、`elite` 与 `élite` 会被视为相同。
