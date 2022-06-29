
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print('-' * 40)
l2 = [1, 2, 'three', 'four', 5.2, 6.8, True, False, 9j, 10j]
print(f"l2 :{l2}")
print(type(l2))

print('-' * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print('-' * 40)
l1 = list(range(1, 6))
print(f"l1 :{l1}")
l1[2] = 2.5
print(f"l1 :{l1}")
del l1[1]
print(f"l1 :{l1}")

print('-' * 40)
l1 = [1, 2, 3, 4.5, 5.2, 6.3, 'seven', 'eight', 'nine']
print(id(l1[0]))
print(id(l1[1]))
print(id(l1[2]))
print(id(l1[3]))

print('-' * 40)
# print(dir(l1))

# insert new element
l1 = list(range(1, 6))
print(f"l1 :{l1}")
l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(l1[8][1:4])
