from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://www.foundit.in/")
#
# driver.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn secondaryBtn']").click()
# driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("/home/dell/Downloads/file-sample_150kB.pdf")
#

#------------------------------------------------------------------------------------------------
# Example 2
driver.get("https://opensource-demo.orangehrmlive.com/")

# Login
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()         # click PIM
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='oxd-topbar-body']//li[3]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='file']").send_keys("/home/dell/Downloads/3304767.jpg")


time.sleep(5)
driver.close()