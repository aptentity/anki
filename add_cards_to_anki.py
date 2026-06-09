import json
import urllib.request

ANKI_URL = "http://localhost:8765"

DECK_NAME = "订单信息闪卡"
MODEL_NAME = "Basic"

CARDS = [
    {
        "front": "这张订单的自提点名称是什么？",
        "back": "龙四自提点"
    },
    {
        "front": "订单中购买的第一款面包是什么？",
        "back": "300g/袋 | 义利全麦果仁切片面包早餐面包"
    },
    {
        "front": "义利全麦果仁切片面包的实付价格是多少？",
        "back": "¥3.79"
    },
    {
        "front": "订单中购买的第二款面包是什么？",
        "back": "330g/袋【品牌直供】桃李阳光的味道切片面包"
    },
    {
        "front": "桃李阳光的味道切片面包的实付价格是多少？",
        "back": "¥3.79"
    },
    {
        "front": "订单编号是什么？",
        "back": "PO-260608-598055401782243"
    },
    {
        "front": "支付方式是什么？",
        "back": "多多支付（招商银行信用卡3153）"
    },
    {
        "front": "下单时间是什么时候？",
        "back": "2026/06/08 20:13:43"
    },
    {
        "front": "订单的实付金额是多少？",
        "back": "¥7.58（免运费）"
    },
    {
        "front": "订单的商品总额是多少？",
        "back": "¥7.98"
    },
    {
        "front": "订单总共优惠了多少钱？",
        "back": "¥0.4"
    },
    {
        "front": "订单的自提点完整地址是什么？",
        "back": "北京市北京市通州区金地格林村庄"
    }
]


def anki_request(action, **params):
    payload = {"action": action, "version": 6, "params": params}
    req = urllib.request.Request(
        ANKI_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    create_deck = anki_request("createDeck", deck=DECK_NAME)
    print(f"创建牌组结果: {create_deck}")

    notes = []
    for card in CARDS:
        notes.append({
            "deckName": DECK_NAME,
            "modelName": MODEL_NAME,
            "fields": {
                "Front": card["front"],
                "Back": card["back"]
            },
            "tags": ["订单信息"]
        })

    add_result = anki_request("addNotes", notes=notes)
    print(f"添加笔记结果: {add_result}")
    print(f"共添加 {len([n for n in add_result['result'] if n])} 张闪卡")


if __name__ == "__main__":
    main()
