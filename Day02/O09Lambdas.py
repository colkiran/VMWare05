
def add(x, y):
    return x + y

a = add
res = a(10, 20)
print(f"res :{res}")

print("-" * 40)

b = lambda x, y: x + y
res = b(200, 500)
print(f"res :{res}")

# map, filter, reduce
print("Map".center(40, "-"))
l = list(range(1, 11))
print(f"l :{l}")

# to find the square of all numbers
squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")

from calendar import month_name
# def srt(mon):
#     l = []
#     for m in list(month_name):
#         l.append(m[0:3].lower())
#     if mon in l:
#         return l.index(mon)

months = ['dec', 'sep', 'aug', 'jan', 'mar', 'nov', 'feb', 'apr', 'jun', 'may', 'oct', 'jul']
print(f"months :{months}")
print("-" * 40)

res = sorted(months, key=list(map(lambda x: x.lower()[0:3], list(month_name))).index)
print(f"res :{res}")

print("filters".center(40, "-"))
l = list(range(1, 25))
print(f"l :{l}")

res = list(filter(lambda x: x % 4 == 0, l))
print(f"res :{res}")

print("Reduce".center(40, "-"))
from functools import reduce

l = [9, 3, 5, 8, 2, 7, 15, 10, 12]
print(f"l :{l}")

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

l = list(range(1, 11))
print(f"l :{l}")
res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")