# The decorator is used to add wrapper function to our original function
# Using decorator, we can add same functionality to multiple function with the code readability

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("This was executed before {} function".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

def display():
    print("Display function ran")


display = decorator_function(display)
display()

# The code on line 11 is the way we execute the decorator for function

# The code from line no. 7 to line no. 12 is same as that the below code using @
@decorator_function
def display1():
    print("Display1 function ran")


display1()

# Using the original function with arguments
@decorator_function
def display_info(name, age):
    print("The name is {} and age is {}".format(name, age))


display_info("Ankush", 22)
