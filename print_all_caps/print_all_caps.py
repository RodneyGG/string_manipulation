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
            all(char.isalpha() or char ["'", ".", " "] for char in name):
            return name
        else:
            print("Invalid Name")
        
#Ask the user to input a name and Convert name to all uppercase
name = input("Enter Name: ").upper().strip()

#print name
print(name)
