# break and continue are key words that we can use to control the flow of our program
# Syntax: while variable_name condition value:
number = 0

while number < 10:
    print(f'its working --> {number}')
    if number == 5:
        break
    number += 1

# take user input with while loop

user_prompt = True

while user_prompt:
    age = input("Please enter your age? ")
    # Note this user input is within while loop so will prompt the user until below if statement is satisfied
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("please provide age in digits")

print(f"your age is {age}")
# isdigit() checks if the input is all digits
