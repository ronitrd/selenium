##We need to install 'requests' package through Setting->ProjectInterpreter-> + -> requests

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://www.deadlinkcity.com/")

allLinks = driver.find_elements(By.TAG_NAME, 'a')
count = 0

for link in allLinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " is broken link")
        count += 1
    else:
        print(url, " is valid link")
print("Total no of broken links:", count)

driver.quit()
