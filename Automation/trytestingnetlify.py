from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")
act=ActionChains(driver)
time.sleep(2)
driver.find_element(By.NAME, 'fname').send_keys("John")
time.sleep(1)
driver.find_element(By.NAME, 'lname').send_keys("Doe")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input[value=male]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'input[value=female]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'input[value=other]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'option[value="option 2"]').click()
time.sleep(1)
multi_sel=driver.find_element(By.XPATH, '//*[@id="owc"]/option[2]')
act.move_to_element(multi_sel).click().key_down(Keys.SHIFT).send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN).key_up(Keys.SHIFT).perform()
time.sleep(1)
#driver.find_element(By.CSS_SELECTOR, 'input[name=option2]').click()
#driver.find_element(By.XPATH,"//input[@type='checkbox' and  contains(@id,'option')]").click()
driver.find_element(By.XPATH,"//input[@name='option1']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='option2']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='option3']").click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/fieldset/input[9]').send_keys("Vanilla")
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="day"]').send_keys("01012024")
time.sleep(1)
elem=driver.find_element(By.CSS_SELECTOR, 'input[name=a]')
for _ in range(10):
    elem.send_keys(Keys.ARROW_RIGHT)
    #time.sleep(1)

driver.find_element(By.CSS_SELECTOR, 'input[id=quantity]').send_keys(Keys.ARROW_UP + Keys.ARROW_UP)
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/fieldset/textarea').send_keys("Also it was playing with Ball.")
time.sleep(1)

driver.find_element(By.XPATH,"//div[@class='pop-up-alert']/button").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
tip=driver.find_element(By.XPATH,"//div[@class='tooltip']")
act.move_to_element(tip).perform()
time.sleep(2)
rows=len(driver.find_elements(By.XPATH,"//tbody/tr"))
cols=len(driver.find_elements(By.XPATH,"//tbody/tr[1]/th"))

for r in range(2,rows+1):
     for c in range(1,cols+1):
         data = driver.find_element(By.XPATH, "//tbody//tr["+str(r)+"]/td["+str(c)+"]").text
         print(data,end='           ')  #to print side by side
     print()  #to print row on next line



# src_ele=driver.find_element(By.ID,"drag1")
# tgt_ele=driver.find_element(By.XPATH,"//div[@id='div1']")
# act.drag_and_drop(src_ele,tgt_ele).perform()
# time.sleep(5)


driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
print("Form submitted.")
# a=ActionChains(driver)
# a.move_to_element(72).perform()
time.sleep(5)