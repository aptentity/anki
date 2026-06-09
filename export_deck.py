import json
import urllib.request

ANKI_URL = "http://localhost:8765"
DECK_NAME = "订单信息闪卡"
EXPORT_PATH = "/Users/admin/Documents/work/anki/订单信息闪卡.apkg"


def anki_request(action, **params):
    payload = {"action": action, "version": 6, "params": params}
    req = urllib.request.Request(
        ANKI_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


result = anki_request("exportPackage", deck=DECK_NAME, path=EXPORT_PATH)
print(f"导出结果: {result}")
