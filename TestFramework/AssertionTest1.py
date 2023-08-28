import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def test_Name(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/")
        titleofWebpage=driver.title

        #asserEqual
        self.assertEqual("Google",titleofWebpage,"webpage title is not same")
        #self.assertNotEqual("Google123",titleofWebpage,"webpage title is equal")
    if __name__=="__main__":
        unittest.main()