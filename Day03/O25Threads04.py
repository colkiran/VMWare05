

import time
import threading
import concurrent.futures

St = time.perf_counter()

def doJob(secs):
    print(f"Job Starting... {threading.current_thread().name}")
    time.sleep(secs)
    print(f"Job completed.... {threading.current_thread().name}")
    return "hello"

with concurrent.futures.ThreadPoolExecutor() as executor:
    thrd1 = executor.submit(doJob, 2)
    thrd2 = executor.submit(doJob, 2)

    res1 = thrd1.result()
    res2 = thrd2.result()


Et = time.perf_counter()

print(f"Completed the job in {round(Et - St, 2)} seconds......")
print(f"res1 :{res1}")
print(f"res2 :{res2}")
