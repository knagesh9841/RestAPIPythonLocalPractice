import requests


def test_Session():
    req = requests.Session()
    cookies = dict(test='test123')
    getdata = req.get('https://httpbin.org/cookies', cookies=cookies)
    print(getdata.text)

