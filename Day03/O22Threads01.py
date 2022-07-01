
# synchronous / sequential execution
import time

St = time.perf_counter()

def doJob():
    print("Job Starting.....")
    time.sleep(2)
    print("Job completed.....")

doJob()
doJob()

Et = time.perf_counter()

print(f"Completed the job in {round(Et - St, 2)} seconds......")