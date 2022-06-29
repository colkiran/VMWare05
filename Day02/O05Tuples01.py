
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = 10,
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 10, 20, 30
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t = (1, 2, 3, 4, 5, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 3)
print(f"t :{t}")
print(type(t))
print(f"t[0] :{t[0]}")
# t[0] = 10
print("1 :", t.count(1))
print("2 :", t.count(2))
print("3 :", t.count(3))

print(f"3 : {t.index(3)}")
print(f"3 :{t.index(3, 3, 20)}")

