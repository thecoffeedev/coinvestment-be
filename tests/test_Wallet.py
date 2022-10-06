import unittest
from models.Wallet import Wallet
from models.Utility import Utility

class TestWalletAddress(unittest.TestCase):

    def setUp(self):
        self.newWallet = Wallet()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newWallet.getWalletAddress())

    def test_must_not_be_none_when_set(self):
        self.newWallet.setWalletAddress("randomstringoftwenty")
        self.assertIsNotNone(self.newWallet.getWalletAddress())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newWallet.setWalletAddress(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newWallet.setWalletAddress(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newWallet.setWalletAddress(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newWallet.setWalletAddress(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newWallet.setWalletAddress(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newWallet.setWalletAddress(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newWallet.setWalletAddress(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newWallet.setWalletAddress(False)

    def test_must_be_string(self):
        self.newWallet.setWalletAddress("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newWallet.getWalletAddress(), str)

    def test_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newWallet.setWalletAddress("r")

    def test_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newWallet.setWalletAddress("rjidsfou32r3ij98")

    def test_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newWallet.setWalletAddress("rjidsfou32r3ij98ou32r3ij98")

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newWallet.setWalletAddress("")

    def test_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newWallet.setWalletAddress(Utility.generateRandomID())
        self.assertIsNotNone(self.newWallet.getWalletAddress())

    def test_must_not_be_an_empty_string(self):
        self.newWallet.setWalletAddress(Utility.generateRandomID())
        self.assertTrue(self.newWallet.getWalletAddress())

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newWallet = Wallet("9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newWallet.getWalletAddress(), "9jDo34hLdfJdsRdsFN29")

class TestCustomerID(unittest.TestCase):

    def setUp(self):
        self.newWallet = Wallet()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newWallet.getCustomerID())

    def test_must_not_be_none_when_set(self):
        self.newWallet.setCustomerID("randomstringoftwenty")
        self.assertIsNotNone(self.newWallet.getCustomerID())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCustomerID(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCustomerID(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCustomerID(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCustomerID(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCustomerID(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCustomerID(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCustomerID(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCustomerID(False)

    def test_must_be_string(self):
        self.newWallet.setCustomerID("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newWallet.getCustomerID(), str)

    def test_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newWallet.setCustomerID("r")

    def test_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newWallet.setCustomerID("rjidsfou32r3ij98")

    def test_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newWallet.setCustomerID("rjidsfou32r3ij98ou32r3ij98")

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newWallet.setCustomerID("")

    def test_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newWallet.setCustomerID(Utility.generateRandomID())
        self.assertIsNotNone(self.newWallet.getCustomerID())

    def test_must_not_be_an_empty_string(self):
        self.newWallet.setCustomerID(Utility.generateRandomID())
        self.assertTrue(self.newWallet.getCustomerID())

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newWallet = Wallet(customerID="9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newWallet.getCustomerID(), "9jDo34hLdfJdsRdsFN29")

class TestInitialBalance(unittest.TestCase):

    def setUp(self):
        self.newWallet = Wallet()

    def tearDown(self):
        pass

    def test_initialBalance_must_throw_error_when_none(self):
        with self.assertRaises(ValueError):
            self.newWallet.setInitialBalance(None)

    def test_initialBalance_must_not_be_none_when_set(self):
        self.newWallet.setInitialBalance(5.0)
        self.assertIsNotNone(self.newWallet.getInitialBalance())

    def test_initialBalance_must_not_be_str(self):
        with self.assertRaises(TypeError):
            self.newWallet.setInitialBalance("12345678901234567890")

    def test_initialBalance_must_not_be_zero(self):
        with self.assertRaises(ValueError):
            self.newWallet.setInitialBalance(0.0)

    def test_initialBalance_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newWallet.setInitialBalance(-1)

    def test_initialBalance_must_not_be_a_negative_float(self):
        with self.assertRaises(ValueError):
            self.newWallet.setInitialBalance(-0.01)

    def test_initialBalance_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(ValueError):
            self.newWallet.setInitialBalance(-1.00)

    def test_initialBalance_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newWallet.setInitialBalance(True)

    def test_initialBalance_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newWallet.setInitialBalance(False)

    def test_initialBalance_must_be_float(self):
        self.newWallet.setInitialBalance(1.0)
        self.assertIsInstance(self.newWallet.getInitialBalance(), float)

    def test_InitialBalance_must_be_set_correctly_at_initilization_when_provided(self):
        self.newWallet = Wallet(initialBalance=5)
        self.assertEqual(self.newWallet.getInitialBalance(), 5)


class TestCurrentBalance(unittest.TestCase):

    def setUp(self):
        self.newWallet = Wallet()

    def tearDown(self):
        pass

    def test_currentBalance_must_throw_error_when_none(self):
        with self.assertRaises(ValueError):
            self.newWallet.setCurrentBalance(None)

    def test_currentBalance_must_not_be_none_when_set(self):
        self.newWallet.setCurrentBalance(5.0)
        self.assertIsNotNone(self.newWallet.getCurrentBalance())

    def test_currentBalance_must_not_be_str(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCurrentBalance("12345678901234567890")

    def test_currentBalance_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCurrentBalance(-1)

    def test_currentBalance_must_not_be_a_negative_float(self):
        with self.assertRaises(ValueError):
            self.newWallet.setCurrentBalance(-0.01)

    # def test_currentBalance_must_not_be_a_positive_float_whole_number(self):
    #     with self.assertRaises(TypeError):
    #         self.newWallet.setCurrentBalance(1.00)

    def test_currentBalance_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(ValueError):
            self.newWallet.setCurrentBalance(-1.00)

    def test_currentBalance_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCurrentBalance(True)

    def test_currentBalance_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCurrentBalance(False)

    def test_currentBalance_must_throw_an_error_for_int_argument(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCurrentBalance(8)

    def test_currentBalance_must_be_set_correctly_at_initilization_when_provided_zero(self):
        self.newWallet = Wallet(currentBalance=0.0)
        self.assertEqual(self.newWallet.getCurrentBalance(), 0.0)

    def test_currentBalance_must_be_set_correctly_at_initilization_when_provided(self):
        self.newWallet = Wallet(currentBalance=5.0)
        self.assertEqual(self.newWallet.getCurrentBalance(), 5.0)

class TestCryptocurrencyCode(unittest.TestCase):

    def setUp(self):
        self.newWallet = Wallet()

    def tearDown(self):
        pass

    def test_cryptocurrencyCode_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newWallet.getCryptocurrencyCode())

    def test_cryptocurrencyCode_must_not_be_only_spaces(self):
        with self.assertRaises(ValueError):
            self.newWallet.setCryptocurrencyCode(" ")

    def test_cryptocurrencyCode_must_not_be_none_when_set(self):
        self.newWallet.setCryptocurrencyCode("vbfhdyroeu")
        self.assertIsNotNone(self.newWallet.getCryptocurrencyCode())

    def test_cryptocurrencyCode_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCryptocurrencyCode(12345678901234567890)

    def test_cryptocurrencyCode_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCryptocurrencyCode(0)

    def test_cryptocurrencyCode_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCryptocurrencyCode(-1)

    def test_cryptocurrencyCode_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCryptocurrencyCode(-0.01)

    def test_cryptocurrencyCode_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCryptocurrencyCode(1.00)

    def test_cryptocurrencyCode_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCryptocurrencyCode(-1.00)

    def test_cryptocurrencyCode_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCryptocurrencyCode(True)

    def test_cryptocurrencyCode_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newWallet.setCryptocurrencyCode(False)

    def test_cryptocurrencyCode_must_be_string(self):
        self.newWallet.setCryptocurrencyCode("vbfhdyroeu")
        self.assertIsInstance(self.newWallet.getCryptocurrencyCode(), str)

    def test_cryptocurrencyCode_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newWallet.setCryptocurrencyCode("r")

    def test_cryptocurrencyCode_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newWallet.setCryptocurrencyCode("")

    def test_cryptocurrencyCode_must_be_equal_to_the_set_value(self):
        self.newWallet = Wallet(cryptocurrencyCode="vbfhdyroeu")
        self.assertEqual(self.newWallet.getCryptocurrencyCode(), "vbfhdyroeu")


class TestHoldingPeriod(unittest.TestCase):

    def setUp(self):
        self.newUser = Wallet()

    def tearDown(self):
        pass

    def test_must_throw_error_when_none(self):
        with self.assertRaises(ValueError):
            self.newUser.setHoldingPeriod(None)

    def test_must_not_be_none_when_set(self):
        self.newUser.setHoldingPeriod(5)
        self.assertIsNotNone(self.newUser.getHoldingPeriod())

    def test_must_not_be_str(self):
        with self.assertRaises(TypeError):
            self.newUser.setHoldingPeriod("12345678901234567890")

    def test_must_not_be_zero(self):
        with self.assertRaises(ValueError):
            self.newUser.setHoldingPeriod(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(ValueError):
            self.newUser.setHoldingPeriod(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setHoldingPeriod(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setHoldingPeriod(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setHoldingPeriod(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setHoldingPeriod(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setHoldingPeriod(False)

    def test_must_be_int(self):
        self.newUser.setHoldingPeriod(1)
        self.assertIsInstance(self.newUser.getHoldingPeriod(), int)

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newUser = Wallet(holdingPeriod=5)
        self.assertEqual(self.newUser.getHoldingPeriod(), 5)
