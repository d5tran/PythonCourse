#Sets are unordered collections of unique elements. Meaning there can only be one representive of the object in the set

myset = set()
myset.add(1)
myset.add(2)

myset.add(2) #when trying to adding a value thats already in the list, it won't do it.

mylist = [1,1,1,1,2,2,2,3,3,3,3]

print(set(mylist))