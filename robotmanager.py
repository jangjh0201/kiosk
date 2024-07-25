import os
import sys
import json
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import requests


class DBClient:
    def __init__(self, url):
        self.url = url

    def robot_request(self, data):
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.post(self.url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # 요청이 성공했는지 확인

        except requests.exceptions.RequestException as e:
            pass
        finally:
            return response


if __name__ == "__main__":
    url = "http://0.0.0.0:8000/robot"
    dbclient = DBClient(url)

    datas = [
        {"OS": {"status": 1}},
        {"OS": {"status": 5}},
        {"OS": {"status": 0}},
        {"OS": {"status": 2}},
        {"OS": {"status": 5}},
        {"OS": {"status": 3}},
        {"OS": {"status": 4}},
        {"OS": {"status": 4}},
        {"OS": {"status": 4}},
        {"OS": {"status": 1}},
        {"OS": {"status": 1}},
        {"OS": {"status": 2}},
        {"OS": {"status": 5}},
        {"OS": {"status": 3}},
    ]

    for data in datas:
        response = dbclient.robot_request(data)
        responseData = response.json()
        print(responseData)

        time.sleep(1)
