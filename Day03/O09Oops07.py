
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __eq__(self, other):                    # will work for not equal also
        return self.salary == other.salary

emp1 = Employee("Jack", 15500)
print(emp1)

print("-" * 40)
emp2 = Employee("Jill", 15000)
print(emp2)

print("-" * 40)
# print(emp1 == emp2)                 # what is it comparing? - comparing the addresses

if (emp1 != emp2):
    print("{} salary of {} is NOT EQUAL to {} salary of {}".format(emp1.name, emp1.salary,
                                                               emp2.name, emp2.salary))
else:
    print("{} salary of {} is EQUAL to {} salary of {}".format(emp1.name, emp1.salary,
                                                               emp2.name, emp2.salary))


