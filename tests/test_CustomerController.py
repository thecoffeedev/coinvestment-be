import unittest
import flask
from flask import Flask, render_template, request, session
from models.Customer import Customer
from models.Utility import Utility
from controllers.CustomerController import CustomerController


class TestCustomerSignUp(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.cController = CustomerController(app)

        self.goodReq = {
            "emailAddress": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword",
            "name": "Test name"
        }

    def tearDown(self):
        pass

    def test_failure_statuscode_missing_key_emailAddress(self):
        missingEmail = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.cController.signUp(missingEmail)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_emailAddress(self):
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

    def test_failure_message_missing_key_password(self):
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

    def test_failure_message_missing_key_name(self):
        missingName = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password",
            "nam": "Test name"
        }
        response = self.cController.signUp(missingName)
        expected = "Name not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_message_email_prev_registered(self):
        missingName = {
            "emailAddress": "beatrice.shilling@hotmail.com",
            "password": "password",
            "name": "Test name"
        }
        response = self.cController.signUp(missingName)
        expected = "Email address already registered with an account"
        self.assertEqual(response.get("status")["statusMessage"], expected)

if __name__ == '__main__':
    unittest.main()
