"""
Prog07: Create a program that ask the user to input a complete statement. 
Print the number of words in the input.
Example:
Input: We will weather the weather whatever the weather whether we like it or not
Output: 14
"""



#Ask the user to input a word/s
words = input("Enter a word/s: ")
#count the words in the word/s
count_word = words.split()
#print the number of words in the word/s
print(len(count_word))