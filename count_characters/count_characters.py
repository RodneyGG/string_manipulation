"""
Prog08: Create a program that ask the user to input their fullname. 
Print the number of characters in the input.
Example:
Input: Juan Dela Cruz
Output: 14
"""

def valid_name(msg):
    while True:
        name = input(msg).strip()
        #Accept only if name has first and last name. 
        if len(name) >= 3 and " " in name and all(char.isalpha() \
            or char in [" ", ".", "'"] for char in name):
            return name
        else:
            print("Invalid Name.")

#ask the user to enter their full name
name = valid_name("Enter your Name: ")
#count the characters in name
count_characters = len(name)
#print the count
print(count_characters)