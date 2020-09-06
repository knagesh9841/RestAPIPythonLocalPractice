import os

import requests
import jsonpath
import json

path = os.getcwd()+"\\jsonFiles"


def test_Firstget():
    # api-endpoint
    APP_URL = 'https://reqres.in/api/users'
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'page': 2}
    # sending get request and saving the response as response object

    #response = requests.get(url=APP_URL, data=PARAMS)
    response = requests.get(url=APP_URL, params=PARAMS)

    # fetch Headers

    #print(response.headers)
    #print(response.headers.get('Date'))
    #print(response.headers.get('Server'))

    # fetch Cookies

    print(response.cookies)

    #Fetch Encoding

    print(response.encoding)

    print(response.content)
    print(response.text)

    print(response.status_code)

    # extracting data in json format in below 2 Ways

    #json_response = response.json()

    json_response = json.loads(response.text)

    # Json path always return list

    email_id = jsonpath.jsonpath(json_response, 'data[0].email')
    print(email_id[0])


def test_FirstPost():
    # api-endpoint
    APP_URL = 'https://reqres.in/api/users'

    # Read Input JSON File

    file = open(path+"\\CreateUser.json", 'r')
    json_inputFile = file.read()
    request_json = json.loads(json_inputFile)

    # Make POST Request with Json Request Body

    response = requests.post(APP_URL, request_json)
    print(response.content)

    print(response.status_code)

    print(response.text)
    json_response = response.json()

    id = jsonpath.jsonpath(json_response, 'id')
    print(id[0])


def test_FirstPut():
    # api-endpoint
    APP_URL = 'https://reqres.in/api/users/2'

    # Read Input JSON File

    file = open(path + "\\UpdateUser.json", 'r')
    json_inputFile = file.read()
    request_json = json.loads(json_inputFile)

    # Make PUT Request with Json Request Body

    response = requests.put(APP_URL, request_json)
    print(response.content)

    print(response.status_code)

    print(response.text)
    json_response = response.json()

    updatedAt = jsonpath.jsonpath(json_response, 'updatedAt')
    print(updatedAt[0])


def test_FirstDelete():

    # api-endpoint
    APP_URL = 'https://reqres.in/api/users/2'

    # Make Delete Request
    response = requests.delete(APP_URL)

    print(response.status_code)

