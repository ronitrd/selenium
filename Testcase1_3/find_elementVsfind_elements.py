from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

# find_element() vs find_elements()
driver.get("https://demo.nopcommerce.com/")

####### find_element() -- returns single web-element
#A)Locator matching with Single web element
# element=driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
# element.send_keys("Apple Mac")

#B)Locator matching with Multiple web elements
# element1=driver.find_element(By.XPATH,'//div[@class="footer"]//a')
# print(element.text)

#C)Element not available then throw NoSuchElementException
# element2=driver.find_element(By.LINK_TEXT, 'Log')
# element2.click()

############# find_elements() -- returns multiple web-elements
#A)Locator matching with Single web element
# elements=driver.find_elements(By.XPATH,'//*[@id="small-searchterms"]')
# print(len(elements))
# elements[0].send_keys("Apple Mac")

#B)Locator matching with Multiple web elements
# elements1=driver.find_elements(By.XPATH,'//div[@class="footer"]//a')
# print(len(elements1)) #23
# #print(elements1[0].text)
# for ele in elements1:
#     print(ele.text)

#C)Element not available then will not return any Exception
# elements2=driver.find_elements(By.LINK_TEXT, 'Log')
# print("elements returned: ",len(elements2))
