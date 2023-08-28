from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

# Capture Cookies from the browser
cookies=driver.get_cookies()
print("size of cookies:",len(cookies))

# print details of all cookies
for c in cookies:
    #print(c)
    print(c.get('name'),":",c.get('value'))

# Add new cookie to the browser
driver.add_cookie({"name":"MyCookie", "value":"123456"})
cookies=driver.get_cookies()
print("size of cookies after adding one more:",len(cookies))

# Delete specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies=driver.get_cookies()
print("size of cookies after deleting one :",len(cookies))

#Delete all the cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("size of cookies after deleting all :",len(cookies))


time.sleep(3)
driver.close()