
class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'Python']

    def __iter__(self):
        return iter(self.tech)

    def __len__(self):
        return len(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value

emp1 = Employee("Joe")

print([emp for emp in emp1])

print(len(emp1))

emp1.append("angularJS")

print([emp for emp in emp1])

x = emp1[2]
print(f"x :{x}")

emp1[2] = "JSP"
print([emp for emp in emp1])
