from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://www.automationtestinginsider.com/2019/08/textarea-textarea-element-defines-multi.html")
#
#
# car_ele=driver.find_element(By.XPATH, "//select[@name='cars']")
# car=Select(car_ele)
        # OR
#car=Select(driver.find_element(By.XPATH, "//select[@name='cars']"))


##select option from the dropdown

# car.select_by_visible_text("Audi")
# car.select_by_value("fiat")
# car.select_by_index(2)

# Capture all the options and print them
# alloptions=car.options
# print("total no of options:",len(alloptions))
#
# for opt in alloptions:
#     print(opt.text)

# Select option from dropdown without using built-in-function
# for opt in alloptions:
#     if opt.text=="Fiat":
#         opt.click()
#         break

# without using select class
# alloptions=driver.find_elements(By.XPATH,"//*[@name='cars']/option")
# driver.quit()

#-------------------------------------------------------------------------------------
# 2nd dropdown assignment

driver.get("https://testautomationpractice.blogspot.com/")

country=Select(driver.find_element(By.XPATH,"//select[@id='country']"))
alloptions=country.options
print("Total No.of options:",len(alloptions))

for opt in alloptions:
    print(opt.text)

for opt in alloptions:
    if opt.text=="India":
        opt.click()
        break

time.sleep(4)
driver.quit()