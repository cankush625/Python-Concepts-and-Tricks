nums = [1, 2, 3, 4, 5, 6, 7, 8]

# get the list of all numbers
new_list = [n for n in nums]
print(new_list)

# get the list of square of all the numbers in the list
squares = [n*n for n in nums]
print(squares)

# Using map and lambda with list comprehensions
square_list = map(lambda n: n*n, nums)
print(square_list.__next__())
print(square_list.__next__())
print(square_list.__next__())
print(square_list.__next__())
print(square_list.__next__())

# get the list of even numbers from the given list
even = [n for n in nums if n % 2 == 0]
print(even)

# Using filter and lambda for getting all odd numbers
odd = filter(lambda n: n % 2 != 0, nums)
print(odd.__next__())
print(odd.__next__())
print(odd.__next__())
print(odd.__next__())

# Nested for loops in list comprehensions
# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
word = "abcd"
number = "0123"
pair = [(letter, num) for letter in word for num in number]
print(pair)
