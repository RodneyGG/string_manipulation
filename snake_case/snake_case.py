"""
Prog10: Create a program that ask the user to input their fullname in incorrect casing. 
Print the input in snake case.
Example:
Input: jUAn DEla CrUZ
Output: juan_dela_cruz
"""

#Name validator
def valid_name(msg):
    while True:
        name = input(msg).strip()
        if len(name) >= 3 and " " in name and all(char.isalpha() \
            or char in [" ", ".", "'"] for char in name):
            return name
        else:
            print("Enter Valid Full Name")
            
            
#ask user to quit
def ask_quit():
    while True:
        ask_user = input("\nDo you wish to exit the program? (Y/N)").lower().strip()
        if ask_user in ("y", "yes"):
            return 0
        elif ask_user in ("n", "no"):
            return 1
        else:
            print("Invalid Input. Only Y/N")

try_again = True

while try_again:
    #Ask user to enter a name
    full_name =  valid_name("Enter Name: ")
    #convert the name in snake case
    snake_case = []
    for name in full_name.split():
        snake_case.append(name.lower())
    #print the name in the snake case
    for i in range(len(snake_case)):
        if i == len(snake_case) - 1: 
            print(snake_case[i], end="")
        else:
            print(snake_case[i], end="_")
    
    try_again = ask_quit()
