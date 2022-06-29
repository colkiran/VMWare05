

def outerFun(greet):

    def innerFun(gname):

        print(greet, gname)

    return innerFun


engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")
tmlGrt = outerFun("Vanakkam")


# simple curry
engGrt("Sachin")                # call the innerFun with Sachin as arg
hndGrt("Virat Kholi")
tmlGrt("Dhoni")
