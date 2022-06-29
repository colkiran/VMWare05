
i = 1

while i <= 10:
    print(i, end=" ")
    i += 1
print()

print(f"i :{i}")

print("-" * 40)
i = 10

while True:
    if i > 100:
        break
    print(i, end=" ")
    i += 10
print()

print(f"i :{i}")

print("-" * 40)
i = 0
while i <= 20:
    i += 1
    if i % 2 == 0:
        continue                # Skip the iteration
    print(i, end=" ")
print()

print("-" * 40)

i  = 10
while i > 0:
    print(i, end=" ")
    i -= 1
else:
    print("\nCompleted iteration....")

