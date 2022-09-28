from data_access.CustomerDataAccess import CustomerDataAccess


class CustomerController:

    def __init__(self, app):
        self.da = CustomerDataAccess(app)
        print(type(app))




