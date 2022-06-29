
def greet():
    print("Hi Mr.Sachin, Welcome to the event....")

def greetGst(gname):
    print(f"Hi Mr.{gname}, Welcome to the event.....")

# gname is non default argument, city  is default argument
def greetGstCty(gname, city="Mumbai"):
    print(f"Hi Mr. {gname} from {city}, Welcome to the event.....")

greet()
greetGst("Rahul")
greetGstCty("Sachin")
greetGstCty("Sunil")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
def enroll(name, dob, conno, emailid, eduq, des):
    print(f"Name :{name}")
    print(f"DOB :{dob}")
    print(f"Con No. :{conno}")
    print(f"Email :{emailid}")
    print(f"Education :{eduq}")
    print(f"Designation :{des}")

enroll(des="MGR", conno='9829295991', emailid="abc@gmail.com", eduq="Mtech", name="ABC", dob="10/08/1983")

# functions can return values

print("-" * 40)
def myProduct(x, y):
    return x * y

print("%i * %i = %i" % (10, 20, myProduct(10, 20)))

print("-" * 40)
from collections import namedtuple
def ArithemeticCalc(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    nmdTpl = namedtuple("Arithmetic", "add sub mul div")
    res = nmdTpl(add=add, sub=sub, mul=mul, div=div)
    return res

res = ArithemeticCalc(20, 8)
print(f"res :{res}")
print(f"Add :{res.add}")
print(f"sub :{res.sub}")
print(f"mul :{res.mul}")
print(f"div :{res.div}")

print("-" * 40)

# variable length arguments
# *var = takes a arguments and stores in a tuple
# **var = takes arguments and stores in a dictionary

def prodAll(*numbers):
    print(numbers)
    print(*numbers)             # unpack the tuple
    prod = 1
    for num in numbers:
        prod *= num
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 40)
def extract_details(**detail):
    print(f"detail :{detail}")
    print("-" * 40)
    for k in detail:
        print(k, "=>", detail[k])


extract_details(name="Sachin", runs=120, oppn="NZL", venue="Auckland")

print("-" * 40)

values = (10, 20, 30)
print(f"values :{values}")

a, b, c = values
print(a, b, c, sep=", ")

print("-" * 40)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values
print(a, b, c, sep=", ")

a, *b, c = values
print(a, b, c, sep=", ")

*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 40)
def admission(name, *tech, **marks):
    print(f"name :{name}")
    print("Technologies :", tech)
    print("Marks :", marks)

admission("David", "C", 'C++', 'Java', 'Spring', 'Hibernate', 'AngularJS',
          Xth="97%", XIIth="98%", degree="89%", pg="95%")


print("-" * 40)
def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World")


fun()
print(fun.__doc__)                 # calls the doc string

print("-" * 40)

def fun1(x, y):
    """
    function: fun1
    args: x, y

    this function fun1 takes two arguments,
    if both arguments are numeric then it will return the sum of the numbers
    if both arguments are strings then it will concatenate the strings and return it.
    """
    return x + y

print(fun1(10, 20))
print(fun1("hello", " world"))

print("-" * 40)
help(fun1)