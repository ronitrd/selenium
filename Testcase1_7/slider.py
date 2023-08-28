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

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_slider=driver.find_element(By.XPATH,"//body//div//span[1]")
max_slider=driver.find_element(By.XPATH,"//body//div//span[2]")

print("Original Location of Sliders:")
print(min_slider.location) #{'x': 59, 'y': 250}
print(max_slider.location) #{'x': 516, 'y': 250}

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-36,0).perform()

print("Location of Sliders after moving:")
print(min_slider.location) #{'x': 160, 'y': 250}
print(max_slider.location) #{'x': 479, 'y': 250}
#------------------------------------------------------------------------
#---------------Example 2-----------------------------------
driver.get("https://demo.automationtesting.in/Slider.html")
time.sleep(2)
slider = driver.find_element(By.XPATH,"//div[@id='slider']/a")
print()
print("Original position",slider.location)

act.drag_and_drop_by_offset(slider,203,0).perform()

print("After Move",slider.location)

time.sleep(5)
driver.close()
