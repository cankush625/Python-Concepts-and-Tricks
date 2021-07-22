class Demo:
    def __get__(self, obj, objtype=None):
        return 10


class A:
    x = 5
    y = Demo()


a = A()
print(a.x)
print(a.y)
