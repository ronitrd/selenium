# #Automation Form

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
time.sleep(2)
driver.find_element(By.NAME, 'firstname').send_keys("Abc")         # First Name
driver.find_element(By.NAME, 'lastname').send_keys("xyz")          # Last Name
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[value=Female]').click()   # Radio button male or female
driver.find_element(By.CSS_SELECTOR, 'input[value="3"]').click()      # No of years experience
time.sleep(2)

# driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[4]/div/form/table/tbody/tr[5]/td[2]/input').send_keys("1/1/2024")
driver.find_element(By.XPATH, "//tbody/tr[5]/td[2]/input[1]").send_keys("01/01/2024")    # Date
time.sleep(1)

# driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[4]/div/form/table/tbody/tr[6]/td[2]/span[2]/input').click()
driver.find_element(By.XPATH, "//input[@value='Automation Tester']").click()    # checkBox
time.sleep(1)

# driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[4]/div/form/table/tbody/tr[8]/td[2]/span[3]/input').click()
driver.find_element(By.XPATH, "//input[@value='Selenium Webdriver']").click()            # checkbox
time.sleep(1)

# # Dropdown --> countries
# # approach 1
# select = Select(driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[4]/div/form/table/tbody/tr[9]/td[2]/select'))
# select.select_by_index(2)

# approach 2
country = Select(driver.find_element(By.XPATH, "//select[@name='continents']"))
country.select_by_visible_text("Europe")
time.sleep(2)

# # select options
# # approach 1
# select2= Select(driver.find_element(By.XPATH,'/html/body/main/div/div/div[2]/div[4]/div/form/table/tbody/tr[10]/td[2]/select'))
# select2.select_by_visible_text('Browser Commands')
# #time.sleep(2)

# approach 2 choose multiple options
act = ActionChains(driver)
command = driver.find_element(By.XPATH, "//option[normalize-space()='Switch Commands']")
act.move_to_element(command).click().key_down(Keys.SHIFT).send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN).key_up(Keys.SHIFT).perform()
time.sleep(2)

# Button (submit)
driver.find_element(By.NAME, 'submit').click()
driver.switch_to.alert.accept()

print("completed!")
time.sleep(5)
driver.quit()