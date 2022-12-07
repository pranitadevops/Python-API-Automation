import requests
import json

token = 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJSb2xlIjpbIlJPTEVfQURNSU5JU1RSQVRPUiJdLCJzdWIiOiIxMDAwMDAwMDAwMDAwMyIsIkxhc3RMb2dpbiI6IjIwMjItMDgtMjMiLCJpc3MiOiJGcmVzZW5pdXNLZXRvQXBwIiwiSW5pdGlhbHMiOiJEQSIsImV4cCI6MTY2MTI4MzMxOSwiaWF0IjoxNjYxMjU0NTE5LCJOYW1lIjoiRE1JICBBZG1pbiJ9.hZH63A28u2ERL-SM-abvbFrCew5wf_b1JyKWFuYTntU'

def test_auth():
    endpoint = 'https://ketoapp-stage-co.fresenius-kabi.com/'
    headers = {'content-type': 'application/json', 'Auth-token': token
               }
    payload = {
        "password": "dmi-3321a",
        "username": "intl.projects.fresenius@dminc.com"
    }

    url = endpoint + 'api/session/login/bo'
    resp = requests.post(url, headers=headers, json=payload)
    print(resp)
    print(resp.json())


test_auth()
