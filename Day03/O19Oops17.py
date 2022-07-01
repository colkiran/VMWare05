
class Animal:

    def __init__(self):
        print("Animal Ctor...")
        self.a = 10

    def eat(self):
        print("Animals eat....")

    def fun(self):
        print("fun of animal class....")

class Person:

    def __init__(self):
        print("Person Ctor.....")
        self.p = 20

    def talk(self):
        print("Person talks......")

    def fun(self):
        print("fun of Person class....")


class Girl(Animal, Person):

    def __init__(self):
        super().__init__()
        Person.__init__(self)
        print("Girl Ctor....")
        self.g = 30

tina = Girl()
tina.eat()
tina.talk()

tina.fun()
print("-" * 40)

print(tina.__dict__)



