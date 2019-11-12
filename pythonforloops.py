#for {i} in the iterable object, i is the temperary variable.
#it iterates through the whole iterable object, assigning the item to the variable
#the variable can be named whatever you want
mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num) 

#print out even numbers

for num in mylist:
    if num % 2 == 0:
        print(num)
    
list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)

mystring = 'Hello World'
for letter in mystring:
    print(letter)

mylist = [(1,2),(3,4),(5,6)]

for item in mylist:
    print(item)

#Tuple Unpacking, make the variable the same as the items in the iterable object
for (a,b) in mylist:
    print(a)
    print(b)

#iterate through dictionary

d ={'k1':1, 'k2':2, 'k3':3}

#By default it will cycle through the keys
for item in d:
    print(item)

#If you want the key/value pair use the .items() method
for item in d.items():
    print(item)
#if you just want the value use the unpacking
for key,values in d.items():
    print(values)