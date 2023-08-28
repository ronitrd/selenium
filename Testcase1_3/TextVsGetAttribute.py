from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/login")

emailbox=driver.find_element(By.XPATH,'//*[@id="Email"]')

emailbox.clear()            # clear the text which is already written
emailbox.send_keys("Abc@gmail.com")

print("result of text:",emailbox.text)
print("result of get_attribute():",emailbox.get_attribute('value'))

button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("result of text:",button.text)
print("result of get attribute('value'):",button.get_attribute('value'))
print("result of get attribute('type'):",button.get_attribute('type'))