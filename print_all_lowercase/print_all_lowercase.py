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

#Ask the user to input a name 
name = valid_name("Enter Name: ")
#print name
print(name)