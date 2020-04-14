#Lambda Expressions are one time use functions. Don't even name them

def square(num):
    return num**2
my_nums = [1,2,3,4,5]

#map, pass in a function that you want to use on each item in a list
for item in map(square,my_nums):
    print(item)
#Or if you want a List back
list(map(square,my_nums))

def splicer(mystring):
    if len (mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))

#filter based off the inputed function's condition. Pass in an iterable object and a function that is true or false. It will yield the iterable item if it's true.

def check_even(num):
    return num%2 == 0

mynumbers = [1,2,3,4,5,6]
#map, pass in a function that you want to use on each item in a list
for item in filter(check_even,mynumbers):
    print(item)
#Or if you want a List back
print(list(filter(check_even,mynumbers)))

#Lambda

lambda num: num **2

print(list(map(lambda num: num**2, my_nums)))


print(list(filter(lambda num : num%2==0,mynumbers)))

#grab first char of each item in list

print(list(map(lambda names:names[0],names)))
