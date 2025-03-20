"""
Prog06: Create a program that ask the user to input their fullname in incorrect casing. 
Print each character of the input in reverse casing.
Example:
Input: jUAn DEla CrUZ
Output: JuaN deLA cRuz
"""

def valid_name(msg):
    while True:
        name = input(msg).strip()
        if len(name) >= 3 and " " in name and all(char.isalpha() \
            or char in ["'", ".", " "] for char in name):
            return name
        else:
            print("Enter Valid Name")



#Ask the user to enter a name
name = valid_name("Enter Name: ")
#Convert in reverse casing
reversed_name = name.swapcase()
#print reverse case name
print(reversed_name)
