"""
Prog06: Create a program that ask the user to input their fullname in incorrect casing. 
Print each character of the input in reverse casing.
Example:
Input: jUAn DEla CrUZ
Output: JuaN deLA cRuz
"""

#Ask the user to enter a name
name = input("Enter Name: ")
#Convert in reverse casing
reversed_name = name.swapcase()
#print reverse case name
print(reversed_name)
