import unittest
from flask import Flask, render_template, request, session
from controllers.WalletController import WalletController
from data_access.WalletDataAccess import WalletDataAccess

class TestGetAllAvailableCryptocurrencies(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.wController = WalletController(app)
        self.WDA = WalletDataAccess(app)

    def tearDown(self):
        self.WDA.testDropTables()

    def test_success_response_cryptocurrencyCode_key_present_in_res(self):
        response = self.wController.getAllAvailableCryptocurrencies()
        self.assertTrue("cryptocurrencyCode" in response.get("availableCryptocurrencies")[0].keys())

    def test_success_response_cryptocurrencyName_key_present_in_res(self):
        response = self.wController.getAllAvailableCryptocurrencies()
        self.assertTrue("cryptocurrencyName" in response.get("availableCryptocurrencies")[0].keys())

    def test_success_response_cryptocurrencyCode_key_present_in_res(self):
        response = self.wController.getAllAvailableCryptocurrencies()
        self.assertTrue("symbol" in response.get("availableCryptocurrencies")[0].keys())

    def test_success_statuscode_all_available_cryptocurrencies_list(self):
        response = self.wController.getAllAvailableCryptocurrencies()
        self.assertEqual("SUCCESS", response.get("status")["statusCode"])

    def test_success_msg_all_available_cryptocurrencies_list(self):
        response = self.wController.getAllAvailableCryptocurrencies()
        expected = "List of all available cryptocurrencies"
        self.assertEqual(expected, response.get("status")["statusMessage"])


class TestGetAllWalletDetailsFromWalletAddress(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.wController = WalletController(app)
        self.WDA = WalletDataAccess(app)

    def tearDown(self):
        self.WDA.testDropTables()

    def test_failure_statuscode_missing_key_customerID(self):
        jsonReqData = {
            "walletAddress": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_customerID(self):
        jsonReqData = {
            "walletAddress": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "Wallet address not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "wallet": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "wallet": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "Wallet address not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_msg_authorization_error_walletAddress_does_not_belong_to_logged_in_customer(self):
        jsonReqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "Authorization Error"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_success_msg_wallet_available(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "All wallet details"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_msg_wallet_unavailable(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIcT"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "No wallet exists"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_success_code_wallet_available(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "SUCCESS"
        self.assertEqual(expected, response.get("status")["statusCode"])

    def test_failure_code_wallet_unavailable(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIcT"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        expected = "FAILURE"
        self.assertEqual(expected, response.get("status")["statusCode"])

    def test_success_response_walletAddress_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("walletAddress" in response["wallet"].keys())

    def test_success_response_customerID_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("customerID" in response["wallet"].keys())

    def test_success_response_initialBalance_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("initialBalance" in response["wallet"].keys())

    def test_success_response_currentBalance_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("currentBalance" in response["wallet"].keys())

    def test_success_response_cryptocurrencyCode_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("cryptocurrencyCode" in response["wallet"].keys())

    def test_success_response_holdingPeriod_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("holdingPeriod" in response["wallet"].keys())

    def test_success_response_transactionID_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("transactionID" in response.get("walletTransactions")[0].keys())

    def test_success_response_transactionDatetime_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("transactionDatetime" in response.get("walletTransactions")[0].keys())

    def test_success_response_chargeApplied_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("chargeApplied" in response.get("walletTransactions")[0].keys())

    def test_success_response_amount_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("amount" in response.get("walletTransactions")[0].keys())

    def test_success_response_action_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("action" in response.get("walletTransactions")[0].keys())

    def test_success_response_cardNumber_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("cardNumber" in response.get("walletTransactions")[0].keys())

    def test_success_response_expiry_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("expiry" in response.get("walletTransactions")[0].keys())

    def test_success_response_unitsSold_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("unitsSold" in response.get("walletTransactions")[0].keys())

    def test_success_response_initialRate_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertTrue("initialRate" in response.get("walletTransactions")[0].keys())

    def test_success_response_key_customerID_value_correct(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertEqual("Debo32tKqJBeZwHHgkvx", response.get("wallet").get(("customerID")))

    def test_success_response_key_walletAddress_value_correct(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.getAllWalletDetailsFromWalletAddress(jsonReqData)
        self.assertEqual("hrD3IxwVUWloVP0nrIct", response.get("wallet").get(("walletAddress")))


class TestGetAllWalletsFromCustomerID(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.wController = WalletController(app)
        self.WDA = WalletDataAccess(app)

    def tearDown(self):
        self.WDA.testDropTables()

    def test_failure_statuscode_missing_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_success_msg_wallet_available(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "All wallets for customer"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_msg_wallet_unavailable(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvu"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "No wallet exists"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_success_response_walletAddress_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertTrue("walletAddress" in response.get("wallet")[0].keys())

    def test_success_response_customerID_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertTrue("customerID" in response.get("wallet")[0].keys())

    def test_success_response_initialBalance_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertTrue("initialBalance" in response.get("wallet")[0].keys())

    def test_success_response_currentBalance_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertTrue("currentBalance" in response.get("wallet")[0].keys())

    def test_success_response_cryptocurrencyCode_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertTrue("cryptocurrencyCode" in response.get("wallet")[0].keys())

    def test_success_response_holdingPeriod_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertTrue("holdingPeriod" in response.get("wallet")[0].keys())

    def test_success_response_key_customerID_value_correct(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        self.assertEqual("Debo32tKqJBeZwHHgkvx", response.get("wallet")[0].get(("customerID")))

    def test_failure_code_wallets_not_present_for_customerID(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvX"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "FAILURE"
        self.assertEqual(expected, response.get("status")["statusCode"])

    def test_success_code_wallets_list(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "SUCCESS"
        self.assertEqual(expected, response.get("status")["statusCode"])

    def test_success_message_wallets_list(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.getAllWalletsFromCustomerID(jsonReqData)
        expected = "All wallets for customer"
        self.assertEqual(expected, response.get("status")["statusMessage"])


class TestPurchaseWallet(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.wController = WalletController(app)
        self.WDA = WalletDataAccess(app)

    def tearDown(self):
        self.WDA.testDropTables()

    def test_failure_statuscode_missing_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_initialBalances(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_initialBalance(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Initial Balance not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_initialBalances(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBal": 1.9492
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_initialBalance(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBal": 1.9492
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Initial Balance not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_cryptocurrencyCode(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_cryptocurrencyCode(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Cryptocurrency Code not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_cryptocurrencyCode(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrency": "bitcoin"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_cryptocurrencyCode(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrency": "bitcoin"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Cryptocurrency Code not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_holdingPeriod(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_holdingPeriod(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin"
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Holding Period not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_holdingPeriod(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "period": 4
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_holdingPeriod(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "period": 4
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Holding Period not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4
        }
        response = self.wController.purchaseWallet(jsonReqData)
        expected = "Initial Rate not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "rate": 38291.34
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

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
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_amount(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "initialBalance": 1.9492,
            "cryptocurrencyCode": "bitcoin",
            "holdingPeriod": 4,
            "initialRate": 38291.34
        }
        response = self.wController.purchaseWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

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
        self.assertEqual(expected, response.get("status")["statusMessage"])

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
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

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
        self.assertEqual(expected, response.get("status")["statusMessage"])

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
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

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
        self.assertEqual(expected, response.get("status")["statusMessage"])

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
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

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
        self.assertEqual(expected, response.get("status")["statusMessage"])

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
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

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
        self.assertEqual(expected, response.get("status")["statusMessage"])

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
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

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
        self.assertEqual(expected, response.get("status")["statusMessage"])

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

    def test_success_response_customerID_key_present_in_res(self):
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
        self.assertTrue("customerID" in response["wallet"].keys())

    def test_success_response_initialBalance_key_present_in_res(self):
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
        self.assertTrue("initialBalance" in response["wallet"].keys())

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

    def test_success_response_cryptocurrencyCode_key_present_in_res(self):
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
        self.assertTrue("cryptocurrencyCode" in response["wallet"].keys())

    def test_success_response_holdingPeriod_key_present_in_res(self):
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
        self.assertTrue("holdingPeriod" in response["wallet"].keys())

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

    def test_success_response_transactionDatetime_key_present_in_res(self):
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
        self.assertTrue("transactionDatetime" in response["walletTransaction"].keys())

    def test_success_response_chargeApplied_key_present_in_res(self):
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
        self.assertTrue("chargeApplied" in response["walletTransaction"].keys())

    def test_success_response_amount_key_present_in_res(self):
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
        self.assertTrue("amount" in response["walletTransaction"].keys())

    def test_success_response_action_key_present_in_res(self):
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
        self.assertTrue("action" in response["walletTransaction"].keys())

    def test_success_response_cardNumber_key_present_in_res(self):
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
        self.assertTrue("cardNumber" in response["walletTransaction"].keys())

    def test_success_response_expiry_key_present_in_res(self):
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
        self.assertTrue("expiry" in response["walletTransaction"].keys())

    def test_success_response_unitsSold_key_present_in_res(self):
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
        self.assertTrue("unitsSold" in response["walletTransaction"].keys())

    def test_success_response_initialRate_key_present_in_res(self):
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
        self.assertTrue("initialRate" in response["walletTransaction"].keys())

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

    def test_success_response_chargeApplied_equals_zero(self):
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
        self.assertEqual(0.0, response["walletTransaction"].get("chargeApplied"))

    def test_success_response_unitsSold_equals_zero(self):
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
        self.assertEqual(0.0, response["walletTransaction"].get("unitsSold"))

    def test_success_response_key_customerID_value_correct(self):
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
        self.assertEqual("Debo32tKqJBeZwHHgkvx", response.get("wallet").get(("customerID")))

    def test_success_response_key_initialBalance_value_correct(self):
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
        self.assertEqual(1.9492, response.get("wallet").get(("initialBalance")))

    def test_success_response_key_cryptocurrencyCode_value_correct(self):
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
        self.assertEqual("bitcoin", response.get("wallet").get(("cryptocurrencyCode")))

    def test_success_response_key_holdingPeriod_value_correct(self):
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
        self.assertEqual(4, response.get("wallet").get(("holdingPeriod")))

    def test_success_response_key_initialRate_value_correct(self):
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
        self.assertEqual(38291.34, response.get("walletTransaction").get(("initialRate")))

    def test_success_response_key_amount_value_correct(self):
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
        self.assertEqual(74638.99, response.get("walletTransaction").get(("amount")))

    def test_success_response_key_cardNumber_value_correct(self):
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
        self.assertEqual("************1963", response.get("walletTransaction").get(("cardNumber")))

    def test_success_response_key_expiry_value_correct(self):
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
        self.assertEqual("**/23", response.get("walletTransaction").get(("expiry")))

    def test_success_code_cryptocurrency_purchased(self):
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
        expected = "SUCCESS"
        self.assertEqual(expected, response.get("status")["statusCode"])

    def test_success_message_cryptocurrency_purchased(self):
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
        expected = "Cryptocurrency purchased"
        self.assertEqual(expected, response.get("status")["statusMessage"])


class TestSellWallet(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.wController = WalletController(app)
        self.WDA = WalletDataAccess(app)

    def tearDown(self):
        self.WDA.testDropTables()

    def test_failure_statuscode_missing_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_customerID(self):
        jsonReqData = {
            "customer": "dkj3284hf0239jr23htr"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Wallet Address not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAdd": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_walletAddress(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAdd": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Wallet Address not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_unitsSold(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_unitsSold(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Units Sold not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_unitsSold(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "units": 0.001
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_unitsSold(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "units": 0.001
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Units Sold not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Initial Rate not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "rate": 38291.34
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_initialRate(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "rate": 38291.34
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Initial Rate not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_amount(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_amount(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Amount not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_amount(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amt": 38.2913
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_amount(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amt": 38.2913
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Amount not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_cardNumber(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_cardNumber(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Card Number not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_cardNumber(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "card": 7281726537281963
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_cardNumber(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "card": 7281726537281963
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Card Number not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_missing_key_expiry(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_missing_key_expiry(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Expiry not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_statuscode_incorrect_key_expiry(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "exp": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_incorrect_key_expiry(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "exp": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Expiry not provided in request JSON"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_success_response_walletAddress_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("walletAddress" in response["wallet"].keys())

    def test_success_response_customerID_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("customerID" in response["wallet"].keys())

    def test_success_response_initialBalance_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("initialBalance" in response["wallet"].keys())

    def test_success_response_currentBalance_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("currentBalance" in response["wallet"].keys())

    def test_success_response_cryptocurrencyCode_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("cryptocurrencyCode" in response["wallet"].keys())

    def test_success_response_holdingPeriod_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("holdingPeriod" in response["wallet"].keys())

    def test_success_response_transactionID_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("transactionID" in response["walletTransaction"].keys())

    def test_success_response_transactionDatetime_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("transactionDatetime" in response["walletTransaction"].keys())

    def test_success_response_chargeApplied_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("chargeApplied" in response["walletTransaction"].keys())

    def test_success_response_amount_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("amount" in response["walletTransaction"].keys())

    def test_success_response_action_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("action" in response["walletTransaction"].keys())

    def test_success_response_cardNumber_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("cardNumber" in response["walletTransaction"].keys())

    def test_success_response_expiry_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("expiry" in response["walletTransaction"].keys())

    def test_success_response_unitsSold_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("unitsSold" in response["walletTransaction"].keys())

    def test_success_response_initialRate_key_present_in_res(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertTrue("initialRate" in response["walletTransaction"].keys())

    def test_failure_statuscode_unitsSold_equals_zero(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.0,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("FAILURE", response.get("status")["statusCode"])

    def test_failure_msg_unitsSold_equals_zero(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.0,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Units Sold must be greater than zero"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_msg_authorization_error_walletAddress_does_not_belong_to_logged_in_customer(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "jNrxO4OyXgdqum0wj2LV",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "Authorization Error"
        self.assertEqual(expected, response.get("status")["statusMessage"])

    def test_failure_code_authorization_error_walletAddress_does_not_belong_to_logged_in_customer(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvX",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "FAILURE"
        self.assertEqual(expected, response.get("status")["statusCode"])

    def test_success_response_key_customerID_value_correct(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("Debo32tKqJBeZwHHgkvx", response.get("wallet").get(("customerID")))

    def test_success_response_key_walletAddress_value_correct(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("hrD3IxwVUWloVP0nrIct", response.get("wallet").get(("walletAddress")))

    def test_success_response_key_initialRate_value_correct(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual(38291.34, response.get("walletTransaction").get(("initialRate")))

    def test_success_response_key_amount_value_correct(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual(38.2913, response.get("walletTransaction").get(("amount")))

    def test_success_response_key_cardNumber_value_correct(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("************1963", response.get("walletTransaction").get(("cardNumber")))

    def test_success_response_key_expiry_value_correct(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        self.assertEqual("**/23", response.get("walletTransaction").get(("expiry")))

    def test_success_code_units_sold(self):
        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": "hrD3IxwVUWloVP0nrIct",
            "unitsSold": 0.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        expected = "SUCCESS"
        self.assertEqual(expected, response.get("status")["statusCode"])


    def test_success_message_units_sold(self):
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
        print(response)

        jsonReqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx",
            "walletAddress": response.get("wallet").get("walletAddress"),
            "unitsSold": 19699.001,
            "initialRate": 38291.34,
            "amount": 38.2913,
            "cardNumber": "7281726537281963",
            "expiry": "12/23"
        }
        response = self.wController.sellWallet(jsonReqData)
        print(response)
        expected = "Units sold successfully"
        self.assertEqual(expected, response.get("status")["statusMessage"])


if __name__ == '__main__':
    unittest.main()
