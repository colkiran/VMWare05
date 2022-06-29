
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print('-' * 40)
d2 = {'name': 'Sachin', 'runs': 85, 'oppn': 'Aus', 'venue': 'Perth'}
print(f"d2 :{d2}")
print(type(d2))

print('-' * 40)
d3 = dict([('name', 'Rahul'), ('runs', 180), ('oppn', 'Eng'), ('venue', 'lords')])
print(f"d3 :{d3}")
print(type(d3))

print('-' * 40)
d4 = dict(name="Sehwag", runs=250, oppn="WI", venue='sabina park')
print(f"d4 :{d4}")
print(type(d4))

print('-' * 40)
# create
player = {'name': 'Sachin', 'runs': 97, 'oppn': 'sri lanka', 'venue': 'gale'}
print(f"player :{player}")

print('-' * 40)
# read
print(f"Name :{player['name']}")
print(f'Opponent :{player["oppn"]}')

print('-' * 40)
for i in player:
    print(i + " => " + str(player[i]))

print('-' * 40)
# update
player['year'] = '2003'
player['venue'] = 'chepauk'
print(f"player :{player}")

print('-' * 40)
# delete
del player['runs']
del player['oppn']
print(f"player :{player}")

player.clear()
print(f"player :{player}")

print('-' * 40)
print(dir(player))
