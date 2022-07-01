
class Product:

    def __init__(self, prc):
        self.price = prc

    @property
    def price(self):
        print("getter called....")
        return self.__price

    @price.setter
    def price(self, prc1):
        print("setter called.....")
        self.__price = prc1

    @price.deleter
    def price(self):
        print("deleter called......")
        self.__price = 0

pepsi = Product(55)
print(pepsi.price)
pepsi.price = 80
print(pepsi.price)
del pepsi.price
print(pepsi.price)


