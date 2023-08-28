from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait  # (For explicit_wait)
from selenium.webdriver.support import expected_conditions as EC

# #####  Implicit-wait()   -----------------
# driver=webdriver.Firefox()
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.get("https://www.google.com/")
# search=driver.find_element(By.NAME,'q')
#
# search.send_keys("Selenium")
# search.submit()
#
# driver.find_element(By.XPATH,'//h3[text()="Selenium"]').click()
#
# driver.quit()

########    Explicit-wait()  -------------------------

driver = webdriver.Chrome()

driver.maximize_window()
# mywait=WebDriverWait(driver,10) #explicit wait declaration #Basic syntax
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         Exception]
                       )

driver.get("https://www.google.com/")
search = driver.find_element(By.NAME, 'q')
#
# search.send_keys("Selenium")
# search.submit()
# # time.sleep(3)
# searchlink = mywait.until(EC.presence_of_element_located((By.XPATH, '//h3[text()="Selenium"]')))
#
# searchlink.click()
# driver.find_element(By.XPATH,'//h3[text()="Selenium"]').click()
search.send_keys("github")
search.submit()

search_link = mywait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='https://github.com/']")))
search_link.click()
driver.quit()
