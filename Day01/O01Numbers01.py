
a = 1
b = -1

print(f'a :{a}')            # f string (Format string)
print(type(a))              # RTTI - runtime type identification
print(f'b :{b}')
print(type(b))

print("-" * 40)
c = 1.0
d = -1.0

print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 40)
e = +2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 40)
g = 2 + 3j
f = 2 - 3j
print(f"g :{g}")
print(type(g))
print(f"f :{f}")
print(type(f))

print("-" * 40)
x = 2 + 3.5
print(f"x :{x}")
print(type(x))

x = 1
y = 2.5
z = x + y
print(type(x))
print(type(y))
print(type(z))

print("Conversion".center(40, "-"))
a = -100

print(type(a))
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
# a = 0
print(f'{type(bool(a))}\t\t{bool(a)}')

print("Number System".center(40, "-"))
print(11)           # decimal
print(0b11)         # binary
print(0b101)        # binary
print(0o11)         # octal
print(0o101)        # octal
print(0xe)          # hexa
print(0xa)          # hexa

print("Number System Conversion".center(40, "-"))
a = 100
print("OCT :", oct(a))
print("BIN :", bin(a))
print("HEX :", hex(a))

# print(dir(a))
