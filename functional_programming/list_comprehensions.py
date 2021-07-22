def is_even(num):
    return (num % 2) == 0


lst = list(x for x in range(10) if is_even(x))
print(lst)
