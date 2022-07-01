

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
    secs = [6, 5, 4, 3, 2, 1]
    results = executor.map(doJob, secs)

    for result in results:
        print(result)

Et = time.perf_counter()

print(f"Completed the job in {round(Et - St, 2)} seconds......")
