import json
import jsonpath
import requests

# Staging BaseURL
baseUrl = "https://ketoapp-stage.fresenius-kabi.com/api/session/login/bo"
email = "intl.projects.fresenius@dminc.com"
password = "dmi-3321a"


# Auth = "Bearer "


# Testcase code must be written in Method.
# Method Name must be started with test

def test_login():
    # UserSignInEndPoint = "/api/session/login/bo"
    headers = {'Content-Type': 'application/json'}

    payload = {
        "password": password,
        "username": email
    }

    response = requests.post(baseUrl, json.dumps(payload), headers=headers)
    print(response.json())

    # Parse Format into json format
    json_response = json.loads(response.text)

    # Fetch value using json path
    Access_Token = jsonpath.jsonpath(json_response, 'token')
    AuthToken = Access_Token[0]
    return AuthToken


Bearer_token = test_login()
print(Bearer_token)
