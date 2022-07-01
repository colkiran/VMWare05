
import time
import threading

St = time.perf_counter()

def doJob():
    print(f"Job Starting....{threading.current_thread().name}")
    time.sleep(2)
    print(f"Job completed.....{threading.current_thread().name}")


thrd1 = threading.Thread(target=doJob, name='thrd1')
thrd2 = threading.Thread(target=doJob, name='thrd2')

thrd1.start()
thrd2.start()

thrd1.join()
thrd2.join()

Et = time.perf_counter()

print(f"Completed the job in {round(Et - St, 2)} seconds......")
