# Closures
# Return the function from another function.
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


# The hi_func is now equal to the inner_function
hi_func = outer_function('hi')
hello_func = outer_function('hello')

hi_func()
hello_func()
