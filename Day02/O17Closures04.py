
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

KanGrt = outerFun("Namaskara")
TigerKan = KanGrt("tiger")

TigerKan("Prabhakar")

"""
engGrt = outerFun("Welcome")
snglnEng = engGrt("------>")
dbllnEng = engGrt("======>>")



snglnEng("Sachin")
dbllnEng("Rahul")
"""
