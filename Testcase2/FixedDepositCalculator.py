import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Testcase2 import XLUtils

ops=webdriver.ChromeOptions()
ops.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")

file = "/home/dell/Downloads/caldata.xlsm"
rows = XLUtils.getRowCount(file, "Sheet1")
driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']").click()
print(rows)

for r in range(2, rows + 1): # it should be range(2, rows + 1) but rows count is shown to be 7 instead of 6
    # Reading data from excel sheet
    pric = XLUtils.readData(file, "Sheet1", r, 1)
    rateofinterest = XLUtils.readData(file, "Sheet1", r, 2)
    per1 = XLUtils.readData(file, "Sheet1", r, 3)
    per2 = XLUtils.readData(file, "Sheet1", r, 4)
    fre = XLUtils.readData(file, "Sheet1", r, 5)
    exp_mvalue = XLUtils.readData(file, "Sheet1", r, 6)

    #print(pric)
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
        XLUtils.writeData(file, "Sheet1", r, 8, "Passed")
        XLUtils.fillGreenColor(file, "Sheet1", r, 8)
    else:
        print("Test Failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)

driver.close()
