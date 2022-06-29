
st = "Hello World"
print(f"st :{st}")
print(type(st))

print('-' * 40)
print(f"st :{st}")
print(f"st[0] :{st[0]}")                # strings are stored like lists(arrays)
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print('-' * 40)
# slicing
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")
print(f"st[::2]  :{st[::2]}")

print('-' * 40)
# reverse indexing
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print('-' * 40)
# Slicing
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print('-' * 40)
# strings are immutable
print(f"st :{st}")
print(f"st[6] :{st[6]}")
# st[6] = "w"

print('-' * 40)
# print(dir(st))
print(f"st :{st}")

# upper
print(st.upper())

print('-' * 40)
emp = "EMP-001, Mike Tyson, 56, New York, USA"
print(f"emp :{emp}")
print(type(emp))

empLst = emp.split(", ")
print(f"empLst :{empLst}")
print(type(empLst))
print(f"Name :{empLst[1]}")

age = emp.split(", ")[2]
print(f"age :{age}")

# convert the list back into a string
emp1 = ", ".join(empLst)
print(f"emp1 :{emp1}")
print(type(emp1))

print('-' * 40)
# maketrans and translate
st = "hello world"
print(f"st :{st}")
a = "helowrd"
b = "HELOWRD"
tbl = st.maketrans(a, b)
print(f"tbl :{tbl}")

res = st.translate(tbl)
print(f"res :{res}")
