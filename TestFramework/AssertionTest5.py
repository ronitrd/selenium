# assertGreater , assertGreaterEqual, assertLess, assertLessEqual

import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def testName(self):

        #self.assertGreater(100,10) #passed
        #self.assertGreaterEqual(100,100) #passed

        #self.assertLess(10,100) #passed
        self.assertLessEqual(90,100) #passed


if __name__=="__main__":
    unittest.main()