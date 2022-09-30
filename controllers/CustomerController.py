import time
from data_access.CustomerDataAccess import CustomerDataAccess
from models.Customer import Customer
from models.Utility import Utility


class CustomerController:

    def __init__(self, app):
        self.CDA = CustomerDataAccess(app)
        # Call createTables here?
        # Insert day zero data here?

    def createTables(self):
        self.CDA.createTables()

    def insertDayZeroData(self):
        self.CDA.insertDayZeroData()

    def registerNewCustomer(self, jsonReqData):
        # Set previous sign in, current sign in, and register date the same
        pass


    def customerSignIn(self, jsonReqData):
        try:
            if not jsonReqData.get("emailAddress"):
                raise ValueError("Email address not provided in request JSON")
            if not jsonReqData.get("password"):
                raise ValueError("Password not provided in request JSON")

            if not self.isExist(jsonReqData.get("emailAddress")):
                raise ValueError("Account not found: not registered")
            else:
                customerFE = Customer()
                customerFE.setEmailAddress(jsonReqData["emailAddress"])
                customerDA = self.CDA.readCustomer(customerFE)

                if Utility.verifyPassword(jsonReqData["password"], customerDA.getPasswordHash()):
                    # Update the sign in times
                    customerDA.setPreviousSignInDatetime = customerDA.getCurrentSignInDatetime()
                    customerDA.setCurrentSignDatetime = time.time()
                    # THen update the customer entry previous and current sign in datetimes





                    response = \
                        {
                            "status": {
                                "statusCode": "SUCCESS",
                                "statusMessage": "Successfully signed in customer with ID " + customerDA.getCustomerID()
                            },
                            "name": customerDA.getName(),
                            "emailAddress": customerDA.getEmailAddress(),
                            "currentSignInDatetime": customerDA.getCurrentSignInDatetime(),
                            "previousSignInDatetime": customerDA.getPreviousSignInDatetime()
                        }


        except Exception as e:
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response

    def isExist(self, emailAddress):
        return self.CDA.isExisting(emailAddress)



