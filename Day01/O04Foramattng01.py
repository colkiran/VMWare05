
# c syntax
format = "Welcome %s, what a %s player..."
print(format)

values = ("Sachin", "class")                # tuples are enclosed in ()
print(values)
print(format % values)

print("-" * 40)
format = "Welcome %s, with a rating of %.3f, what a %s player...."
print(format % ("Sachin", 4, 'class'))
print(format % ("Sachin", 4.2, "class"))
print(format % ("Sachin", 4.2252, "class"))
print(format % ("Sachin", 4.2999, "class"))

print("-" * 40)
print("Welcome %s, your rating of %.f, what a %s player...." % ("Sachin", 4.4999, 'class'))

# Unix shell Syntax
from string import Template
tmpl = Template("Welcome $name, with a rating of $rate what a $adj player")
print(f"tmpl :{tmpl}")
print(tmpl.substitute(name="Sachin", rate=4.799, adj="class"))

# print("-" * 40)
# format of strings in python
print("python strings".center(40,"-"))
print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcome {2}, what a {0} player for {1}".format( "class", "India", "Sachin"))
print("Welcome {name}, what a {adj} player for {ctr}".format( adj = "class", ctr = "India", name ="Sachin"))

print("Welcome {name}, your rating {rating:.3f}, what a {adj} player".format(name="Sachin", rating=4.8, adj="super"))

print("Interpolation".center(40, '-'))
from math import pi, e
print(f"PI = {pi} and Eulers Constant = {e}")


print("PI = {} and Eulers Constant = {}".format(pi, e))

print("-" * 40)
full_name = ['Sachin', 'Tendulkar']                  #  list
print("Mr.{name}".format(name=full_name))
print("Mr.{name[0]}".format(name=full_name))
print("Mr. {name[0]} {name[1]}".format(name=full_name))

print("-" * 40)
import math
print(math.__name__)
print(f"Current Module Name :{__name__}")

# dunder main (__main__)      =>  double underscore main