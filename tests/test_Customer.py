import unittest
from models.Customer import Customer
from models.Utility import Utility


class TestCustomerID(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_customerID_must_not_be_none_if_not_set(self):
        self.newUser = Customer()
        self.assertIsNone(self.newUser.getCustomerID())

    def test_customerID_must_not_be_none_when_set(self):
        self.newUser = Customer()
        self.newUser.setCustomerID("randomstringoftwenty")
        self.assertIsNotNone(self.newUser.getCustomerID())

    def test_customerID_must_not_be_int(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(12345678901234567890)

    def test_customerID_must_not_be_zero(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(0)

    def test_customerID_must_not_be_a_negative_int(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-1)

    def test_customerID_must_not_be_a_negative_float(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-0.01)

    def test_customerID_must_not_be_a_positive_float_whole_number(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(1.00)

    def test_customerID_must_not_be_a_negative_float_whole_number(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-1.00)

    def test_customerID_must_not_be_a_true_bool(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(True)

    def test_customerID_must_not_be_a_false_bool(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(False)

    def test_customerID_must_be_string(self):
        self.newUser = Customer()
        self.newUser.setCustomerID("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newUser.getCustomerID(), str)

    def test_customerID_must_throw_error_when_one_character(self):
        self.newUser = Customer()
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("r")
    def test_customerID_must_throw_error_when_less_than_twenty_characters(self):
        self.newUser = Customer()
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("rjidsfou32r3ij98")

    def test_customerID_must_throw_error_when_more_than_twenty_characters(self):
        self.newUser = Customer()
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("rjidsfou32r3ij98ou32r3ij98")

    def test_customerID_must_throw_error_when_zero_characters(self):
        self.newUser = Customer()
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("")

    def test_customerID_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newUser = Customer()
        self.newUser.setCustomerID(Utility.generateNewCustomerID())
        self.assertIsNotNone(self.newUser.getCustomerID())

    def test_customerID_must_not_be_an_empty_string(self):
        self.newUser = Customer()
        self.newUser.setCustomerID(Utility.generateNewCustomerID())
        self.assertTrue(self.newUser.getCustomerID())

    def test_customerID_must_be_set_correctly_at_initilization_when_provided(self):
        self.newUser = Customer("9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newUser.getCustomerID(), "9jDo34hLdfJdsRdsFN29")


class TestPasswordHash(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_passwordHash_must_not_be_none(self):
        self.newUser = Customer()
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash(None)

    def test_passwordHash_must_not_be_true_bool(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(True)

    def test_password_must_not_be_false_bool(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(False)

    def test_passwordHash_must_not_be_int(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(123)

    def test_passwordHash_must_not_be_zero(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(0)

    def test_passwordHash_must_not_be_a_negative_int(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(-1)

    def test_passwordHash_must_not_be_a_negative_float(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-0.01)

    def test_passwordHash_must_not_be_a_positive_float_whole_number(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(1.00)

    def test_passwordHash_must_not_be_a_negative_float_whole_number(self):
        self.newUser = Customer()
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(-1.00)

    def test_passwordHash_must_throw_error_when_one_character(self):
        self.newUser = Customer()
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash("r")
    def test_passwordHash_must_throw_error_when_less_than_sixty_characters(self):
        self.newUser = Customer()
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash("rjidsfou32r3ij98")

    def test_passwordHash_must_throw_error_when_more_than_sixty_characters(self):
        self.newUser = Customer()
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash("rjidsfou32r3ij98ou32r3ij98")

    def test_passwordHash_must_throw_error_when_zero_characters(self):
        self.newUser = Customer()
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash("")


class TestRegisterDatetime(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_registerDatetime_must_not_be_none(self):
        self.newUser = Customer()
        with self.assertRaises(ValueError):
            self.newUser.setRegisterDatetime(None)



if __name__ == '__main__':
    unittest.main()
