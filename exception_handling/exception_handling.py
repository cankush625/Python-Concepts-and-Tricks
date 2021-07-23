a = 4
b = 0

result = 0
try:
    result = a / b
except ZeroDivisionError:
    print("Trying to divide by zero")
except Exception as e:
    print(e)
else:
    # Code inside else will run if the try block get executed successfully
    print("Into the else block")
finally:
    print("Into the finally block")

print(result)
