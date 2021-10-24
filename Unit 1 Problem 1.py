"""Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
your program should print:

Paste your code into this box """

def number_of_vovels(sentense):
    vowels = ['a', 'e', 'i', 'o', 'u']
    number = 0
    
    for letter in s:
        if letter in vowels:
            number+=1
    return number

number_of_vovels('azcbobobegghakl')
