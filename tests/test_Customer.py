import unittest
# import sys
# sys.path.append("../models")
# print(sys.path)
from models.Customer import Customer


class TestCredentials(unittest.TestCase):

    # def setUp(self):
    #     newUser = Customer()
    #     print(newUser.walletAddress())

    def test_walletAddress_is_none(self):
        newUser = Customer("p", "e", "name")
        self.assertNotEqual(newUser.getUserID(), None)  # add assertion here


if __name__ == '__main__':
    unittest.main()
