
class Player:

    team = "India"          # class attribute

    def __init__(self, name, age):
        print("Ctor called.....")
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        print("Factory....")
        return cls(f"Mr. {fname} {lname}", age)

    @classmethod
    def UpdatePlayer(cls, tm):
        cls.team = tm


ply1 = Player("Sachin", 34)
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("Rahul", "Dravid", 31)
ply2.get_details()

print("-" * 40)
print("Player :", Player.team)
Player.UpdatePlayer("RCB")

print("Player :", Player.team)
