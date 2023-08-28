import unittest
from package1.TC_LoginTest import LoginTest
from package1.TC_signupTest import SignUpTest

from package2.TC_PaymentTest import PaymentTest
from package2.TC_PaymentReturnsTest import PaymentReturnsTest

# Get All tests from classes
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#creating test suites
sanityTestSuite = unittest.TestSuite([tc1,tc2])
functionalTestSuite = unittest.TestSuite([tc3,tc4])
masterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])

#unittest.TextTestRunner().run(sanityTestSuite)
#unittest.TextTestRunner().run(functionalTestSuite)
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)