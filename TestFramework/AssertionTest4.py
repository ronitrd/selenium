# assertIn , assertNotIn

import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def testName(self):
        list={"python","selenium","java"}

        #self.assertIn("python",list) #passed
        #self.assertIn("ruby",list) #failed

        self.assertNotIn("ruby",list) #passed
        #self.assertNotIn("python",list) #failed


if __name__=="__main__":
    unittest.main()