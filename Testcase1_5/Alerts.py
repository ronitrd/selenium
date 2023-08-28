## Alerts/PopUps

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#
# #opens Alert window
# driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
# time.sleep(5)
#
# alertwindow=driver.switch_to.alert
#
# print(alertwindow.text)
# alertwindow.send_keys("Welcome")
# time.sleep(2)
# #alertwindow.accept() # close alert window by using OK button
# alertwindow.dismiss() # close alert window by using CANCEL button

#------------------------------------------------------------
# Alert2
# driver.get("https://demoqa.com/alerts")
# driver.find_element(By.XPATH,"//button[@id='alertButton']").click()
# time.sleep(3)
# driver.switch_to.alert.accept()

#-----------------------------------------------------------
driver.get("https://mypage.rediff.com/login/dologin")
driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(2)
driver.switch_to.alert.accept()

time.sleep(3)
#------------------------------------------------------------

driver.get("https://trytestingthis.netlify.app/")
driver.find_element(By.XPATH,"//button[@onclick='alertfunction()']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(3)

#---------------------------------------------------------------
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.find_element(By.XPATH,"//a[normalize-space()='Alert with OK']").click()
driver.find_element(By.XPATH,"//button[contains(text(),'click the button to display an')]").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='Alert with OK & Cancel']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='click the button to display a confirm box']").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='Alert with Textbox']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='click the button to demonstrate the prompt box']").click()
time.sleep(2)
textbox = driver.switch_to.alert
textbox.send_keys("Auto")
time.sleep(2)
textbox.accept()

time.sleep(3)
driver.quit()

