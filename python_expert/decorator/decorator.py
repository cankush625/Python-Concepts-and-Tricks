# Decorator is used for allowing us to take the wrapping behaviour for functions and to wrap
# wide sorts of functions without having to rewrite all of the code

from time import time


# Creating the decorator for calculating the runtime of the function
def timer(func):
    def f(*args, **kwargs):
        before = time()
        return_value = func(*args, **kwargs)
        after = time()
        print('elapsed ', after - before)
        return return_value
    return f


# Using decorator we have created just above
@timer
def add(x, y=10):
    return x + y


print(f'Addition is: {add(10)}')
print(f'Addition is: {add(10, 30)}')
