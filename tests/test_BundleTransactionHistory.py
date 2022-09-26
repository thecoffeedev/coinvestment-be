import unittest
from models.BundleTransactionHistory import BundleTransactionHistory
from models.Utility import Utility


class TestBundleAddress(unittest.TestCase):

    def setUp(self):
        self.newBundleTransactionHistory = BundleTransactionHistory()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newBundleTransactionHistory.getBundleAddress())

    def test_must_not_be_none_when_set(self):
        self.newBundleTransactionHistory.setBundleAddress("randomstringoftwenty")
        self.assertIsNotNone(self.newBundleTransactionHistory.getBundleAddress())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newBundleTransactionHistory.setBundleAddress(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newBundleTransactionHistory.setBundleAddress(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newBundleTransactionHistory.setBundleAddress(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newBundleTransactionHistory.setBundleAddress(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundleTransactionHistory.setBundleAddress(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundleTransactionHistory.setBundleAddress(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newBundleTransactionHistory.setBundleAddress(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newBundleTransactionHistory.setBundleAddress(False)

    def test_must_be_string(self):
        self.newBundleTransactionHistory.setBundleAddress("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newBundleTransactionHistory.getBundleAddress(), str)

    def test_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newBundleTransactionHistory.setBundleAddress("r")

    def test_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newBundleTransactionHistory.setBundleAddress("rjidsfou32r3ij98")

    def test_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newBundleTransactionHistory.setBundleAddress("rjidsfou32r3ij98ou32r3ij98")

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newBundleTransactionHistory.setBundleAddress("")

    def test_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newBundleTransactionHistory.setBundleAddress(Utility.generateRandomID())
        self.assertIsNotNone(self.newBundleTransactionHistory.getBundleAddress())

    def test_must_not_be_an_empty_string(self):
        self.newBundleTransactionHistory.setBundleAddress(Utility.generateRandomID())
        self.assertTrue(self.newBundleTransactionHistory.getBundleAddress())

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newBundleTransactionHistory = BundleTransactionHistory(bundleAddress="9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newBundleTransactionHistory.getBundleAddress(), "9jDo34hLdfJdsRdsFN29")