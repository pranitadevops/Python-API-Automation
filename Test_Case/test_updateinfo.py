import jsonpath
import requests
import json

import Test_Case.test_login
from Test_Case.Environment import baseUrl, Auth


def test_update():
    # Take Input from User to update values

    id = input("Which Information id would you like to update? ")
    endpoint = '/api/information/' + str(id)
    headers = {'Content-Type': 'application/json', 'Authorization': Auth + Test_Case.test_login.Bearer_token}
    title = input("What would you like your Title to be updated:")
    payload = {
        "image": "string",
        "imageContent": [
            "string"
        ],
        "text": "string",
        "title": title,
        "type": "THE_KIDNEYS",
        "video": "string"
    }
    # Make Put Request with Payload
    response = requests.put(baseUrl + endpoint, headers=headers, json=payload)
    print(response.text)

    # Validating Response code
    assert response.status_code == 200, "the request has succeeded"

    # Parse the response content
    resp = json.loads(response.text)
    title = jsonpath.jsonpath(resp, "title")
    print(title)




# validate id which does not exist in system,(Compare with response of createinformation.py )