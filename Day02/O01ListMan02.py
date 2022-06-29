import locale

l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(l1[8][1:4])

print("{txt:-^40}".format(txt="Extend"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")
l1.extend([6, 7, 8, 9])
print(f"l1 :{l1}")

print("Insert".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")
l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)
print(f"l1 :{l1}")

# copy function
print("{:-^40}".format("Copy"))
l1 = list(range(1, 6))
print(f"l1 Before :{l1}")
l2 = l1                     # shallow copy - l1 is sharing the adress along with data
print(f"l2 Before :{l2}")

l2.extend([6, 7, 8, 9])
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("-" * 40)
l3 = list(range(6, 11))
print(f"l3 Before :{l3}")
l4 = l3.copy()              # deep copy - only the data is shared
print(f"l4 Before :{l4}")

l4.append(11)
l4.append(12)
l4.append(13)

print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("-" * 40)
l5 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 5]
print(f"l5 Before :{l5}")
l6 = l5.copy()
print(f"l6 Before :{l6}")

print(f"l6[4] :{l6[4]}")
l6[4].append(60)
l6[4].append(70)
l6[4].append(80)
print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

print("-" * 40)
from copy import deepcopy
l7 = [1, 2, 3, 4, ['a', 'b', 'c', 'd', 'e'] ,5]
print(f"l7 before :{l7}")
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

print(l8[4])
l8[4].append('f')
l8[4].append('g')
l8[4].append('h')

print(f"l8 After :{l8}")
print(f"l7 After :{l7}")


