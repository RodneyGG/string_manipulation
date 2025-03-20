"""
Prog09: Create a program that ask the user to input their fullname in incorrect casing. 
Print the input in pascal case.
Example:
Input: jUAn DEla CrUZ
Output: JuanDelaCruz
"""

#ask user to input their full name
full_name = input("Enter Name: ")
#convert it into pascal case
pascal_case = []
for name in full_name.split():
    pascal_case.append(name.title())
#print name in pascal case
for word in pascal_case:
    print(word, end= "")
