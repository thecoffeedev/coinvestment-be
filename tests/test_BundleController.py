import unittest
import flask
from flask import Flask, render_template, request, session
from models.Customer import Customer
from models.Utility import Utility
from controllers.BundleController import BundleController
from data_access.BundleDataAccess import BundleDataAccess


class TestGetBundleNameByBundleID(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.BController = BundleController(app)
        self.BDA = BundleDataAccess(app)

    def tearDown(self):
        self.BDA.testDropTables()

    def test_does_not_return_a_set(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertNotIsInstance(bundle, set)

    def test_does_not_return_a_list(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertNotIsInstance(bundle, list)

    def test_does_return_a_tuple(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertIsInstance(bundle, tuple)

    def test_does_not_return_empty_tuple(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertIsNot(bundle, ())

    def test_return_strings_in_tuple_element_zero(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertIsInstance(bundle[0], str)

    def test_return_strings_in_tuple_element_one(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertIsInstance(bundle[1], str)

    def test_correct_value_name_for_key_1(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertEqual(bundle[0], "Alpha")

    def test_correct_value_risk_for_key_1(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertEqual(bundle[1], "Low risk/Short term")

    def test_correct_value_name_for_key_2(self):
        bundle = self.BController.getBundleNameByBundleID("2")
        self.assertEqual(bundle[0], "Beta")

    def test_correct_value_risk_for_key_2(self):
        bundle = self.BController.getBundleNameByBundleID("2")
        self.assertEqual(bundle[1], "Medium risk/Short term")

    def test_correct_value_name_for_key_3(self):
        bundle = self.BController.getBundleNameByBundleID("3")
        self.assertEqual(bundle[0], "Mu")

    def test_correct_value_risk_for_key_3(self):
        bundle = self.BController.getBundleNameByBundleID("3")
        self.assertEqual(bundle[1], "Low risk/Medium term")

    def test_correct_value_name_for_key_4(self):
        bundle = self.BController.getBundleNameByBundleID("4")
        self.assertEqual(bundle[0], "Omega")

    def test_correct_value_risk_for_key_4(self):
        bundle = self.BController.getBundleNameByBundleID("4")
        self.assertEqual(bundle[1], "Medium risk/Medium term")

    def test_correct_value_name_for_key_5(self):
        bundle = self.BController.getBundleNameByBundleID("5")
        self.assertEqual(bundle[0], "Pi")

    def test_correct_value_risk_for_key_5(self):
        bundle = self.BController.getBundleNameByBundleID("5")
        self.assertEqual(bundle[1], "Medium risk/Long term")

    def test_correct_value_name_for_key_6(self):
        bundle = self.BController.getBundleNameByBundleID("6")
        self.assertEqual(bundle[0], "Sigma")

    def test_correct_value_risk_for_key_6(self):
        bundle = self.BController.getBundleNameByBundleID("6")
        self.assertEqual(bundle[1], "High risk/Long term")


class TestGetAllAvailableBundles(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.BController = BundleController(app)
        self.BDA = BundleDataAccess(app)

    def tearDown(self):
        self.BDA.testDropTables()

    def test_success_statuscode(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "SUCCESS"
        self.assertEqual(bundles.get("status").get("statusCode"), expected)

    def test_success_status_message(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "All available bundles"
        self.assertEqual(bundles.get("status").get("statusMessage"), expected)

    def test_bundleID_is_correct_for_bundle_1(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "1"
        self.assertEqual(bundles.get("availableBundles")[0].get("bundleID"), expected)

    def test_bundleName_is_correct_for_bundle_1(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Alpha"
        self.assertEqual(bundles.get("availableBundles")[0].get("bundleName"), expected)

    def test_minimumHoldingPeriod_is_correct_for_bundle_1(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 6
        self.assertEqual(bundles.get("availableBundles")[0].get("minimumHoldingPeriod"), expected)

    def test_riskLevel_is_correct_for_bundle_1(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Low risk/Short term"
        self.assertEqual(bundles.get("availableBundles")[0].get("riskLevel"), expected)

    def test_bundleCryptocurrencies_is_correct_for_bundle_1(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "bitcoin"
        self.assertEqual(bundles.get("availableBundles")[0]
                         .get("bundleCryptocurrencies")[0].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies2_is_correct_for_bundle_1(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "ethereum"
        self.assertEqual(bundles.get("availableBundles")[0]
                         .get("bundleCryptocurrencies")[1].get("cryptocurrencyCode"),
                         expected)

    def test_percentage_is_correct_for_bundle_1(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 50
        self.assertEqual(bundles.get("availableBundles")[0]
                         .get("bundleCryptocurrencies")[0].get("percentage"),
                         expected)

    def test_percentage2_is_correct_for_bundle_1(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 50
        self.assertEqual(bundles.get("availableBundles")[0]
                         .get("bundleCryptocurrencies")[1].get("percentage"),
                         expected)
    def test_bundleID_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "2"
        self.assertEqual(bundles.get("availableBundles")[1].get("bundleID"), expected)

    def test_bundleName_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Beta"
        self.assertEqual(bundles.get("availableBundles")[1].get("bundleName"), expected)

    def test_minimumHoldingPeriod_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 6
        self.assertEqual(bundles.get("availableBundles")[1].get("minimumHoldingPeriod"), expected)

    def test_riskLevel_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Medium risk/Short term"
        self.assertEqual(bundles.get("availableBundles")[1].get("riskLevel"), expected)

    def test_bundleCryptocurrencies_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "bitcoin-cash"
        self.assertEqual(bundles.get("availableBundles")[1]
                         .get("bundleCryptocurrencies")[0].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies2_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "tether"
        self.assertEqual(bundles.get("availableBundles")[1]
                         .get("bundleCryptocurrencies")[1].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies3_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "ripple"
        self.assertEqual(bundles.get("availableBundles")[1]
                         .get("bundleCryptocurrencies")[2].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies4_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "litecoin"
        self.assertEqual(bundles.get("availableBundles")[1]
                         .get("bundleCryptocurrencies")[3].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies5_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "monero"
        self.assertEqual(bundles.get("availableBundles")[1]
                         .get("bundleCryptocurrencies")[4].get("cryptocurrencyCode"),
                         expected)

    def test_percentage1_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 25
        self.assertEqual(bundles.get("availableBundles")[1]
                         .get("bundleCryptocurrencies")[0].get("percentage"),
                         expected)

    def test_percentage2_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 15
        self.assertEqual(bundles.get("availableBundles")[1]
                         .get("bundleCryptocurrencies")[1].get("percentage"),
                         expected)

    def test_percentage3_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 15
        self.assertEqual(bundles.get("availableBundles")[1]
                         .get("bundleCryptocurrencies")[2].get("percentage"),
                         expected)

    def test_percentage4_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 25
        self.assertEqual(bundles.get("availableBundles")[1]
                         .get("bundleCryptocurrencies")[3].get("percentage"),
                         expected)

    def test_percentage5_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[1]
                         .get("bundleCryptocurrencies")[4].get("percentage"),
                         expected)

    def test_bundleID_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "3"
        self.assertEqual(bundles.get("availableBundles")[2].get("bundleID"), expected)

    def test_bundleName_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Mu"
        self.assertEqual(bundles.get("availableBundles")[2].get("bundleName"), expected)

    def test_minimumHoldingPeriod_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 12
        self.assertEqual(bundles.get("availableBundles")[2].get("minimumHoldingPeriod"), expected)

    def test_riskLevel_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Low risk/Medium term"
        self.assertEqual(bundles.get("availableBundles")[2].get("riskLevel"), expected)

    def test_bundleCryptocurrencies_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "dogecoin"
        self.assertEqual(bundles.get("availableBundles")[2]
                         .get("bundleCryptocurrencies")[0].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies2_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "shiba-inu"
        self.assertEqual(bundles.get("availableBundles")[2]
                         .get("bundleCryptocurrencies")[1].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies3_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "ethereum-classic"
        self.assertEqual(bundles.get("availableBundles")[2]
                         .get("bundleCryptocurrencies")[2].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies4_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "apecoin"
        self.assertEqual(bundles.get("availableBundles")[2]
                         .get("bundleCryptocurrencies")[3].get("cryptocurrencyCode"),
                         expected)

    def test_percentage1_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[2]
                         .get("bundleCryptocurrencies")[0].get("percentage"),
                         expected)

    def test_percentage2_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[2]
                         .get("bundleCryptocurrencies")[1].get("percentage"),
                         expected)

    def test_percentage3_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 30
        self.assertEqual(bundles.get("availableBundles")[2]
                         .get("bundleCryptocurrencies")[2].get("percentage"),
                         expected)

    def test_percentage4_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 30
        self.assertEqual(bundles.get("availableBundles")[2]
                         .get("bundleCryptocurrencies")[3].get("percentage"),
                         expected)

    def test_bundleID_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "4"
        self.assertEqual(bundles.get("availableBundles")[3].get("bundleID"), expected)

    def test_bundleName_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Omega"
        self.assertEqual(bundles.get("availableBundles")[3].get("bundleName"), expected)

    def test_minimumHoldingPeriod_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 12
        self.assertEqual(bundles.get("availableBundles")[3].get("minimumHoldingPeriod"), expected)

    def test_riskLevel_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Medium risk/Medium term"
        self.assertEqual(bundles.get("availableBundles")[3].get("riskLevel"), expected)

    def test_bundleCryptocurrencies_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "chainlink"
        self.assertEqual(bundles.get("availableBundles")[3]
                         .get("bundleCryptocurrencies")[0].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies2_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "decentraland"
        self.assertEqual(bundles.get("availableBundles")[3]
                         .get("bundleCryptocurrencies")[1].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies3_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "quant-network"
        self.assertEqual(bundles.get("availableBundles")[3]
                         .get("bundleCryptocurrencies")[2].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies4_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "wrapped-bitcoin"
        self.assertEqual(bundles.get("availableBundles")[3]
                         .get("bundleCryptocurrencies")[3].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies5_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "usd-coin"
        self.assertEqual(bundles.get("availableBundles")[3]
                         .get("bundleCryptocurrencies")[4].get("cryptocurrencyCode"),
                         expected)

    def test_percentage1_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[3]
                         .get("bundleCryptocurrencies")[0].get("percentage"),
                         expected)

    def test_percentage2_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[3]
                         .get("bundleCryptocurrencies")[3].get("percentage"),
                         expected)

    def test_percentage3_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[3]
                         .get("bundleCryptocurrencies")[2].get("percentage"),
                         expected)

    def test_percentage4_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[3]
                         .get("bundleCryptocurrencies")[3].get("percentage"),
                         expected)

    def test_percentage5_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[3]
                         .get("bundleCryptocurrencies")[4].get("percentage"),
                         expected)

    def test_bundleID_is_correct_for_bundle_5(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "5"
        self.assertEqual(bundles.get("availableBundles")[4].get("bundleID"), expected)

    def test_bundleName_is_correct_for_bundle_5(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Pi"
        self.assertEqual(bundles.get("availableBundles")[4].get("bundleName"), expected)

    def test_minimumHoldingPeriod_is_correct_for_bundle_5(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 18
        self.assertEqual(bundles.get("availableBundles")[4].get("minimumHoldingPeriod"), expected)

    def test_riskLevel_is_correct_for_bundle_5(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Medium risk/Long term"
        self.assertEqual(bundles.get("availableBundles")[4].get("riskLevel"), expected)

    def test_bundleCryptocurrencies_is_correct_for_bundle_5(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "dai"
        self.assertEqual(bundles.get("availableBundles")[4]
                         .get("bundleCryptocurrencies")[0].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies2_is_correct_for_bundle_5(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "binancecoin"
        self.assertEqual(bundles.get("availableBundles")[4]
                         .get("bundleCryptocurrencies")[1].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies3_is_correct_for_bundle_5(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "solana"
        self.assertEqual(bundles.get("availableBundles")[4]
                         .get("bundleCryptocurrencies")[2].get("cryptocurrencyCode"),
                         expected)

    def test_percentage1_is_correct_for_bundle_5(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[4]
                         .get("bundleCryptocurrencies")[0].get("percentage"),
                         expected)

    def test_percentage3_is_correct_for_bundle_5(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[4]
                         .get("bundleCryptocurrencies")[2].get("percentage"),
                         expected)

    def test_bundleID_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "6"
        self.assertEqual(bundles.get("availableBundles")[5].get("bundleID"), expected)

    def test_bundleName_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Sigma"
        self.assertEqual(bundles.get("availableBundles")[5].get("bundleName"), expected)

    def test_minimumHoldingPeriod_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 18
        self.assertEqual(bundles.get("availableBundles")[5].get("minimumHoldingPeriod"), expected)

    def test_riskLevel_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "High risk/Long term"
        self.assertEqual(bundles.get("availableBundles")[5].get("riskLevel"), expected)

    def test_bundleCryptocurrencies_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "algorand"
        self.assertEqual(bundles.get("availableBundles")[5]
                         .get("bundleCryptocurrencies")[0].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies2_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "binance-usd"
        self.assertEqual(bundles.get("availableBundles")[5]
                         .get("bundleCryptocurrencies")[1].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies3_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "flow"
        self.assertEqual(bundles.get("availableBundles")[5]
                         .get("bundleCryptocurrencies")[2].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies4_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "filecoin"
        self.assertEqual(bundles.get("availableBundles")[5]
                         .get("bundleCryptocurrencies")[3].get("cryptocurrencyCode"),
                         expected)

    def test_bundleCryptocurrencies5_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "polkadot"
        self.assertEqual(bundles.get("availableBundles")[5]
                         .get("bundleCryptocurrencies")[4].get("cryptocurrencyCode"),
                         expected)

    def test_percentage1_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[5]
                         .get("bundleCryptocurrencies")[0].get("percentage"),
                         expected)

    def test_percentage2_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[5]
                         .get("bundleCryptocurrencies")[3].get("percentage"),
                         expected)

    def test_percentage3_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[5]
                         .get("bundleCryptocurrencies")[2].get("percentage"),
                         expected)

    def test_percentage4_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[5]
                         .get("bundleCryptocurrencies")[3].get("percentage"),
                         expected)

    def test_percentage5_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = 20
        self.assertEqual(bundles.get("availableBundles")[5]
                         .get("bundleCryptocurrencies")[4].get("percentage"),
                         expected)

class TestGetAllBundleDetailsFromBundleAddress(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.BController = BundleController(app)
        self.BDA = BundleDataAccess(app)

    def tearDown(self):
        self.BDA.testDropTables()

    def test_failure_statusCode_missing_key_customerID(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_customerID(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_customerID(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customer": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_customerID(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customer": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_bundleAddress(self):
        reqData = {
             "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_bundleAddress(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "Bundle Address not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_bundleAddress(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_bundleAddress(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "Bundle Address not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_unauthorized_access_to_non_owner_bundle(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_unauthorized_access_to_non_owner_bundle(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "Authorization Error"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_for_bundle_not_existing(self):
        reqData = {
            "bundleAddress": "328hfdSDFjsfih3foejf",
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_for_bundle_not_existing(self):
        reqData = {
            "bundleAddress": "328hfdSDFjsfih3foejf",
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "No bundle found with address provided"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_success_statuscode_for_correct_request(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_success_statusMessage_for_correct_request(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        expected = "Details for bundle"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_success_response_is_not_empty(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        self.assertIsNot(response, {})

    def test_success_response_key_bundleAddress_is_(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        self.assertIsNot(response, {})

"""
"Debo32tKqJBeZwHHgkvx"

        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
"""

if __name__ == '__main__':
    unittest.main()
