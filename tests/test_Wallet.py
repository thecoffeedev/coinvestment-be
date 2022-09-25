import unittest
from models.Wallet import Wallet
from models.Utility import Utility

class TestWalletAddress(unittest.TestCase):

    def setUp(self):
        self.newUser = Wallet()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newUser.getWalletAddress())

    def test_must_not_be_none_when_set(self):
        self.newUser.setWalletAddress("randomstringoftwenty")
        self.assertIsNotNone(self.newUser.getWalletAddress())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setWalletAddress(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newUser.setWalletAddress(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setWalletAddress(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setWalletAddress(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setWalletAddress(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setWalletAddress(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setWalletAddress(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setWalletAddress(False)

    def test_must_be_string(self):
        self.newUser.setWalletAddress("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newUser.getWalletAddress(), str)

    def test_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newUser.setWalletAddress("r")

    def test_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setWalletAddress("rjidsfou32r3ij98")

    def test_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setWalletAddress("rjidsfou32r3ij98ou32r3ij98")

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setWalletAddress("")

    def test_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newUser.setWalletAddress(Utility.generateRandomID())
        self.assertIsNotNone(self.newUser.getWalletAddress())

    def test_must_not_be_an_empty_string(self):
        self.newUser.setWalletAddress(Utility.generateRandomID())
        self.assertTrue(self.newUser.getWalletAddress())

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newUser = Wallet("9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newUser.getWalletAddress(), "9jDo34hLdfJdsRdsFN29")

class TestCustomerID(unittest.TestCase):

    def setUp(self):
        self.newUser = Wallet()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newUser.getCustomerID())

    def test_must_not_be_none_when_set(self):
        self.newUser.setCustomerID("randomstringoftwenty")
        self.assertIsNotNone(self.newUser.getCustomerID())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(False)

    def test_must_be_string(self):
        self.newUser.setCustomerID("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newUser.getCustomerID(), str)

    def test_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("r")

    def test_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("rjidsfou32r3ij98")

    def test_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("rjidsfou32r3ij98ou32r3ij98")

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("")

    def test_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newUser.setCustomerID(Utility.generateNewCustomerID())
        self.assertIsNotNone(self.newUser.getCustomerID())

    def test_must_not_be_an_empty_string(self):
        self.newUser.setCustomerID(Utility.generateNewCustomerID())
        self.assertTrue(self.newUser.getCustomerID())

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newUser = Wallet(customerID="9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newUser.getCustomerID(), "9jDo34hLdfJdsRdsFN29")

class TestInitialBalance(unittest.TestCase):

    def setUp(self):
        self.newUser = Wallet()

    def tearDown(self):
        pass

    def test_initialBalance_must_throw_error_when_none(self):
        with self.assertRaises(ValueError):
            self.newUser.setInitialBalance(None)

    def test_initialBalance_must_not_be_none_when_set(self):
        self.newUser.setInitialBalance(5)
        self.assertIsNotNone(self.newUser.getInitialBalance())

    def test_initialBalance_must_not_be_str(self):
        with self.assertRaises(TypeError):
            self.newUser.setInitialBalance("12345678901234567890")

    def test_initialBalance_must_not_be_zero(self):
        with self.assertRaises(ValueError):
            self.newUser.setInitialBalance(0)

    def test_initialBalance_must_not_be_a_negative_int(self):
        with self.assertRaises(ValueError):
            self.newUser.setInitialBalance(-1)

    def test_initialBalance_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setInitialBalance(-0.01)

    def test_initialBalance_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setInitialBalance(1.00)

    def test_initialBalance_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setInitialBalance(-1.00)

    def test_initialBalance_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setInitialBalance(True)

    def test_initialBalance_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setInitialBalance(False)

    def test_initialBalance_must_be_int(self):
        self.newUser.setInitialBalance(1)
        self.assertIsInstance(self.newUser.getInitialBalance(), int)

    def test_InitialBalance_must_be_set_correctly_at_initilization_when_provided(self):
        self.newUser = Wallet(initialBalance=5)
        self.assertEqual(self.newUser.getInitialBalance(), 5)


class TestCurrentBalance(unittest.TestCase):

    def setUp(self):
        self.newUser = Wallet()

    def tearDown(self):
        pass

    def test_currentBalance_must_throw_error_when_none(self):
        with self.assertRaises(ValueError):
            self.newUser.setCurrentBalance(None)

    def test_currentBalance_must_not_be_none_when_set(self):
        self.newUser.setCurrentBalance(5)
        self.assertIsNotNone(self.newUser.getCurrentBalance())

    def test_currentBalance_must_not_be_str(self):
        with self.assertRaises(TypeError):
            self.newUser.setCurrentBalance("12345678901234567890")

    def test_currentBalance_must_not_be_a_negative_int(self):
        with self.assertRaises(ValueError):
            self.newUser.setCurrentBalance(-1)

    def test_currentBalance_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setCurrentBalance(-0.01)

    def test_currentBalance_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setCurrentBalance(1.00)

    def test_currentBalance_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setCurrentBalance(-1.00)

    def test_currentBalance_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setCurrentBalance(True)

    def test_currentBalance_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setCurrentBalance(False)

    def test_currentBalance_must_be_int(self):
        self.newUser.setCurrentBalance(1)
        self.assertIsInstance(self.newUser.getCurrentBalance(), int)

    def test_currentBalance_must_be_set_correctly_at_initilization_when_provided_zero(self):
        self.newUser = Wallet(currentBalance=0)
        self.assertEqual(self.newUser.getCurrentBalance(), 0)

    def test_currentBalance_must_be_set_correctly_at_initilization_when_provided(self):
        self.newUser = Wallet(currentBalance=5)
        self.assertEqual(self.newUser.getCurrentBalance(), 5)

class TestCryptocurrencyCode(unittest.TestCase):

    def setUp(self):
        self.newUser = Wallet()

    def tearDown(self):
        pass

    def test_cryptocurrencyCode_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newUser.getCryptocurrencyCode())

    def test_cryptocurrencyCode_must_not_be_only_spaces(self):
        with self.assertRaises(ValueError):
            self.newUser.setCryptocurrencyCode(" ")

    def test_cryptocurrencyCode_must_not_be_none_when_set(self):
        self.newUser.setCryptocurrencyCode("vbfhdyroeu")
        self.assertIsNotNone(self.newUser.getCryptocurrencyCode())

    def test_cryptocurrencyCode_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setCryptocurrencyCode(12345678901234567890)

    def test_cryptocurrencyCode_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newUser.setCryptocurrencyCode(0)

    def test_cryptocurrencyCode_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setCryptocurrencyCode(-1)

    def test_cryptocurrencyCode_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setCryptocurrencyCode(-0.01)

    def test_cryptocurrencyCode_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setCryptocurrencyCode(1.00)

    def test_cryptocurrencyCode_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setCryptocurrencyCode(-1.00)

    def test_cryptocurrencyCode_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setCryptocurrencyCode(True)

    def test_cryptocurrencyCode_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setCryptocurrencyCode(False)

    def test_cryptocurrencyCode_must_be_string(self):
        self.newUser.setCryptocurrencyCode("vbfhdyroeu")
        self.assertIsInstance(self.newUser.getCryptocurrencyCode(), str)

    def test_cryptocurrencyCode_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newUser.setCryptocurrencyCode("r")

    def test_cryptocurrencyCode_must_throw_error_when_less_than_ten_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCryptocurrencyCode("vbfhdyro")

    def test_cryptocurrencyCode_must_throw_error_when_more_than_ten_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCryptocurrencyCode("vbfhdyroeuvnbejkr")

    def test_cryptocurrencyCode_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCryptocurrencyCode("")

    def test_cryptocurrencyCode_must_be_equal_to_the_set_value(self):
        self.newUser = Wallet(cryptocurrencyCode="vbfhdyroeu")
        self.assertEqual(self.newUser.getCryptocurrencyCode(), "vbfhdyroeu")

class TestCustomerID(unittest.TestCase):

    def setUp(self):
        self.newUser = Wallet()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newUser.getCustomerID())

    def test_must_not_be_none_when_set(self):
        self.newUser.setCustomerID("randomstringoftwenty")
        self.assertIsNotNone(self.newUser.getCustomerID())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(False)

    def test_must_be_string(self):
        self.newUser.setCustomerID("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newUser.getCustomerID(), str)

    def test_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("r")

    def test_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("rjidsfou32r3ij98")

    def test_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("rjidsfou32r3ij98ou32r3ij98")

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("")

    def test_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newUser.setCustomerID(Utility.generateRandomID())
        self.assertIsNotNone(self.newUser.getCustomerID())

    def test_must_not_be_an_empty_string(self):
        self.newUser.setCustomerID(Utility.generateRandomID())
        self.assertTrue(self.newUser.getCustomerID())

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newUser = Wallet(customerID="9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newUser.getCustomerID(), "9jDo34hLdfJdsRdsFN29")


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
