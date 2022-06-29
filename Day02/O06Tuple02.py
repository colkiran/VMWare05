
from collections import namedtuple

nmdTpl = namedtuple("Players", "plyname age runs wickets")
ply1 = nmdTpl(plyname="Rahul", age=30, runs = 8500, wickets=45)

print(ply1)
print(f"Name :{ply1.plyname}")
print(f"Age :{ply1.age}")
print(f"Runs :{ply1.runs}")
ply1.runs = 9500
