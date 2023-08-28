# open testautomationpractice website and perform operations on Links and Alerts

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//button[normalize-space()='Confirm Box']").click()
time.sleep(3)

alert=driver.switch_to.alert
alert.accept()

time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
Links=driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']/div/a")

for link in Links:
    link.click()
    time.sleep(1)

main_window = driver.current_window_handle
windowIDs=driver.window_handles

for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)
    time.sleep(1)
    if winid != main_window:
        driver.close()

driver.switch_to.window(main_window)
driver.refresh()

driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("python")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
Links1=driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']/div/a")

for link in Links1:
    link.click()
    time.sleep(1)

windowIDs=driver.window_handles

for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)
    time.sleep(1)


driver.quit()
