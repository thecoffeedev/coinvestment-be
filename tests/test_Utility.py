import unittest
from models.Utility import Utility


class TestGeneratePasswordHash(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generatePasswordHash_must_not_accept_none_argument(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash(None)

    def test_generatePasswordHash_must_not_be_a_float(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(0.01)

    def test_generatePasswordHash_must_not_be_false_boolean(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(False)

    def test_generatePasswordHash_must_not_be_true_boolean(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(True)

    def test_generatePasswordHash_must_not_be_an_int(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(1)

    def test_generatePasswordHash_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(0)

    def test_generatePasswordHash_must_not_be_empty_string(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("")

    def test_generatePasswordHash_must_not_be_a_single_character(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("a")

    def test_generatePasswordHash_must_not_be_seven_characters(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("aaaaaaa")

    def test_generatePasswordHash_must_not_be_seventy_three_characters(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


class TestVerifyPassword(unittest.TestCase):

    def setUp(self):
        self.passwordHash = "$2b$12$kV09x18sf3k//AWzikwG6OpCAZWJmDap.tV9TDjoGN.RqlXLIQYLK"
        self.al0ngerpassw0rd = "$2b$12$JKpQ8JbIdTtLdwWmABRpTuRQaOPy27/Pv3bQdJ8xWppXAvAPvAzeK"
        self.aShorterHash = "$2b$12$JKpQ8JbIdTtLdwWmABRpTuRQaOPy27/Pv3bQdJ8xWppXAvAP"
        self.aLongerHash = "$2b$12$JKpQ8JbIdTtLdwWmABRpTuRQaOPy27/Pv3bQdJ8xWppXAvAPvAzeKjsih2"

    def tearDown(self):
        pass

    def test_verifyPassword_must_not_accept_none_argument_for_password(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword(None, self.passwordHash)

    def test_verifyPassword_must_not_accept_none_argument_for_passwordHash(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("passwordHash", None)

    def test_verifyPassword_must_not_be_a_float(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(0.01, 0.01)

    def test_verifyPassword_must_not_be_false_boolean(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(False, False)

    def test_verifyPassword_must_not_be_true_boolean(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(True)

    def test_verifyPassword_must_not_be_an_int(self):
        with self.assertRaises(TypeError):
            Utility.generatePasswordHash(1)

    def test_verifyPassword_must_not_be_zero(self):
        with self.assertRaises(TypeError):
            Utility.verifyPassword(0)

    def test_verifyPassword_must_not_be_empty_string(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("")

    def test_verifyPassword_must_not_be_a_single_character(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("a")

    def test_verifyPassword_must_not_be_seven_characters(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("aaaaaaa")

    def test_verifyPassword_must_not_be_seventy_three_characters(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    def test_verifyPassword_must_not_be_seventy_three_characters(self):
        with self.assertRaises(ValueError):
            Utility.verifyPassword("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


class TestGenerateRandomID(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generatePasswordHash_must_not_be_none(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash(None)

class TestUnixTimestampToString(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generatePasswordHash_must_not_be_none(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash(None)


if __name__ == '__main__':
    unittest.main()
