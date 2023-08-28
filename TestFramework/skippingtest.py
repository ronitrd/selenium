import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest  #decorator
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping test method bcoz its not ready yet")
    def test_advancedsearch(self):
        print("This is advanced search method")

    @unittest.skipIf(1==1,"one equals to one")
    def test_prepaidrecharge(self):
        print("This is Pre-paid recharge")

    def test_postpaidRecharge(self):
        print("This is Post-paid recharge")

    def test_loginbygmail(self):
        print("This is Login by Email")

    def test_loginbytwitter(self):
        print("This is login by twitter")

if __name__=="__main__":
    unittest.main()