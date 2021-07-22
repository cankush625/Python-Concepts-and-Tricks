# Python has built-in context managers that are useful in managing the resources.
# With context manager, we don't need to manually close the resources like file,
# or database connection
# The context manager will open the resource do the mentioned operation and the
# close that resource by themselves.
# with is the context manager that is used to open and close the file automatically.

with open('data.dat', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
print(words)
