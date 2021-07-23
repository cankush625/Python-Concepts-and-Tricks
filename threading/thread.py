import threading
import time


def do_something():
    print("first line \n")
    time.sleep(1)
    print("function executed \n")


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

# Running both threads at the same time using join() method
t1.join()
t2.join()

print("Finished")
