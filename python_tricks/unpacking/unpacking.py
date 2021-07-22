# Unpacking is used to get the values from list or tuple
a, b = (1, 2)

print(a, b)

# If we are using only one unpacked variable then IDE will throw a warning that says
# "your are not using this variable". To avoid this warning, we will use the underscore (_)
# at the place of the variable that is not required in future.
# When we have to ignore the variable in Python, we will use the underscore (_)
a, _ = (1, 2)
print(a)

# If number of elements in list are more than the number of variables then it will throw the error
# We will use * in front of the last variable to assign all of the remaining values to that variable
a, b, *c = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)

# If we don't require the extra values then we will use *_ as the last variable to ignore the variable
# and ignore the values
a, b, *_ = [1, 2, 3, 4, 5]
print(a)
print(b)

# Advanced unpacking
# Here  c will have the values until last element and d will have the last element
a, b, *c, d = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)
print(d)
