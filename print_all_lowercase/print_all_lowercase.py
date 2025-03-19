"""
Prog04: Create a program that ask the user to input their fullname. 
Print the input in all lower case.
Example:
Input: Juan Dela Cruz
Output: juan dela cruz
"""

def valid_name(msg):
    while True:
        #convert it to lowercase
        name = input(msg).strip().lower()
        if len(name) >= 3 and " " in name \
            and all(char.isalpha() or char in [".", "'", " "] for char in name):
            return name
        else:
            print("Invalid Name")

def ask_quit():
    while True:
        ask_user = input("Do you wish to exit the program? (Y/N)").strip().lower()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")
            
try_again = True

while try_again:    
    #Ask the user to input a name 
    name = valid_name("Enter Name: ")
    #print name
    print(name)
    
    try_again = ask_quit()