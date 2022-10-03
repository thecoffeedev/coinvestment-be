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
        missingEmail = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signUp(missingEmail)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_emailAddress(self):
        missingEmail = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signUp(missingEmail)
        expected = "Email address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_password(self):
        missingPassword = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password",
            "name": "Test name"
        }
        response = self.cController.signUp(missingPassword)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_password(self):
        missingPassword = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password",
            "name": "Test name"
        }
        response = self.cController.signUp(missingPassword)
        expected = "Password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_name(self):
        missingName = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password",
            "nam": "Test name"
        }
        response = self.cController.signUp(missingName)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_name(self):
        missingName = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password",
            "nam": "Test name"
        }
        response = self.cController.signUp(missingName)
        expected = "Name not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_message_email_prev_registered(self):
        existing = {
            "emailAddress": "beatrice.shilling@hotmail.com",
            "password": "password",
            "name": "Test name"
        }
        response = self.cController.signUp(existing)
        expected = "Email address already registered with an account"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_code_good_req(self):
        goodReq = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.cController.signUp(goodReq)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_msg_good_req(self):
        goodReq = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.cController.signUp(goodReq)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)


class TestCustomerSignIn(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.cController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_emailAddress(self):
        missingEmail = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signIn(missingEmail)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_emailAddress(self):
        missingEmail = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signIn(missingEmail)
        expected = "Email address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_password(self):
        missingPassword = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password"
        }
        response = self.cController.signIn(missingPassword)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_password(self):
        missingPassword = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password"
        }
        response = self.cController.signIn(missingPassword)
        expected = "Password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_message_email_prev_registered(self):
        existing = {
            "emailAddress": "beatrice.shilling@hotmail.com",
            "password": "password"
        }
        response = self.cController.signIn(existing)
        expected = "Successfully signed in customer"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_message_with_non_registered(self):
        goodReq = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        response = self.cController.signIn(goodReq)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_msg_good_req(self):
        signUp = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        signIn = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        r = self.cController.signUp(signUp)
        response = self.cController.signIn(signIn)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)


class TestCustomerChangePassword(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.cController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_currentPassword(self):
        missingcurrentPassword = {
            "password": "password1",
            "newPaassword": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(missingcurrentPassword)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_currentPassword(self):
        missingcurrentPassword = {
            "password": "password1",
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(missingcurrentPassword)
        expected = "Current password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_newPassword(self):
        missingNewPassword = {
            "currentPassword": "password1",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(missingNewPassword)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_password(self):
        missingNewPassword = {
            "currentPassword": "password1",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.changePassword(missingNewPassword)
        expected = "New password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statusCode_incorrect_password(self):
        missingNewPassword = {
            "currentPassword": "password1",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.cController.changePassword(missingNewPassword)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_msg_incorrect_password(self):
        missingNewPassword = {
            "currentPassword": "password1",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.cController.changePassword(missingNewPassword)
        expected = "Current password provided is incorrect"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_not_existing(self):
        missingNewPassword = {
            "currentPassword": "password1",
            "password": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaZ0"  # Beatrice ID
        }
        response = self.cController.changePassword(missingNewPassword)
        expected = "New password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

class TestCustomerChangeEmailAddress(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.cController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_currentPassword(self):
        missingcurrentPassword = {
            "password": "password1",
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "t845hjw0g9j3285yejoi"
        }
        response = self.cController.changeEmailAddress(missingcurrentPassword)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_currentPassword(self):
        missingcurrentPassword = {
            "password": "password1",
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.cController.changeEmailAddress(missingcurrentPassword)
        expected = "Current password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_newEmailAddress(self):
        missingNewEmail = {
            "currentPassword": "password1",
            "customerID": "328uewijfj3258ykr39d"
        }
        response = self.cController.changeEmailAddress(missingNewEmail)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_newEmailAddress(self):
        missingNewPassword = {
            "currentPassword": "password1",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.changeEmailAddress(missingNewPassword)
        expected = "New password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statusCode_customer_not_exists(self):
        missingNewPassword = {
            "currentPassword": "password1",
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "ORjf832hr0192jfj32rh"
        }
        response = self.cController.changeEmailAddress(missingNewPassword)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_msg_customer_not_exists(self):
        missingNewPassword = {
            "currentPassword": "password1",
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "ORjf832hr0192jfj32rh"
        }
        response = self.cController.changeEmailAddress(missingNewPassword)
        expected = "Account not found: not registered"
        self.assertEqual(response.get("status")["statusMessage"], expected)


if __name__ == '__main__':
    unittest.main()
