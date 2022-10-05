import unittest
import flask
from flask import Flask, render_template, request, session
from models.Customer import Customer
from models.Utility import Utility
from controllers.WalletController import WalletController
from data_access.WalletDataAccess import WalletDataAccess


class TestGetAllWalletDetailsFromWalletAddress(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.wController = WalletController(app)
        self.WDA = WalletDataAccess(app)

    def tearDown(self):
        self.WDA.testDropTables()

    def test_failure_statuscode_missing_key_walletAddress(self):
        missingWalletAddress = {
            "wallet": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(missingWalletAddress)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_walletAddress(self):
        missingWalletAddress = {
            "wallet": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(missingWalletAddress)
        expected = "Wallet address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)


    # def test_failure_message_email_prev_registered(self):
    #     existing = {
    #         "emailAddress": "beatrice.shilling@hotmail.com",
    #         "password": "password",
    #         "name": "Test name"
    #     }
    #     response = self.cController.signUp(existing)
    #     expected = "Email address already registered with an account"
    #     self.assertEqual(response.get("status")["statusMessage"], expected)
    #
    # def test_success_code_good_req(self):
    #     goodReq = {
    #         "emailAddress": "alan.turing@hotmail.com",
    #         "password": "password",
    #         "name": "Alan Turing"
    #     }
    #     response = self.cController.signUp(goodReq)
    #     expected = "SUCCESS"
    #     self.assertEqual(response.get("status")["statusCode"], expected)
    #
    # def test_success_msg_good_req(self):
    #     goodReq = {
    #         "emailAddress": "alan.turing@hotmail.com",
    #         "password": "password",
    #         "name": "Alan Turing"
    #     }
    #     response = self.cController.signUp(goodReq)
    #     expected = "SUCCESS"
    #     self.assertEqual(response.get("status")["statusCode"], expected)




if __name__ == '__main__':
    unittest.main()
