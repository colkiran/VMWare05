

def BankFun(fnc):                   # HOF

    def helper(amt):
        print("logging into the service.....")
        fnc(amt)                    # callback
        print("logging out of the service......")
        print("-" * 40)

    return helper

@BankFun
def deposit(amt):
    print(f"Amount of {amt} successfully credited into the account...")

@BankFun
def withdraw(amt):
    print(f"Amount of {amt} successfully debited from the account...")


deposit(50000)
withdraw(10000)