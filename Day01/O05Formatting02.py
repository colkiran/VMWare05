
print("Conversions".center(40, '-'))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 40)
print("{val} {val} {val}".format(val=36))
print("{val} {val:f} {val:b}".format(val=36))
print("{val:10} {val:f} {val:b}".format(val=36))
print("{val:5} {val:f} {val:b}".format(val=36))
print("{val:5} {val:f} {val:b}".format(val=36786410))

print("-" * 40)
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 40)
# alignment
print("{name:15}Tendulkar".format(name="Sachin"))
print("{name:15}Tendulkar".format(name=123))

print("-" * 40)
print("{name:<15} Tendulkar".format(name="Sachin"))
print("{name:^15} Tendulkar".format(name="Sachin"))
print("{name:>15} Tendulkar".format(name="Sachin"))

print("-" * 40)
print("{st:^40}".format(st="Alignment"))
print("{st:-^40}".format(st="Alignment"))


print("-" * 40)
print("One googol is {}".format(10 ** 100))
print("One googol is {:,}".format(10 ** 100))
