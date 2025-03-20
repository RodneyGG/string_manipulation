"""
Prog09: Create a program that ask the user to input their fullname in incorrect casing. 
Print the input in pascal case.
Example:
Input: jUAn DEla CrUZ
Output: JuanDelaCruz
"""

# Name validator
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
    #ask user to input their full name
    full_name = valid_name("Enter Name: ")
    
    #convert it into pascal case
    pascal_case = []
    for name in full_name.split():
        pascal_case.append(name.title())
    
    #print name in pascal case
    for word in pascal_case:
        print(word, end= "")
    
    #ask user to quit
    try_again = ask_quit()
    
    
