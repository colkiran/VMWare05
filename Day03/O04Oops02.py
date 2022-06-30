

class Player:

    def __init__(self):             # constructor
        print("Ctor called.....")
        self.name = "Sachin"
        self.age = 32

    def get_details(self):             # self is like a this pointer
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player()
ply1.get_details()

print("-" * 40)
ply2 = Player()
ply2.name = "Rahul"
ply2.age = 30
ply2.get_details()