
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Acnt Ctor.....")

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):

    def deposit(self):
        print("Amount credited into the account successfully.....")

    def getBalance(self):
        print("Balance in the account is ######.##")

class Current(Account):

    def getBalance(self):
        print("Balance in the account is ######.##")

save = Savings()
save.deposit()
save.getBalance()

cur = Current()
cur.getBalance()
