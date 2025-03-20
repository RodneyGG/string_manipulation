"""
Prog09: Create a program that ask the user to input their fullname in incorrect casing. 
Print the input in pascal case.
Example:
Input: jUAn DEla CrUZ
Output: JuanDelaCruz
"""

def valid_name(msg):
    while True:
        name = input(msg).strip()
        if len(name) >= 3 and " " in name and all(char.isalpha() \
            or char in [" ", ".", "'"] for char in name):
            return name
        else:
            print("Enter Valid Full Name")

#ask user to input their full name
full_name = valid_name("Enter Name: ")
#convert it into pascal case
pascal_case = []
for name in full_name.split():
    pascal_case.append(name.title())
#print name in pascal case
for word in pascal_case:
    print(word, end= "")
