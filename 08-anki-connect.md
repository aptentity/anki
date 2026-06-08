# AnkiConnect 教程：让 Anki 与外部程序无缝对接

AnkiConnect 是一个强大的 Anki 插件，它通过 HTTP API 让 Anki 与各种外部程序通信。无论是自动化卡片创建、查询复习状态，还是集成 AI 辅助学习，AnkiConnect 都能帮你实现。

## 一、什么是 AnkiConnect

AnkiConnect 是 Anki 的一个插件，它在 Anki 运行时启动一个本地 HTTP 服务器，允许外部程序调用 Anki 的功能。

**核心能力**：
- 通过 REST API 与 Anki 交互
- 支持增删改查卡片
- 获取复习统计信息
- 触发复习流程

**典型应用场景**：
- 将网页内容自动转换为 Anki 卡片
- AI 辅助生成卡片内容
- 与笔记软件集成（Obsidian、Logseq）
- 自定义复习提醒

## 二、安装 AnkiConnect

### 步骤1：安装插件

1. 打开 Anki → 工具 → 获取插件
2. 输入插件代码：`2055492159`
3. 点击确定，重启 Anki

### 步骤2：验证安装

重启后，打开 Anki 的插件文件夹，确认 `anki_connect` 文件存在：

```
Anki 插件目录（macOS）：
~/Library/Application Support/Anki2/addons21/2055492159/
```

### 步骤3：默认配置

AnkiConnect 默认配置：
- 地址：`http://127.0.0.1:8765`
- 允许所有来源的请求
- 启用所有 API 方法

**生产环境建议**：修改配置，只允许特定来源访问。

## 三、快速开始

### 发送第一个请求

使用 curl 测试连接：

```bash
curl -X POST http://127.0.0.1:8765 -d '{"action": "version", "version": 6}'
```

**响应**：
```json
{"result": "6", "success": true}
```

返回 `"6"` 表示 API 版本，连接成功！

### 请求格式

AnkiConnect 使用 JSON-RPC 2.0 格式：

```json
{
  "action": "方法名",
  "version": 6,
  "params": {
    "参数1": "值1",
    "参数2": "值2"
  }
}
```

### Python 示例

```python
import requests

def anki_action(action, **params):
    """发送请求到 AnkiConnect"""
    return requests.post(
        "http://127.0.0.1:8765",
        json={"action": action, "version": 6, "params": params}
    ).json()

# 获取牌组列表
result = anki_action("getDeckNames")
print(result)
```

## 四、常用 API 方法

### 1. 牌组操作

**获取所有牌组**：
```python
decks = anki_action("getDeckNames")
# 返回: ["Default", "日语::N5词汇", "医学::解剖学"]
```

**创建牌组**：
```python
anki_action("createDeck", deck="我的牌组")
```

**删除牌组**：
```python
anki_action("deleteDeck", deck="我的牌组", cardsToo=True)
```

### 2. 卡片操作

**添加卡片**：
```python
anki_action(
    "addNote",
    note={
        "deckName": "日语::N5词汇",
        "modelName": "Basic",
        "fields": {
            "Front": "猫",
            "Back": "ねこ / 宠物动物"
        },
        "options": {
            "close": False  # 添加后不关闭窗口
        }
    }
)
```

**添加 Cloze 卡片**：
```python
anki_action(
    "addNote",
    note={
        "deckName": "英语",
        "modelName": "Cloze",
        "fields": {
            "Text": "{{c1::Ephemeral}} means temporary.",
            "Back Extra": "adj. 短暂的"
        }
    }
)
```

**查找卡片**：
```python
cards = anki_action(
    "findCards",
    query="deck:日语 tag:动词"
)
```

**删除卡片**：
```python
anki_action("deleteNotes", notes=[123456, 789012])
```

### 3. 复习操作

**获取待复习数量**：
```python
counts = anki_action("getNumCardsReviewedToday")
print(f"今日复习：{counts} 张")
```

**触发复习**：
```python
anki_action("guiDeckReview", deck="日语::N5词汇")
```

### 4. 统计信息

**获取牌组统计**：
```python
stats = anki_action("getDeckStats", decks=["日语::N5词汇"])
```

**获取卡片信息**：
```python
info = anki_action("getCardInfo", card=123456)
```

## 五、实用场景

### 场景1：自动从网页创建卡片

```python
import requests
from bs4 import BeautifulSoup

def create_card_from_url(url, deck_name):
    """从网页自动提取内容创建卡片"""
    # 获取网页内容
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 提取标题和描述（示例）
    title = soup.find('h1').text
    description = soup.find('meta', attrs={'name': 'description'})['content']
    
    # 创建卡片
    anki_action(
        "addNote",
        note={
            "deckName": deck_name,
            "modelName": "Basic",
            "fields": {"Front": title, "Back": description}
        }
    )
    print(f"已创建卡片：{title}")

# 使用
create_card_from_url("https://example.com/article", "收藏")
```

### 场景2：批量导入 CSV

```python
import csv

def import_csv(csv_file, deck_name):
    """从 CSV 文件批量导入卡片"""
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for front, back in reader:
            anki_action(
                "addNote",
                note={
                    "deckName": deck_name,
                    "modelName": "Basic",
                    "fields": {"Front": front, "Back": back}
                }
            )
    print(f"导入完成：{csv_file}")

import_csv("vocabulary.csv", "英语")
```

### 场景3：AI 辅助生成卡片

```python
def generate_card_with_ai(keyword):
    """使用 AI 生成卡片内容"""
    # 调用 AI API 生成问题和答案
    response = call_ai_api(f"为 '{keyword}' 生成一个 Anki 卡片问题和答案")
    
    # 解析 AI 返回的内容
    question, answer = parse_ai_response(response)
    
    # 创建卡片
    anki_action(
        "addNote",
        note={
            "deckName": "AI-生成",
            "modelName": "Basic",
            "fields": {"Front": question, "Back": answer}
        }
    )

# 使用
generate_card_with_ai("Photosynthesis")
```

### 场景4：与 Obsidian 集成

Obsidian 用户可以使用社区插件 `AnkiConnect` 实现双向同步：

1. 安装 Obsidian 的 AnkiConnect 插件
2. 配置插件连接到本地 Anki
3. 使用 `{{anki}}` 语法在笔记中标记内容

```markdown
# 笔记标题

{{anki:什么是光合作用?}} - {{anki:植物通过光合作用将光能转化为化学能}}

{{cloze:光合作用发生在植物的{{c1::叶绿体}}中}}
```

## 六、注意事项

### 安全建议

1. **默认配置仅本地访问**：127.0.0.1 无法从外部网络访问
2. **生产环境限制来源**：修改插件配置，只允许特定 IP
3. **不要暴露到公网**：否则可能被人恶意添加卡片

### 常见问题

**Q: AnkiConnect 无法连接？**
- 确认 Anki 已启动
- 检查插件是否安装成功
- 确认端口 8765 未被占用

**Q: 卡片添加失败？**
- 检查牌组名称是否正确
- 检查笔记类型是否存在
- 检查字段名称是否匹配

**Q: 如何调试？**
- 查看 Anki 的插件日志
- 使用 `POST http://127.0.0.1:8765` 手动测试
- 检查返回的 `error` 字段

### 性能优化

1. **批量操作**：多次添加时使用批量请求
2. **避免频繁查询**：使用缓存减少 API 调用
3. **后台运行**：确保 Anki 在后台运行

## 七、API 完整列表

| 类别 | 方法 | 说明 |
|-----|------|------|
| 牌组 | `getDeckNames` | 获取所有牌组 |
| 牌组 | `createDeck` | 创建牌组 |
| 牌组 | `deleteDeck` | 删除牌组 |
| 牌组 | `getDeckStats` | 获取牌组统计 |
| 卡片 | `addNote` | 添加卡片 |
| 卡片 | `updateNote` | 更新卡片 |
| 卡片 | `deleteNotes` | 删除卡片 |
| 卡片 | `findCards` | 查找卡片 |
| 卡片 | `getCardInfo` | 获取卡片信息 |
| 复习 | `guiDeckReview` | 开始复习 |
| 复习 | `getNumCardsReviewedToday` | 获取今日复习数 |
| 统计 | `getCollectionStats` | 获取集合统计 |

完整 API 文档：https://foosoft.net/projects/anki-connect/

## 总结

AnkiConnect 为 Anki 打开了无限可能：

| 能力 | 说明 |
|-----|------|
| 自动化 | 自动从各种来源创建卡片 |
| 集成 | 与笔记软件、AI 工具无缝对接 |
| 扩展 | 自定义工作流，满足特殊需求 |
| 生态 | 社区提供了丰富的集成方案 |

---

**相关资源**：
- [Anki 基础卡片创建教程](04-anki-basic-cards.md) - 学习卡片创建
- [Anki Cloze 完形填空教程](05-anki-cloze.md) - 学习 cloze 语法
- [Anki 优质卡片制作原则](07-anki-card-principles.md) - 学习高质量卡片制作