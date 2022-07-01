
import time
import threading

St = time.perf_counter()

def doJob(secs, tname):
    print(f"Job Starting... {threading.current_thread().name}")
    time.sleep(secs)
    print(f"Job completed.... {threading.current_thread().name}")

threads = []

for i in range(10):
    t = threading.Thread(target=doJob, name="thrd-"+str(i), args=[2, 'thrd-'+str(i)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

Et = time.perf_counter()

print(f"Completed the job in {round(Et - St, 2)} seconds......")