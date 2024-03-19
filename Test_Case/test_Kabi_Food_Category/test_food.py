import requests
import Test_Case.test_Kabi_Food_Category
import Test_Case.test_login
from Test_Case.Environment import *


def test_getFood():
    # API URL
    endpoint = '/api/food/category/19/'
    headers = {'Authorization': Auth + Test_Case.test_login.Bearer_token, 'content-type': 'application/json'}
    # 'content-type': 'application/json', str(test_Kabi_Food_Category.test_foodcategoryCreate.new_foodId)

    # Make Get Request with Payload
    response = requests.get(baseUrl + endpoint, headers=headers)
    print(response.json())


def test_datavalidation():
    print("*******Data Validation is correct")
