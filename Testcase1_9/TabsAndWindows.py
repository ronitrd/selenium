from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://demo.nopcommerce.com/")
#
# regilink=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(regilink)
#
# driver.switch_to.window(driver.window_handles[1])
#------------------------------------------------------
# #open a new tab and switches to new tab
# driver.get("https://demo.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://demo.nopcommerce.com/")

#open a new Browser window and switches to new window
driver.get("https://demo.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://demo.nopcommerce.com/")

time.sleep(5)
driver.close()