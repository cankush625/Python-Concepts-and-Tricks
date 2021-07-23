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
    results = [executor.submit(do_something, 2) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
