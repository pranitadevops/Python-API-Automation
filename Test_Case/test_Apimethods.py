import requests
import json
import jsonpath
from pytest import mark, fixture

endpoint = "https://reqres.in"


def test_get_api():
    url = endpoint + "/api/Users"
    param = {"page": 2}
    headers = {"accept": "application/json"}
    resp = requests.get(url, params=param, headers=headers)
    resp = json.loads(resp.text)
    id = resp["data"][0]["id"]
    if id == 7:
        print("TC PASSED")
    else:
        print("TC FAILED")


def test_post_api():
    url = "https://reqres.in/api/users"
    data = {
        "name": "Automation",
        "job": "SDET"
    }

    resp = requests.post(url, data=data)
    print(resp.json()['id'])
    assert resp.json()["job"] == 'SDEnT', "Job Tittle is wrong"
    resp = json.loads(resp.text)
    name = resp["name"]
    assert name == "Automation"


def test_delete_api():
    end_point = 'https://reqres.in'
    url = end_point + '/api/Users/2'
    resp = requests.delete(url)
    print(resp)

    assert resp.status_code == 204


def test_patch_api():
    end_point = 'https://reqres.in'
    url = end_point + '/api/User/2'
    payload = {
        "name": "Path",
        "job": "Patch APIs"
    }
    resp = requests.patch(url, data=payload)
    print(resp)
    print(resp.json())
