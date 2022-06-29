
# closures
def outerFun(gname):
    gname += " Tendulkar"

    def innerFun():

        print("Hello World")
        print(f"Greetings {gname}")

    innerFun()

outerFun("Sachin")

