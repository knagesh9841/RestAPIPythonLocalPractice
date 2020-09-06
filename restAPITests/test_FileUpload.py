import os

import requests

path = os.getcwd()+"\\jsonFiles"

def test_FileUpload():
    myurl = 'https://httpbin.org/post'
    files = {'file': open(path+"\\test.txt", 'rb')}
    getdata = requests.post(myurl, files=files)
    print(getdata.text)
