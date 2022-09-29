from data_access.CustomerDataAccess import CustomerDataAccess
from models.Customer import Customer
from models.Utility import  Utility


class CustomerController:

    def __init__(self, app):
        self.da = CustomerDataAccess(app)
        print(type(app))

    def customerSignIn(self, jsonData):
        try:
            print("Inside customerSignIn")
            customer = Customer()
            customer.setEmailAddress(jsonData["emailAddress"])
            customer.setPasswordHash(Utility.generatePasswordHash(jsonData["password"]))
        except Exception as e:
            print(e)
            response = \
                {
                    "status":
                        {
                            "status code": "FAILURE",
                            "status message": e.args[0]
                        },
                }
            return response



