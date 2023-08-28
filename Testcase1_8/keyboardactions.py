from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait  # (For explicit_wait)
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.select import Select

# ops=webdriver.ChromeOptions()
# ops.add_argument("--disable-notifications")
# ops.add_experimental_option("detach",True)          #Chrome stays open even after script has stopped running.
# serv_obj=Service("/home/dell/PycharmProjects/selenium/Drivers/chromedriver")
driver = webdriver.Chrome()  # service=serv_obj,options=ops)
driver.implicitly_wait(10)
driver.maximize_window()

mywait = WebDriverWait(driver, 10, poll_frequency=2)

driver.get("https://text-compare.com/")


input1 = mywait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='inputText1']")))
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")
#driver.execute_script("window.stop();")     # to stop loading of page
#driver.set_page_load_timeout(10)           # actually to stop loading page but closes browser

input1.send_keys("Welcome To Selenium")
time.sleep(3)
act = ActionChains(driver)

# input1 ---> Ctrl+A - select the text
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()
#######   OR ----------
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(3)
# input1 ---> Ctrl+C copy text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(3)
# press Tab key to navigate to input2 (second)
act.send_keys(Keys.TAB).perform()
time.sleep(3)
# input2 ---> Ctrl+V paste the text
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)
driver.close()
