from datetime import datetime


class BaseModel:
    _number_of_objects = 0
    def __init__(self):
        self.__created_at = datetime.now()
        BaseModel._number_of_objects += 1
    @property
    def created_at(self): # convert method to the attribute and get the value
        return self.__created_at

    @created_at.setter
    def created_at(self, value): # convert method to the attribute and set the value
        self.__created_at = value


class User(BaseModel):
    def __init__(self, username, password, fullname, email):
        self._username = username
        self.__password = password
        self.fullname = fullname
        self.email = email
        super().__init__()

    def check_password(self, password):
        return self.__password == password

    @classmethod
    def create(cls, username, password, fullname, email):
        cls.validate_password(password)
        return cls(username, password, fullname, email)

    @staticmethod
    def validate_password(password):
        if len(password) < 4:
            print("password should have more than 3 char")
            return False
        return True

    def __str__(self):
        return f"{id(self)}, {self._username}: {self.fullname} "


class Address(BaseModel):
    def __init__(self, name, geo_location, complete_address):
        super().__init__()
        self.name = name
        self.geo_location = geo_location
        self.complete_address = complete_address

    def __str__(self):
        return f"{self.name}: {self.geo_location} "


class Customer(User):
    counter = 0

    def __init__(self, username, password, fullname, email, address):
        super().__init__(username, password, fullname, email)
        self.__wallet_amount = 0
        self._is_enable = False
        self.address = address
        Customer.counter += 1

    def set_enable(self):
        self._is_enable = True


    @property
    def wallet(self):  # convert method to the attribute
        return self.__wallet_amount


class Reseller(User):
    def __init__(self, logo, brand, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logo = logo
        self.brand = brand


    def check_password(self, password):
        return print("password login is not available")


class Product(BaseModel):
    product_list = list()

    def __init__(self, upc, name, price=0, description='', reseller=None):
        super().__init__()
        self.upc = upc
        self.name = name
        self.price = price
        self.description = description
        self.reseller = reseller
        Product.product_list.append(self)

    def __str__(self):
        return f'upc: {self.upc}\tname: {self.name}'

    @classmethod
    def all_amount(cls):
        return sum([product.price for product in cls.product_list])
