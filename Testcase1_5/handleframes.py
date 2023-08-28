# Handle frames,inner iframes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.maximize_window()

# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#
# driver.switch_to.frame("packageListFrame")
# driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
# driver.switch_to.default_content()  #go back to main page
#
# driver.switch_to.frame("packageFrame")
# driver.find_element(By.LINK_TEXT, "WebDriver").click()
# driver.switch_to.default_content()  #go back to main page
#
# driver.switch_to.frame("classFrame")
# driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()

#-------------------------------------------------------------------
# Assign 2
##########        Inner Iframes   -----------------
# driver.get("https://demo.automationtesting.in/Frames.html")
# driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
#
# outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
# driver.switch_to.frame(outerframe)
#
# innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
# driver.switch_to.frame(innerframe)
#
# driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")
#
# driver.switch_to.parent_frame() #directly switch to parent frame(outerframe)


#=-------------------------------------------------------------------------------------------
# # Assign 3
#
# driver.get("https://the-internet.herokuapp.com/frames")
#
# driver.find_element(By.LINK_TEXT,"Nested Frames").click()
# driver.switch_to.frame("frame-top")
# print("The 1st Frame is: TOP")
# driver.switch_to.frame("frame-left")
# print("The Frame is: ",driver.find_element(By.XPATH,"//body").text)
# driver.switch_to.default_content()
#
#
# driver.switch_to.frame("frame-top")
# driver.switch_to.frame("frame-middle")
# print("The Frame is: ",driver.find_element(By.XPATH,"//body").text)
# driver.switch_to.default_content()
#
# driver.switch_to.frame("frame-top")
# driver.switch_to.frame("frame-right")
# print("The Frame is: ",driver.find_element(By.XPATH,"//body").text)
# driver.switch_to.default_content()
#
# driver.switch_to.frame("frame-bottom")
# print("The 2nd Frame is: ",driver.find_element(By.XPATH,"//body").text)

#-------------------------------------------------------------------------
# Assign 4

driver.get("https://demoqa.com/frames")
driver.switch_to.frame("frame1")
print("The Frame contains: ",driver.find_element(By.XPATH,"//h1[@id='sampleHeading']").text)
driver.switch_to.default_content()

driver.switch_to.frame("frame2")
print("Frame 2 contains: ",driver.find_element(By.XPATH,"//h1[@id='sampleHeading']").text + " Too")

driver.switch_to.default_content()
time.sleep(2)
#### Nested Frames

nest = driver.find_element(By.XPATH,"//div[@class='element-list collapse show']//li[@id='item-3']")
driver.execute_script("arguments[0].scrollIntoView();",nest)
nest.click()

driver.switch_to.frame("frame1")
print("This Frame is: ",driver.find_element(By.XPATH,"//body").text)
time.sleep(2)

fram3 = driver.find_element(By.XPATH,"/html/body/iframe")
driver.switch_to.frame(fram3)
print("This Frame is: ",driver.find_element(By.XPATH,"//body").text)

time.sleep(3)
driver.close()

