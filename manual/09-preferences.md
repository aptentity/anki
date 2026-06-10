# 偏好设置

- [外观](#外观)
  - [常规](#常规)
  - [用户界面](#用户界面)
  - [减少干扰](#减少干扰)
- [复习](#复习)
  - [调度器](#调度器)
  - [复习选项](#复习选项)
- [编辑](#编辑)
  - [编辑选项](#编辑选项)
  - [浏览](#浏览)
- [同步](#同步)
  - [同步设置](#同步设置)
  - [AnkiWeb 账户](#ankiweb-账户)
  - [自托管同步服务器](#自托管同步服务器)
- [备份](#备份)

偏好设置可通过 **Windows / Linux 的"工具"菜单**，或 **Mac 的"Anki"菜单**访问。

## 外观

### 常规

**Language（语言）**

更改界面显示语言。你可以[在这里](https://translating.ankiweb.net/)协助改进翻译。

### 用户界面

**Theme（主题）**

Dark（夜间）模式会让 Anki 的界面变暗，卡片以**黑底白字**显示。某些卡片模板可能需要修改才能在此模式下正确显示 —— 详见[夜间模式样式](https://docs.ankiweb.net/templates/styling.html#night-mode)。

从 2.1.50+ 起，新增了"自动切换日 / 夜间模式"的选项。

**User interface size（界面大小）**

如果觉得界面元素太小，可以调大此设置。

**Reset Window Sizes（重置窗口尺寸）**

把所有窗口的大小和位置恢复到默认设置。

**Video driver（视频驱动）**

Anki 的库需要视频驱动来在屏幕上绘制内容。由于硬件和软件配置不同，你机器上效果最好的驱动可能因人而异。Software（软件渲染）通常较慢，但在某些系统上其他选项无法工作时它能用。

> 注：如果在 Windows 上，请参考[此页面](https://docs.ankiweb.net/platform/windows/display-issues.html)。

### 减少干扰

这些选项让你在复习时**隐藏一些不必要的界面元素**。你可以：

- 复习时隐藏顶部和底部栏
- 启用"极简"模式，让界面更紧凑
- 减少动效，关闭一些过渡 / 动画
- 在原生样式和 Anki 主题间切换（仅 Mac / Linux）

## 复习

### 调度器

**Next day starts at（第二天开始时间）**

控制 Anki 应何时开始显示"第二天"的卡片。默认的凌晨 4 点可以保证：如果你在午夜前后学习，不会一次性看到两天的卡片。如果你熬夜很晚或起得很早，可以把它调整为你通常的睡眠时间。注意：第二天的开始时间是相对于**当前时区**计算的；任何跨日期边界的卡片都会[显示在它们调度的那一天的开始](https://docs.ankiweb.net/deck-options.html#day-boundaries)，和复习卡片一样。

**Learn ahead limit（提前学习阈值）**

告诉 Anki 在"当前牌组没有到期卡片但有学习中的卡片"时该怎么办。默认的 20 分钟表示：如果有延迟 < 20 分钟的学习中卡片且无其他事可做，就提前显示。如果设为 0，Anki 会**始终等满延迟**，在剩余卡片准备好前一直显示"恭喜完成"界面。

**Timebox time limit（时间盒限制）**

"时间盒"是一种把长时间活动（如 30 分钟学习）拆成小块的专注技巧。如果你把"时间盒限制"设为非零的分钟数，Anki 会在达到该时长时定期提示你在限定时间内复习了多少张卡片。

### 复习选项

**Show play buttons on cards with audio（带音频的卡片显示播放按钮）**

学习界面中，是否为带音频的卡片显示可点击的（重）播按钮。

**Interrupt current audio when answering（答题时打断当前音频）**

答题时是否停止正在播放的音频。

**Show remaining card count（显示剩余卡片数）**

关闭此项可隐藏屏幕底部的卡片计数。

**Show next review time above answer buttons（在答案按钮上方显示下次复习时间）**

便于知道卡片被推到了多久以后。

**Spacebar (or enter) also answers card（空格 / 回车也算答题）**

定义按空格或回车是否也算"答题"。

## 编辑

### 编辑选项

**Paste clipboard images as PNG（剪贴板图片粘贴为 PNG）**

默认 Anki 把剪贴板里的图片粘贴为 JPG 以节省空间。你可以打开此选项改为粘贴为 PNG。PNG 支持透明背景且无损，但文件通常大很多。

**Paste without Shift strips formatting（不带 Shift 粘贴时去除格式）**

默认情况下，粘贴会**保留**粗体、颜色等格式，除非按住 Shift。此选项反转该行为。

**Default deck（默认牌组）**

控制笔记类型和牌组之间的交互方式：

- **When adding, default to current deck（添加时默认用当前牌组）**：Anki 会为每个牌组保存"上次使用的笔记类型"，下次选该牌组时会自动选用（并且从任何地方点 **Add** 时默认选中当前牌组）。
- **Change deck depending on note type（按笔记类型切换牌组）**：Anki 为每个笔记类型保存"上次使用的牌组"（并且从任何地方点 **Add** 时默认选中上次用的笔记类型）。

如果你在每个牌组中总是用同一个笔记类型，第二种可能更方便。

> "上次使用的牌组 / 笔记类型"在**添加卡片时**才会更新。如果你换了牌组但没添加卡片就关闭了添加窗口，这个选择**不会保存**。

### 浏览

**Default search text（默认搜索文本）**

自定义浏览器启动时的初始搜索文本（例如默认以 `deck:current` 开头）。

**Ignore accents in search (slower)（搜索时忽略重音，较慢）**

开启后，简单的文本搜索会自动[忽略重音符号](https://docs.ankiweb.net/searching.html#ignoring-accentscombining-characters)。

## 同步

此标签页包含与 AnkiWeb 同步相关的选项。

### 同步设置

**Synchronize audio and images too（同步音频和图片）**

开启后，媒体也会与 AnkiWeb 同步。

**Automatically sync on profile open/close（打开 / 关闭 profile 时自动同步）**

如果你不想在打开 / 关闭 [profile](https://docs.ankiweb.net/profiles.html) 时自动与 AnkiWeb 同步，可以关闭此选项。

**Periodically sync media（定期同步媒体）**

开启后，Anki 会每 15 分钟自动同步一次媒体。不开启时，媒体会在常规同步时批量同步。**慢速网络**下建议开启，避免常规同步时大文件上下传。

**示例**

假设你创建了一些含媒体文件的新卡片。开启此设置后，如果你添加卡片一小时，过程中会有 4 次较小的媒体上传。不开启的话，你得在下一次常规同步时上传所有媒体，可能要花更多时间。

**On next sync, force changes in one direction（下次同步时强制单向覆盖）**

开启后，下次同步会询问你是要上传还是下载。这在你意外做了改动，想用 AnkiWeb 上的旧版本覆盖本地时很有用。

### AnkiWeb 账户

登录后，点击 **Log Out** 即可登出。

### 自托管同步服务器

关于自定义同步服务器的说明，参见[此章节](https://docs.ankiweb.net/sync-server.html)。

## 备份

请参考手册的[此章节](https://docs.ankiweb.net/backups.html#automatic-backups)。
