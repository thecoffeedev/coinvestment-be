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

    def test_does_not_return_a_tuple(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertNotIsInstance(bundle, tuple)

    def test_does_return_a_list(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertIsInstance(bundle, list)

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
        self.assertEqual(bundle[1], "Low risk")

    def test_correct_value_term_for_key_1(self):
        bundle = self.BController.getBundleNameByBundleID("1")
        self.assertEqual(bundle[2], "Short term")

    def test_correct_value_name_for_key_2(self):
        bundle = self.BController.getBundleNameByBundleID("2")
        self.assertEqual(bundle[0], "Beta")

    def test_correct_value_risk_for_key_2(self):
        bundle = self.BController.getBundleNameByBundleID("2")
        self.assertEqual(bundle[1], "Medium risk")

    def test_correct_value_term_for_key_2(self):
        bundle = self.BController.getBundleNameByBundleID("2")
        self.assertEqual(bundle[2], "Short term")

    def test_correct_value_name_for_key_3(self):
        bundle = self.BController.getBundleNameByBundleID("3")
        self.assertEqual(bundle[0], "Mu")

    def test_correct_value_risk_for_key_3(self):
        bundle = self.BController.getBundleNameByBundleID("3")
        self.assertEqual(bundle[1], "Low risk")

    def test_correct_value_term_for_key_3(self):
        bundle = self.BController.getBundleNameByBundleID("3")
        self.assertEqual(bundle[2], "Medium term")

    def test_correct_value_name_for_key_4(self):
        bundle = self.BController.getBundleNameByBundleID("4")
        self.assertEqual(bundle[0], "Omega")

    def test_correct_value_risk_for_key_4(self):
        bundle = self.BController.getBundleNameByBundleID("4")
        self.assertEqual(bundle[1], "Medium risk")

    def test_correct_value_term_for_key_4(self):
        bundle = self.BController.getBundleNameByBundleID("4")
        self.assertEqual(bundle[2], "Medium term")

    def test_correct_value_name_for_key_5(self):
        bundle = self.BController.getBundleNameByBundleID("5")
        self.assertEqual(bundle[0], "Pi")

    def test_correct_value_risk_for_key_5(self):
        bundle = self.BController.getBundleNameByBundleID("5")
        self.assertEqual(bundle[1], "Medium risk")

    def test_correct_value_term_for_key_5(self):
        bundle = self.BController.getBundleNameByBundleID("5")
        self.assertEqual(bundle[2], "Long term")

    def test_correct_value_name_for_key_6(self):
        bundle = self.BController.getBundleNameByBundleID("6")
        self.assertEqual(bundle[0], "Sigma")

    def test_correct_value_risk_for_key_6(self):
        bundle = self.BController.getBundleNameByBundleID("6")
        self.assertEqual(bundle[1], "High risk")

    def test_correct_value_term_for_key_6(self):
        bundle = self.BController.getBundleNameByBundleID("6")
        self.assertEqual(bundle[2], "Long term")


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
        expected = "Low risk"
        self.assertEqual(bundles.get("availableBundles")[0].get("riskLevel"), expected)

    def test_term_is_correct_for_bundle_1(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Short term"
        self.assertEqual(bundles.get("availableBundles")[0].get("term"), expected)

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
        expected = "Medium risk"
        self.assertEqual(bundles.get("availableBundles")[1].get("riskLevel"), expected)

    def test_term_is_correct_for_bundle_2(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Short term"
        self.assertEqual(bundles.get("availableBundles")[1].get("term"), expected)

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
        expected = "Low risk"
        self.assertEqual(bundles.get("availableBundles")[2].get("riskLevel"), expected)

    def test_term_is_correct_for_bundle_3(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Medium term"
        self.assertEqual(bundles.get("availableBundles")[2].get("term"), expected)

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
        expected = "Medium risk"
        self.assertEqual(bundles.get("availableBundles")[3].get("riskLevel"), expected)

    def test_term_is_correct_for_bundle_4(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Medium term"
        self.assertEqual(bundles.get("availableBundles")[3].get("term"), expected)

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
        expected = "Medium risk"
        self.assertEqual(bundles.get("availableBundles")[4].get("riskLevel"), expected)

    def test_term_is_correct_for_bundle_5(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Long term"
        self.assertEqual(bundles.get("availableBundles")[4].get("term"), expected)

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
        expected = "High risk"
        self.assertEqual(bundles.get("availableBundles")[5].get("riskLevel"), expected)

    def test_term_is_correct_for_bundle_6(self):
        bundles = self.BController.getAllAvailableBundles()
        expected = "Long term"
        self.assertEqual(bundles.get("availableBundles")[5].get("term"), expected)

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

    def test_success_response_key_bundleAddress_exists(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        self.assertTrue("bundleAddress" in response.get("bundle").keys())

    def test_success_response_key_bundleAddress_correct(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        self.assertEqual(response.get("bundle").get("bundleAddress"),
                         "kv908kmPkhFImJrZ4R1i")

    def test_success_response_key_bundleID_exists(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        self.assertTrue("bundleID" in response.get("bundle").keys())

    def test_success_response_key_customerID_exists(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        self.assertTrue("customerID" in response.get("bundle").keys())

    def test_success_response_key_customerID_is_correct(self):
        reqData = {
            "bundleAddress": "kv908kmPkhFImJrZ4R1i",
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundleDetailsFromBundleAddress(reqData)
        self.assertEqual(response.get("bundle").get("customerID"),
                         "1WNJKpBpYfWwKIlvbaz0")


class TestGetAllBundlesFromCustomerID(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.BController = BundleController(app)
        self.BDA = BundleDataAccess(app)

    def tearDown(self):
        self.BDA.testDropTables()

    def test_failure_statusCode_missing_key_customerID(self):
        reqData = {

        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_customerID(self):
        reqData = {

        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_customerID(self):
        reqData = {
            "customer": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_customerID(self):
        reqData = {
            "customer": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statuscode_customerID_does_not_exist(self):
        reqData = {
            "customerID": "1wNJKpBpYfWwKIlvbaz0"  # Lower case w after 1
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_customerID_does_not_exist(self):
        reqData = {
            "customerID": "1wNJKpBpYfWwKIlvbaz0"   # Lower case w after 1
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        expected = "No bundle found with customer ID provided"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_success_statuscode_customerID_does_exist(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_success_statusMessage_customerID_does_exist(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        expected = "All bundles for customer"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_success_reponse_key_bundles_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("bundles" in response.keys())

    def test_success_reponse_key_bundleAddress_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("bundleAddress" in response.get("bundles")[0].keys())

    def test_success_reponse_key_bundleAddress_is_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        expected = "kv908kmPkhFImJrZ4R1i"
        self.assertEqual(response.get("bundles")[0].get("bundleAddress"), expected)

    def test_success_reponse_key_customerID_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("customerID" in response.get("bundles")[0].keys())

    def test_success_reponse_key_customerID_is_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        expected = "1WNJKpBpYfWwKIlvbaz0"
        self.assertEqual(response.get("bundles")[0].get("customerID"), expected)

    def test_success_reponse_key_bundleID_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("bundleID" in response.get("bundles")[0].keys())

    def test_success_reponse_key_purchaseDatetime_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("purchaseDatetime" in response.get("bundles")[0].keys())

    def test_success_reponse_key_holdingPeriod_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("holdingPeriod" in response.get("bundles")[0].keys())

    def test_success_reponse_key_status_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("status" in response.get("bundles")[0].keys())

    def test_success_reponse_key_amount_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("amount" in response.get("bundles")[0].keys())

    def test_success_reponse_key_bundleName_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("bundleName" in response.get("bundles")[0].keys())

    def test_success_reponse_key_riskLevel_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("riskLevel" in response.get("bundles")[0].keys())

    def test_success_reponse_key_term_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("term" in response.get("bundles")[0].keys())

    def test_success_reponse_key_minimumHoldingPeriod_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("bundleCryptocurrencies" in response.get("bundles")[0].keys())

    def test_success_reponse_key_cryptocurrencyCode_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("cryptocurrencyCode" in response.get("bundles")[0].get("bundleCryptocurrencies")[0].keys())

    def test_success_reponse_key_cryptocurrencyName_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("cryptocurrencyName" in response.get("bundles")[0].get("bundleCryptocurrencies")[0].keys())

    def test_success_reponse_key_percentage_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("percentage" in response.get("bundles")[0].get("bundleCryptocurrencies")[0].keys())

    def test_success_reponse_key_bundleCryptocurrencies_is_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)
        self.assertTrue("bundleCryptocurrencies" in response.get("bundles")[0].keys())

    def test_success_reponse_cryptocurrencies_for_bundles(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)

    def test_success_reponse_cryptocurrencies_for_bundles(self):
        reqData = {
            "customerID": "Debo32tKqJBeZwHHgkvx"
        }
        response = self.BController.getAllBundlesFromCustomerID(reqData)


class TestPurchaseBundle(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.BController = BundleController(app)
        self.BDA = BundleDataAccess(app)

    def tearDown(self):
        self.BDA.testDropTables()

    def test_failure_statusCode_missing_key_customerID(self):
        reqData = {
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_customerID(self):
        reqData = {
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_customerID(self):
        reqData = {
            "customer": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_customerID(self):
        reqData = {
            "customer": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_bundleID(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_bundleID(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Bundle ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_bundleID(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundle": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_bundleID(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundle": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Bundle ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_holdingPeriod(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_holdingPeriod(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Holding Period not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_holdingPeriod(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holding": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_holdingPeriod(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holding": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Holding Period not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_initialRate(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_initialRate(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Initial Rate not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_initialRate(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initial": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_initialRate(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initial": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Initial Rate not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_amount(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_amount(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Amount not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_amount(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initial": 22000.00,
            "amoun": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_amount(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amoun": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Amount not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_cardNumber(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_cardNumber(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Card Number not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_cardNumber(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "card": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_cardNumber(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "card": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Card Number not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_expiry(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_expiry(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Expiry not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_expiry(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expired": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_expiry(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expired": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Expiry not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_success_statusCode(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_success_statusMessage(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "Bundle purchased successfully"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_success_response_key_bundleAddress_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("bundleAddress" in response.get("bundle").keys())

    def test_success_response_key_customerID_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("customerID" in response.get("bundle").keys())

    def test_success_response_key_customerID_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "1WNJKpBpYfWwKIlvbaz0"
        self.assertEqual(response.get("bundle").get("customerID"),
                         expected)

    def test_success_response_key_bundleID_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("bundleID" in response.get("bundle").keys())

    def test_success_response_key_bundleID_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "1"
        self.assertEqual(response.get("bundle").get("bundleID"),
                         expected)

    def test_success_response_key_status_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("status" in response.get("bundle").keys())

    def test_success_response_key_status_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "ACTIVE"
        self.assertEqual(response.get("bundle").get("status"),
                         expected)

    def test_success_response_key_purchaseDatetime_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("purchaseDatetime" in response.get("bundle").keys())

    def test_success_response_key_holdingPeriod_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("holdingPeriod" in response.get("bundle").keys())

    def test_success_response_key_holdingPeriod_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = 12
        self.assertEqual(response.get("bundle").get("holdingPeriod"),
                         expected)

    def test_success_response_key_transactionID_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("transactionID" in response.get("bundleTransaction").keys())

    def test_success_response_key_transactionDatetime_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("transactionDatetime" in response.get("bundleTransaction").keys())

    def test_success_response_key_chargeApplied_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("chargeApplied" in response.get("bundleTransaction").keys())


    def test_success_response_key_chargeApplied_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = 0.0
        self.assertEqual(response.get("bundleTransaction")
                         .get("chargeApplied"),
                         expected)

    def test_success_response_key_amount_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("amount" in response.get("bundleTransaction").keys())


    def test_success_response_key_amount_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = 1000.00
        self.assertEqual(response.get("bundleTransaction")
                         .get("amount"),
                         expected)

    def test_success_response_key_action_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("action" in response.get("bundleTransaction").keys())


    def test_success_response_key_action_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "BUY"
        self.assertEqual(response.get("bundleTransaction")
                         .get("action"),
                         expected)

    def test_success_response_key_cardNumber_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("cardNumber" in response.get("bundleTransaction").keys())


    def test_success_response_key_cardNumber_correct_and_masked(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "************3456"
        self.assertEqual(response.get("bundleTransaction")
                         .get("cardNumber"),
                         expected)

    def test_success_response_key_expiry_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("expiry" in response.get("bundleTransaction").keys())


    def test_success_response_key_expiry_correct_and_masked(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = "**/24"
        self.assertEqual(response.get("bundleTransaction")
                         .get("expiry"),
                         expected)

    def test_success_response_key_initialRate_exists(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        self.assertTrue("initialRate" in response.get("bundleTransaction").keys())


    def test_success_response_key_initialRate_correct(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "holdingPeriod": 12,
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.purchaseBundle(reqData)
        expected = 22000.00
        self.assertEqual(response.get("bundleTransaction")
                         .get("initialRate"),
                         expected)


class TestSellBundle(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.BController = BundleController(app)
        self.BDA = BundleDataAccess(app)

    def tearDown(self):
        self.BDA.testDropTables()

    def test_failure_statusCode_missing_key_customerID(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_customerID(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_customerID(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customer": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_customerID(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customer": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Customer ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_bundleID(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_bundleID(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Bundle ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_bundleID(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundle": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_bundleID(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundle": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Bundle ID not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_bundleAddress(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_bundleAddress(self):
        reqData = {
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Bundle Address not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_bundleAddress(self):
        reqData = {
            "bundle": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_bundleAddress(self):
        reqData = {
            "bundle": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Bundle Address not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_initialRate(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_initialRate(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Initial Rate not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_initialRate(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initial": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_initialRate(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initial": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Initial Rate not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_amount(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_amount(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Amount not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_amount(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amoun": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_amount(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amoun": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Amount not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_cardNumber(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_cardNumber(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Card Number not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_cardNumber(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "card": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_cardNumber(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "card": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Card Number not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_missing_key_expiry(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_missing_key_expiry(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Expiry not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_failure_statusCode_incorrect_key_expiry(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expired": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "FAILURE"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_failure_statusMessage_incorrect_key_expiry(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expired": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Expiry not provided in request JSON"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_success_statusCode(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "SUCCESS"
        self.assertEqual(response.get("status").get("statusCode"), expected)

    def test_success_statusMessage(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "Bundle sold successfully"
        self.assertEqual(response.get("status").get("statusMessage"), expected)

    def test_success_response_key_bundleAddress_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("bundleAddress" in response.get("bundle").keys())

    def test_success_response_key_customerID_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("customerID" in response.get("bundle").keys())

    def test_success_response_key_customerID_correct(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "1WNJKpBpYfWwKIlvbaz0"
        self.assertEqual(response.get("bundle").get("customerID"),
                         expected)

    def test_success_response_key_bundleID_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("bundleID" in response.get("bundle").keys())

    def test_success_response_key_bundleID_correct(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "1"
        self.assertEqual(response.get("bundle").get("bundleID"),
                         expected)

    def test_success_response_key_status_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("status" in response.get("bundle").keys())

    def test_success_response_key_status_correct(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "INACTIVE"
        self.assertEqual(response.get("bundle").get("status"),
                         expected)

    def test_success_response_key_purchaseDatetime_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("purchaseDatetime" in response.get("bundle").keys())

    def test_success_response_key_holdingPeriod_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("holdingPeriod" in response.get("bundle").keys())

    def test_success_response_key_holdingPeriod_correct(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = 18
        self.assertEqual(response.get("bundle").get("holdingPeriod"),
                         expected)

    def test_success_response_key_transactionID_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("transactionID" in response.get("bundleTransaction").keys())

    def test_success_response_key_transactionDatetime_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("transactionDatetime" in response.get("bundleTransaction").keys())

    def test_success_response_key_chargeApplied_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("chargeApplied" in response.get("bundleTransaction").keys())


    def test_success_response_key_chargeApplied_correct(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = 100.0
        self.assertEqual(response.get("bundleTransaction")
                         .get("chargeApplied"),
                         expected)

    def test_success_response_key_amount_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("amount" in response.get("bundleTransaction").keys())


    def test_success_response_key_amount_correct(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = 1000.00
        self.assertEqual(response.get("bundleTransaction")
                         .get("amount"),
                         expected)

    def test_success_response_key_action_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("action" in response.get("bundleTransaction").keys())


    def test_success_response_key_action_correct(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "SELL"
        self.assertEqual(response.get("bundleTransaction")
                         .get("action"),
                         expected)

    def test_success_response_key_cardNumber_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("cardNumber" in response.get("bundleTransaction").keys())


    def test_success_response_key_cardNumber_correct_and_masked(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "************3456"
        self.assertEqual(response.get("bundleTransaction")
                         .get("cardNumber"),
                         expected)

    def test_success_response_key_expiry_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("expiry" in response.get("bundleTransaction").keys())


    def test_success_response_key_expiry_correct_and_masked(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = "**/24"
        self.assertEqual(response.get("bundleTransaction")
                         .get("expiry"),
                         expected)

    def test_success_response_key_initialRate_exists(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        self.assertTrue("initialRate" in response.get("bundleTransaction").keys())


    def test_success_response_key_initialRate_correct(self):
        reqData = {
            "bundleAddress": "CiHp30zstnE1ufu7M8P5",
            "customerID": "1WNJKpBpYfWwKIlvbaz0",
            "bundleID": "1",
            "initialRate": 22000.00,
            "amount": 1000.00,
            "cardNumber": "1234567890123456",
            "expiry": "12/24"
        }
        response = self.BController.sellBundle(reqData)
        expected = 22000.00
        self.assertEqual(response.get("bundleTransaction")
                         .get("initialRate"),
                         expected)


if __name__ == '__main__':
    unittest.main()
