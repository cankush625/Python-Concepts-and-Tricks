# The basic idea behind using partial functions is to take one function,
# set values to some parameters of this function and create a new function
# so that the existing function can be reused.

from functools import partial


def greater_than(num1: float, num2: float) -> bool:
    return num1 > num2


# Creating new function greater_than_50 using the partial functions concept
# Here we are using the existing greater_than function and setting num2
# parameter a fixed value, that is 50.
greater_than_50 = partial(greater_than, num2=50)

print(greater_than_50(40))
print(greater_than_50(50))
print(greater_than_50(60))
