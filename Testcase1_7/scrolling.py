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

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# # 1.Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value)

# # 2.Scroll down page till the element is visible
# flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value=driver.execute_script("return window.pageYOffset;")  #To see the number of pixels it moved
# print("Number of pixels moved:",value)

# 3.Scroll till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")  #To see the number of pixels it moved
print("Number of pixels moved:",value)
time.sleep(2)

#Scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")  #To see the number of pixels it moved
print("Number of pixels moved:",value)


time.sleep(5)
driver.close()