class Person:
    pass


person = Person()

key = 'name'
val = 'Ankush'

# set attribute
setattr(person, key, val)

# get attribute
myName = getattr(person, key)
print(myName)

# Set attributes from the dictionary
person_info = {'address': 'Mumbai', 'age': 21}
for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))
