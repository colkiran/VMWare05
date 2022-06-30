

def deposit(amt):
    print(f"Amount of {amt} successfully credited into the account...")

def withdraw(amt):
    print(f"Amount of {amt} successfully debited from the account...")

def BankFun(fnc):                   # HOF

    def helper(amt):
        print("logging into the service.....")
        fnc(amt)                    # callback
        print("logging out of the service......")
        print("-" * 40)

    return helper

dpsFun = BankFun(deposit)
wtdFun = BankFun(withdraw)

dpsFun(65000)
wtdFun(15000)


