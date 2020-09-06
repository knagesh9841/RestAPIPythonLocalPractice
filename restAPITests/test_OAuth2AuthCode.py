import json

import requests
import jsonpath
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.common.by import By
from time import sleep


def test_OAuth2AuthorizationCode():

    authorize_url = "http://coop.apps.symfonycasts.com/authorize?client_id=TestRestApi&client_secret=0132899a7d02713e669bc9875ea9da70&scope =chickens-feed&redirect_uri=http://coop.apps.symfonycasts.com/api&response_type=code"
    token_url = "http://coop.apps.symfonycasts.com/token"

    callback_uri = "http://coop.apps.symfonycasts.com/api"

    client_id = 'TestRestApi'
    client_secret = '0132899a7d02713e669bc9875ea9da70'

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("prefs", {"download.default_directory": "E:\Export"})

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-notifications')

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    driver.get(authorize_url)

    driver.implicitly_wait(5)
    driver.maximize_window()

    wait = WebDriverWait(driver, 30)
    wait.until(expected_conditions.visibility_of_element_located((By.NAME, "_username")))

    userName = driver.find_element_by_name("_username")

    password = driver.find_element_by_name("_password")

    loginBtn = driver.find_element_by_xpath("//button[text()='Login!']")

    userName.send_keys("knagesh143s@gmail.com")
    password.send_keys("OAuth2")

    loginBtn.click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Yes, I Authorize This Request')]")))

    btn = driver.find_element_by_xpath("//a[contains(text(),'Yes, I Authorize This Request')]")

    btn.click();

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//span[text()='The Coop']")))

    codeURL = driver.current_url

    print("CodeUrl:- "+codeURL)

    code = codeURL

    code = code.split("=")
    code = code[1]

    code = code[0:(len(code) - 1)]

    print("Code:- " + code)

    driver.close()

    data = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': callback_uri}

    access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False,
                                          auth=(client_id, client_secret))

    # we can now use the access_token as much as we want to access protected resources.

    tokens = json.loads(access_token_response.text)
    access_token = tokens['access_token']
    print("access token: " + access_token)

    test_api_url = "http://coop.apps.symfonycasts.com/api/685/chickens-feed"

    api_call_headers = {'Authorization': 'Bearer ' + access_token}
    api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)

    print(api_call_response.status_code)
