import pytest
import requests
BASE_URL = "http://127.0.0.1:5000/api"
HEADER = {"X-API-KEY": "A21WFJHNJREGG8784WDMKM"}

def test_create_question():
    url = f"{BASE_URL}/question/create"
    data = {
        "title": "hello world!",
        "description": """學習所有程式語言的第一個練習題 
請寫一個程式，可以讀入指定的字串，並且輸出指定的字串。

比如：
輸入字串 "world", 則請輸出 "hello, world"
輸入字串 "ARISU", 則請輸出 "hello, ARISU\"""",
        "SampleInput": "ARISU\n",
        "SampleOutput": "hello, ARISU\n",
        "Input": "QiuShAwa\n",
        "Output": "hello, QiuShAwa\n"
    }
    response = requests.post(url, json=data, headers=HEADER)
    assert response.status_code == 201
    assert response.json()["message"] == "Question created successfully"


