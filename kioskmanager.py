import re
import requests
import os
import sys
import json
from random import choice, randint
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class DBClient:
    def __init__(self, url):
        self.url = url

    def order_request(self, data):
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                self.url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # 요청이 성공했는지 확인
            return response

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def show_tables(self):
        try:
            response = requests.get(
                self.url)
            response.raise_for_status()  # 요청이 성공했는지 확인
            print("응답 데이터:", response.json())
            print(f"1번 테이블: {response.json()[0]}")
            return response

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def use_table_one(self):
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.patch(
                self.url + "/1", headers=headers, json={"status": 0}
            )
            response.raise_for_status()  # 요청이 성공했는지 확인

            # 응답 데이터를 JSON으로 파싱하여 출력
            response_data = response.json()
            print("응답 데이터:", response_data)
            print(f"1번 테이블: {response_data[0]}")

            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None


def get_random_dates(n):
    today = datetime.now()
    start_date = today - timedelta(days=30)
    random_dates = [
        start_date
        + timedelta(
            days=randint(0, 30),
            hours=randint(0, 23),
            minutes=randint(0, 59),
            seconds=randint(0, 59),
        )
        for _ in range(n)
    ]
    random_dates.sort()  # 날짜를 오름차순으로 정렬
    return random_dates


def generate_orders(dbclient, n):
    icecreams = ["mint", "choco", "strawberry"]
    toppings = ["chocoball", "cereal", "oreo"]

    # 가능한 토핑 조합
    combinations = [
        [],
        [toppings[0]],
        [toppings[1]],
        [toppings[2]],
        [toppings[0], toppings[1]],
        [toppings[0], toppings[2]],
        [toppings[1], toppings[2]],
        [toppings[0], toppings[1], toppings[2]],
    ]

    # n개의 랜덤 날짜 생성
    random_dates = get_random_dates(n)

    # n개의 주문 생성
    for attempt, order_time in enumerate(random_dates, 1):
        icecream = choice(icecreams)
        topping_combo = choice(combinations)
        topping_str = ", ".join(topping_combo)
        order_time_str = order_time.strftime("%Y-%m-%d %H:%M:%S")

        data = {
            "OR": {
                "icecream": icecream,
                "topping": topping_str,
                "order_time": order_time_str,
            }
        }

        response = dbclient.order_request(data)
        if response:
            responseData = response.json()
            print(f"주문시도 {attempt}회:", responseData)
        else:
            print(f"주문시도 {attempt}회: 요청 실패")


if __name__ == "__main__":
    # url = "http://0.0.0.0:8000/test"
    url = "http://0.0.0.0:8000/table"
    dbclient = DBClient(url)

    # 100개의 주문 생성
    # generate_orders(dbclient, 100)

    # 테이블 조회
    dbclient.show_tables()

    # 테이블 선택
    # dbclient.use_table_one()
