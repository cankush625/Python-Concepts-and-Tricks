from functools import reduce

nums = [1, 2, 3, 4, 5]

# filter() function is used to filter the data based on the condition.
evens = list(filter(lambda n: n % 2 == 0, nums))

print(evens)

# map() function is used to do some operation on the data using expression.
doubles = list(map(lambda n: n * 2, nums))

print(doubles)

# reduce() function is used to reduce the data to a single number using an expression or function.
# At the first step, first two elements of the sequence are picked and the result is obtained.
# In the next step, same expression or function is applied on the previously obtained result and the
# number just next to the second element. This continues till the last element in the sequence.
num = reduce(lambda a, b: a + b, nums)
print(num)
