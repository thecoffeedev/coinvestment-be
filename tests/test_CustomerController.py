import string
import unittest
from flask import Flask, render_template, request, session
from models.Customer import Customer
from models.Utility import Utility
from controllers.CustomerController import CustomerController
from data_access.CustomerDataAccess import CustomerDataAccess

class TestGenerateToken(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.CController = CustomerController(app)

    def tearDown(self):
        pass

    def test_token_must_not_be_none(self):
        token = self.CController.generateToken()
        self.assertIsNotNone(token)

    def test_token_length_is_not_less_than_19_characters(self):
        token = self.CController.generateToken()
        self.assertGreater(len(token), 19)

    def test_token_length_is_not_19_characters(self):
        token = self.CController.generateToken()
        self.assertIsNot(len(token), 19)

    def test_token_length_is_not_more_than_21_characters(self):
        token = self.CController.generateToken()
        self.assertLess(len(token), 21)
    def test_token_length_is_not_21_characters(self):
        token = self.CController.generateToken()
        self.assertIsNot(len(token), 21)

    def test_token_length_is_20_characters(self):
        token = self.CController.generateToken()
        self.assertEqual(len(token), 20)

    def test_token_is_not_an_int(self):
        token = self.CController.generateToken()
        self.assertNotIsInstance(token, int)

    def test_token_is_not_a_float(self):
        token = self.CController.generateToken()
        self.assertNotIsInstance(token, float)

    def test_token_is_not_a_dict(self):
        token = self.CController.generateToken()
        self.assertNotIsInstance(token, dict)

    def test_token_is_not_a_list(self):
        token = self.CController.generateToken()
        self.assertNotIsInstance(token, list)

    def test_token_is_a_string(self):
        token = self.CController.generateToken()
        self.assertIsInstance(token, str)

    def test_token_is_not_empty(self):
        token = self.CController.generateToken()
        self.assertIsNot(token, "")

    def test_token_is_not_whitespace(self):
        token = self.CController.generateToken()
        self.assertIsNot(token, " ")

    def test_token_is_not_multiple_whitespace(self):
        token = self.CController.generateToken()
        self.assertIsNot(token.strip(), "")

    def test_token_is_a_printable_string(self):
        token = self.CController.generateToken()
        self.assertTrue(token.isprintable())

    def test_token_is_ascii(self):
        token = self.CController.generateToken()
        self.assertTrue(token.isascii())

    def test_token_is_alnum(self):
        token = self.CController.generateToken()
        self.assertTrue(token.isalnum())

class TestSignUp(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.CController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_emailAddress(self):
        reqData = {
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_emailAddress(self):
        reqData = {
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.signUp(reqData)
        expected = "Email address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_emailAddress(self):
        reqData = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_emailAddress(self):
        reqData = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.signUp(reqData)
        expected = "Email address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "name": "Test name"
        }
        response = self.CController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "name": "Test name"
        }
        response = self.CController.signUp(reqData)
        expected = "Password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password",
            "name": "Test name"
        }
        response = self.CController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password",
            "name": "Test name"
        }
        response = self.CController.signUp(reqData)
        expected = "Password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_name(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password"
        }
        response = self.CController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_name(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password"
        }
        response = self.CController.signUp(reqData)
        expected = "Name not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_name(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password",
            "nam": "Test name"
        }
        response = self.CController.signUp(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_name(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "password": "password",
            "nam": "Test name"
        }
        response = self.CController.signUp(reqData)
        expected = "Name not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_message_email_prev_registered(self):
        reqData = {
            "emailAddress": "beatrice.shilling@hotmail.com",
            "password": "password",
            "name": "Test name"
        }
        response = self.CController.signUp(reqData)
        expected = "Email address already registered with an account"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_code_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.CController.signUp(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_message_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.CController.signUp(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_response_customerID_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.CController.signUp(reqData)
        self.assertEqual("customerID" in response.keys(), True)

    def test_success_response_emailAddress_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.CController.signUp(reqData)
        self.assertEqual(response.get("emailAddress"), "alan.turing@hotmail.com")

    def test_success_name_key_good_req(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password",
            "name": "Alan Turing"
        }
        response = self.CController.signUp(reqData)
        self.assertEqual(response.get("name"), "Alan Turing")


class TestSignIn(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.CController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_emailAddress(self):
        reqData = {
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.signIn(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_emailAddress(self):
        reqData = {
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.signIn(reqData)
        expected = "Email address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_emailAddress(self):
        reqData = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.signIn(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_emailAddress(self):
        reqData = {
            "email": "sandhu63@coventry.ac.uk",
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.signIn(reqData)
        expected = "Email address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
        }
        response = self.CController.signIn(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
        }
        response = self.CController.signIn(reqData)
        expected = "Password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password"
        }
        response = self.CController.signIn(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_password(self):
        reqData = {
            "emailAddress": "thisisnotagoodpassword",
            "pass": "password"
        }
        response = self.CController.signIn(reqData)
        expected = "Password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_statuscode_email_prev_registered(self):
        reqData = {
            "emailAddress": "beatrice.shilling@hotmail.com",
            "password": "password"
        }
        response = self.CController.signIn(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_message_email_prev_registered(self):
        reqData = {
            "emailAddress": "beatrice.shilling@hotmail.com",
            "password": "password"
        }
        response = self.CController.signIn(reqData)
        expected = "Successfully signed in customer"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_with_non_registered(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        response = self.CController.signIn(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_message_with_non_registered(self):
        reqData = {
            "emailAddress": "alan.turing@hotmail.com",
            "password": "password"
        }
        response = self.CController.signIn(reqData)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
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
        r = self.CController.signUp(reqData)
        response = self.CController.signIn(reqData2)
        self.assertEqual(response.get("name"), "Alan Turing")


class TestChangePassword(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.CController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_currentPassword(self):
        reqData = {
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.CController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_currentPassword(self):
        reqData = {
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.CController.changePassword(reqData)
        expected = "Current password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_currentPassword(self):
        reqData = {
            "password": "password1",
            "newPaassword": "thisisnotagoodpassword"
        }
        response = self.CController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_currentPassword(self):
        reqData = {
            "password": "password1",
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.CController.changePassword(reqData)
        expected = "Current password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_newPassword(self):
        reqData = {
            "currentPassword": "password1"
        }
        response = self.CController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_password(self):
        reqData = {
            "currentPassword": "password1"
        }
        response = self.CController.changePassword(reqData)
        expected = "New password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_newPassword(self):
        reqData = {
            "currentPassword": "password1",
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_password(self):
        reqData = {
            "currentPassword": "password1",
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.changePassword(reqData)
        expected = "New password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.CController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.CController.changePassword(reqData)
        expected = "customerID not added to request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customer": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.CController.changePassword(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customer": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.CController.changePassword(reqData)
        expected = "customerID not added to request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statusCode_incorrect_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1wNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.CController.changePassword(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_message_incorrect_customerID(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1wNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.CController.changePassword(reqData)
        expected = "Account not found with customer ID provided"
        self.assertEqual(response.get("status")["statusMessage"], expected)


    def test_failure_statusCode_incorrect_currentPassword(self):
        reqData = {
            "currentPassword": "password1",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.CController.changePassword(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_message_incorrect_currentPassword(self):
        reqData = {
            "currentPassword": "password1",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.CController.changePassword(reqData)
        expected = "Current password provided is incorrect"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_not_existing_customer(self):
        reqData = {
            "currentPassword": "password1",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "tj3jf0jlSFjsojflsfsf"  # Beatrice ID
        }
        response = self.CController.changePassword(reqData)
        expected = "Account not found with customer ID provided"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_statuscode_correct_currentPassword(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.CController.changePassword(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_message_correct_currentPassword(self):
        reqData = {
            "currentPassword": "password",
            "newPassword": "thisisnotagoodpassword",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"  # Beatrice ID
        }
        response = self.CController.changePassword(reqData)
        expected = "Successfully changed password for customer. You will be signed out. Sign in with new password"
        self.assertEqual(response.get("status")["statusMessage"], expected)


class TestChangeEmailAddress(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.CController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_currentPassword(self):
        reqData = {
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "t845hjw0g9j3285yejoi"
        }
        response = self.CController.changeEmailAddress(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_currentPassword(self):
        reqData = {
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "t845hjw0g9j3285yejoi"
        }
        response = self.CController.changeEmailAddress(reqData)
        expected = "Current password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_currentPassword(self):
        reqData = {
            "password": "password1",
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "t845hjw0g9j3285yejoi"
        }
        response = self.CController.changeEmailAddress(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_currentPassword(self):
        reqData = {
            "password": "password1",
            "newPassword": "thisisnotagoodpassword"
        }
        response = self.CController.changeEmailAddress(reqData)
        expected = "Current password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_newEmailAddress(self):
        reqData = {
            "currentPassword": "password1",
            "customerID": "328uewijfj3258ykr39d"
        }
        response = self.CController.changeEmailAddress(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_newEmailAddress(self):
        reqData = {
            "currentPassword": "password1",
            "password": "thisisnotagoodpassword"
        }
        response = self.CController.changeEmailAddress(reqData)
        expected = "New password not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statusCode_customer_not_exists(self):
        reqData = {
            "currentPassword": "password1",
            "newEmailAddress": "thisisnotagoodpassword",
            "customerID": "ORjf832hr0192jfj32rh"
        }
        response = self.CController.changeEmailAddress(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_message_customer_not_exists(self):
        reqData = {
            "currentPassword": "password1",
            "newEmailAddress": "email@email.com",
            "customerID": "ORjf832hr0192jfj32rh"
        }
        response = self.CController.changeEmailAddress(reqData)
        expected = "Account not found: not registered"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_statuscode_successful_change(self):
        reqData = {
            "currentPassword": "password",
            "newEmailAddress": "email@email.com",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.changeEmailAddress(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_message_successful_change(self):
        reqData = {
            "currentPassword": "password",
            "newEmailAddress": "email@email.com",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.changeEmailAddress(reqData)
        expected = "Successfully changed email address for customer"
        self.assertEqual(response.get("status")["statusMessage"], expected)


class TestGetCustomerDetails(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.CController = CustomerController(app)
        self.CDA = CustomerDataAccess(app)

    def tearDown(self):
        self.CDA.testDropTables()

    def test_failure_statuscode_missing_key_customerID(self):
        reqData = {
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_missing_key_customerID(self):
        reqData = {
        }
        response = self.CController.getCustomerDetails(reqData)
        expected = "customerID not added to request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_customerID(self):
        reqData = {
            "customer": "t845hjw0g9j3285yejoi"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_message_incorrect_key_currentPassword(self):
        reqData = {
            "customer": "t845hjw0g9j3285yejoi"
        }
        response = self.CController.getCustomerDetails(reqData)
        expected = "customerID not added to request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_customer_not_exist(self):
        reqData = {
            "customerID": "t845hjw0g9j3285yejoi"
        }
        response = self.CController.getCustomerDetails(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_failure_message_customer_not_exist(self):
        reqData = {
            "customerID": "t845hjw0g9j3285yejoi"
        }
        response = self.CController.getCustomerDetails(reqData)
        expected = "Account not found: not registered"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_statuscode_customer_exist(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status")["statusCode"], expected)

    def test_success_message_customer_exist(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        expected = "Successfully retrieved customer details"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_returned_response_is_not_an_empty_dict(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertIsNot(response, {})

    def test_returned_response_is_dict(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertIsInstance(response, dict)

    def test_customerID_for_retrieved_customer(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        expected = "1WNJKpBpYfWwKIlvbaz0"
        self.assertEqual(response.get("customerID"), expected)

    def test_registerDatetime_is_string_for_retrieved_customer(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertIsInstance(response.get("registerDatetime"), str)

    def test_registerDatetime_is_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertEqual(response.get("registerDatetime"), "29-09-2022 18:18:12")

    def test_previousSignInDatetime_is_string_for_retrieved_customer(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertIsInstance(response.get("previousSignInDatetime"), str)

    def test_previousSignInDatetime_is_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertEqual(response.get("previousSignInDatetime"), "30-09-2022 20:57:51")

    def test_currentSignInDatetime_is_string_for_retrieved_customer(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertIsInstance(response.get("currentSignInDatetime"), str)

    def test_currentSignInDatetime_is_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertEqual(response.get("currentSignInDatetime"), "30-09-2022 20:47:24")

    def test_name_is_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertEqual(response.get("name"), "Beatrice Shilling")

    def test_emailAddress_is_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.CController.getCustomerDetails(reqData)
        self.assertEqual(response.get("emailAddress"), "beatrice.shilling@hotmail.com")

if __name__ == '__main__':
    unittest.main()
