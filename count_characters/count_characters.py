"""
Prog08: Create a program that ask the user to input their fullname. 
Print the number of characters in the input.
Example:
Input: Juan Dela Cruz
Output: 14
"""

#Name Validator
def valid_name(msg):
    while True:
        name = input(msg).strip()
        #Accept only if name has first and last name. 
        if len(name) >= 3 and " " in name and all(char.isalpha() \
            or char in [" ", ".", "'"] for char in name):
            return name
        else:
            print("Invalid Name. (First Name Last Name)")
            
#ask user to quit
def ask_quit():
    while True:
        ask_user = input("Do you wish to exit the program? (Y/N)").lower().strip()
        if ask_user in ("y", "yes"):
            return 0
        elif ask_user in ('n', "no"):
            return 1
        else:
            print("Invalid Input")
            
try_again = True

while try_again:
    #ask the user to enter their full name
    name = valid_name("Enter your Name: ")
    #count the characters in name
    count_characters = len(name)
    #print the count
    print(count_characters)
    
    #ask user to quit
    try_again = ask_quit()