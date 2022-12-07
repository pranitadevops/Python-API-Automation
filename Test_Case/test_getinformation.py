import json

import jsonpath
import requests

import Test_Case.test_login
from Test_Case.Environment import baseUrl, Auth
import Test_Case.test_createinformation


def test_getinfo():
    # API URL
    UserEndPoint = '/api/information/' + str(Test_Case.test_createinformation.new_id)
    headers = {'Authorization': Auth + Test_Case.test_login.Bearer_token}

    # Make Get Request with Payload
    response = requests.get(baseUrl + UserEndPoint, headers=headers)
    print(response.json())

    # Assertion Check
    json_response = json.loads(response.text)
    category = jsonpath.jsonpath(json_response, 'category')
    print(category)
    assert category == 'API Automation'
