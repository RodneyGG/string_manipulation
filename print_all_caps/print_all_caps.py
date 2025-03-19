"""
Prog03: Create a program that ask the user to input their fullname. 
Print the input in all capital letter.
Example:
Input: Juan Dela Cruz
Output: JUAN DELA CRUZ
"""

def valid_name(msg):
    while True:
        name = input(msg)
        if len(name) >= 3 and " " in name and \
            all(char.isalpha() or char in ["'", " ", "."] for char in name):
            return name
        else:
            print("Invalid Name")
            
def ask_quit():
    while True:
        ask_user = input("Do you wish to exit the program? (Y/N)").lower().strip()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")
            
try_again = True

while try_again:        
    #Ask the user to input a name and Convert name to all uppercase
    name = valid_name("Enter Name: ").upper().strip()

    #print name
    print(name)
    
    #ask user to quit
    try_again = ask_quit()
