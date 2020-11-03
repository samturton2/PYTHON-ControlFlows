# Get the users age
age = int(input("please enter your age:\n=> "))

# check if the user is over 18 first
if age >= 18:
    print("You can watch any movie.")
# Then check if user is over 15, and so on...
elif age >= 15:
    print("you can watch U, PG and 15 rated movies.")
elif age >= 12:
    print("you can watch U rated movies and PG if you parents approve.")
else:
    print("you can only watch U rated movies")
