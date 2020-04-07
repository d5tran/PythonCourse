#Dictionaries use a key-value pairing. Dictionaries use {} and colons to signify their keys
#Dictionaries vs Lists
#Dictionaries are unordered and cannot be sorted
#Dictionaries retrieve objects by key name wheras #Lists use locations to retrieve objects
#Dictionaries you don't need to know the location of the object in it, just it's key-value pair. Con it can't be sorted

my_dict = {'key1':'value1','key2':'value2'}


print(my_dict)
print(my_dict['key1'])

#Prices in a store is agood use of a dictionary

prices_lookup = {'apples':2.99,'oranges':1.99,'milk':5.80}

#Dictionaries can hold hold anything from strings, lists, dictionaries

d = {'k1':123, 'k2': [0,1,2],'k3':{'insidekey':100}}

print(d['k2'])
print(d['k2'][1])

#To add to a dictionary

d['k4'] = 100
print(d['k4'])

#Useful dictionary methods: 
print(prices_lookup.keys())
print(prices_lookup.values())
print(prices_lookup.items())