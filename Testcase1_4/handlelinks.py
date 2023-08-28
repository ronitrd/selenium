from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()

#driver.get("https://demo.nopcommerce.com/")

#click on link
# driver.find_element(By.LINK_TEXT,'Digital downloads').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,'Digital').click()

#Find number of links in a page
# links=driver.find_elements(By.TAG_NAME, 'a')
# print("Total no of links:",len(links))
#
# for link in links:
#     print(link.text)

###### Broken Links
driver.get("http://www.deadlinkcity.com/")


driver.quit()