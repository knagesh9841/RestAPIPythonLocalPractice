import requests
import jsonpath
import json

from requests.auth import HTTPDigestAuth, HTTPBasicAuth


def test_BasicAuthetication():
    response_data = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('knagesh9841', 'knagesh9841'))
    print(response_data.text)


def test_DigestAuthetication():
    response_data = requests.get('https://httpbin.org/digest-auth/auth/admin/admin123', auth=HTTPDigestAuth('admin', 'admin123'))
    print(response_data.text)
    user = jsonpath.jsonpath(response_data.json(), 'user')
    print(user[0])