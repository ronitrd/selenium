# assertTrue, assertFalse

import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def testName(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/")

        titleofwebpage=driver.title

        #self.assertTrue(titleofwebpage == "Google")
        self.assertFalse(titleofwebpage == "Google123")
if __name__=="__main__":
    unittest.main()