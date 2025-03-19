"""
Prog05: Create a program that ask the user to input their fullname in incorrect casing. 
Print the input in proper casing.
Example:
Input: jUAn DEla CrUZ
Output: Juan Dela Cruz
"""
def valid_name(msg):
    while True:
        name = input(msg).strip()
        if len(name) >= 3 and " " in name \
            and all(char.isalpha() or char in [" ", "'", "."] for char in name):
            return name
        else:
            print("Invalid Input")
            
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
    #ask the user to input theri fullname in incorrect casing
    name = valid_name("Enter Name in incorrect casing(jUAn DEla CrUZ):  ")
    #Convert in proper casing
    correct_casing = name.title()
    #print name
    print(correct_casing)
    
    #ask user to quit
    try_again = ask_quit()