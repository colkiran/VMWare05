
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3, 4, 5, 1, 1, 2, 2, 3, 3, 'apple', 'orange', 7.5, True, False}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 40)
s1 = {1, 2, 3}
print(f"s1 :{s1}")

# add
s1.add(2)
s1.add(4)
s1.add(3)
s1.add(5)
s1.add(6)
print(f"s1 :{s1}")

print("-" * 40)
# update
s1.update([1, 2, 3])
s1.update([5, 6, 7])
s1.update([4, 5, 6])
s1.update([8, 9, 10])
print(f"s1 :{s1}")

print("-" * 40)
for i in s1:
    print(i, end=" ")
print()

print("-" * 40)
# delete
res = s1.pop()
print(f"res :{res}")
res = s1.pop()
print(f"res :{res}")
res = s1.pop()
print(f"res :{res}")
print(f"s1 :{s1}")

print("-" * 40)
s1.remove(10)
s1.remove(7)
# s1.remove(2)
print(f"s1 :{s1}")

print("-" * 40)
s1.discard(5)
s1.discard(8)
s1.discard(2)
print(f"s1 :{s1}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
print('A union B :', A | B)
print('B union A :', B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B.difference(A))

print("-" * 40)
print("A symmetric_difference B :", A ^ B)
print("B symmetric_difference A :", B.symmetric_difference(A))

print("-" * 40)
# frozen sets are immutable
a = frozenset([1, 2, 3, 4, 5])
print(f"a :{a}")
print(type(a))

