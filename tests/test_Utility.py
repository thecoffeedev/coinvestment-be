import unittest
from models.Utility import Utility


class TestGeneratePasswordHash(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generatePasswordHash_must_throw_error_for_none_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash(None)

    def test_generatePasswordHash_must_throw_error_for_float_argument(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(0.01)

    def test_generatePasswordHash_must_throw_error_for_false_boolean_argument(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(False)

    def test_generatePasswordHash_must_throw_error_for_true_boolean_argument(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(True)

    def test_generatePasswordHash_must_not_be_an_int_argument(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(1)

    def test_generatePasswordHash_must_throw_error_for_0_argument(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(0)

    def test_generatePasswordHash_must_throw_error_for_empty_string_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("")

    def test_generatePasswordHash_must_throw_error_for_1_character_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("a")

    def test_generatePasswordHash_must_throw_error_for_7_characters_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("aaaaaaa")

    def test_generatePasswordHash_must_throw_error_for_73_characters_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    def test_generatePasswordHash_must_return_a_string_of_printable_characters(self):
        passwordHash = Utility.generatePasswordHash("password")
        self.assertTrue(passwordHash.isprintable())

    def test_generatePasswordHash_must_not_return_a_string_of_alphanumeric_characters(self):
        passwordHash = Utility.generatePasswordHash("password")
        self.assertFalse(passwordHash.isalnum())

    def test_generatePasswordHash_must_return_a_string_of_ascii_characters(self):
        passwordHash = Utility.generatePasswordHash("password")
        self.assertTrue(passwordHash.isascii())

    def test_generatePasswordHash_must_not_return_a_string_of_space_characters(self):
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

    def test_verifyPassword_must_throw_error_for_none_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword(None, self.passwordHash)

    def test_verifyPassword_must_throw_error_for_none_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("passwordHash", None)

    def test_verifyPassword_must_throw_error_for_float_argument_for_password(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(0.01, self.passwordHash)

    def test_verifyPassword_must_throw_error_for_float_argument_for_passwordHash(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword("password", 0.01)

    def test_verifyPassword_must_throw_error_for_false_boolean_argument_for_password(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(False, self.passwordHash)

    def test_verifyPassword_must_throw_error_for_false_boolean_argument_for_passwordHash(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword("password", False)

    def test_verifyPassword_must_throw_error_for_true_boolean_argument_for_password(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(True, self.passwordHash)

    def test_verifyPassword_must_throw_error_for_true_boolean_argument_for_passwordHash(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword("password", True)

    def test_verifyPassword_must_throw_error_for_int_argument_for_password(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(1, self.passwordHash)

    def test_verifyPassword_must_throw_error_for_int_argument_for_passwordHash(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword("password", 1)

    def test_verifyPassword_must_throw_error_for_0_argument_for_password(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(0, self.passwordHash)

    def test_verifyPassword_must_throw_error_for_0_argument_for_passwordHash(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword("password", 0)

    def test_verifyPassword_must_throw_error_for_empty_string_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("", self.passwordHash)

    def test_verifyPassword_must_throw_error_for_empty_string_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("password", "")

    def test_verifyPassword_must_throw_error_for_1_character_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("a", self.passwordHash)

    def test_verifyPassword_must_throw_error_for_1_character_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("password", "a")

    def test_verifyPassword_must_throw_error_for_7_characters_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("aaaaaaa", self.passwordHash)

    def test_verifyPassword_must_throw_error_for_73_characters_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", self.passwordHash)

    def test_verifyPassword_must_throw_error_for_59_characters_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("al0ngerpassw0rd", self.aShorterHash)

    def test_verifyPassword_must_throw_error_for_61_characters_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("al0ngerpassw0rd", self.aLongerHash)

    def test_verifyPassword_must_return_true_when_password_verified(self):
        result = Utility.verifyPassword("password", self.passwordHash)
        self.assertTrue(result)

    def test_verifyPassword_must_return_true_when_longer_password_verified(self):
        result = Utility.verifyPassword("al0ngerpassw0rd", self.al0ngerpassw0rd)
        self.assertTrue(result)

    def test_verifyPassword_must_return_false_when_password_unverified(self):
        result = Utility.verifyPassword("paassword", self.passwordHash)
        self.assertFalse(result)

    def test_verifyPassword_must_return_false_when_longer_password_unverified(self):
        result = Utility.verifyPassword("al00ngerpassw0rd", self.al0ngerpassw0rd)
        self.assertFalse(result)

class TestGenerateRandomID(unittest.TestCase):

    def setUp(self):
        self.randomID = Utility.generateRandomID()

    def tearDown(self):
        pass

    def test_generateRandomID_must_not_return_int(self):
        self.assertNotIsInstance(self.randomID, int)
    def test_generateRandomID_must_not_return_float(self):
        self.assertNotIsInstance(self.randomID, float)

    def test_generateRandomID_must_not_return_boolean(self):
        self.assertNotIsInstance(self.randomID, bool)
    def test_generateRandomID_must_not_return_dict(self):
        self.assertNotIsInstance(self.randomID, dict)

    def test_generateRandomID_must_not_return_tuple(self):
        self.assertNotIsInstance(self.randomID, tuple)

    def test_generateRandomID_must_not_return_bytes(self):
        self.assertNotIsInstance(self.randomID, bytes)

    def test_generateRandomID_must_not_return_set(self):
        self.assertNotIsInstance(self.randomID, set)

    def test_generateRandomID_must_return_a_string(self):
        self.assertIsInstance(self.randomID, str)

    def test_generateRandomID_must_not_return_a_string_of_19_characters(self):
        self.assertNotEqual(len(self.randomID), 19)

    def test_generateRandomID_must_not_return_a_string_of_21_characters(self):
        self.assertNotEqual(len(self.randomID), 21)

    def test_generateRandomID_must_return_a_string_of_20_characters(self):
        self.assertEqual(len(self.randomID), 20)

    def test_generateRandomID_must_return_a_string_of_printable_characters(self):
        self.assertTrue(self.randomID.isprintable())

    def test_generateRandomID_must_return_a_string_of_alphanumeric_characters(self):
        self.assertTrue(self.randomID.isalnum())

    def test_generateRandomID_must_return_a_string_of_ascii_characters(self):
        self.assertTrue(self.randomID.isascii())


class TestUnixTimestampToString(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generatePasswordHash_must_throw_error_for_none_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash(None)


if __name__ == '__main__':
    unittest.main()
