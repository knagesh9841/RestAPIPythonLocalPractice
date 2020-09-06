import os

import requests
import jsonpath
import json


def test_RestAPIWithRequestHeader():

    # api-endpoint
    APP_URL = 'https://reqres.in/api/users'
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'page': 2}
    # sending get request and saving the response as response object

    headers = {'Content-Type': 'application/json; charset=utf-8'}
    response = requests.get(url=APP_URL, params=PARAMS, headers=headers)

    print(response.headers)

