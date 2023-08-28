from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://trytestingthis.netlify.app/")

#1) Select specific checkbox
#driver.find_element(By.XPATH,"//*[@id='moption']").click()

#2) Select all the checkboxes ---- when you have multiple elements use "driver.find_elements()"
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and  contains(@id,'option')]")
print(len(checkboxes))

#Approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

#Approach 2
for checkbox in checkboxes:
    checkbox.click()
time.sleep(3)
#3) Select multiple checkboxes with choice
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('name')
#     if weekname=='option1' or weekname=='option3':
#         checkbox.click()

#4) Select last 2 checkboxes
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

#5) Select first 2 checkboxes:
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

#6) Clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

#//input[@type='checkbox' and  contains(@id,'option')]
time.sleep(3)