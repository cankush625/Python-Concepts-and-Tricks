# Creating a decorator to run the function as many times as we want
# We need to pass the number of times we want to run the function
def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                return_value = f(*args, **kwargs)
            return return_value
        return wrapper
    return inner


@ntimes(2)
def print_me():
    print("Im printed")


print(print_me())
