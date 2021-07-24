# Generators are performance efficient than the comprehensions because generators does not calculate
# the values in advance and does not store the values in the memory in advance.
nums = [1, 2, 3, 4, 5]

squares = (x*x for x in nums)

# Print will return a generator object because generate will not generate all of the values in the memory
# As we required, generator will generate the value.
print(squares)

# To get the values from the generator, we need to use either __next__() method OR
# we can use for loop to get the values from generator. For loop knows when to stop for StopIteration exception
for square in squares:
    print(square)

print()

# Generators are the resumable functions
# Using send(value) method, we can resume the generator function
# We can't send the value to the newly started generator. At least one value should be generated or fetched.
# We can't send the value to the fully exhausted generator.

squares = (x*x for x in nums)
print(squares.__next__())
squares.send(3)
for square in squares:
    print(square)
