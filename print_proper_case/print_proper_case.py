"""
Prog05: Create a program that ask the user to input their fullname in incorrect casing. 
Print the input in proper casing.
Example:
Input: jUAn DEla CrUZ
Output: Juan Dela Cruz
"""

#ask the user to input theri fullname in incorrect casing
name = input("Enter Name in incorrect casing(jUAn DEla CrUZ):  ")
#Convert in proper casing
correct_casing = name.title()
#print name
print(correct_casing)