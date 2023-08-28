from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

browser=webdriver.Chrome()

browser.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(5)
browser.find_element(By.NAME,'username').send_keys('Admin')
browser.find_element(By.NAME, 'password').send_keys('admin123')
browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(3)
title=browser.title
exp_title="OrangeHRM"

if title==exp_title:
    print("Login Success")
else:
    print("Login failed")
# links=browser.find_elements(By.TAG_NAME, 'a')
# print(len(links))
# browser.find_element(By.LINK_TEXT,'Time').click()
# time.sleep(2)
# browser.back()
# time.sleep(3)
browser.find_element(By.LINK_TEXT, 'Admin').click()
time.sleep(3)

browser.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Admin4")
time.sleep(2)
select = Select(browser.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div'))
select.select_by_index(1)
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Type for hints..."]').send_keys("john")
time.sleep(2)
select2 = Select(browser.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div'))
select2.select_by_visible_text('Enabled')
time.sleep(2)
browser.find_element(By.CSS_SELECTOR,'button.oxd-button').click()
#browser.back()
# browser.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span').click()
# time.sleep(2)
# browser.find_element(By.PARTIAL_LINK_TEXT, 'Log').click()
time.sleep(4)
#print("Logout Success")
browser.close()
