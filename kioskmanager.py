import os
import sys
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import requests


class DBClient:
    def __init__(self, url):
        self.url = url

    def order_request(self):
        try:
            data = {"OR": {"icecream": "mint", "topping": "chocoball, cereal"}}
            headers = {"Content-Type": "application/json"}
            response = requests.post(self.url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # 요청이 성공했는지 확인
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"주문 요청 처리 중 오류: {e}")
            return None


if __name__ == "__main__":
    url = "http://172.30.1.5:8000/kiosk"
    dbclient = DBClient(url)
    response = dbclient.order_request()

    if response:
        print("Order ID:", response.get("orderId"))
        print("Order IceCream:", response.get("icecream"))
        print("Order Topping:", response.get("topping"))
    else:
        print("주문 요청에 실패했습니다.")
