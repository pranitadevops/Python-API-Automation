import json

import requests
import jsonpath

import Test_Case.test_login
from Test_Case.Environment import baseUrl, Auth

endpoint = "/api/user/nutritionist/list?"


class UserList:
    def __init__(self, direction, order_by, pageNumber, search):
        self.direction = direction
        self.order_by = order_by
        self.pageNumber = pageNumber
        self.search = search

        self.params = {"direction": self.direction,
                       "orderBy": self.order_by,
                       "pageNumber": self.pageNumber,
                       "search": self.search}

    def test_user(self):
        headers = {'content-type': 'application/json', 'Authorization': Auth + Test_Case.test_login.Bearer_token}
        response = requests.get(baseUrl + endpoint, headers=headers, params=self.params)
        print(response.text)
        resp = json.loads(response.text)
        if resp["totalElements"] >= 1:
            assert resp["pageNumber"] == 0
            assert "mar22".upper() in resp["list"][0]["fullName"]

        else:
            print("\n Total Elements count is not matching with response")


obj1 = UserList("DESC", "NAME", 0, "0jj")
obj1.test_user()





