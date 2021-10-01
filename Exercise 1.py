"""
In this problem you'll be given a chance to practice writing some for loops.

1. Convert the following code into code that uses a for loop.

prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""

# First soultion
for count in range(2,11,2):
    print(count)
print("Goodbye!")

# Second soultion
for count in range(10):
    if count != 0 and count % 2 == 0:
        print(count)
print("Goodbye!")

"""
2. Convert the following code into code that uses a for loop.

prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
"""

# First solution
print("Hello!") 
for count in range(10,0,-2):   
    print(count)
    
 """
 3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:
 21
 which is 1 + 2 + 3 + 4 + 5 + 6.
 """
# First solution

number = int(input("Define a number: "))
end = 0
for number in range(number+1):
    end += number
print(end)

# Another solution
total = end
for next in range(end):
    total += next
print(total)  
