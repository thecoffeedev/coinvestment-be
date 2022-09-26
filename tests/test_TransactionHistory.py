import unittest
from models.TransactionHistory import TransactionHistory
from models.Utility import Utility


class TestTransactionID(unittest.TestCase):

    def setUp(self):
        self.newTransactionHistory = TransactionHistory()

    def tearDown(self):
        pass

    def test_transactionID_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newTransactionHistory.getTransactionID())

    def test_transactionID_must_not_be_none_when_set(self):
        self.newTransactionHistory.setTransactionID("randomstringoftwenty")
        self.assertIsNotNone(self.newTransactionHistory.getTransactionID())

    def test_transactionID_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionID(12345678901234567890)

    def test_transactionID_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionID(0)

    def test_transactionID_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionID(-1)

    def test_transactionID_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionID(-0.01)

    def test_transactionID_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionID(1.00)

    def test_transactionID_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionID(-1.00)

    def test_transactionID_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionID(True)

    def test_transactionID_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionID(False)

    def test_transactionID_must_be_string(self):
        self.newTransactionHistory.setTransactionID("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newTransactionHistory.getTransactionID(), str)

    def test_transactionID_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setTransactionID("r")

    def test_transactionID_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setTransactionID("rjidsfou32r3ij98")

    def test_transactionID_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setTransactionID("rjidsfou32r3ij98ou32r3ij98")

    def test_transactionID_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setTransactionID("")

    def test_transactionID_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newTransactionHistory.setTransactionID(Utility.generateRandomID())
        self.assertIsNotNone(self.newTransactionHistory.getTransactionID())

    def test_transactionID_must_not_be_an_empty_string(self):
        self.newTransactionHistory.setTransactionID(Utility.generateRandomID())
        self.assertTrue(self.newTransactionHistory.getTransactionID())

    def test_transactionID_must_be_set_correctly_at_initilization_when_provided(self):
        self.newTransactionHistory = TransactionHistory(transactionID="9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newTransactionHistory.getTransactionID(), "9jDo34hLdfJdsRdsFN29")


class TestTransactionDateTime(unittest.TestCase):

    def setUp(self):
        self.newTransactionHistory = TransactionHistory()

    def tearDown(self):
        pass

    def test_transactionDateTime_must_be_none_if_not_set(self):
        self.assertIsNone(self.newTransactionHistory.getTransactionDateTime())

    def test_transactionDateTime_must_not_accept_none_argument(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionDateTime(None)

    def test_transactionDateTime_must_not_be_a_string(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionDateTime("1232434334.3843943")

    def test_transactionDateTime_must_not_be_a_false_boolean(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionDateTime(False)

    def test_transactionDateTime_must_not_be_a_true_boolean(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setTransactionDateTime(True)

    def test_transactionDateTime_must_return_a_float(self):
        self.newTransactionHistory.setTransactionDateTime(632432525.232)
        self.assertIsInstance(self.newTransactionHistory.getTransactionDateTime(), float)


class TestChargeApplied(unittest.TestCase):

    def setUp(self):
        self.newTransactionHistory = TransactionHistory()

    def tearDown(self):
        pass

    def test_must_throw_error_when_none(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setChargeApplied(None)

    def test_must_not_be_none_when_set(self):
        self.newTransactionHistory.setChargeApplied(5.0)
        self.assertIsNotNone(self.newTransactionHistory.getChargeApplied())

    def test_must_not_be_str(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setChargeApplied("12345678901234567890")

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setChargeApplied(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setChargeApplied(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setChargeApplied(-0.01)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setChargeApplied(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setChargeApplied(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setChargeApplied(False)

    def test_must_raise_an_error_for_int_argument(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setChargeApplied(1)

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newTransactionHistory = TransactionHistory(chargeApplied=5)
        self.assertEqual(self.newTransactionHistory.getChargeApplied(), 5)


class TestAmount(unittest.TestCase):

    def setUp(self):
        self.newTransactionHistory = TransactionHistory()

    def tearDown(self):
        pass

    def test_must_throw_error_when_none(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setAmount(None)

    def test_must_not_be_none_when_set(self):
        self.newTransactionHistory.setAmount(5.0)
        self.assertIsNotNone(self.newTransactionHistory.getAmount())

    def test_must_not_be_str(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAmount("12345678901234567890")

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAmount(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAmount(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setAmount(-0.01)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setAmount(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAmount(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAmount(False)

    def test_must_raise_an_error_for_int_argument(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAmount(1)

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newTransactionHistory = TransactionHistory(amount=5)
        self.assertEqual(self.newTransactionHistory.getAmount(), 5)


class TestAction(unittest.TestCase):

    def setUp(self):
        self.newTransactionHistory = TransactionHistory()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newTransactionHistory.getAction())

    def test_must_not_be_none_when_set(self):
        self.newTransactionHistory.setAction("buy")
        self.assertIsNotNone(self.newTransactionHistory.getAction())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAction(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAction(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAction(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAction(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAction(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAction(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAction(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setAction(False)

    def test_must_be_string(self):
        self.newTransactionHistory.setAction("sell")
        self.assertIsInstance(self.newTransactionHistory.getAction(), str)

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setAction("")

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setAction("9jDo34hLdfJdsRdsFN29")

    def test_must_not_be_an_empty_string(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setAction("")

    def test_must_be_set_as_upper_case_for_active_status(self):
        self.newTransactionHistory.setAction("buy")
        self.assertEqual(self.newTransactionHistory.getAction(), "BUY")

    def test_must_be_set_as_upper_case_for_inactive_status(self):
        self.newTransactionHistory.setAction("sell")
        self.assertEqual(self.newTransactionHistory.getAction(), "SELL")

    def test_must_not_be_set_as_lower_case_for_active_status(self):
        self.newTransactionHistory.setAction("buy")
        self.assertNotEqual(self.newTransactionHistory.getAction(), "buy")

    def test_must_not_be_set_as_lower_case_for_inactive_status(self):
        self.newTransactionHistory.setAction("sell")
        self.assertNotEqual(self.newTransactionHistory.getAction(), "sell")
    

class TestCardNumber(unittest.TestCase):

    def setUp(self):
        self.newTransactionHistory = TransactionHistory()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newTransactionHistory.getCardNumber())

    def test_must_not_be_only_spaces(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setCardNumber(" ")

    def test_must_not_be_none_when_set(self):
        self.newTransactionHistory.setCardNumber("4637281746372834")
        self.assertIsNotNone(self.newTransactionHistory.getCardNumber())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setCardNumber(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setCardNumber(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setCardNumber(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setCardNumber(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setCardNumber(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setCardNumber(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setCardNumber(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setCardNumber(False)

    def test_must_be_string(self):
        self.newTransactionHistory.setCardNumber("4637281746372834")
        self.assertIsInstance(self.newTransactionHistory.getCardNumber(), str)

    def test_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setCardNumber("r")

    def test_must_throw_error_when_less_than_sixteen_characters(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setCardNumber("463728174637")

    def test_must_throw_error_when_more_than_sixteen_characters(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setCardNumber("4637281746372834213")

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setCardNumber("")

    def test_must_be_equal_to_the_set_numeric_value(self):
        self.newTransactionHistory = TransactionHistory(cardNumber="4637281746372834")
        self.assertEqual(self.newTransactionHistory.getCardNumber(), "4637281746372834")

    def test_must_throw_error_when_alphanumeric_value(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setCardNumber("ehdgs83726hyr625")


class TestExpiry(unittest.TestCase):

    def setUp(self):
        self.newTransactionHistory = TransactionHistory()

    def tearDown(self):
        pass

    def test_transactionID_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newTransactionHistory.getExpiry())

    def test_transactionID_must_not_be_none_when_set(self):
        self.newTransactionHistory.setExpiry("07/23")
        self.assertIsNotNone(self.newTransactionHistory.getExpiry())

    def test_transactionID_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setExpiry(12345)

    def test_transactionID_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setExpiry(0)

    def test_transactionID_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setExpiry(-1)

    def test_transactionID_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setExpiry(-0.01)

    def test_transactionID_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setExpiry(1.00)

    def test_transactionID_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setExpiry(-1.00)

    def test_transactionID_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setExpiry(True)

    def test_transactionID_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newTransactionHistory.setExpiry(False)

    def test_transactionID_must_be_string(self):
        self.newTransactionHistory.setExpiry("07/23")
        self.assertIsInstance(self.newTransactionHistory.getExpiry(), str)

    def test_transactionID_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setExpiry("r")

    def test_transactionID_must_throw_error_when_less_than_five_characters(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setExpiry("07/2")

    def test_transactionID_must_throw_error_when_more_than_five_characters(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setExpiry("07/232")

    def test_transactionID_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newTransactionHistory.setExpiry("")

    def test_transactionID_must_be_set_correctly_at_initilization_when_provided(self):
        self.newTransactionHistory = TransactionHistory(expiry="07/23")
        self.assertEqual(self.newTransactionHistory.getExpiry(), "07/23")
