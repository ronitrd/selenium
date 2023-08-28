from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://jqueryui.com/datepicker/")
#
# driver.switch_to.frame(0)
#
# # By using send_keys
# # driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/18/2024" + Keys.ENTER)  #mm/dd/yyyy
#
# # By using Logic
year = "2024"
month = "May"
date = "15"
#
# driver.find_element(By.XPATH, "//input[@id='datepicker']").click()  # open datepicker
#
# # for selecting month and year
# while True:
#     mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
#     yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
#
#     if mon == month and yr == year:
#         break
#
#     else:
#         if yr <= year:
#             driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  # next arrow
#         else:
#             driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click() #previous arrow - old date
#
# # Select date(from table)
#
# dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
#
# for ele in dates:
#     if ele.text == date:
#         ele.click()
#         break

#-------------------------------------------------------------------------
# # Another Example - Date Of Birth
#
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
#
# driver.find_element(By.XPATH,"//input[@id='dob']").click()
#
# d_mon = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
#
# d_mon.select_by_visible_text("Apr")
#
# d_yr = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
#
# d_yr.select_by_visible_text("1998")
#
# d_date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
#
# for ele in d_date:
#     if ele.text == "5":
#         ele.click()
#         break
#-------------------------------------------------------------

#Example 3

driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.find_element(By.XPATH,"//input[@id='datepicker1']").click()

while True:
    mth = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yer = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mth == month and yer == year:
        break

    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

dt = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")

for i in dt:
    if i.text == date:
        i.click()
        break

print(driver.find_element(By.XPATH,"//input[@id='datepicker1']").text)

time.sleep(3)
driver.close()
