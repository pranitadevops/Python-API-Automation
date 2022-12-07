import requests
import json


import Test_Case.test_login
from Test_Case.Environment import baseUrl, Auth


def test_delete():
    id = input("Which information id you want to Delete: ")
    endpoint = '/api/information/' + str(id)
    headers = {'Authorization': Auth + Test_Case.test_login.Bearer_token}
    response = requests.delete(baseUrl + endpoint, headers=headers)
    print(response.text, "Successfully Deleted")

