
from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's Job......")


class Developer(Employee):

    def doJob(self):
        print("Developer's Job......")


def BankJob(emp):               # polymorphism
    print("Bank job started......")
    emp.doJob()
    print("Bank job ended........")
    print("-" * 40)


Mike = Manager()
David = Developer()

BankJob(Mike)
BankJob(David)



