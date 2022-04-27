from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pandas as pd

import login_config #import credentials


# Chrome settings
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito") #don't want cache

service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service, options= chrome_options)
url = "https://campus.icu.ac.jp/icumap/ehb/SearchCO.aspx"

# Open site (will be sent to SSO login)
driver.get(url)
driver.implicitly_wait(10)

# Login to ICU SSO
driver.find_element(By.CLASS_NAME,"username_input").send_keys(login_config.username)
driver.find_element(By.CLASS_NAME,"password_input").send_keys(login_config.password)
driver.find_element(By.CLASS_NAME,"login_button").click()

