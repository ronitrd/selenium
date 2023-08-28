import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        print("Title of page is:",self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.bing.com/")
        print("Title of page is :",self.driver.title)
        self.driver.close()

if __name__=="__main__":
    unittest.main()