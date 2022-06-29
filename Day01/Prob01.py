
for i in range(6, 2, -1):
    for k in  range(7-i, 1, -1):
        print(" ", end="")
    for j in range(1, i):
        print(j, end=" ")
    print()

for i in range(6, 1, -1):
    for k in range(1, i-1):
        print(" ", end="")
    for j in range(7-i, 0, -1):
        print(j, end=" ")
    print()
