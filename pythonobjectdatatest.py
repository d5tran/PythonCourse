import math
mynumber = 10

#Find square root

mysquareroot = mynumber ** 0.5
print(mysquareroot)

#Find square
mysquare = mynumber ** 2
print(mysquare)
s = 'hello'

#return the letter e
print(s[1])

#Reverse the string using slicing
print(s[::-1])

#Given the string hello, give two methods of producing the letter 'o' using indexing.
print(s[4])
print(s[-1])

#Lists
#Build this list [0,0,0] two separate ways.
mylist = [0,0,0]
print(mylist)
mylist2 = [0]*3

print(mylist2)

#Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)



#Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()

#Dictionaries
#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
# Grab 'hello'

print(d['simple_key'])
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

#[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]

print(d['k1'][2]['k2'][1]['tough'][2][0])

#Sets
#make a set
list5 = [1,2,2,33,4,4,11,22,3,3,2]
setList5 = set(list5)
print(setList5)