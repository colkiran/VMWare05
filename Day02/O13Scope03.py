
"""
outerFun is the parent of innerFun
The code in innerFun is abstracted

"""


def outerFun():
    gname = "Sachin"        # local

    def innerFun():
        nonlocal gname          # we can only convert a local variable into nonlocal
        gname += ' Tendulkar'
        print("Hello World")
        print(f"Greeting Mr.{gname}")

    innerFun()
    print(f"Outside :{gname}")

outerFun()
# print(f"main :{gname}")