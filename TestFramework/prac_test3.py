# classmethods- setUp,tearDown,setupclass,teardownclass,setupmodule,teardownmodule
import unittest
from selenium import webdriver

def setUpModule():  # will be executed before executing any class or any methods present in test class
    print("setUpModule")

def tearDownModule():   #will be executed after completing everything present in python module
    print("tearDownModule")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):        # Execute before all test methods
        print("This is Login test")

    @classmethod
    def tearDown(self):     # execute after all test methods
        print("This is Logout test")

    @classmethod
    def setUpClass(cls):        # Execute Once when class is started
        print("Open Application")

    @classmethod
    def tearDownClass(cls):     # Execute once after the class is completed
        print("Close Application")

    def test_search(self):
        print("This is Search test")

    def test_advancedsearch(self):
        print("This is Advanced Search test")

    def test_prepaidRecharge(self):
        print("This is Prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is Postpaid Recharge test")

if __name__=="__main__":
    unittest.main()