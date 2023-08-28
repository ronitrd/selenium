from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

# driver.get('https://www.google.com')
# search = driver.find_element(By.NAME ,'q')
# search.send_keys('amazon')
# time.sleep(5)
# search.clear()
# time.sleep(2)
# search.send_keys('OrangeHRM')
# search.send_keys(Keys.RETURN)
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,2000)","")
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[@href='https://opensource-demo.orangehrmlive.com/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='OrangeHRM']").click()
# #open site https://opensource-demo.orangehrmlive.com/
# time.sleep(2)
driver.get("https://www.youtube.com/watch?v=Mi5c2Mz8s4s")
time.sleep(2)
# search1=driver.find_element(By.XPATH,"//input[@id='search']")
# time.sleep(2)
# search1.click()
# search1.send_keys("Mind relaxing music")
# driver.find_element(By.XPATH,"//button[@id='search-icon-legacy']").click()
# time.sleep(3)
# icon=driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-image/img")
# driver.execute_script("arguments[0].scrollIntoView();",icon)
# icon.click()
# time.sleep(5)
# print("doesnt end")
