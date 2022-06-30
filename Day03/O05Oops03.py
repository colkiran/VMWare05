"""
whenever we make a call to the method inside a class, the method will implicitly take the name of
the object as an argument and store it in self.

"""
class Player:

    def __init__(self, name, age):
        print("Ctor called.....")
        self.name = name
        self.age = age

    def get_details(self):             # self is like a this pointer
        print(f"Name is {self.name}\nAge is {self.age}")

    def __del__(self):
        print("-" * 40)
        print(f"{self.name} destroyed....")

ply1 = Player("Sachin", 32)
ply1.get_details()
# del ply1

print("-" * 40)
ply2 = Player("Rahul", 30)
ply2.get_details()

print("-" * 40)
ply2.score = 150

print(ply2.score)
# print(ply1.score)

print("-" * 40)
print("ply1 :", ply1.__dict__)
print("ply2 :", ply2.__dict__)

