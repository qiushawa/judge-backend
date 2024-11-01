import pytest
import requests
BASE_URL = "http://127.0.0.1:5000/api"
HEADER ={"X-API-KEY": "A21WFJHNJREGG8784WDMKM"}

def submit_code(language, file_path):
    endpoint = "submit"
    url = f"{BASE_URL}/{endpoint}"

    with open(file_path, 'r') as file:
        code = file.read()

    payload = {
        "language": language,
        "code": code
    }

    response = requests.post(url, headers=HEADER, json=payload, params={"id": 1})

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}
def test_submit_code():
    result = submit_code("python", "code/hello_world.py")
    assert result["result"] == "Accept"
    result = submit_code("c", "code/hello_world.c")
    assert result["result"] == "Accept"
    result = submit_code("cpp", "code/hello_world.cpp")
    assert result["result"] == "Accept"