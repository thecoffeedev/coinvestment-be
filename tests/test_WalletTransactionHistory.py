import unittest
from models.WalletTransactionHistory import WalletTransactionHistory
from models.Utility import Utility


class TestWalletAddress(unittest.TestCase):

    def setUp(self):
        self.newWalletTransactionHistory = WalletTransactionHistory()

    def tearDown(self):
        pass

    def test_walletAddress_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newWalletTransactionHistory.getWalletAddress())

    def test_walletAddress_must_not_be_none_when_set(self):
        self.newWalletTransactionHistory.setWalletAddress("randomstringoftwenty")
        self.assertIsNotNone(self.newWalletTransactionHistory.getWalletAddress())

    def test_walletAddress_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setWalletAddress(12345678901234567890)

    def test_walletAddress_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setWalletAddress(0)

    def test_walletAddress_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setWalletAddress(-1)

    def test_walletAddress_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setWalletAddress(-0.01)

    def test_walletAddress_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setWalletAddress(1.00)

    def test_walletAddress_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setWalletAddress(-1.00)

    def test_walletAddress_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setWalletAddress(True)

    def test_walletAddress_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setWalletAddress(False)

    def test_walletAddress_must_be_string(self):
        self.newWalletTransactionHistory.setWalletAddress("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newWalletTransactionHistory.getWalletAddress(), str)

    def test_walletAddress_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newWalletTransactionHistory.setWalletAddress("r")

    def test_walletAddress_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newWalletTransactionHistory.setWalletAddress("rjidsfou32r3ij98")

    def test_walletAddress_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newWalletTransactionHistory.setWalletAddress("rjidsfou32r3ij98ou32r3ij98")

    def test_walletAddress_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newWalletTransactionHistory.setWalletAddress("")

    def test_walletAddress_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newWalletTransactionHistory.setWalletAddress(Utility.generateRandomID())
        self.assertIsNotNone(self.newWalletTransactionHistory.getWalletAddress())

    def test_walletAddress_must_not_be_an_empty_string(self):
        self.newWalletTransactionHistory.setWalletAddress(Utility.generateRandomID())
        self.assertTrue(self.newWalletTransactionHistory.getWalletAddress())

    def test_walletAddress_must_be_set_correctly_at_initilization_when_provided(self):
        self.newWalletTransactionHistory = WalletTransactionHistory(walletAddress="9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newWalletTransactionHistory.getWalletAddress(), "9jDo34hLdfJdsRdsFN29")


class TestUnitsSold(unittest.TestCase):

    def setUp(self):
        self.newWalletTransactionHistory = WalletTransactionHistory()

    def tearDown(self):
        pass

    def test_unitsSold_must_throw_error_when_none(self):
        with self.assertRaises(ValueError):
            self.newWalletTransactionHistory.setUnitsSold(None)

    def test_unitsSold_must_not_be_none_when_set(self):
        self.newWalletTransactionHistory.setUnitsSold(5.0)
        self.assertIsNotNone(self.newWalletTransactionHistory.getUnitsSold())

    def test_unitsSold_must_not_be_str(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setUnitsSold("12345678901234567890")

    def test_unitsSold_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setUnitsSold(-1)

    def test_unitsSold_must_not_be_a_negative_float(self):
        with self.assertRaises(ValueError):
            self.newWalletTransactionHistory.setUnitsSold(-0.01)

    def test_unitsSold_must_not_be_a_positive_int_number(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setUnitsSold(1)

    def test_unitsSold_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(ValueError):
            self.newWalletTransactionHistory.setUnitsSold(-1.00)

    def test_unitsSold_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setUnitsSold(True)

    def test_unitsSold_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newWalletTransactionHistory.setUnitsSold(False)

    def test_unitsSold_must_be_float(self):
        self.newWalletTransactionHistory.setUnitsSold(1.0)
        self.assertIsInstance(self.newWalletTransactionHistory.getUnitsSold(), float)

    def test_unitsSold_must_be_set_correctly_at_initilization_when_provided_zero(self):
        self.newWalletTransactionHistory = WalletTransactionHistory(unitsSold=0.0)
        self.assertEqual(self.newWalletTransactionHistory.getUnitsSold(), 0.0)

    def test_unitsSold_must_be_set_correctly_at_initilization_when_provided(self):
        self.newWalletTransactionHistory = WalletTransactionHistory(unitsSold=5.0)
        self.assertEqual(self.newWalletTransactionHistory.getUnitsSold(), 5.0)