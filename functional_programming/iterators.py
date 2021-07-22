list1 = [1, 2, 3, 4, 5]

it = iter(list1)

# using iterator
while True:
    try:
        print(it.__next__())
    except StopIteration:
        break

# another way of using iterator
itr = iter(list1)

while True:
    try:
        print(next(itr))
    except StopIteration:
        break

# materializing iterator as tuple
L = [1, 2, 3]
iterator = iter(L)

t = tuple(iterator)

print(t)

# sequence unpacking using iterator
L = [1, 2, 3]
iterator1 = iter(L)
a, b, c = iterator1

print ("a = ", a, "b = ", b, "c = ", c)

# using in operator with iterator
lst = [1, 2, 3]
itr1 = iter(lst)

for x in itr1:
    print(x)

# list of key, value tuples to dictionary
L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
itr = iter(L)

d = dict(itr)
print(d)
