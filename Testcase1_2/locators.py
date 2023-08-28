from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get('https://www.facebook.com/')

# NAME
# driver.find_element(By.NAME, 'email').send_keys("abc@gmail.com")
# driver.find_element(By.NAME, 'pass').send_keys("xyz")

# ID
# driver.find_element(By.ID, 'email').send_keys("abc@gmail.com")
# driver.find_element(By.ID, 'pass').send_keys("xyz")

# Locators CSS_SELECTOR

driver.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, 'input.inputtext[data-testid=royal_pass]').send_keys("xyz")
time.sleep(5)
driver.close()


