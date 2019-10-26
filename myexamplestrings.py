#Python, variables are dynamic where as other lanagues they are static.
#So you can do a = 5, a = 'Hello World" and it will still work
#However, in C or C++ you declare the variable type at the beginnging, ex. int a = 5, and then you can't delcare a to be anothter type without type casting

my_income = 100
tax_rate = 0.1
my_taxes = my_income*tax_rate
print(my_taxes)

string_test  = "I'm going on a run"
print(string_test)

#len() returns length of string

print(len(string_test))

#Indexing and slicing strings

mystring ="Hello World"
#Return first character of string
print(mystring[0])
#Return 9 character of string
print(mystring[8])
#Reverse count if you don't know the length of the string and you want to return the last char
print(mystring[-1])


#Slicing returns a sub section of the string
#[Start:End:Step], Note: Up to End, but not include it

myslice = 'abcdefghijk'
#return from c to the end
print(myslice[2:])
#return everything upto a index, print everything up to d
print(myslice[:4])
#Grab def
print(myslice[3:6])

#Step size is how many it skips, step size includes the number it is in
#Return acegik
print(myslice[::2])

#Reverse string
print(myslice[::-1])

#String immutability
#Strings are immutable, meaning you can't re-assign the S in Sam with P
name = 'Sam'
#name[0] = 'P' does not work
#Use string concatenation
last_letters = name[1:]
name = 'P' + last_letters
print(name)
#If you want to use multiple string concat
letter = 'z'
print(letter*10)

#string Methods

x = 'Hello World'
print(x.upper())

#SPlit method, splits a string based on white space or letter passed in. By default split by whitespace

y ='This is a string'
print(y.split())

#split on i's
print(y.split('i'))

