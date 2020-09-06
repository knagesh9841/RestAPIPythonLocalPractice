import os

import requests
import jsonpath
import json

path = os.getcwd()+"\\jsonFiles"


def test_RequestChaining():

    App_Url = 'http://thetestingworldapi.com/api/studentsDetails'
    file = open(path+"\\Add_StudentDetails.json", 'r')

    requests_json = json.loads(file.read())

    response = requests.post(App_Url, requests_json)

    print(response.text)

    id = jsonpath.jsonpath(response.json(), 'id')

    print(id[0])

    App_Url = 'http://thetestingworldapi.com/api/technicalskills'

    file = open(path + "\\Add_TechnicalDetails.json", 'r')

    requests_json = json.loads(file.read())

    requests_json['id'] = int(id[0])
    requests_json['st_id'] = id[0]

    response = requests.post(App_Url, requests_json)

    print(response.text)

    App_Url = 'http://thetestingworldapi.com/api/studentsDetails/'+str(id[0])

    response = requests.get(App_Url)

    print(response.text)



