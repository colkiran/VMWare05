

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

emp1 = Employee("Smith", 50000)
print(emp1)

print("-" * 40)
emp2 = Employee("Jones", 45000)
print(emp2)

print("-" * 40)
print("Addition :", emp1 + emp2)
print("Subtraction :", emp1 - emp2)
print("Multiplication :", emp1 * emp2)
print("Division :", emp1 / emp2)
print("Floor Div :", emp1 // emp2)



