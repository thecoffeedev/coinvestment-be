import unittest
from flask import Flask, render_template, request, session
from controllers.WalletController import WalletController
from data_access.WalletDataAccess import WalletDataAccess


class TestGetAllWalletDetailsFromWalletAddress(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.wController = WalletController(app)
        self.WDA = WalletDataAccess(app)

    def tearDown(self):
        # self.WDA.testDropTables()
        pass

    def test_failure_statuscode_missing_key_customerID(self):
        jsonReqData = {
            "walletAddress": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_customerID(self):
        jsonReqData = {
            "walletAddress": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "Wallet address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "wallet": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "wallet": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "Wallet address not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_msg_authorization_error_walletAddress_does_not_belong_to_logged_in_customer(self):
        jsonReqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "Authorization Error"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_msg_wallet_available(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "All wallet details"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_msg_wallet_unavailable(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIcx"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "No wallet exists"
        self.assertEqual(response.get("status")["statusMessage"], expected)


class TestGetAllWalletsFromCustomerID(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.wController = WalletController(app)
        self.WDA = WalletDataAccess(app)

    def tearDown(self):
        # self.WDA.testDropTables()
        pass

    def test_failure_statuscode_missing_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_msg_wallet_available(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "All wallets for customer"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_msg_wallet_unavailable(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvu"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "No wallet exists"
        self.assertEqual(response.get("status")["statusMessage"], expected)


class TestPurchaseWallet(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.wController = WalletController(app)
        self.WDA = WalletDataAccess(app)

    def tearDown(self):
        # self.WDA.testDropTables()
        pass

    def test_failure_statuscode_missing_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_initialBalances(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_initialBalance(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Initial Balance not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_initialBalances(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBal": 1.9492
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_initialBalance(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBal": 1.9492
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Initial Balance not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_cryptocurrencyCode(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_cryptocurrencyCode(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Cryptocurrency Code not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_cryptocurrencyCode(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrency": "bitcoin"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_cryptocurrencyCode(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrency": "bitcoin"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Cryptocurrency Code not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_holdingPeriod(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_holdingPeriod(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Holding Period not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_holdingPeriod(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "period": 4
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_holdingPeriod(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "period": 4
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Holding Period not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Initial Rate not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "rate": 38291.34
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "rate": 38291.34
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Initial Rate not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_amount(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_amount(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Amount not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_amount(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amt":74638.99
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_amount(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amt": 74638.99
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Amount not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_cardNumber(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_cardNumber(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Card Number not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_cardNumber(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99,
            "card": 7281726537281963
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_cardNumber(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99,
            "card": 7281726537281963
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Card Number not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_missing_key_expiry(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99,
            "cardNumber": "7281726537281963"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_missing_key_expiry(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99,
            "cardNumber": "7281726537281963"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Expiry not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_failure_statuscode_incorrect_key_expiry(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount":74638.99,
            "cardNumber": "7281726537281963",
            "exp": "12/23"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response.get("status")["statusCode"], "FAILURE")

    def test_failure_msg_incorrect_key_expiry(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99,
            "cardNumber": "7281726537281963",
            "exp": "12/23"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Expiry not provided in request JSON"
        self.assertEqual(response.get("status")["statusMessage"], expected)

    def test_success_response_walletAddress_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertTrue("walletAddress" in response["wallet"].keys())

    def test_success_response_transactionID_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertTrue("transactionID" in response["walletTransaction"].keys())

    def test_success_response_currentBalance_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertTrue("currentBalance" in response["wallet"].keys())

    def test_success_response_initialBalance_equal_to_currentBalance(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(response["wallet"].get("initialBalance"), response["wallet"].get("currentBalance"))

    def test_success_response_currentBalance_equals_value(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34,
            "amount": 74638.99,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual(1.9492, response["wallet"].get("currentBalance"))


if __name__ == '__main__':
    unittest.main()
