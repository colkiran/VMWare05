
class Player:

    team = "India"          # class attribute

    def __init__(self, name, age):
        print("Ctor called.....")
        self.name = name
        self.age = age

    def get_details(self):             # self is like a this pointer
        print(f"Name is {self.name}\nAge is {self.age}")

ply1  = Player("Sachin", 32)
ply1.get_details()

print("-" * 40)

ply2 = Player("Rahul", 29)
ply2.get_details()

print("-" * 40)
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
Player.team = "MI"
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
ply2.team = "RR"                    # cannot change the class attribute values
print(f"ply2   :{ply2.team}")

print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")

print("-" * 40)
print(f"ply2 :{ply2.__dict__}")

print("-" * 40)
print(Player.__dict__)

