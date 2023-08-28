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

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

act=ActionChains(driver)

source_ele=driver.find_element(By.ID,"box6")    #Rome
target_ele=driver.find_element(By.ID,"box106")  #Italy
act.drag_and_drop(source_ele,target_ele).perform()
time.sleep(1)

seoul_ele=driver.find_element(By.ID,"box5")      #seoul
s_korea_ele=driver.find_element(By.ID,"box105")  #south korea
act.drag_and_drop(seoul_ele,s_korea_ele).perform()
time.sleep(1)

madrid_ele=driver.find_element(By.ID,"box7")    #madrid
spain_ele=driver.find_element(By.ID,"box107")   #spain
act.drag_and_drop(madrid_ele,spain_ele).perform()
time.sleep(1)

stockholm_ele=driver.find_element(By.ID,"box2")    #stockholm
sweden_ele=driver.find_element(By.ID,"box102")     #sweden
act.drag_and_drop(stockholm_ele,sweden_ele).perform()
time.sleep(1)

wshngtn_ele=driver.find_element(By.ID,"box3")    #washington
us_ele=driver.find_element(By.ID,"box103")       #US
act.drag_and_drop(wshngtn_ele,us_ele).perform()
time.sleep(1)

copen_ele=driver.find_element(By.ID,"box4")    #copenhagen
denmark_ele=driver.find_element(By.ID,"box104")  #denmark
act.drag_and_drop(copen_ele,denmark_ele).perform()
time.sleep(1)

oslo_ele=driver.find_element(By.ID,"box1")    #oslo
norway_ele=driver.find_element(By.ID,"box101")  #norway
act.drag_and_drop(oslo_ele,norway_ele).perform()

time.sleep(5)
driver.close()