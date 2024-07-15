import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import requests

url = "http://127.0.0.1:8000/order"
data = {
    "ice_cream_name": "바닐라",
    "topping_names": "초코볼, 시리얼",
    "consumable_names": "스푼, 홀더",
}

response = requests.post(url, data=data)
print(response.status_code)
