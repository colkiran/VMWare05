
class Product:

    def __init__(self, prc):
        self.set_price(prc)

    def get_price(self):
        print("getter called....")
        return self.__price

    def set_price(self, prc1):
        print("setter called.....")
        self.__price = prc1

    def del_price(self):
        print("deleter called......")
        self.__price = 0

    price = property(get_price, set_price, del_price)

pepsi = Product(75)
print(pepsi.price)
pepsi.price = 60
print(pepsi.price)

del pepsi.price
print(pepsi.price)



