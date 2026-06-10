# 卡片模板

- [模板界面](#模板界面)
- [模板选项](#模板选项)
  - [重命名 / 重新排序卡片](#重命名--重新排序卡片)
  - [Deck Override（牌组覆盖）](#deck-override牌组覆盖)
  - [Browser Appearance（浏览器外观）](#browser-appearance浏览器外观)
- [子章节](#子章节)

**卡片模板**告诉 Anki 哪些字段应该出现在卡片的正面和背面，并控制当某些字段有内容时将生成哪些卡片。通过调整卡片模板，你可以**一次性**改变许多卡片的设计和样式。

卡片模板在以下入门视频中有介绍：

- [Switching Card Order（切换卡片顺序）](http://www.youtube.com/watch?v=DnbKwHEQ1mA&yt:cc=on)
- [Styling Cards（卡片样式）](http://www.youtube.com/watch?v=F1j1Zx0mXME&yt:cc=on)
- [Typing in the Answer（在答案中输入）](http://www.youtube.com/watch?v=5tYObQ3ocrw&yt:cc=on)

## 模板界面

你可以通过点击**编辑窗口中的"卡片…"按钮**来修改卡片模板。

可以使用 **Ctrl+1、Ctrl+2、Ctrl+3** 在"正面模板"、"背面模板"和"样式"之间切换。

在 Anki 中，模板使用 **HTML** 编写（也就是网页使用的语言）。样式部分使用 **CSS**（用于给网页添加样式的语言）。

右侧是当前所选卡片的**正面和背面预览**：

- 如果你是在**添加笔记**时打开该窗口，预览将基于你在"添加笔记"窗口中输入的文本。
- 如果你是在**编辑笔记**时打开，预览将基于该笔记的内容。
- 如果你是在**工具 → 管理笔记类型**中打开，Anki 会在内容的位置以括号形式显示每个**字段的名称**。

## 模板选项

窗口右上角有一个 **"选项"按钮**，可用于重命名 / 重新排序卡片，以及配置以下选项：

### 重命名 / 重新排序卡片

当一个笔记类型下有多个卡片模板时，Anki 会按"卡片 1"、"卡片 2"… 的默认名称生成。你可以在此：

- **重命名**：给卡片模板起更有意义的名字（如"识别卡"、"主动回忆卡"），便于在浏览器中区分。
- **重新排序**：调整同一条笔记下多张卡片的生成顺序，间接影响复习时的出现顺序。

### Deck Override（牌组覆盖）

- **作用**：改变该卡片类型生成的卡片**将要放入的牌组**。
- **默认行为**：卡片会被放入"添加笔记"窗口中你选择的牌组。
- **设置后**：该卡片类型生成的卡片会**强制放入你在模板里指定的牌组**，而不是"添加笔记"窗口中选择的牌组。
- **使用场景**：想把卡片分到不同牌组时（例如：学语言时，把"主动回忆"卡片放一个牌组，"识别型"卡片放另一个）。
- 💡 想查看卡片当前去哪个牌组，再次打开 Deck Override 即可查看。

### Browser Appearance（浏览器外观）

- **作用**：为浏览器中"问题"和"答案"列设置**不同（通常是简化的）**模板。
- 详细说明参见：[Browser Appearance（浏览器外观）](https://docs.ankiweb.net/templates/styling.html#browser-appearance)。

## 子章节

- [字段替换](https://docs.ankiweb.net/templates/fields.html)
- [卡片生成](https://docs.ankiweb.net/templates/generation.html)
- [样式与 HTML](https://docs.ankiweb.net/templates/styling.html)
- [检查与错误](https://docs.ankiweb.net/templates/errors.html)
