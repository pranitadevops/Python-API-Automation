import json
import jsonpath
import requests
import Test_Case.test_login
from Test_Case.Environment import baseUrl, Auth


def test_uploadCsvMap():
    global response
    endpoint = '/api/ketomap/upload/bo/'
    headers = {'Authorization': Auth + Test_Case.test_login.Bearer_token}
    # Read Excel file!
    files = {'file': open('C:\\Users\\ptalekar\\Downloads\\KetoMapaChile1.csv', 'rb')}
    response = requests.post(baseUrl + endpoint, headers=headers, files=files)


def test_verifyRsp():
    assert response.status_code == 200, "Status OK"
    assert response.text == 'Successfully', "It should be Successfully"
