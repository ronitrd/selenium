from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
import time
ops=webdriver.FirefoxOptions()
ops.add_argument("--disable-notifications")
#ops.add_experimental_option("detach",True)          #Chrome stays open even after script has stopped running.
#serv_obj=Service("/home/dell/PycharmProjects/selenium/Drivers/chromedriver")
#serv_obj=Service("/home/dell/PycharmProjects/selenium/Drivers/geckodriver")
#driver=webdriver.Chrome(service=serv_obj,options=ops)
driver = webdriver.Firefox(options=ops)
# driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://whatmylocation.com/")

time.sleep(5)
#driver.close()

