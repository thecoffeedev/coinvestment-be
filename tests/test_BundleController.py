import unittest
import flask
from flask import Flask, render_template, request, session
from models.Customer import Customer
from models.Utility import Utility
from controllers.BundleController import BundleController
from data_access.BundleDataAccess import BundleDataAccess

class TestGetAllWalletDetailsFromWalletAddress(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        self.bController = BundleController(app)
        self.BDA = BundleDataAccess(app)

    def tearDown(self):
        self.BDA.testDropTables()


if __name__ == '__main__':
    unittest.main()
