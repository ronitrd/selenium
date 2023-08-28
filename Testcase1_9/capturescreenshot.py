
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

#driver.save_screenshot("//home//dell//PycharmProjects//selenium//Testcase1_9//scrnshot1.png")
driver.save_screenshot(os.getcwd() + "//scrnshot1.png")

# # Few other methods to capture Screenshot
# driver.get_screenshot_as_file()
# driver.get_screenshot_as_png()    #saves in Binary format
# driver.get_screenshot_as_base64() #saves in Binary format

time.sleep(3)
driver.close()