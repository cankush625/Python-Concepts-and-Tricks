# Creating custom context manager using class
class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


# here, f is the file object, because it is returned by the __enter__ method in the OpenFile class
with OpenFile('sample.txt', 'w') as f:
    f.write("This is the sample file")

print(f.closed)
