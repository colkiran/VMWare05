

cntr = 0
for i in range(150,49, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
        cntr += 1
print()

print(f"There are {cntr} prime numbers between 150 and 50")