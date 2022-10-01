import unittest
from models.Bundle import Bundle
from models.Utility import Utility


class TestBundleAddress(unittest.TestCase):

    def setUp(self):
        self.newBundle = Bundle()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newBundle.getBundleAddress())

    def test_must_not_be_none_when_set(self):
        self.newBundle.setBundleAddress("randomstringoftwenty")
        self.assertIsNotNone(self.newBundle.getBundleAddress())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleAddress(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleAddress(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleAddress(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleAddress(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleAddress(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleAddress(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleAddress(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleAddress(False)

    def test_must_be_string(self):
        self.newBundle.setBundleAddress("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newBundle.getBundleAddress(), str)

    def test_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newBundle.setBundleAddress("r")

    def test_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newBundle.setBundleAddress("rjidsfou32r3ij98")

    def test_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newBundle.setBundleAddress("rjidsfou32r3ij98ou32r3ij98")

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newBundle.setBundleAddress("")

    def test_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newBundle.setBundleAddress(Utility.generateRandomID())
        self.assertIsNotNone(self.newBundle.getBundleAddress())

    def test_must_not_be_an_empty_string(self):
        self.newBundle.setBundleAddress(Utility.generateRandomID())
        self.assertTrue(self.newBundle.getBundleAddress())

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newBundle = Bundle("9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newBundle.getBundleAddress(), "9jDo34hLdfJdsRdsFN29")


class TestBundleID(unittest.TestCase):

    def setUp(self):
        self.newBundle = Bundle()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newBundle.getBundleID())

    def test_must_not_be_none_when_set(self):
        self.newBundle.setBundleID("randomstringoftwenty")
        self.assertIsNotNone(self.newBundle.getBundleID())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleID(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleID(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleID(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleID(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleID(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleID(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleID(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setBundleID(False)

    def test_must_be_string(self):
        self.newBundle.setBundleID("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newBundle.getBundleID(), str)

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newBundle.setBundleID("")

    def test_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newBundle.setBundleID(Utility.generateRandomID())
        self.assertIsNotNone(self.newBundle.getBundleID())

    def test_must_not_be_an_empty_string(self):
        self.newBundle.setBundleID(Utility.generateRandomID())
        self.assertTrue(self.newBundle.getBundleID())

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newBundle = Bundle(bundleID="9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newBundle.getBundleID(), "9jDo34hLdfJdsRdsFN29")


class TestCustomerID(unittest.TestCase):

    def setUp(self):
        self.newBundle = Bundle()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newBundle.getCustomerID())

    def test_must_not_be_none_when_set(self):
        self.newBundle.setCustomerID("randomstringoftwenty")
        self.assertIsNotNone(self.newBundle.getCustomerID())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newBundle.setCustomerID(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newBundle.setCustomerID(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newBundle.setCustomerID(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newBundle.setCustomerID(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundle.setCustomerID(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundle.setCustomerID(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setCustomerID(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setCustomerID(False)

    def test_must_be_string(self):
        self.newBundle.setCustomerID("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newBundle.getCustomerID(), str)

    def test_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newBundle.setCustomerID("r")

    def test_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newBundle.setCustomerID("rjidsfou32r3ij98")

    def test_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newBundle.setCustomerID("rjidsfou32r3ij98ou32r3ij98")

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newBundle.setCustomerID("")

    def test_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newBundle.setCustomerID(Utility.generateRandomID())
        self.assertIsNotNone(self.newBundle.getCustomerID())

    def test_must_not_be_an_empty_string(self):
        self.newBundle.setCustomerID(Utility.generateRandomID())
        self.assertTrue(self.newBundle.getCustomerID())

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newBundle = Bundle(customerID="9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newBundle.getCustomerID(), "9jDo34hLdfJdsRdsFN29")


class TestAmount(unittest.TestCase):

    def setUp(self):
        self.newBundle = Bundle()

    def tearDown(self):
        pass

    def test_must_throw_error_when_none(self):
        with self.assertRaises(ValueError):
            self.newBundle.setAmount(None)

    def test_must_not_be_none_when_set(self):
        self.newBundle.setAmount(5.0)
        self.assertIsNotNone(self.newBundle.getAmount())

    def test_must_not_be_str(self):
        with self.assertRaises(TypeError):
            self.newBundle.setAmount("12345678901234567890")

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newBundle.setAmount(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newBundle.setAmount(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(ValueError):
            self.newBundle.setAmount(-0.01)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(ValueError):
            self.newBundle.setAmount(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setAmount(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setAmount(False)

    def test_must_raise_an_error_for_int_argument(self):
        with self.assertRaises(TypeError):
            self.newBundle.setAmount(1)

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newBundle = Bundle(amount=5)
        self.assertEqual(self.newBundle.getAmount(), 5)


class TestHoldingPeriod(unittest.TestCase):

    def setUp(self):
        self.newBundle = Bundle()

    def tearDown(self):
        pass

    def test_must_throw_error_when_none(self):
        with self.assertRaises(TypeError):
            self.newBundle.setHoldingPeriod(None)

    def test_must_not_be_none_when_set(self):
        self.newBundle.setHoldingPeriod(5)
        self.assertIsNotNone(self.newBundle.getHoldingPeriod())

    def test_must_not_be_str(self):
        with self.assertRaises(TypeError):
            self.newBundle.setHoldingPeriod("12345678901234567890")

    def test_must_not_be_zero(self):
        with self.assertRaises(ValueError):
            self.newBundle.setHoldingPeriod(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(ValueError):
            self.newBundle.setHoldingPeriod(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newBundle.setHoldingPeriod(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundle.setHoldingPeriod(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundle.setHoldingPeriod(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setHoldingPeriod(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setHoldingPeriod(False)

    def test_must_be_int(self):
        self.newBundle.setHoldingPeriod(1)
        self.assertIsInstance(self.newBundle.getHoldingPeriod(), int)

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        self.newBundle = Bundle(holdingPeriod=5)
        self.assertEqual(self.newBundle.getHoldingPeriod(), 5)


class TestPurchaseDatetime(unittest.TestCase):

    def setUp(self):
        self.newBundle = Bundle()

    def tearDown(self):
        pass

    def test_must_be_none_if_not_set(self):
        self.assertIsNone(self.newBundle.getPurchaseDatetime())

    def test_must_throw_error_for_none_argument(self):
        with self.assertRaises(TypeError):
            self.newBundle.setPurchaseDatetime(None)

    def test_must_throw_error_for_a_string_argument(self):
        with self.assertRaises(TypeError):
            self.newBundle.setPurchaseDatetime("1232434334.3843943")

    def test_must_throw_error_for_false_boolean_argument(self):
        with self.assertRaises(TypeError):
            self.newBundle.setPurchaseDatetime(False)

    def test_must_throw_error_for_true_boolean_argument(self):
        with self.assertRaises(TypeError):
            self.newBundle.setPurchaseDatetime(True)

    def test_must_return_a_int(self):
        self.newBundle.setPurchaseDatetime(632432525)
        self.assertIsInstance(self.newBundle.getPurchaseDatetime(), int)


class TestStatus(unittest.TestCase):

    def setUp(self):
        self.newBundle = Bundle()

    def tearDown(self):
        pass

    def test_must_not_be_none_if_not_set(self):
        self.assertIsNone(self.newBundle.getStatus())

    def test_must_not_be_none_when_set(self):
        self.newBundle.setStatus("active")
        self.assertIsNotNone(self.newBundle.getStatus())

    def test_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newBundle.setStatus(12345678901234567890)

    def test_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newBundle.setStatus(0)

    def test_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newBundle.setStatus(-1)

    def test_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newBundle.setStatus(-0.01)

    def test_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundle.setStatus(1.00)

    def test_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newBundle.setStatus(-1.00)

    def test_must_not_be_a_true_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setStatus(True)

    def test_must_not_be_a_false_bool(self):
        with self.assertRaises(TypeError):
            self.newBundle.setStatus(False)

    def test_must_be_string(self):
        self.newBundle.setStatus("inactive")
        self.assertIsInstance(self.newBundle.getStatus(), str)

    def test_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newBundle.setStatus("")

    def test_must_be_set_correctly_at_initilization_when_provided(self):
        with self.assertRaises(ValueError):
            self.newBundle.setStatus("9jDo34hLdfJdsRdsFN29")

    def test_must_not_be_an_empty_string(self):
        with self.assertRaises(ValueError):
            self.newBundle.setStatus("")
    def test_must_be_set_as_upper_case_for_active_status(self):
        self.newBundle.setStatus("active")
        self.assertEqual(self.newBundle.getStatus(), "ACTIVE")

    def test_must_be_set_as_upper_case_for_inactive_status(self):
        self.newBundle.setStatus("inactive")
        self.assertEqual(self.newBundle.getStatus(), "INACTIVE")

    def test_must_not_be_set_as_lower_case_for_active_status(self):
        self.newBundle.setStatus("active")
        self.assertNotEqual(self.newBundle.getStatus(), "active")

    def test_must_not_be_set_as_lower_case_for_inactive_status(self):
        self.newBundle.setStatus("inactive")
        self.assertNotEqual(self.newBundle.getStatus(), "inactive")


if __name__ == '__main__':
    unittest.main()
