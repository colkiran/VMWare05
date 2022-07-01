
class Employee:

    def __init__(self, name):
        self.__name = name                  # private variable
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'Python']

    def __str__(self):
        return "Name :" + self.__name + " \nTech is " + ",".join(v for v in self.tech)

emp1 = Employee("Mike")
print(emp1)

# print(emp1.__dict__)
print("-" * 40)
emp1._Employee__name = "Tyson"
print(emp1)
