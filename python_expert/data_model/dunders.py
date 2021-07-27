class Polynomial:
    # Initialize the member variables or initialize the object
    def __init__(self, *coefficients):
        self.coefficients = coefficients

    # Get printable representation of the class
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coefficients)

    # Add two objects of the class
    def __add__(self, other):
        return Polynomial(*(x + y for x,y in zip(self.coefficients, other.coefficients)))

    # Get the size of the object
    def __len__(self):
        return len(self.coefficients)


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 3)

print(p1.__add__(p2))
print(p1.__len__())
