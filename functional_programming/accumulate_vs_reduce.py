# both accumulate() and reduce() can be used for summation of a sequence
# The reduce() function is defined in functools module and accumulate() is defined in the itertools module
# reduce() returns only final value whereas, accumulate() returns an iterator that contains all of the intermediate
# calculation values
# The last number in the iterator is the final value of the operation performed on the sequence

from itertools import accumulate


nums = [1, 2, 3, 4, 5]

itr = accumulate(nums, lambda a, b: a + b)
print(itr)

for res in itr:
    print(res)
