
player = {'name': 'Sachin', 'runs': 97, 'oppn': 'sri lanka', 'venue': 'gale', 'year': 2003}
print(f"player :{player}")

# setdefault => add new value pair into the dictionary
player.setdefault('venue', 'chepauk')
player.setdefault('age', 32)
print(f"player :{player}")

print("-" * 40)
# fromkeys - convert a list into a dictionary (list elements will become the keys of the dictionary)
cities = ['blr', 'che', 'mum', 'hyd', 'kol', 'del', 'pun']
print(type(cities))
print(f"cities :{cities}")
temp1 = dict.fromkeys(cities)
print(f"temp1 :{temp1}")

temp2 = dict.fromkeys(cities, 21)
print(f"temp2 :{temp2}")

print("-" * 40)
print(f"temp2 :{temp2}")
print(temp2.get('hyd', "Invalid key please enter a valid one...."))

print("blr" in temp2)
print("mys" in temp2)

print("-" * 40)
for i in temp2.keys():
    print(i)
# print(temp2.values())
