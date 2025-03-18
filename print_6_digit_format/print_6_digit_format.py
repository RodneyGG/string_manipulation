"""
Prog02: Create a program that ask the user to input a number (0-1000). 
Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
Example:
Input: 143
Output: 000143
"""

def valid_num(msg):
    num = input(msg).strip()
    try:
        if float(num) == int(num):
            return int(num)
        else:     
            return None
    except ValueError:
        print("Invalid Input")

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
    #Ask the user to input a number 
    num = valid_num("Enter a number(0-1000): ")
    
    if num is None:
        print("This program only accept Whole numbers")
    elif 0 <= num <= 1000: 
        #convert the number into 6 digit format and print the number
        print(f"{num:06}")
    else:
        print("Enter numbers from 0 to 1000 Only")
        
    try_again = ask_quit()
