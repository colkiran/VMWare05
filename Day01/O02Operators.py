"""
1. arithmetic
2. comparison or relational
3. logical operator
4. Bitwise
5. Ternary

"""

print("Arithmetic Operators".center(40, "-"))
print(10 + 3)
print(10 - 3)
print(10 / 3)
print(10 // 3)          # floor division - result is always integer
print(10 % 3)           # modulus
print(10 ** 3)

print("Augmentor Operator".center(40, "-"))
# =, +=, -=, *=     (+= => ++)
x = 10
x += 3
print(f"x :{x}")

x //= 3
print(f"x :{x}")

print("Comparison Operator".center(40, "-"))
# ==, >, <. !=,  >=, <=
print(1 == 1)
print(1 < 2)
print(1 != 1)

print("Logical Operators".center(40, "-"))
a = 10
b = 20

print(f"a :{a}")
print(f"b :{b}")

print(f"a < b :{a < b}")
print(f"b > a :{b > a}")

print(a < b and b > a)
print(a < b and b < a)

print(a < b or b > a)
print(a < b or b < a)

print(not(a < b or b > a))
print(not(a < b or b < a))

print("-" * 40)
print("a :", ord("a"))
print("z :", ord("z"))
print("A :", ord("A"))
print("Z :", ord("Z"))

print("apple" > "orange")
print("apple" < "orange")

print("Bitwise Operators".center(40, "-"))

print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(8 << 2)
print(5 << 2)
print(16 >> 1)
print(5 >> 1)
print(~0)
print(~1)
print(~5)

print("Ternary".center(40, "-"))

age = 19
print("Eligible" if age >= 18 else "Not Eligible")
