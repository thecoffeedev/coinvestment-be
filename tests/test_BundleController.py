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



class TestGetAllWalletDetailsFromWalletAddress(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.bController = BundleController(app)
        self.BDA = BundleDataAccess(app)

    def tearDown(self):
        self.BDA.testDropTables()


if __name__ == '__main__':
    unittest.main()
