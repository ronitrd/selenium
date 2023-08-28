
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countrieslist = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countrieslist))

for country in countrieslist:
    if country.text=="India":
        country.click()
        break



time.sleep(5)
driver.close()