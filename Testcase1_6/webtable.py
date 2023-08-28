from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://testautomationpractice.blogspot.com/")
#
# # 1) Total no of rows and columns
# total_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
#
# total_columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
# print("No of Rows:",total_rows)
# print("No of Columns:",total_columns)
#
# # 2) Read specific row and column data
# data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
# print(data) # master of selenium
#
# # # 3) Read all the rows & columns data
# # print("printing all the rows and columns: ")
# #
# # for r in range(2,total_rows+1):
# #     for c in range(1,total_columns+1):
# #         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
# #         print(data,end='           ')  #to print side by side
# #     print()  #to print row on next line
#
# # 4) Read data based on condition(List books name whose author is mukesh)
# for r in range(2,total_rows+1):
#     author=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
#     if author=="Mukesh":
#         Book=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
#         price=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
#         print(Book,"        ",author,"    ",price)

#--------------------------------------------------------------------------------------------------
#  #Example 2

driver.get("https://demoqa.com/webtables")
driver.execute_script("window.scrollBy(0,400)","")
select = Select(driver.find_element(By.XPATH,"//select[@aria-label='rows per page']"))
select.select_by_index(0)

columns = len(driver.find_elements(By.XPATH,"//div[@class='rt-tr']/child::div"))
print(columns)
rows = len(driver.find_elements(By.XPATH,"//div[@class='rt-tbody']/child::div"))
print(rows)

for r in range(1,rows+1):
    for c in range(1,columns+1):
        data = driver.find_element(By.XPATH,"//body/div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']/div[@class='col-12 mt-4 col-md-6']/div[@class='web-tables-wrapper']/div[@class='ReactTable -striped -highlight']/div[@role='grid']/div[@class='rt-tbody']/div["+str(r)+"]/div[1]/child::div["+str(c)+"]").text
        print(data,end="     ")
    print()

# Add new entry to table
driver.find_element(By.XPATH,"//button[@id='addNewRecordButton']").click()
driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("Mark")       #First Name
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("Hail")       #Last Name
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys("MarkHail@op.cm")       #Email
driver.find_element(By.XPATH,"//input[@id='age']").send_keys("35")       #Age
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='salary']").send_keys("35000")       #Salary
driver.find_element(By.XPATH,"//input[@id='department']").send_keys("Administration")    #Department
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='submit']").click()

for r in range(1,rows+1):
    for c in range(1,columns+1):
        data = driver.find_element(By.XPATH,"//body/div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']/div[@class='col-12 mt-4 col-md-6']/div[@class='web-tables-wrapper']/div[@class='ReactTable -striped -highlight']/div[@role='grid']/div[@class='rt-tbody']/div["+str(r)+"]/div[1]/child::div["+str(c)+"]").text
        print(data,end="     ")
    print()

time.sleep(3)
driver.quit()


