import requests
import jsonpath
import json
from requests_oauthlib import OAuth2


def test_OAuth2ClientCredentials():

    token_url = 'http://coop.apps.symfonycasts.com/token'

    test_api_url = 'http://coop.apps.symfonycasts.com/api/685/chickens-feed'

    client_id = 'TestRestApi'
    client_secret = '0132899a7d02713e669bc9875ea9da70'

    data = {'grant_type': 'client_credentials'}

    access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

    accessToken = jsonpath.jsonpath(access_token_response.json(), 'access_token')

    print("Access Token "+accessToken[0])

    api_call_headers = {'Authorization': 'Bearer ' + accessToken[0]}
    api_call_response = requests.post(test_api_url, headers=api_call_headers, verify=False)

    print(api_call_response.text)






