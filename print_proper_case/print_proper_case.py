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


#ask the user to input theri fullname in incorrect casing
name = valid_name("Enter Name in incorrect casing(jUAn DEla CrUZ):  ")
#Convert in proper casing
correct_casing = name.title()
#print name
print(correct_casing)