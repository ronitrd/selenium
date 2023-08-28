from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time

#serv=Service("/home/dell/PycharmProjects/selenium/Drivers/geckodriver")
driver=webdriver.Firefox()
#driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)
driver.find_element(By.NAME,'username').send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME, 'password').send_keys("admin123" + Keys.ENTER)
time.sleep(3)
ac_title=driver.title
exp_title="OrangeHRM"

if ac_title==exp_title:
    print("login test successful!")
else:
    print("test failed!")

# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
# print("page Title: " + driver.title)
# time.sleep(3)
# driver.back()
# print("page Title: " + driver.title)
time.sleep(15)
driver.close()