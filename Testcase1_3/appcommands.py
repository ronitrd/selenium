from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

#Application commands
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)
print("Title of webpage: ",driver.title)
print("URL of current webpage: ",driver.current_url)
print("Source code of webpage: ",driver.page_source)
time.sleep(2)
#driver.close()
##--------------------------------------------------

#Conditional commands
driver.get("https://demo.nopcommerce.com/register")
#is_displayed()  is_enabled()

searchbox=driver.find_element(By.XPATH, "//*[@id='small-searchterms']")
print("Display status: ",searchbox.is_displayed()) #True
print("Enabled status: ",searchbox.is_enabled())   #True

#is_selected()
rd_male=driver.find_element(By.XPATH, '//*[@id="gender-male"]')
rd_female=driver.find_element(By.XPATH, '//*[@id="gender-female"]')

print(rd_male.is_selected())     #False
print(rd_female.is_selected())   #False

rd_male.click()
print("After selecting male radio button:")
print(rd_male.is_selected())     #True
print(rd_female.is_selected())   #False
time.sleep(1)
rd_female.click()
print("After selecting female radio button:")
print(rd_male.is_selected())     #False
print(rd_female.is_selected())   #True
#driver.close()
#-------------------------------------------------

##Browser Commands
# driver.get("https://opensource-demo.orangehrmlive.com/")
# time.sleep(2)
#
# driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()
# time.sleep(2)
# driver.close()
# #driver.quit()
##---------------------------------------------------

##Navigational commands
# driver.get("https://www.snapdeal.com/")
# driver.get("https://www.amazon.in/")
#
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(1)
# driver.quit()

##----------------------------------------
# find_element() vs find_elements()
driver.get("https://demo.nopcommerce.com/")

###### find_element() -- returns single web-element
#A)Locator matching with Single web element
element=driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
element.send_keys("Apple Mac")
time.sleep(1)
element.clear()

#B)Locator matching with Multiple web elements
element1=driver.find_element(By.XPATH,'//div[@class="footer"]//a')
print(element1.text)
time.sleep(2)

#C)Element not available then throw NoSuchElementException
element2=driver.find_element(By.PARTIAL_LINK_TEXT, 'Log')
element2.click()
time.sleep(2)

############ find_elements() -- returns multiple web-elements
#A)Locator matching with Single web element
elements=driver.find_elements(By.XPATH,'//*[@id="small-searchterms"]')
print(len(elements))
elements[0].send_keys("Apple Mac")
time.sleep(1)

#B)Locator matching with Multiple web elements
elements1=driver.find_elements(By.XPATH,'//div[@class="footer"]//a')
print(len(elements1)) #23
#print(elements1[0].text)
for ele in elements1:
    print(ele.text)
time.sleep(1)

#C)Element not available then will not return any Exception
elements2=driver.find_elements(By.LINK_TEXT, 'Log')
print("elements returned: ",len(elements2))


time.sleep(5)