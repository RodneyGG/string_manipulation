"""
Prog07: Create a program that ask the user to input a complete statement. 
Print the number of words in the input.
Example:
Input: We will weather the weather whatever the weather whether we like it or not
Output: 14
"""
#ask user to quit
def ask_quit():
    while True:
        ask_user = input("Do you wish to exit the program? (Y/N)").strip().lower()
        if ask_user in ("y", "yes"):
            return 0
        elif ask_user in ("n", "no"):
            return 1
        else:
            print("Invalid Input")

try_again = True

while try_again:
    #Ask the user to input a word/s
    words = input("Enter a word/s: ")
    #count the words in the word/s
    count_word = words.split()
    #print the number of words in the word/s
    print(len(count_word))
    
    #Ask user to quit
    try_again = ask_quit()
    