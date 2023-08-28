import unittest

class LoginTest(unittest.TestCase):

    def test_loginbyemail(self):
        print("This is login by email test")
        self.assertTrue(True)

    def test_loginbyfacebook(self):
        print("This is login by facebook test")
        self.assertTrue(True)

    def test_loginbytwitter(self):
        print("This is login by twitter test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()