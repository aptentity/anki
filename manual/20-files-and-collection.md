# 管理文件与卡片集

- [检查卡片集](#检查卡片集)
- [用户数据](#用户数据)
- [程序文件](#程序文件)
- [启动选项](#启动选项)
- [Dropbox 和文件同步](#dropbox-和文件同步)
- [网络文件系统](#网络文件系统)
- [在 U 盘中运行](#在-u-盘中运行)
- [备份](#备份)
- [无法访问硬盘](#无法访问硬盘)
- [临时文件夹权限](#临时文件夹权限)
- [损坏的卡片集](#损坏的卡片集)
  - [Linux / macOS](#linux--macos)
  - [Windows](#windows)
  - [最后一步](#最后一步)

## 检查卡片集

建议定期检查卡片集文件是否有问题。可以通过 **工具 > 检查数据库** 菜单来执行。检查数据库可以确保文件没有被损坏、重建部分内部结构，并对文件进行优化。

检查数据库时，标签列表也会被重建。当单独删除牌组或卡片时，Anki 不会更新已使用标签的列表（因为这样效率太低）。如果想清理掉不再使用的旧标签，检查数据库是唯一的方法。

> ℹ️ Anki 每两周会自动优化一次卡片集。这个优化能确保卡片集运行良好，但自动优化时不会检查错误，也不会重建标签列表。

## 用户数据

<a id="file-locations"></a>

- **Windows**：最新版 Anki 将卡片集文件存储在 appdata 文件夹中。打开文件管理器，在地址栏输入 `%APPDATA%\Anki2` 即可访问。旧版 Anki 存储在 `Documents` 文件夹下的 `Anki` 文件夹中。
- **Mac**：最新版 Anki 将所有用户数据存储在 `~/Library/Application Support/Anki2` 文件夹中。Library 文件夹默认是隐藏的，但在 Finder 中按住 **Option** 键再点击"前往"菜单即可显示。旧版 Anki 存储在 `Documents/Anki` 文件夹中。
- **Linux**：最新版 Anki 将用户数据存储在 `~/.local/share/Anki2`，如果你设置了自定义数据路径，则为 `$XDG_DATA_HOME/Anki2`。如果你使用的是第三方 **Flatpak** 版本，文件会存储在 `~/.var/app/net.ankiweb.Anki/data/Anki2/`。旧版 Anki 存储在 `~/Documents/Anki` 或 `~/Anki` 中。

在 Anki 文件夹中，程序级和 profile 级的偏好设置存储在一个名为 `prefs.db` 的文件中。

每个 profile 还有一个独立的文件夹，包含：

- 笔记、牌组、卡片等，存储在 `collection.anki2` 文件中
- 音频和图片，存储在 `collection.media` 文件夹中
- 备份文件夹
- 一些系统文件

> ⚠️ **不要在 Anki 运行时复制或移动卡片集**，否则可能导致卡片集损坏。也**不要移动或修改**文件夹中的其他文件。

## 程序文件

Anki 启动器默认安装在以下位置：

- Windows：`%LOCALAPPDATA%\Programs\Anki`
- macOS：`/Applications/Anki.app`
- Linux：`/usr/local/share/anki`

用启动器安装 / 更新 Anki 时，辅助文件会下载到以下位置：

- Windows：`%LOCALAPPDATA%\AnkiProgramFiles`
- macOS：`~/Library/Application Support/AnkiProgramFiles`
- Linux：`~/.local/share/AnkiProgramFiles`

删除该文件夹后，启动器会变成全新安装状态。

`AnkiProgramFiles` 包含启动 Anki 所需的所有文件（除了启动器本身）。你可以把它复制到其他文件夹或系统，通过打开 `AnkiProgramFiles/.venv/bin/anki`（Windows 上为 `AnkiProgramFiles\.venv\scripts\anki`）从新位置启动 Anki。如果放在新电脑的标准位置，启动器也能复用现有文件（前提是复制时保留了修改时间）。

更多内容参见下文的 U 盘运行部分。

## 启动选项

如果你在一台电脑上做了破坏性修改，而另一台电脑上有未损坏的副本，你可能希望在**不同步的情况下**启动 Anki，以便使用完整同步选项而不必先下载更改。同样，如果遇到 Anki 问题，你可能需要（或者被指示）临时禁用插件来排查问题。

同时做这两件事的方法是：在启动 Anki 时**按住 `Shift` 键**，直到屏幕上出现消息告知 Anki 已以安全模式启动。如果在 Linux 上不生效，运行 `anki --safemode`。

可以在启动时指定自定义文件夹位置。这是一个高级功能，主要用于便携式安装，大多数情况下建议使用默认位置。

指定替代文件夹的语法：

```
anki -b /path/to/anki/folder
```

- 如果有多个 profile，可以传 `-p <名称>` 加载指定 profile
- 如果传入 `-p` 加一个不存在的名称，Anki 会在启动时显示 Profile 选择界面。如果不指定 profile，则加载上次使用的 profile
- 要更改界面语言，使用 `-l <ISO 639-1 语言代码>`，例如 `-l ja` 表示日语

如果想始终使用自定义文件夹位置，可以修改 Anki 的快捷方式。在 Windows 上，右键点击快捷方式，选择"属性"，切换到"快捷方式"标签页，在程序路径后添加 `-b \path\to\data\folder`，最终结果类似于：

```
"C:\Program Files\Anki\anki.exe" -b "C:\AnkiDataFolder"
```

你也可以用 `-l` 选项来实现不同语言版本的快速切换。

Windows 上路径本身必须用反斜杠（`\`），不是正斜杠（`/`）。

在 Mac 上，点击 Anki 图标的行为不太好改，但可以从终端用自定义基础文件夹启动 Anki：

```
open /Applications/Anki.app --args -b ~/myankifolder
```

另外，你也可以定义环境变量 `ANKI_BASE`：
- Windows：`set "ANKI_BASE=C:/path/to/AnkiDataFolder"`
- Linux / macOS：`export ANKI_BASE="/path/to/AnkiDataFolder"`

## Dropbox 和文件同步

> ⚠️ **不建议**直接将 Anki 文件夹通过第三方同步服务（如 Dropbox）同步，因为这可能导致文件在同步过程中被修改，造成数据库损坏。

如果你只想同步媒体文件，可以把外部文件夹链接到 Dropbox 等服务。更多内容参见 [DropboxWiki: Sync Folders Outside Dropbox (archive.org)](http://web.archive.org/web/20180919153730/http://www.dropboxwiki.com/tips-and-tricks/sync-other-folders)。

如果你确实想同步卡片集本身，强烈建议创建一个脚本：先把文件从同步文件夹复制到本地文件夹，启动 Anki，关闭 Anki 后再把文件复制回去。这样可以确保文件在打开状态下永远不会被同步。

## 网络文件系统

> ⚠️ 强烈建议将 Anki 文件存储在本地硬盘上，因为网络文件系统可能导致数据库损坏。如果网络文件系统是唯一选择，建议定期使用 **工具 > 检查数据库** 来检测损坏。

## 在 U 盘中运行

在 Windows 上，可以将 Anki 安装到 USB / U 盘并作为便携式应用程序运行。以下示例假设 U 盘盘符为 E，请根据实际情况调整。

> ⚠️ **盘符必须在所有设备上相同**。如果在 E 盘设置，移动到 D 盘后无法使用。
>
> ⚠️ 如果 U 盘格式化为 FAT32，媒体与 AnkiWeb 同步可能不正常。请格式化为 NTFS 以确保媒体正常同步。

1. 下载最新版 Anki 启动器，安装到自定义位置：`E:\Anki\Launcher`（注意不是 `E:\Anki\Launcher\Anki`）
2. 启动器出现后，直接关闭，不要完成安装
3. 创建文件 `E:\Anki\Anki.bat`，内容如下：

```bat
@echo off
echo Starting Anki...
set USB_ROOT=%~dp0
set ANKI_LAUNCHER_VENV_ROOT=%USB_ROOT%\AnkiProgramFiles
set ANKI_LAUNCHER=%USB_ROOT%\Launcher\anki
set ANKI_BASE=%USB_ROOT%\AnkiData
start /b %ANKI_LAUNCHER%
```

4. 双击创建的 .bat 文件，正常安装 Anki
5. 之后双击 .bat 文件即可在其他机器上运行 Anki

> ℹ️ **工具 > 升级 / 降级** 功能会继续生效，但仅在机器可以访问互联网时可用。

## 备份

详见[备份章节](./backups.html)。

## 无法访问硬盘

如果 Anki 无法写入 [Anki 文件夹](#user-data) 中的文件，启动时会显示"无法访问硬盘"的消息，然后关闭。如果不确定如何修复权限问题，请联系身边的电脑高手寻求帮助。

## 临时文件夹权限

Anki 使用系统临时文件夹存储临时数据。如果临时文件夹的权限被恶意软件或有问题的杀毒软件从默认值修改了，Anki 将无法正常工作。

如果你使用的是 Windows 7，修复步骤如下（比较复杂，不确定时请找专业人士）：

1. 点击开始栏，输入 `%temp%`（包括百分号），按回车
2. 进入上一级文件夹，找到 temp 文件夹，右键点击，选择"属性"
3. 切换到"安全"标签页，点击"高级"
4. 切换到"所有者"标签页。如果你的用户名不在列表中，点击按钮获取所有权
5. 在安全属性页的高级设置中，确保你有完全控制权。在默认 W7 安装中，权限实际是从 `c:\Users\你的用户名` 继承的

## 损坏的卡片集

Anki 使用的文件格式对程序崩溃和电脑崩溃有很强的抵抗力，但如果文件在 Anki 打开时被修改、存储在网络驱动器上，或因 Bug 而损坏，卡片集仍然可能损坏。

运行 **工具 > 检查数据库** 时，如果 Anki 检测到文件已损坏，会收到相应提示。**最好的恢复方式是从最近的[自动备份](#备份)恢复**；如果备份太旧，可以尝试修复损坏。

在 Linux 上，确保已安装 sqlite3。在 Mac 上 sqlite3 应该已内置。在 Windows 上，下载 [sqlite3 for Windows](https://www.sqlite.org/download.html)。

接下来，先备份你的 `collection.anki2` 文件，以防后续步骤出问题。

### Linux / macOS

打开终端，切换到 `collection` 所在文件夹，输入：

```bash
sqlite3 collection.anki2 .dump > dump.txt
```

用文本编辑器打开生成的 `dump.txt`，查看最后一行。如果显示 `rollback;`，改为 `commit;`

然后在终端运行：

```bash
cat dump.txt | sqlite3 temp.file
```

> ⚠️ 一定要用 `temp.file`，不要把 `collection.anki2` 放在右边，否则会清空文件！

完成后进入最后一步。

### Windows

把 `sqlite3.exe` 和你的牌组文件复制到桌面。然后点击 **开始 > 运行**，输入 `cmd.exe`。

如果是新版 Windows，命令提示符可能不会从桌面启动。如果在命令提示符中看不到 desktop，输入类似以下内容（把 "administrator" 替换为你的登录名）：

```
cd C:\Users\Administrator\Desktop
```

然后输入：

```
sqlite3 collection.anki2 .dump > dump.txt
```

用文本编辑器打开生成的 `dump.txt`，查看最后一行。如果显示 `rollback;`，改为 `commit;`

然后运行：

```
type dump.txt | sqlite3 temp.file
```

> ⚠️ 一定要用 `temp.file`，不要把 `collection.anki2` 放在右边，否则会清空文件！

完成后进入最后一步。

### 最后一步

检查是否出现错误信息，并确认 `temp.file` 不为空。这个过程会优化卡片集，所以新文件比旧文件略小是正常的。

确认文件非空后：

1. 将原始 `collection.anki2` 文件重命名为其他名称
2. 将 `temp.file` 重命名为 `collection.anki2`
3. 将 `collection.anki2` 移回卡片集文件夹，覆盖旧版本
4. 启动 Anki，进入 **工具 > 检查数据库**，确保卡片集已成功恢复