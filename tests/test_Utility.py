import unittest
from models.Utility import Utility


class TestGeneratePasswordHash(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generatePasswordHash_must_not_be_none(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash(None)


class TestVerifyPassword(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_verifyPassword_must_not_be_none(self):
        with self.assertRaises(ValueError):
            Utility.generatePasswordHash(None)


class TestGenerateNewCustomerID(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()
