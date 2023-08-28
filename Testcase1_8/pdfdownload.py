from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

location=os.getcwd()

from selenium.webdriver.support.select import Select


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("/home/dell/PycharmProjects/selenium/Drivers/chromedriver")
    preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}  # download directory is changed to current directory
    ops = webdriver.ChromeOptions()
    #ops.add_argument("--disable-notifications")
    ops.add_experimental_option("detach", True)     # Chrome stays open even after script has stopped running.
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver


def firefox_setup():
    #from selenium.webdriver.firefox.service import Service
    #serv_obj = Service("/home/dell/PycharmProjects/selenium/Drivers/geckodriver")
    ops=webdriver.FirefoxOptions()

    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")  #mimetype "application/pdf","application/msword"
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList",2) #0-desktop,1-downloads folder,2-Desired location
    ops.set_preference("browser.download.dir",location)
    ops.set_preference("pdfjs.disabled",True) #for pdf
    driver = webdriver.Firefox(options=ops)
    return driver

# Automation Code

#driver = firefox_setup()
driver = chrome_setup()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")

driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()


# when download button is clicked it opens google ad.given below are some attempts to neutralize the ad(did not work)

#driver.execute_script("document.getElementById('ad_element_id').style.display = 'none';")
# driver.switch_to.frame(1)
# button=driver.find_element(By.XPATH,'//*[@id="dismiss-button"]').click()
#driver.find_element(By.CSS_SELECTOR,"div[id=dismiss-button]").click()
# act=ActionChains(driver)
# act.move_to_element(button).click().perform()
#driver.switch_to.default_content()

#----- Google AD is inside shadow DOM.To access Shadow DOM steps given below:
# shadow_host = driver.find_element(By.CSS_SELECTOR,'#page-top')
# shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
# element_within_shadow = shadow_root.querySelector('//*[@id="dismiss-button"]')
# element_within_shadow.click()

time.sleep(10)
#driver.close()
