from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def headless_chrome():
    ops=webdriver.ChromeOptions()
    #ops.headless=True  #OR
    ops.add_argument('--headless')  # automation runs in backend
    driver=webdriver.Chrome(options=ops)
    return driver

def headless_firefox():
    ops=webdriver.FirefoxOptions()
    #ops.headless=True  #OR
    ops.add_argument('--headless')  # automation runs in backend
    driver=webdriver.Firefox(options=ops)
    return driver


driver=headless_chrome()
#driver=headless_firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()