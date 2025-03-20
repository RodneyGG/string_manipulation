"""
Prog06: Create a program that ask the user to input their fullname in incorrect casing. 
Print each character of the input in reverse casing.
Example:
Input: jUAn DEla CrUZ
Output: JuaN deLA cRuz
"""

#Validate the name
def valid_name(msg):
    while True:
        name = input(msg).strip()
        if len(name) >= 3 and " " in name and all(char.isalpha() \
            or char in ["'", ".", " "] for char in name):
            return name
        else:
            print("Enter Valid Full Name")

#Ask the user to quit           
def ask_quit():
    ask_user = input("Do you wish to exit the program? (Y/N)").lower().strip()
    if ask_user in ("y", "yes"):
        return 0
    elif ask_user in ('n', "no"):
        return 1
    else:
        print("Invalid Input. Only Y or N)")

try_again = True

while try_again:
    #Ask the user to enter a name
    name = valid_name("Enter Name: ")
    #Convert in reverse casing
    reversed_name = name.swapcase()
    #print reverse case name
    print(reversed_name)
    
    try_again = ask_quit()
