import time
from data_access.CustomerDataAccess import CustomerDataAccess
from models.Customer import Customer
from models.Utility import Utility


class CustomerController:

    def __init__(self, app):
        self.CDA = CustomerDataAccess(app)
        self.CDA.createTables()
        self.CDA.insertDayZeroData()

    def generateToken(self):
        return Utility.generateRandomID()

    def signUp(self, jsonReqData):

        try:
            if not jsonReqData.get("emailAddress"):
                raise ValueError("Email address not provided in request JSON")
            if not jsonReqData.get("password"):
                raise ValueError("Password not provided in request JSON")
            if not jsonReqData.get("name"):
                raise ValueError("Name not provided in request JSON")

            customerFE = Customer()
            customerFE.setEmailAddress(jsonReqData.get("emailAddress"))
            customerFE.setPasswordHash(Utility.generatePasswordHash(jsonReqData.get("password")))
            customerFE.setName(jsonReqData.get("name"))

            # If the email is not already registered
            if not self.CDA.isCustomerExistingByEmailAddress(customerFE.getEmailAddress()):
                # Set previous sign in, current sign in, and register date the same
                timeNow = int(time.time())
                customerFE.setRegisterDatetime(timeNow)
                customerFE.setPreviousSignInDatetime(timeNow)
                customerFE.setCurrentSignInDatetime(timeNow)
                customerFE.setCustomerID(Utility.generateRandomID())

                self.CDA.insertCustomer(customerFE)

                response = \
                    {
                        "status": {
                            "statusCode": "SUCCESS",
                            "statusMessage": "Successfully registered new customer"
                        },
                        "name": customerFE.getName(),
                        "emailAddress": customerFE.getEmailAddress(),
                        "customerID": customerFE.getCustomerID()
                    }

                return response

            else:
                raise ValueError("Email address already registered with an account")


        except Exception as e:
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response

    def signIn(self, jsonReqData):
        try:
            if not jsonReqData.get("emailAddress"):
                raise ValueError("Email address not provided in request JSON")
            if not jsonReqData.get("password"):
                raise ValueError("Password not provided in request JSON")

            customerFE = Customer()
            customerFE.setEmailAddress(jsonReqData.get("emailAddress"))

            if not self.CDA.isCustomerExistingByEmailAddress(customerFE.getEmailAddress()):
                raise ValueError("Account not found: not registered")
            else:
                customerDA = self.CDA.readCustomerByEmail(customerFE.getEmailAddress())

                # Verify the plain text password against hash
                if Utility.verifyPassword(jsonReqData.get("password"), customerDA.getPasswordHash()):
                    # Update the sign in times
                    customerDA.setPreviousSignInDatetime = customerDA.getCurrentSignInDatetime()
                    customerDA.setCurrentSignDatetime = int(time.time())
                    # Then update the customer DB record previous and current sign in datetimes
                    self.CDA.updateCustomerSignInDatetimes(customerDA)

                    response = \
                        {
                            "status": {
                                "statusCode": "SUCCESS",
                                "statusMessage": "Successfully signed in customer"
                            },
                            "customerID": customerDA.getCustomerID(),
                            "name": customerDA.getName(),
                            "emailAddress": customerDA.getEmailAddress(),
                            "currentSignInDatetime": Utility.unixTimestampToStrings(customerDA.getCurrentSignInDatetime()),
                            "previousSignInDatetime": Utility.unixTimestampToStrings(customerDA.getPreviousSignInDatetime())
                        }

                    return response
                else:
                    raise ValueError("Customer email address or password incorrect")

        except Exception as e:
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response

    def changePassword(self, jsonReqData):
        try:
            if not jsonReqData.get("currentPassword"):
                raise ValueError("Current password not provided in request JSON")
            if not jsonReqData.get("newPassword"):
                raise ValueError("New password not provided in request JSON")
            if not jsonReqData.get("customerID"):
                raise ValueError("customerID not added to request JSON")

            customerFE = Customer()
            customerFE.setCustomerID(jsonReqData.get("customerID"))

            if not self.CDA.isCustomerExistingByCustomerID(customerFE.getCustomerID()):
                raise ValueError("Account not found: not registered")

            customerDA = self.CDA.readCustomerByCustomerID(customerFE.getCustomerID())

            if Utility.verifyPassword(jsonReqData.get("currentPassword"), customerDA.getPasswordHash()):
                customerDA.setPasswordHash(Utility.generatePasswordHash(jsonReqData.get("newPassword")))

                self.CDA.updateCustomerPassword(customerDA)

                response = \
                    {
                        "status": {
                            "statusCode": "SUCCESS",
                            "statusMessage": "Successfully changed password for customer with ID " + customerDA.getCustomerID()
                            + " You will be signed out. Sign in with new password"
                        },
                        "customerID": customerDA.getCustomerID()
                    }

                # Invalidate session by removing the token for the customer
                return response

            else:
                raise ValueError("Current password provided is incorrect")

        except Exception as e:
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response

    def changeEmailAddress(self, jsonReqData):
        try:
            if not jsonReqData.get("currentPassword"):
                raise ValueError("Current password not provided in request JSON")
            if not jsonReqData.get("newEmailAddress"):
                raise ValueError("New password not provided in request JSON")
            if not jsonReqData.get("customerID"):
                raise ValueError("customerID not added to request JSON")

            customerFE = Customer()
            customerFE.setCustomerID(jsonReqData.get("customerID"))

            if not self.CDA.isCustomerExistingByCustomerID(customerFE.getCustomerID()):
                raise ValueError("Account not found: not registered")

            customerDA = self.CDA.readCustomerByCustomerID(customerFE.getCustomerID())

            if Utility.verifyPassword(jsonReqData.get("currentPassword"), customerDA.getPasswordHash()):
                customerDA.setPasswordHash(Utility.generatePasswordHash(jsonReqData.get("newPassword")))

                self.CDA.updateCustomerEmailAddress(customerDA)

                response = \
                    {
                        "status": {
                            "statusCode": "SUCCESS",
                            "statusMessage": "Successfully changed password for customer"
                            + " You will be signed out. Sign in with new password"
                        },
                        "customerID": customerDA.getCustomerID()
                    }

                # Invalidate session by removing the token for the customer
                return response

            else:
                raise ValueError("Current password provided is incorrect")

        except Exception as e:
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response


