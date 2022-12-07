import json

import jsonpath
import requests
import Test_Case

from Test_Case.Environment import *


def test_createFood():
    endpoint = '/api/food/category'
    headers = {'Authorization': Auth + Test_Case.test_login.Bearer_token, 'content-type': 'application/json'}

    # Read Data from file
    f = open('C:/Users/ptalekar/OneDrive - DMI/Desktop/post json.json', 'r')

    # Read input data from variable
    # payload = {
    #     "description": "djpo Estceg",
    #     "foodSubCategory": [
    #         {
    #             "description": "SSDescription",
    #             "name": "wwebtv b e"
    #         }
    #     ],
    #     "name": "njsc_esc"
    # }

    json_request = json.loads(f.read())
    response = requests.post(baseUrl + endpoint, json=json_request, headers=headers)
    print(response.text)

    # parse the Data
    id = jsonpath.jsonpath(response.json(), 'id')
    food_id = id
    return food_id


new_foodId = test_createFood()
print(new_foodId)
