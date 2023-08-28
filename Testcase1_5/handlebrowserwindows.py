# Handle browser window ,multiple browser window

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://opensource-demo.orangehrmlive.com/")
#
# # w_id=driver.current_window_handle
# # print(w_id)
#
# driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
# w_IDs=driver.window_handles
#
# # #Approach 1 if you have 1 or 2 browser windows
# # parentw_ID=w_IDs[0]
# # childw_ID=w_IDs[1]
# #
# # #print(parentw_ID,childw_ID)
# #
# # driver.switch_to.window(childw_ID)
# # print("Title of child window:",driver.title)
# #
# # driver.switch_to.window(parentw_ID)
# # print("Title of parent window:",driver.title)
#
# #----------------------------------------------------------------------------------
# # #Approach 2 for more than 2 windows
# # for winid in w_IDs:
# #     driver.switch_to.window(winid)
# #     print(driver.title)
#
# time.sleep(3)
#
# ##To close specific browser window we need to have title of that browser window which will be used to close that window.
# for winid in w_IDs:
#     driver.switch_to.window(winid)
#     if driver.title=="OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM":
#         driver.close()
#

#time.sleep(5)
#driver.close()

#OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM

#-------------Another Example-------------------------------------------------------

driver.get("https://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH, "//a[normalize-space()='Open New Tabbed Windows']").click()
driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()

wid = driver.window_handles
time.sleep(2)
parent_w = wid[0]
child_w = wid[1]

driver.switch_to.window(parent_w)
# time.sleep(1)
# driver.switch_to.window(child_w)
# time.sleep(2)
# driver.close()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Open New Seperate Windows']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
time.sleep(2)

wid1 = driver.window_handles
window1 = wid1[0]
window2 = wid1[1]
window3 = wid1[2]
time.sleep(2)

driver.switch_to.window(window1)
time.sleep(2)
driver.switch_to.window(window3)
time.sleep(2)
driver.close()

