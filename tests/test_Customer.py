import unittest
from models.Customer import Customer
from models.Utility import Utility


class TestCustomerID(unittest.TestCase):

    def setUp(self):
        self.newUser = Customer()

    def tearDown(self):
        pass

    def test_customerID_must_be_none_if_not_assigned(self):
        self.assertIsNone(self.newUser.getCustomerID())

    def test_customerID_must_not_be_none_when_assigned(self):
        self.newUser.setCustomerID("randomstringoftwenty")
        self.assertIsNotNone(self.newUser.getCustomerID())

    def test_customerID_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(12345678901234567890)

    def test_customerID_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(0)

    def test_customerID_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-1)

    def test_customerID_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-0.01)

    def test_customerID_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(1.00)

    def test_customerID_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-1.00)

    def test_customerID_must_not_be_a_true_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(True)

    def test_customerID_must_not_be_a_false_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(False)

    def test_customerID_must_not_be_an_string_of_space(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID(" ")

    def test_customerID_must_not_be_an_string_of_multiple_space(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("      ")

    def test_customerID_must_be_string(self):
        self.newUser.setCustomerID("rjidsfou32r3ij98vslf")
        self.assertIsInstance(self.newUser.getCustomerID(), str)

    def test_customerID_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("r")

    def test_customerID_must_throw_error_when_less_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("rjidsfou32r3ij98")

    def test_customerID_must_throw_error_when_more_than_twenty_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("rjidsfou32r3ij98ou32r3ij98")

    def test_customerID_must_throw_error_when_zero_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setCustomerID("")

    def test_customerID_must_be_generated_when_not_set_or_provided_in_initilization(self):
        self.newUser.setCustomerID(Utility.generateRandomID())
        self.assertIsNotNone(self.newUser.getCustomerID())

    def test_customerID_must_not_be_an_empty_string(self):
        self.newUser.setCustomerID(Utility.generateRandomID())
        self.assertTrue(self.newUser.getCustomerID())

    def test_customerID_must_be_set_correctly_at_initilization_when_provided(self):
        self.newUser = Customer("9jDo34hLdfJdsRdsFN29")
        self.assertEqual(self.newUser.getCustomerID(), "9jDo34hLdfJdsRdsFN29")


class TestPasswordHash(unittest.TestCase):

    def setUp(self):
        self.newUser = Customer()

    def tearDown(self):
        pass

    def test_passwordHash_must_be_none_if_not_set(self):
        self.assertIsNone(self.newUser.getPasswordHash())

    def test_passwordHash_must_not_accept_none_argument(self):
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(None)

    def test_passwordHash_must_not_be_true_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(True)

    def test_password_must_not_be_false_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(False)

    def test_passwordHash_must_not_be_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(123)

    def test_passwordHash_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(0)

    def test_passwordHash_must_not_be_a_negative_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(-1)

    def test_passwordHash_must_not_be_a_negative_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setCustomerID(-0.01)

    def test_passwordHash_must_not_be_a_positive_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(1.00)

    def test_passwordHash_must_not_be_a_negative_float_whole_number(self):
        with self.assertRaises(TypeError):
            self.newUser.setPasswordHash(-1.00)

    def test_passwordHash_must_not_be_an_string_of_space(self):
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash(" ")

    def test_passwordHash_must_not_be_an_string_of_multiple_space(self):
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash("      ")

    def test_passwordHash_must_throw_error_when_one_character(self):
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash("r")
    def test_passwordHash_must_throw_error_when_less_than_sixty_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash("rjidsfou32r3ij98")

    def test_passwordHash_must_throw_error_when_more_than_sixty_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash("rjidsfou32r3ij98ou32r3ij98")

    def test_passwordHash_must_throw_error_when_empty_string(self):
        with self.assertRaises(ValueError):
            self.newUser.setPasswordHash("")


class TestRegisterDatetime(unittest.TestCase):

    def setUp(self):
        self.newUser = Customer()

    def tearDown(self):
        pass

    def test_registerDatetime_must_be_none_if_not_set(self):
        self.assertIsNone(self.newUser.getRegisterDatetime())

    def test_registerDatetime_must_not_accept_none_argument(self):
        with self.assertRaises(TypeError):
            self.newUser.setRegisterDatetime(None)

    def test_registerDatetime_must_not_be_a_string(self):
        with self.assertRaises(TypeError):
            self.newUser.setRegisterDatetime("1232434334.3843943")

    def test_registerDatetime_must_not_be_a_false_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setRegisterDatetime(False)

    def test_registerDatetime_must_not_be_a_true_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setRegisterDatetime(True)

    def test_registerDatetime_must_return_a_float(self):
        self.newUser.setRegisterDatetime(632432525.232)
        self.assertIsInstance(self.newUser.getRegisterDatetime(), float)


class TestEmailAddress(unittest.TestCase):

    def setUp(self):
        self.newUser = Customer()

    def tearDown(self):
        pass

    def test_email_address_must_be_none_if_not_set(self):
        self.assertIsNone(self.newUser.getEmailAddress())

    def test_email_address_must_not_accept_none_argument(self):
        with self.assertRaises(TypeError):
            self.newUser.setEmailAddress(None)

    def test_email_address_must_not_be_a_zero(self):
        with self.assertRaises(TypeError):
            self.newUser.setEmailAddress(0)

    def test_email_address_must_not_be_an_int(self):
        with self.assertRaises(TypeError):
            self.newUser.setEmailAddress(1)

    def test_email_address_must_not_be_a_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setEmailAddress(1.01)

    def test_email_address_must_not_be_an_string_of_space(self):
        with self.assertRaises(ValueError):
            self.newUser.setEmailAddress(" ")

    def test_email_address_must_not_be_an_string_of_multiple_space(self):
        with self.assertRaises(ValueError):
            self.newUser.setEmailAddress("      ")

    def test_email_address_must_not_accept_a_single_character(self):
        with self.assertRaises(ValueError):
            self.newUser.setEmailAddress("a")

    def test_email_address_must_not_accept_a_single_at_character(self):
        with self.assertRaises(ValueError):
            self.newUser.setEmailAddress("@")

    def test_email_address_must_not_accept_just_at_dot_characters(self):
        with self.assertRaises(ValueError):
            self.newUser.setEmailAddress("@.")

    def test_email_address_must_follow_the_pattern(self):
        self.newUser.setEmailAddress("aaaa@aaaa.aaa")
        self.assertEqual(self.newUser.getEmailAddress(), "aaaa@aaaa.aaa")

    def test_email_address_must_follow_the_pattern_with_numbers(self):
        self.newUser.setEmailAddress("aaa000@aaa.aaa")
        self.assertEqual(self.newUser.getEmailAddress(), "aaa000@aaa.aaa")

    def test_email_address_must_follow_the_pattern3(self):
        self.newUser.setEmailAddress("sandhu63@uni.coventry.ac.uk")
        self.assertEqual(self.newUser.getEmailAddress(), "sandhu63@uni.coventry.ac.uk")


class TestPreviousSignInDatetime(unittest.TestCase):

    def setUp(self):
        self.newUser = Customer()

    def tearDown(self):
        pass

    def test_previousSignInDatetime_must_be_none_if_not_set(self):
        self.assertIsNone(self.newUser.getPreviousSignInDatetime())

    def test_previousSignInDatetime_must_not_accept_none_argument(self):
        with self.assertRaises(TypeError):
            self.newUser.setPreviousSignInDatetime(None)

    def test_previousSignInDatetime_must_not_be_a_string(self):
        with self.assertRaises(TypeError):
            self.newUser.setPreviousSignInDatetime("1232434334.3843943")

    def test_previousSignInDatetime_must_not_be_a_false_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setPreviousSignInDatetime(False)

    def test_previousSignInDatetime_must_not_be_a_true_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setPreviousSignInDatetime(True)

    def test_previousSignInDatetime_must_return_a_float(self):
        self.newUser.setPreviousSignInDatetime(632432525.232)
        self.assertIsInstance(self.newUser.getPreviousSignInDatetime(), float)


class TestCurrentSignInDatetime(unittest.TestCase):

    def setUp(self):
        self.newUser = Customer()

    def tearDown(self):
        pass

    def test_currentSignInDatetime_must_be_none_if_not_set(self):
        self.assertIsNone(self.newUser.getCurrentSignInDatetime())

    def test_currentSignInDatetime_must_not_accept_none_argument(self):
        with self.assertRaises(TypeError):
            self.newUser.setCurrentSignInDatetime(None)

    def test_currentSignInDatetime_must_not_be_a_string(self):
        with self.assertRaises(TypeError):
            self.newUser.setCurrentSignInDatetime("1232434334.3843943")

    def test_currentSignInDatetime_must_not_be_a_false_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setCurrentSignInDatetime(False)

    def test_currentSignInDatetime_must_not_be_a_true_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setCurrentSignInDatetime(True)

    def test_currentSignInDatetime_must_return_a_float(self):
        self.newUser.setCurrentSignInDatetime(632432525.232)
        self.assertIsInstance(self.newUser.getCurrentSignInDatetime(), float)


class TestName(unittest.TestCase):

    def setUp(self):
        self.newUser = Customer()

    def tearDown(self):
        pass

    def test_currentSignInDatetime_must_be_none_if_not_set(self):
        self.assertIsNone(self.newUser.getName())

    def test_name_must_not_accept_none_argument(self):
        with self.assertRaises(TypeError):
            self.newUser.setName(None)

    def test_name_must_not_accept_an_int_argument(self):
        with self.assertRaises(TypeError):
            self.newUser.setName(1)

    def test_name_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            self.newUser.setName(0)

    def test_name_must_not_be_float(self):
        with self.assertRaises(TypeError):
            self.newUser.setName(0.01)

    def test_name_must_not_be_true_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setName(True)

    def test_name_must_not_be_false_boolean(self):
        with self.assertRaises(TypeError):
            self.newUser.setName(False)

    def test_name_must_not_be_an_string_of_space(self):
        with self.assertRaises(ValueError):
            self.newUser.setName(" ")

    def test_name_must_not_be_an_string_of_multiple_space(self):
        with self.assertRaises(ValueError):
            self.newUser.setName("      ")

    def test_name_must_not_be_empty_string(self):
        with self.assertRaises(ValueError):
            self.newUser.setName("")

    def test_name_must_not_be_a_single_character(self):
        with self.assertRaises(ValueError):
            self.newUser.setName("a")


if __name__ == '__main__':
    unittest.main()
