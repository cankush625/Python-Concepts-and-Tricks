import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print("first line \n")
    time.sleep(seconds)
    print("function executed \n")
    return "success"


with concurrent.futures.ThreadPoolExecutor() as executor:
    # Passing function name and the arguments
    t1 = executor.submit(do_something, 2)
    print(t1.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
