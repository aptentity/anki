# 样式与 HTML

- [卡片样式](#卡片样式)
- [图片缩放](#图片缩放)
- [字段样式](#字段样式)
- [音频重播按钮](#音频重播按钮)
- [文本方向](#文本方向)
- [显示代码片段](#显示代码片段)
  - [行内代码](#行内代码)
  - [代码块](#代码块)
- [其他 HTML](#其他-html)
- [浏览器外观](#浏览器外观)
- [平台特定 CSS](#平台特定-css)
- [安装字体](#安装字体)
  - [将字体添加到媒体文件夹](#将字体添加到媒体文件夹)
  - [更新模板以使用该字体](#更新模板以使用该字体)
- [夜间模式](#夜间模式)
- [淡入与滚动](#淡入与滚动)
- [JavaScript](#javascript)

## 卡片样式

你可以在 YouTube 上观看[关于卡片样式的视频](http://www.youtube.com/watch?v=F1j1Zx0mXME&yt:cc=on)。视频展示的是 Anki 2.0 的界面，但概念大体相同。

在"卡片"界面中，可以通过点击"Back Template"（背面模板）按钮旁边的 **"Styling"（样式）** 按钮进入样式区。在该区域，你可以修改卡片的背景颜色、默认字体、文本对齐方式等。

可用的标准选项有：

**font-family（字体族）**

卡片使用的字体名称。如果你的字体名包含空格（如"MS Unicode"），需要用双引号包起来，如 `font-family: "MS Unicode";`。也可以在一张卡片上使用多个字体，相关信息见下文。

**font-size（字体大小）**

字号（像素）。修改时**一定要保留 `px` 后缀**。

**text-align（文本对齐）**

文本居中、左对齐还是右对齐。

**color（颜色）**

文本颜色。简单的颜色名（如 `blue`、`lightyellow` 等）就能用；也可以用 HTML 颜色代码选取任意颜色。更多信息请参考 [htmlcolorcodes.com](https://htmlcolorcodes.com/)。

**background-color（背景颜色）**

卡片背景色。

样式区里可以放任意 CSS——高级用户可以做诸如加背景图、渐变等操作。如果你想实现某种特定格式，建议上网搜 CSS 相关的资料，网上有大量文档。

样式在该笔记类型的**所有卡片间共享**，这意味着一次调整会影响该类型的所有卡片。不过，也可以为单张卡片指定样式。例如，下面的代码会让除第一张外的所有卡片都用黄色背景：

```css
.card {
 background-color: yellow;
}
.card1 {
 background-color: blue;
}
```

## 图片缩放

Anki 默认会把图片缩放到适合屏幕。要更改此行为，可以在样式区底部（默认 `.card { ... }` 之外）加：

```css
img {
 max-width: none;
 max-height: none;
}
```

AnkiDroid 有时[无法将图片缩放到适合屏幕](https://github.com/ankidroid/Anki-Android/issues/3612)。用 CSS 设置图片最大尺寸应该能解决，但 AnkiDroid 2.9 之后似乎被忽略。一种解决办法是在每个样式指令后加 `!important`，例如：

```css
img {
 max-width: 300px !important;
 max-height: 300px !important;
}
```

如果你修改图片样式时发现"已标记"卡片的星标也受影响（例如变得过大），可以用以下选择器单独定位它：

```css
img#star {
 ...;
}
```

你可以用 Chrome 交互式地探索卡片样式：

[https://addon-docs.ankiweb.net/porting2.0.html#webview-changes](https://addon-docs.ankiweb.net/porting2.0.html#webview-changes)

Anki 2.1.50+ 在编辑器中原生支持图片缩放。

## 字段样式

默认样式作用于整张卡片。你也可以让某些字段或卡的某部分使用不同的字体、颜色等。这在学外语时特别重要——如果没有合适的字体，Anki 有时无法正确显示某些字符。

假设你有一个"Expression"字段，想用 macOS 的泰文字体"Ayuthaya"。模板原本是这样的：

```
What is {{Expression}}?

{{Notes}}
```

要做的是把想设置样式的文本用 HTML 包起来。在文本前加：

```html
<div class=mystyle1>
```

文本后加：

```html
</div>
```

像上面这样包起来后，Anki 就会用一个名为"mystyle1"的自定义样式来渲染被包住的文本。这个样式稍后会创建。

所以，如果你想让整个"What is … ?"使用泰文字体，可以这样写：

```html
<div class=mystyle1>What is {{Expression}}?</div>

{{Notes}}
```

如果你只想让 Expression 字段本身用泰文字体，可以这样：

```
What is <div class=mystyle1>{{Expression}}</div>?

{{Notes}}
```

模板改完后，需要切到模板之间的 **Styling（样式）** 区。编辑前它大概是这样：

```css
.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}
```

在末尾添加新样式：

```css
.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}

.mystyle1 {
 font-family: ayuthaya;
}
```

你可以在样式里放任何想要的样式。如果还想增大字号，把 mystyle1 部分改成：

```css
.mystyle1 {
 font-family: ayuthaya;
 font-size: 30px;
}
```

也可以把自定义字体**打包到牌组中**，这样无需在电脑或手机上单独安装。详见[安装字体](#安装字体)章节。

## 音频重播按钮

当卡片包含音频或 TTS 时，Anki 会显示可点击的重播按钮。

如果你不想看到这些按钮，可以在偏好设置中隐藏。

你可以用卡片样式自定义它们的外观。例如，让它们变小并变颜色：

```css
.replay-button svg {
 width: 20px;
 height: 20px;
}
.replay-button svg circle {
 fill: blue;
}
.replay-button svg path {
 stroke: white;
 fill: green;
}
```

## 文本方向

如果你使用的是从右到左的语言（如阿拉伯语、希伯来语），可以在 `.card` 中加 CSS 的 `direction` 属性，让复习时正确显示：

```css
.card {
 direction: rtl;
}
```

这样会改变整张卡片的文字方向。如果只想改变某些字段的方向，可以把字段引用包在 HTML 里：

```html
<div dir="rtl">{{Front}}</div>
```

想修改编辑器中字段的方向，请参考[编辑](https://docs.ankiweb.net/editing.html#customizing-fields)章节。

## 显示代码片段

如果你想在 Anki 卡片中放代码，可以用 HTML 标签把文本格式化为代码。这需要打开[ HTML 视图](https://docs.ankiweb.net/editing.html#editing-features)。

### 行内代码

把文本包在 `<code>` 标签里：

```html
<code>console.log("Hello World!");</code>
```

### 代码块

多行代码用 `<pre><code>`：

```html
<pre><code>
function square(number) {
 return number * number;
};
</code></pre>
```

## 其他 HTML

你的模板可以包含任意 HTML，这意味着互联网上网页用到的所有排版方式都能用在卡片上。表格、列表、图片、外部链接等都支持。比如用表格，可以让卡片的正面和背面对齐排成左右两栏，而不是上下两栏。

本手册不涵盖 HTML 的所有特性，但网上有大量优秀的 HTML 入门指南。

## 浏览器外观

如果你的卡片模板很复杂，[卡片列表](https://docs.ankiweb.net/browsing.html#cardnote-table)中的"问题"和"答案"列（也叫"Front"和"Back"）可能难以阅读。"浏览器外观"选项允许你**只用于浏览器**的自定义模板，因此你只列出重要字段、按你希望的顺序排列即可。语法与标准卡片模板相同。

使用此选项时，如果问题列的文本在答案列开头重复出现，Anki 会在答案列省略重复部分，只在问题列显示。例如：问题列文本是"People in Ladakh speak"，答案是"People in Ladakh speak Ladakhi"，则答案列只会显示"Ladakhi"。

## 平台特定 CSS

Anki 定义了一些特殊的 CSS 类，可让你为不同平台定义不同的样式。下面的例子展示了如何根据复习平台使用不同字体：

```css
/* Windows */ .win .example {
 font-family: "Example1";
}
/* macOS */
.mac .example {
 font-family: "Example2";
}
/* Linux 桌面 */ .linux:not(.android) .example {
 font-family: "Example3";
}
/* Linux 桌面 + Android 设备 */ .linux .example {
 font-family: "Example4";
}
/* Android + iOS */ .mobile .example {
 font-family: "Example5";
}
/* iOS */ .iphone .example,
.ipad .example {
 font-family: "Example6";
}
/* Android */
.android .example {
 font-family: "Example7";
}
```

模板中这样写：

```html
<div class="example">{{Field}}</div>
```

在 AnkiWeb 上还可以用 `.gecko`、`.opera`、`.ie` 等属性选择特定浏览器。完整选项请参考 [http://rafael.adm.br/css_browser_selector/](http://rafael.adm.br/css_browser_selector/)。

## 安装字体

你可以直接给 Anki 安装字体。这在以下场景很有用：使用工作或学校电脑无法安装新字体、或在移动设备上使用 Anki。

Anki 支持最常用的字体格式，如 TrueType（.ttf）、OpenType（.otf）、Web Open Font Format（.woff） 等。

### 将字体添加到媒体文件夹

下载好受支持的字体（如"Arial.ttf"）后，需要把它放进媒体文件夹：

1. 把文件重命名，在开头加下划线，例如改成 `_arial.ttf`。加下划线告诉 Anki：该文件会被模板引用，在检查未使用的媒体时**不要删除**它。
2. 在系统的文件浏览器中，进入 Anki 的应用数据文件夹（详见[文件位置](https://docs.ankiweb.net/files.html#file-locations)），再进入你的 profile 文件夹（如"User 1"）。
3. 在该文件夹下，应该能看到一个名为 `collection.media` 的文件夹。把重命名后的文件拖进去。

### 更新模板以使用该字体

字体加到媒体文件夹后，需要更新模板：

1. 在主界面顶部点击 **Add（添加）**，再用左上角按钮选择要修改的笔记类型。
2. 点击 **Cards（卡片）**。
3. 在样式区底部（最后一个 `}` 之后）加如下代码，把 `_arial.ttf` 替换成你复制到媒体文件夹的文件名：

```css
@font-face {
 font-family: myfont;
 src: url("_arial.ttf");
}
```

**只能改 `"arial"` 那部分，不要改 `"myfont"` 那部分。**

之后，你可以选择修改整张卡片的字体，或只修改特定字段的字体。要改整张卡片的字体，在 `.card` 部分找到 `font-family:` 那一行，把字体名改成 `myfont` 即可。要只改某些字段，请参考上面的[字段样式](#字段样式)章节。

> ⚠️ 文件名务必完全匹配。如果文件叫 `arial.TTF` 而模板里写 `arial.ttf`，将无法生效。

## 夜间模式

当偏好设置中开启夜间模式时，你可以自定义模板的显示效果。

如果你想要更浅的灰色背景，可以这样写：

```css
.card.nightMode {
 background-color: #555;
}
```

如果你有"myclass"样式，下面的代码会在夜间模式下把文字显示为黄色：

```css
.nightMode .myclass {
 color: yellow;
}
```

## 淡入与滚动

默认情况下，Anki 会自动滚动到答案位置。它会查找 `id=answer` 的 HTML 元素并滚动到那里。你可以把 `id` 放在别的元素上以调整滚动位置，或者删掉 `id=answer` 来关闭滚动。

卡片的**问题侧**默认会淡入。如果想调整淡入延迟，可以在正面模板顶部加：

```html
<script>
 qFade = 100;
 if (typeof anki !== "undefined") anki.qFade = qFade;
</script>
```

`100`（毫秒）是默认值；设为 `0` 关闭淡入。

## JavaScript

由于 Anki 卡片被当作网页处理，可以通过卡片模板嵌入一些 JavaScript。推荐阅读论坛上的[这篇文章](https://forums.ankiweb.net/t/card-templates-user-input-101-buttons-keyboard-shortcuts-etc-guide/13756) 作为参考。

⚠️ 由于 JavaScript 是高级功能且容易出错，**JavaScript 功能不提供任何支持或保证**。我们无法协助编写 JavaScript，也无法保证你编写的代码在未来的 Anki 更新中继续可用。如果你无法独立处理遇到的问题，请避免使用 JavaScript。

不同 Anki 客户端的卡片显示实现方式可能不同，因此你需要**在多个平台测试**。许多客户端采用"长生命周期网页 + 动态更新部分内容"的方式实现，所以你的 JS 应当使用 `document.getElementById()` 之类的 API 更新文档中的内容，而不要用 `document.write()` 之类的接口。

`window.alert` 等函数可能不可用。Anki 会把 JavaScript 错误写入终端，你需要[查看控制台](https://addon-docs.ankiweb.net/console-output.html#console-output) 来定位。要调试 JavaScript，可以用 Chrome 的[开发者工具](https://addon-docs.ankiweb.net/debugging.html#webviews)。
