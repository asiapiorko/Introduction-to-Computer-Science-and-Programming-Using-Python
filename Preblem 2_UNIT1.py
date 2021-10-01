"""Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2"""

N = len(letters)
letters = "bob"
sentense = 'azcbobobegbobghakl'
res =[]
for i in range(len(sentense)):
    res.append(sentense[0+i:N+i])
if letters in res:
    count=res.count(letters)
    print(count)
