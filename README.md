# Control Flows
## if statements, elif and else
- Syntax: ```if then condition```
- check someones age with if statements
```python
age = 15

if age > 15:
    print("you are at the correct age to watch the movie")
elif age < 15:
    print("Sorry you do not meet the age criteria to watch this movie")
else:
    print("you are just about old enough to watch ths movie")
```
## for loops and while loops
#### for loops
- for loops are used to iterate through data
- Syntax: ```for variable_name in name_of_data_collection_variable```
- finding an item in shopping list
```python
shopping_list = ["eggs", "milk", "supermalt"]

for items in shopping_list:
    if items == "milk":
        print(items)
        break
```

#### while loops
- While loops are not regularly used however you do see it being used for monitoring
- we use key-words `break` and `continue` that help control the flow of our loop

- lets create a while loop
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