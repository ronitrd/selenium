import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import mysql.connector

ops = webdriver.ChromeOptions()
ops.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='wzrk-cancel']").click()

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="ron", passwd="paswrd", database="mydb")
    curs = con.cursor()  # create cursor
    curs.execute("select * from caldata")  # Execute query through cursor

    for row in curs:
        # Reading data
        pric = row[0]
        rateofinterest = row[1]
        per1 = row[2]
        per2 = row[3]
        fre = row[4]
        exp_mvalue = row[5]
        # print(pric)
        # passing data to the application
        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pric)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

        perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        perioddrp.select_by_visible_text(per2)

        frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        frequencydrp.select_by_visible_text(fre)
        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()  # Calculate Button

        act_mvalue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        # Validation
        if float(exp_mvalue) == float(act_mvalue):
            print("Test Passed")

        else:
            print("Test Failed")

        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(2)
    con.close()
except:
    print("Connection unsuccessful...")

driver.close()
