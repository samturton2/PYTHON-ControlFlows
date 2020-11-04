# Control Flows
## if statements, elif and else
## for loops and while loops

- While loops are not regularly used however you do see it being used for monitoring
- we use key-words `break` and `continue` that help control the flow of our loop


- lets create a while loop
- `break` and `continue` are `key-words`
- Syntax: ```while variable_name condition value:```
- Take user input with while loops
```python 
user_prompt = True

while user_prompt:
    age = input("Please enter your age? ")
    # Note this user input is within while loop so will prompt the user until below if statement is satisfied
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("please provide age in digits")

print(f"your age is {age}")
```