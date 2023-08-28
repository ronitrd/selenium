from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)

# Right-Click
act.context_click(button).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
time.sleep(2)
driver.switch_to.alert.accept()

time.sleep(5)
driver.close()

