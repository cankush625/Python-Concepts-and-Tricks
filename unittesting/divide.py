def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2


if __name__ == '__main__':
    print(divide(5, 2))
