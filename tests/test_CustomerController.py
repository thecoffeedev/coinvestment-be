import unittest
import flask
from flask import Flask, render_template, request, session
from models.Customer import Customer
from models.Utility import Utility
from controllers.CustomerController import CustomerController
from data_access.CustomerDataAccess import CustomerDataAccess


class TestCustomerSignUp(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.cController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_emailAddress(self):
        reqData = {
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_emailAddress(self):
        reqData = {
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signUp(reqData)
        expected = "Email address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_emailAddress(self):
        reqData = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_emailAddress(self):
        reqData = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signUp(reqData)
        expected = "Email address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "name": "Test name"
        }
        response = self.cController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "name": "Test name"
        }
        response = self.cController.signUp(reqData)
        expected = "Password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password",
            "name": "Test name"
        }
        response = self.cController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password",
            "name": "Test name"
        }
        response = self.cController.signUp(reqData)
        expected = "Password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_name(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password"
        }
        response = self.cController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_name(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password"
        }
        response = self.cController.signUp(reqData)
        expected = "Name not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_name(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password",
            "nam": "Test name"
        }
        response = self.cController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_name(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password",
            "nam": "Test name"
        }
        response = self.cController.signUp(reqData)
        expected = "Name not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_message_email_prev_registered(self):
        reqData = {
            "emailAddress": "beatrice.shilling@hotmail.com",
            "password": "password",
            "name": "Test name"
        }
        response = self.cController.signUp(reqData)
        expected = "Email address already registered with an account"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_code_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.cController.signUp(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_message_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.cController.signUp(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_response_customerID_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.cController.signUp(reqData)
        self.assertEqual("customerID" in response.keys(), True)

    def test_success_response_emailAddress_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.cController.signUp(reqData)
        self.assertEqual(response.get("emailAddress"), "alan.turing@hotmail.com")

    def test_success_name_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.cController.signUp(reqData)
        self.assertEqual(response.get("name"), "Alan Turing")


class TestCustomerSignIn(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.cController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_emailAddress(self):
        reqData = {
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signIn(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_emailAddress(self):
        reqData = {
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signIn(reqData)
        expected = "Email address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_emailAddress(self):
        reqData = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signIn(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_emailAddress(self):
        reqData = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signIn(reqData)
        expected = "Email address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
        }
        response = self.cController.signIn(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
        }
        response = self.cController.signIn(reqData)
        expected = "Password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password"
        }
        response = self.cController.signIn(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password"
        }
        response = self.cController.signIn(reqData)
        expected = "Password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_statuscode_email_prev_registered(self):
        reqData = {
            "emailAddress": "beatrice.shilling@hotmail.com",
            "password": "password"
        }
        response = self.cController.signIn(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_message_email_prev_registered(self):
        reqData = {
            "emailAddress": "beatrice.shilling@hotmail.com",
            "password": "password"
        }
        response = self.cController.signIn(reqData)
        expected = "Successfully signed in customer"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_with_non_registered(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        response = self.cController.signIn(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_message_with_non_registered(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        response = self.cController.signIn(reqData)
        expected = "Account not found: not registered"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_good_req_incorrect_email_address(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alanturing@hotmail.com",
            "password": "password"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_message_good_req_incorrect_email_address(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alanturing@hotmail.com",
            "password": "password"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        expected = "Account not found: not registered"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_good_req_incorrect_password(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password123"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_message_good_req_incorrect_password(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password123"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        expected = "Customer email address or password incorrect"
        self.assertEqual(response.get("status")["statusMessage"], expected)


    def test_success_statuscode_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_message_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        expected = "Successfully signed in customer"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_response_customerID_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        self.assertEqual("customerID" in response.keys(), True)

    def test_success_response_currentSignInDatetime_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        self.assertEqual("currentSignInDatetime" in response.keys(), True)

    def test_success_response_previousSignInDatetime_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        self.assertEqual("previousSignInDatetime" in response.keys(), True)

    def test_success_response_emailAddress_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        self.assertEqual(response.get("emailAddress"), "alan.turing@hotmail.com")

    def test_success_response_name_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        reqData2 = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        r = self.cController.signUp(reqData)
        response = self.cController.signIn(reqData2)
        self.assertEqual(response.get("name"), "Alan Turing")


class TestCustomerChangePassword(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.cController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_currentPassword(self):
        reqData = {
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_currentPassword(self):
        reqData = {
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(reqData)
        expected = "Current password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_currentPassword(self):
        reqData = {
            "password": "password1",
            "newPaassword": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_currentPassword(self):
        reqData = {
            "password": "password1",
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(reqData)
        expected = "Current password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_newPassword(self):
        reqData = {
            "currentPassword": "password1"
        }
        response = self.cController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_password(self):
        reqData = {
            "currentPassword": "password1"
        }
        response = self.cController.changePassword(reqData)
        expected = "New password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_newPassword(self):
        reqData = {
            "currentPassword": "password1",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_password(self):
        reqData = {
            "currentPassword": "password1",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(reqData)
        expected = "New password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(reqData)
        expected = "customerID not added to request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customer": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.cController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customer": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.cController.changePassword(reqData)
        expected = "customerID not added to request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statusCode_incorrect_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1wNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.cController.changePassword(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_message_incorrect_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1wNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.cController.changePassword(reqData)
        expected = "Account not found with customer ID provided"
        self.assertEqual(response.get("status")["statusMessage"], expected)


    def test_failure_statusCode_incorrect_currentPassword(self):
        reqData = {
            "currentPassword": "password1",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.cController.changePassword(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_message_incorrect_currentPassword(self):
        reqData = {
            "currentPassword": "password1",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.cController.changePassword(reqData)
        expected = "Current password provided is incorrect"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_not_existing_customer(self):
        reqData = {
            "currentPassword": "password1",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "tj3jf0jlSFjsojflsfsf"  # Beatrice ID
        }
        response = self.cController.changePassword(reqData)
        expected = "Account not found with customer ID provided"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_statuscode_correct_currentPassword(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.cController.changePassword(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_message_correct_currentPassword(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.cController.changePassword(reqData)
        expected = "Successfully changed password for customer. You will be signed out. Sign in with new password"
        self.assertEqual(response.get("status")["statusMessage"], expected)

class TestCustomerChangeEmailAddress(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.cController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_currentPassword(self):
        reqData = {
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "t845hjw0g9j3285yejoi"
        }
        response = self.cController.changeEmailAddress(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_currentPassword(self):
        reqData = {
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "t845hjw0g9j3285yejoi"
        }
        response = self.cController.changeEmailAddress(reqData)
        expected = "Current password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_currentPassword(self):
        reqData = {
            "password": "password1",
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "t845hjw0g9j3285yejoi"
        }
        response = self.cController.changeEmailAddress(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_currentPassword(self):
        reqData = {
            "password": "password1",
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.cController.changeEmailAddress(reqData)
        expected = "Current password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_newEmailAddress(self):
        reqData = {
            "currentPassword": "password1",
            "customerID": "328uewijfj3258ykr39d"
        }
        response = self.cController.changeEmailAddress(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_newEmailAddress(self):
        reqData = {
            "currentPassword": "password1",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.changeEmailAddress(reqData)
        expected = "New password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statusCode_customer_not_exists(self):
        reqData = {
            "currentPassword": "password1",
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "ORjf832hr0192jfj32rh"
        }
        response = self.cController.changeEmailAddress(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_msg_customer_not_exists(self):
        reqData = {
            "currentPassword": "password1",
            "newEmailAddress": "email@email.com",
            "customerID": "ORjf832hr0192jfj32rh"
        }
        response = self.cController.changeEmailAddress(reqData)
        expected = "Account not found: not registered"
        self.assertEqual(response.get("status")["statusMessage"], expected)


if __name__ == '__main__':
    unittest.main()
