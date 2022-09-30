import unittest
from models.Customer import Customer
from models.Utility import Utility
from controllers.CustomerController import CustomerController


class TestCustomerSignIn(unittest.TestCase):

    def setUp(self):
        self.cController = CustomerController

        self.goodReqData = {
            "emailAddress": "sandhu63@uni.coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }

        self.badReqData = {
            "email": "sandhu63@uni.coventry.ac.uk",
            "pass": "thisisnotagoodpassword"
        }

    def tearDown(self):
        pass

    def test_json_key_emailAddress_exists(self):
        pass
        # try:
        #     self.cController.customerSignIn((self.badReqData))
        #     self.fail("Didn't raise ValueError")
        # except Exception as e:
        #     expectedErrorMsg = "Email address not provided in request JSON"
        #     print(e.args[0])
        #     self.assertEqual(expectedErrorMsg, e.args[0])

        # expectedErrorMsg = "Email address not provided in request JSON"
        # self.assertEqual(str(ctx.exception), expectedErrorMsg)


if __name__ == '__main__':
    unittest.main()
