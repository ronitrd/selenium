import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        #ops=webdriver.ChromeOptions()
        #ops.add_argument("--headless")
        self.driver=webdriver.Chrome()#options=ops)
        self.driver.maximize_window()

    def test_login(self):
        driver=self.driver
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123" + Keys.RETURN)
        print(driver.title)
        self.assertIn("OrangeHRM",driver.title)

    def test_automation(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://testautomationpractice.blogspot.com/")

        driver.find_element(By.XPATH, "//button[normalize-space()='Confirm Box']").click()
        time.sleep(3)

        alert = driver.switch_to.alert
        alert.accept()

        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        Links = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']/div/a")
        for link in Links:
            link.click()
            time.sleep(1)
        windowIDs = driver.window_handles
        for winid in windowIDs:
            driver.switch_to.window(winid)
            print(driver.title)
            time.sleep(1)

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()