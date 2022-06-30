
def calculatetime(fun):

    def helper():
        from datetime import datetime
        current_time=datetime.now()
        fun()
        after_execution=datetime.now()
        print("TOtal time taken", after_execution-current_time)

    return helper

@calculatetime
def greet():
   l = []
   for i in range(1, 7000):
       for j in range(1, i+1):
           l.append(j ** 2)

greet()