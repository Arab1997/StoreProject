from models import Customer, Product, Reseller, Address, User

if __name__ == "__main__":
    # c1 = Customer('mr.rezoo', '1234', 'reza mobaraki', 'rezam578@gmail.com')
    # print(c1.email)
    #
    p1 = Product(1, 'book #1', 10000, 'python trick book')
    p2 = Product(2, 'book #2', 30000, 'python trick book')
    p3 = Product(3, 'book #3', 10000, 'python trick book')
    print(Product.product_list)
    for product in Product.product_list:
        print(product)
    address1 = Address(name='shirez', geo_location=(1.4345345,1.000767745), complete_address='something completer')
    c3 = Customer(username='mr.rezoo', password='1234', email='Rreza@gmail.com', fullname='Reza Mobaraki', address=address1)
    # print(type(c3), type(address1), type(c3.address))
    # print(c3.username, c3.address.name)

    r1 = Reseller('logo/path', 'apple', username='applies', password='124', fullname='asd',
                  email='aa@gmail.com')

    print(Product.all_amount())
    # print(c3._username, r1._username)
    # print(type(r1), type(c3))

    # p1 = Product(1, 'book python', 1234, 'tricks', reseller=r1)
    # print(type(p1), type(p1.reseller))
    # print(p1.name, p1.reseller.check_password('124'))

    # u2 = User.create('mr.rezoo', '1273', 'reza mobaraki', 'rezam578@gmail.com')
    # print(u2)
