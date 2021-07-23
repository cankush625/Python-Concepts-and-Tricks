import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping for {seconds} \n")
    time.sleep(seconds)
    print("function executed \n")
    return "success"


# Passing list of argument values to the function using map function in thread pool
# executor.map() function returns an iterator
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
