# Print hello 10 times
for num in range(10):
    print("Hello")

# create an empty name list to append names to
list_names = []
while True:
    # append input to list of names
    list_names.append(input("(Enter space to end loop)\nEnter name:\n=> "))
    # enter no name to exit loop
    if list_names[-1] == " ":
        # remove space
        list_names.pop()
        # exit loop
        break

# create lower name list to add to
list_names_lower = []
#loop over name list and append to lower name list in lowercase
for name in list_names:
    list_names_lower.append(name.lower())

# print out our list of names in lowercase
print(list_names_lower)

# list of values created
values = [1, 2, 3, 4, 7, 3, 9, 7, 4, 2]
# Loop over values and if print if ODD or EVEN
for num in values:
    if num %2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
