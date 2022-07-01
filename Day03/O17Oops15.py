
class Animal:
    def __init__(self):
        print("Animal Ctor.....")
        self.age = '1 yr'

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.size = '1k'
        print("Bird Ctor......")

    def fly(self):
        print("Birds fly....")


cuckoo = Bird()
print(cuckoo.__dict__)