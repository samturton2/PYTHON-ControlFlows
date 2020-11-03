from datetime import datetime

# Define age and name of user
age = int(input("please enter your age: "))
name = input("whats your name: ")

# Ask if their birthday has happened this year
ask = input("Have you had your birthday this year yet? ")

# use their answer to account for birthyear
if ask[0].lower() == 'y':
    birthyear = int(datetime.today().year) - age
else:
    birthyear = int(datetime.today().year) - (age + 1)

# Print out their name and predicted birth year
print(f"OMG {name} you are {age} years old and you were born in {birthyear}.")

