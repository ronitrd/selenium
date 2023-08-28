from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.automationpractice.pl/index.php")

# #Absolute Xpath
# # (search element)
# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

# # Relative XPath
# # (search element)
# driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()

# #OR
driver.find_element(By.XPATH,"//input[@id='search_query_top' or @name='search_query']").send_keys("T-shirts")
# #AND
driver.find_element(By.XPATH,"//button[@type='submit' and @name='submit_search']").click()
time.sleep(3)

