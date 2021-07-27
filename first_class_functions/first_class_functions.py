# A programming language is said to have first class functions if it treats functions as first-class citizens

# First class citizens
# A first-class citizens (sometimes called as first-class objects) in programming language is an entity which
# supports all the operations generally available to other entities. These operations typically include being
# passed as an argument, returned from a function, and assigned to a variable.
def square(num):
    return num * num


# Here, we are assigning function to a variable
f = square

print(square)
# Now, we can treat the variable f as a function. This is one of the aspects of the first class functions.
print(f(5))

# We can pass function as an argument to another function
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


# Passing square function to the my_map function as an argument. This is another aspect of first class functions.
squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)

# Return a function from another function. This is also an aspect of the first-class functions.
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('h1')
print_h1('Test headline')
