from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

# Login
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(3)

# Admin --> UserManagement --> users
driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()

# Total No of Rows
total_column=len(driver.find_elements(By.XPATH,"//div[@class='oxd-table-header']//div[@role='row']/div"))
print("No of Columns: ",total_column)

total_row=len(driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div"))
print("No of Rows: ",total_row)
count1=0
count2=0
count3=0
for r in range(1,total_row+1):
    status=driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/child::div/div[5]").text
    if status=="Disabled":
        #name=driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/child::div/div[4]").text
        count1+=1
        #print(name,"    ",status)
    else:
        #name1 = driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div[" + str(r) + "]/child::div/div[4]").text
        count2+=1
        #print(name1,"    ",status)
print("Total Number of users:",total_row)
print("Total Number of Enabled users: ",count2)
#print("Total Number of Disabled users: ",count1)
#       #OR
print("Total Number of Disabled users: ",(total_row-count2))

#-----------------------------------------------------------------------------------------------------------------
# to print user-roles and usernames from table
for r in range(1,total_row+1):
    user_role=driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/child::div/div[3]").text
    if user_role=="ESS":
        usrname=driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/child::div/div[2]").text
        print(usrname,"    ",user_role)
        count3+=1
print("Count of ESS:",count3)
time.sleep(3)
driver.close()