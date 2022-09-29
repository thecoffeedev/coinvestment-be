from data_access.CustomerDataAccess import CustomerDataAccess
from models.Customer import Customer
from models.Utility import Utility


class CustomerController:

    def __init__(self, app):
        self.CDA = CustomerDataAccess(app)

    def createTables(self):
        self.CDA.createTables()

    def customerSignIn(self, jsonReqData):
        try:
            if not jsonReqData.get("emailAddress"):
                raise ValueError("Email address not provided in request JSON")
            if not jsonReqData.get("password"):
                raise ValueError("Password not provided in request JSON")

            if not self.isExist():
                raise ValueError("Account not found: not registered")
            else:
                customer = Customer()
                customer.setEmailAddress(jsonReqData["emailAddress"])
                customer.setPasswordHash(Utility.generatePasswordHash(jsonReqData["password"]))


        except Exception as e:
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response

    def isExist(self):
        return self.CDA.isExisting("aff")



