from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://opensource-demo.orangehrmlive.com/")
#
# # Login
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
# time.sleep(3)
#
# # Admin --> UserManagement --> users
# admin=driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]")
# user_management=driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
# user=driver.find_element(By.XPATH,"//ul[@role='menu']//li")
#
#
# # Mouse Hover
# act=ActionChains(driver)
#
# act.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform()

driver.get("https://jqueryui.com/datepicker/")

support=driver.find_element(By.XPATH,"//a[@href='https://jquery.org/support/'][normalize-space()='Support']")
learn=driver.find_element(By.XPATH,"//li[@class='dropdown']//ul//li//a[normalize-space()='Learning Center']")
forum=driver.find_element(By.XPATH,"//a[normalize-space()='Forums']")

act=ActionChains(driver)
act.move_to_element(support).move_to_element(learn).move_to_element(forum).click().perform()

time.sleep(5)