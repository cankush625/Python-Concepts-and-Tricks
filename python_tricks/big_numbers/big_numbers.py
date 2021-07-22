# For reading the bigger numbers easily, we can separate the digits using underscore(_)
# In python, if we use underscore between the digits then the number will remain as the original
# Using underscore makes the number easy to read
# In below code a is equal to b
a = 100000000
b = 10_00_00_000

print(a == b)

sum = a + b

print(sum)

# We can make the variable readable by using the formatter.
print(f'{sum:,}')
