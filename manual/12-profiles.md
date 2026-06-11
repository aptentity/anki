# Profile（多用户配置）

- [Profile 窗口](#profile-窗口)

如果多人想在同一台电脑上使用 Anki，你可以为每个用户设置**独立的 profile**。每个用户 profile 有自己的卡片集和程序设置。插件在所有 profile 间共享。打开 **File → Switch Profile** 即可配置 profile。

> ⚠️ **警告：只有一个 profile 可以同步到 AnkiWeb 账户。**
>
> 如果电脑上有多位用户，每个用户的 profile 需要创建自己独立的 AnkiWeb 账户。如果尝试把两个或多个 profile 链接到同一个 AnkiWeb 账户，一个 profile 的数据会被另一个覆盖。

Profile 主要用于不同的人，**不推荐用来拆分你自己的内容**。如果你为自己创建了多个 profile，最好的做法是把它们合并成一个：把 profile A 的一个牌组导出，然后导入到 profile B，对 profile A 中的其他牌组重复此操作，直到所有内容都在 profile B 中。

> 📌 AnkiDroid 不支持 profile。

## Profile 窗口

从主窗口通过 **File → Switch Profile** 进入 Profile 窗口，你可以：

- **打开 / 添加 / 重命名 / 删除**用户 profile
- **退出**程序
- **恢复**[自动备份](https://docs.ankiweb.net/backups.html)
- **降级**你的卡片集——如果你想用旧版 Anki 打开它，这一步是必要的。如果跳过此步骤，在旧版 Anki 中打开卡片集时可能会收到错误消息，你需要回到当前版本、降级、再重试