from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
ops.add_experimental_option("detach",True)          #Chrome stays open even after script has stopped running.
serv_obj=Service("/home/dell/PycharmProjects/selenium/Drivers/chromedriver")
driver=webdriver.Chrome(service=serv_obj,options=ops)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

driver.switch_to.frame("iframeResult")

field1=driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("Welcome")

d_click=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act=ActionChains(driver)
act.double_click(d_click).perform()
time.sleep(3)
#-----------------------------------------------------------------------------------
# example 2
driver.execute_script("window.open('about:blank','secondtab');")

# It is switching to second tab now
driver.switch_to.window("secondtab")
driver.get("https://testautomationpractice.blogspot.com/")

button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act=ActionChains(driver)
act.double_click(button).perform()
time.sleep(3)
wid=driver.window_handles
driver.switch_to.window(wid[0])

#======-----------------------==-====================--------------------=================----------
# example 3
driver.switch_to.new_window()
driver.get("https://demoqa.com/buttons")
button1 = driver.find_element(By.XPATH,"//button[@id='doubleClickBtn']")
button2 = driver.find_element(By.XPATH,"//button[@id='rightClickBtn']")
button3 = driver.find_element(By.XPATH,"//div[@class='col-12 mt-4 col-md-6']//div//div[3]/button")
act.double_click(button1).perform()
time.sleep(1)
act.context_click(button2).perform()
time.sleep(1)
act.click(button3).perform()

time.sleep(5)
driver.quit()