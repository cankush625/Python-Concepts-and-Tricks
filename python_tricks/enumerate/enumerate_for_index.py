# If we need to get the index of the element in the loop then we can ge the index using
# enumerate() function
names = ["Ankush", "Bob", "James"]

for index, name in enumerate(names):
    print(index, name)

# Starting the index count from custom number
for index, name in enumerate(names, start=1):
    print(index, name)
