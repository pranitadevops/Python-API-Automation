import json

import jsonpath
import requests

import Test_Case.test_login
from Test_Case.Environment import baseUrl, Auth


def test_listinfo():
    pageNumber = input("Enter Page number: ")
    endpoint = f"/api/information/list?category=THE_KIDNEYS&pageNumber={pageNumber}"
    headers = {'Authorization': Auth + Test_Case.test_login.Bearer_token}
    response = requests.get(baseUrl + endpoint, headers=headers)
    print(response.text)
    print(json.dumps(response.json(), indent=4))

    # parse response content
    resp = json.loads(response.text)

    # Validate the response
    for i in resp['list']:
        title_from_resp = jsonpath.jsonpath(i, 'title')
        print(title_from_resp[0])

    # print(f"title : {resp['list'][0]['title']}")

    if resp['list'][0]['id'] == [29]:
        # if resp['list'][0]['id'] % 3 == 0:  We can check if ID is even or odd
        print("\nCorrect!!")
    else:
        print("\nIncorrect Data")

    assert response.status_code == 200


