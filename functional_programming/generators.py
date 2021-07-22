# yield always returns a generator object
def generate_numbers(num):
    for i in range(num):
        yield i


gen = generate_numbers(4)

while True:
    try:
        print(gen.__next__())
    except StopIteration:
        break


# send(value) method is used to resume the generator function
# and yield expression returns the specified value
def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        if val is not None:
            i = val
        else:
            i += 1


it = counter(10)
print(it.__next__())
print(it.__next__())
print(it.send(8))
print(it.__next__())
