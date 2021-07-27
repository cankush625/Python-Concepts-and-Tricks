# Metaclass is used to enforce the constraints on the parent class
# Here, BaseMeta is the metaclass that is used to ensure that the bar() method is implemented in Base class
class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if name != 'Base' and 'bar' not in body:
            raise TypeError("Bad user class")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

    def __init_subclass__(cls, *a, **kwargs):
        print("Init Subclass", a, kwargs)
        return super().__init_subclass__(*a, **kwargs)
