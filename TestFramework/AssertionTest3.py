# assertIsNone , assertIsNotNone

import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def testName(self):
        driver=webdriver.Chrome()
        #driver = None

        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)


if __name__=="__main__":
    unittest.main()