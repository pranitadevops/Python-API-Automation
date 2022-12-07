import json

import jsonpath
import requests

import Test_Case.test_login
from Test_Case.Environment import baseUrl, Auth


def test_createInfo():
    # API URL
    UserEndPoint = "/api/information"
    headers = {'Content-Type': 'application/json', 'Authorization': Auth + Test_Case.test_login.Bearer_token}
    # Read Input from payload
    payload = {
        "image": "string",
        "imageContent": [
            "string"
        ],
        "text": "Kabi_Keto",
        "title": "Session Meet",
        "type": "CHRONIC_KIDNEY_DISEASE",
        "video": "string.mov4"
    }
    # Make Post Request with Payload
    response = requests.post(baseUrl + UserEndPoint, json=payload, headers=headers)
    print(response.json())

    # Parse Format into json format

    # resp = json.loads(response.text)

    # Validating Response code
    # if response.status_code == 200:
    #     print('Successful:' + response.text)
    # else:
    #     print('Failed')
    #
    # assert resp["title"] == 'Pranita', "Title is incorrect"
    # assert resp["text"] == 'Pycharm_TesTing', "text is incorrect"
    # assert resp["image"] == 'string', "image is Correct"
    # assert resp["video"] == 'Video VM', "video is correct"
    # print(resp.content)

    # Parse the Response content
    id = jsonpath.jsonpath(response.json(), 'id')
    info_id = id[0]
    return info_id


new_id = test_createInfo()
print(new_id)
