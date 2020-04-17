#Write a function that computes the volume of a sphere given its radius.
import math

def vol(rad):
    return (4/3)*(math.pi)*rad**3

print(vol(5))

#

#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    return num >= low and num <= high

print(ran_check(3,4,5))

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    lows = 0
    uppers = 0
    for x in s:
        if x.isupper():
            uppers += 1
        else:
            lows +=1
    print(F'Number of Upper case chars: {uppers}')
    print(F'Number of Lower case chars: {lows}')

up_low('The Dog went up Tomorrow')

#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
     # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

#Write a Python function to multiply all the numbers in a list

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

