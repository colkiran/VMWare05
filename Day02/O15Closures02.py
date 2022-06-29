
# closures
def outerFun(gname):                #HOF- higher order functions
    gname += " Tendulkar"

    def innerFun():

        print("Hello World")
        print(f"Greetings {gname}")

    return innerFun

inFun = outerFun("Sachin")

print("before calling infun.....")

inFun()

print("-" * 40)
outerFun("Rahul")()             # calls the innerFun