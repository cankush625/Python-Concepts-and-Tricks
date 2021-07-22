# For iterating through two or more lists, we will use the zip function
# Zip function allow us to iterate through multiple lists, provided the list size should be same
# If list size is not same then the zip function will execute till the size of the small list
names = ["james", "david", "steve"]
marks = [89, 97, 78]
grades = ['B', 'A', 'C']

for name, mark in zip(names, marks):
    print(f'{name} got {mark} marks')

# unpacking the data received from zip function using name, mark and grade variables
for name, mark, grade in zip(names, marks, grades):
    print(f'{name} got {mark} marks with {grade} grade')

# Using packed values from zip function
for values in zip(names, marks, grades):
    print(values)
