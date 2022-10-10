import unittest
from models.Utility import Utility


class TestGeneratePasswordHash(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_must_throw_error_for_none_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash(None)

    def test_must_throw_error_for_float_argument(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(0.01)

    def test_must_throw_error_for_false_boolean_argument(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(False)

    def test_must_throw_error_for_true_boolean_argument(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(True)

    def test_must_not_be_an_int_argument(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(1)

    def test_must_throw_error_for_0_argument(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(0)

    def test_must_throw_error_for_empty_string_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("")

    def test_must_throw_error_for_1_character_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("a")

    def test_must_throw_error_for_7_characters_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("aaaaaaa")

    def test_must_throw_error_for_73_characters_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    def test_must_return_a_string_of_printable_characters(self):
        passwordHash = Utility.generatePasswordHash("password")
        self.assertTrue(passwordHash.isprintable())

    def test_must_not_return_a_string_of_alphanumeric_characters(self):
        passwordHash = Utility.generatePasswordHash("password")
        self.assertFalse(passwordHash.isalnum())

    def test_must_return_a_string_of_ascii_characters(self):
        passwordHash = Utility.generatePasswordHash("password")
        self.assertTrue(passwordHash.isascii())

    def test_must_not_return_a_string_of_space_characters(self):
        passwordHash = Utility.generatePasswordHash("password")
        self.assertFalse(passwordHash.isspace())


class TestVerifyPassword(unittest.TestCase):

    def setUp(self):
        self.passwordHash = "$2b$12$kV09x18sf3k//AWzikwG6OpCAZWJmDap.tV9TDjoGN.RqlXLIQYLK"
        self.al0ngerpassw0rd = "$2b$12$JKpQ8JbIdTtLdwWmABRpTuRQaOPy27/Pv3bQdJ8xWppXAvAPvAzeK"
        self.aShorterHash = "$2b$12$JKpQ8JbIdTtLdwWmABRpTuRQaOPy27/Pv3bQdJ8xWppXAvAPvAze"
        self.aLongerHash = "$2b$12$JKpQ8JbIdTtLdwWmABRpTuRQaOPy27/Pv3bQdJ8xWppXAvAPvAzeKj"

    def tearDown(self):
        pass

    def test_must_throw_error_for_none_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword(None, self.passwordHash)

    def test_must_throw_error_for_none_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("passwordHash", None)

    def test_must_throw_error_for_float_argument_for_password(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(0.01, self.passwordHash)

    def test_must_throw_error_for_float_argument_for_passwordHash(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword("password", 0.01)

    def test_must_throw_error_for_false_boolean_argument_for_password(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(False, self.passwordHash)

    def test_must_throw_error_for_false_boolean_argument_for_passwordHash(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword("password", False)

    def test_must_throw_error_for_true_boolean_argument_for_password(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(True, self.passwordHash)

    def test_must_throw_error_for_true_boolean_argument_for_passwordHash(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword("password", True)

    def test_must_throw_error_for_int_argument_for_password(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(1, self.passwordHash)

    def test_must_throw_error_for_int_argument_for_passwordHash(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword("password", 1)

    def test_must_throw_error_for_0_argument_for_password(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(0, self.passwordHash)

    def test_must_throw_error_for_0_argument_for_passwordHash(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword("password", 0)

    def test_must_throw_error_for_empty_string_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("", self.passwordHash)

    def test_must_throw_error_for_empty_string_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("password", "")

    def test_must_throw_error_for_1_character_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("a", self.passwordHash)

    def test_must_throw_error_for_1_character_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("password", "a")

    def test_must_throw_error_for_7_characters_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("aaaaaaa", self.passwordHash)

    def test_must_throw_error_for_73_characters_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", self.passwordHash)

    def test_must_throw_error_for_59_characters_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("al0ngerpassw0rd", self.aShorterHash)

    def test_must_throw_error_for_61_characters_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("al0ngerpassw0rd", self.aLongerHash)

    def test_must_return_true_when_password_verified(self):
        result = Utility.verifyPassword("password", self.passwordHash)
        self.assertTrue(result)

    def test_must_return_true_when_longer_password_verified(self):
        result = Utility.verifyPassword("al0ngerpassw0rd", self.al0ngerpassw0rd)
        self.assertTrue(result)

    def test_must_return_false_when_password_unverified(self):
        result = Utility.verifyPassword("paassword", self.passwordHash)
        self.assertFalse(result)

    def test_must_return_false_when_longer_password_unverified(self):
        result = Utility.verifyPassword("al00ngerpassw0rd", self.al0ngerpassw0rd)
        self.assertFalse(result)

class TestGenerateRandomID(unittest.TestCase):

    def setUp(self):
        self.randomID = Utility.generateRandomID()

    def tearDown(self):
        pass

    def test_must_not_return_int(self):
        self.assertNotIsInstance(self.randomID, int)
    def test_must_not_return_float(self):
        self.assertNotIsInstance(self.randomID, float)

    def test_must_not_return_boolean(self):
        self.assertNotIsInstance(self.randomID, bool)
    def test_must_not_return_dict(self):
        self.assertNotIsInstance(self.randomID, dict)

    def test_must_not_return_tuple(self):
        self.assertNotIsInstance(self.randomID, tuple)

    def test_must_not_return_bytes(self):
        self.assertNotIsInstance(self.randomID, bytes)

    def test_must_not_return_set(self):
        self.assertNotIsInstance(self.randomID, set)

    def test_must_return_a_string(self):
        self.assertIsInstance(self.randomID, str)

    def test_must_not_return_a_string_of_19_characters(self):
        self.assertNotEqual(len(self.randomID), 19)

    def test_must_not_return_a_string_of_21_characters(self):
        self.assertNotEqual(len(self.randomID), 21)

    def test_must_return_a_string_of_20_characters(self):
        self.assertEqual(len(self.randomID), 20)

    def test_must_return_a_string_of_printable_characters(self):
        self.assertTrue(self.randomID.isprintable())

    def test_must_return_a_string_of_alphanumeric_characters(self):
        self.assertTrue(self.randomID.isalnum())

    def test_must_return_a_string_of_ascii_characters(self):
        self.assertTrue(self.randomID.isascii())


class TestUnixTimestampToString(unittest.TestCase):

    def setUp(self):
        self.timeStringsFromInt = Utility.unixTimestampToStrings(1663815575)
        self.timeStringsFromFloat = Utility.unixTimestampToStrings(1664116575.343252)

    def tearDown(self):
        pass

    def test_must_throw_error_for_none_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash(None)

    def test_must_not_return_int_when_argument_is_int(self):
        self.assertNotIsInstance(self.timeStringsFromInt, int)

    def test_must_not_return_int_when_argument_is_float(self):
        self.assertNotIsInstance(self.timeStringsFromFloat, int)

    def test_must_not_return_float_when_argument_is_int(self):
        self.assertNotIsInstance(self.timeStringsFromInt, float)

    def test_must_not_return_float_when_argument_is_float(self):
        self.assertNotIsInstance(self.timeStringsFromFloat, float)

    def test_must_not_return_boolean_when_argument_is_int(self):
        self.assertNotIsInstance(self.timeStringsFromInt, bool)

    def test_must_not_return_boolean_when_argument_is_float(self):
        self.assertNotIsInstance(self.timeStringsFromFloat, bool)

    def test_must_not_return_dict_when_argument_is_int(self):
        self.assertNotIsInstance(self.timeStringsFromInt, dict)

    def test_must_not_return_dict_when_argument_is_float(self):
        self.assertNotIsInstance(self.timeStringsFromFloat, dict)

    def test_must_not_return_tuple_when_argument_is_int(self):
        self.assertNotIsInstance(self.timeStringsFromInt, tuple)

    def test_must_not_return_tuple_when_argument_is_float(self):
        self.assertNotIsInstance(self.timeStringsFromFloat, tuple)

    def test_must_not_return_bytes_when_argument_is_int(self):
        self.assertNotIsInstance(self.timeStringsFromInt, bytes)

    def test_must_not_return_bytes_when_argument_is_float(self):
        self.assertNotIsInstance(self.timeStringsFromFloat, bytes)

    def test_must_not_return_set_when_argument_is_int(self):
        self.assertNotIsInstance(self.timeStringsFromInt, set)

    def test_must_not_return_set_when_argument_is_float(self):
        self.assertNotIsInstance(self.timeStringsFromFloat, set)

    def test_must_not_return_a_list_when_argument_is_int(self):
        self.assertNotIsInstance(self.timeStringsFromInt, list)

    def test_must_not_return_a_list_when_argument_is_float(self):
        self.assertNotIsInstance(self.timeStringsFromFloat, list)

    def test_must_return_a_string_when_argument_is_int(self):
        self.assertIsInstance(self.timeStringsFromInt, str)

    def test_must_return_a_string_when_argument_is_float(self):
        self.assertIsInstance(self.timeStringsFromFloat, str)

    def test_must_return_a_string_date_up_to_element_10(self):
        self.assertIsInstance(self.timeStringsFromInt[0:10], str)

    def test_must_return_a_string_time_from_element_10_to_end(self):
        self.assertIsInstance(self.timeStringsFromInt[10:-1], str)

    def test_must_return_a_string_in_return_list_element_0_when_argument_is_float(self):
        self.assertIsInstance(self.timeStringsFromFloat[0], str)

    def test_must_return_a_string_in_return_list_element_1_when_argument_is_float(self):
        self.assertIsInstance(self.timeStringsFromFloat[1], str)

    def test_must_return_a_space_between_date_and_time_when_argument_is_int(self):
        self.assertEqual(self.timeStringsFromInt[10], " ")

    def test_must_return_a_space_between_date_and_time_when_argument_is_float(self):
        self.assertEqual(self.timeStringsFromFloat[10], " ")

    def test_must_return_correct_date_string_when_argument_is_int(self):
        self.assertEqual(self.timeStringsFromInt[0:10], "22-09-2022")

    def test_must_return_correct_time_string_when_argument_is_int(self):
        self.assertEqual(self.timeStringsFromInt[11:], "03:59:35")

    def test_must_return_correct_date_string_when_argument_is_float(self):
        self.assertEqual(self.timeStringsFromFloat[0:10], "25-09-2022")

    def test_must_return_correct_time_string_when_argument_is_float(self):
        self.assertEqual(self.timeStringsFromFloat[11:], "15:36:15")


if __name__ == '__main__':
    unittest.main()
