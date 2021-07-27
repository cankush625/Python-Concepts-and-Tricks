# We can create the decorator using class as well
# We will use the __init__ method for passing the original function
# Ww will use the __call__ method for executing the wrapper function
# This decorator will behave exactly the same as that of the decorator created in the decorator.py file
class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("This is executed by call method before {} method".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display():
    print("Display method ran")

@DecoratorClass
def display_info(name, age):
    print("The name is {} and age is {}".format(name, age))


display()
display_info("Ankush", 22)
