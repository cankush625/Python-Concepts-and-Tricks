import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print("first line \n")
    time.sleep(seconds)
    print("function executed \n")


threads = []

# Run 10 threads in the parallel
for _ in range(10):
    t = threading.Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
