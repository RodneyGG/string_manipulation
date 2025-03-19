"""
Prog01: Create a program that ask the user to input their fullname with several space characters 
at the beginning. Print the input without the spaces in the beginning.
Example:
Input:         Juan Dela Cruz
Output: Juan Dela Cruz
"""
def valid_name(msg):
    while True:
        #remove the leading space
        name = input(msg).strip()
        #Make sure the name has a First and Last Name. 
        #Also accepts names like Shaquille O'neal
        if len(name) >= 3 and " " in name \
            and all(char.isalpha() or char in ["'", " ", "."] for char in name):
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
    #Enter the name 
    name = valid_name("Enter Name: ")
    #print name
    print(name)
    
    try_again = ask_quit()