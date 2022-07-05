
x = [12.1, 34.0]
print(len(' '.join(list(map(str, x)))))

res = list(map(str, x))
print(res)

res1 = " ".join(res)
print(res1)
print(len(res1))
print(type(res1))
