my_list =['String', '123','5.123']
print(len(my_list))

#Can combine lists with +

new_list = [1,2,3]

another_list = my_list + new_list
print(another_list)

#Lists are mutable meaning, you can change any element in the list
new_list[0] = 'Mutate!'

print(new_list)

#to Add to the end of a list

new_list.append(4)

#To remove from the list use the pop function. Pop function also returns the popped item

new_list.pop()
print(new_list)

#popped_item = new_list.pop()

#If you provide a location, it pops that item in the middle

new_list.pop(2)

#List can be sorted using the sort() method. It sorts in place meaning, it replaces the original list with the sorted list

alpha_list = ['b', 'a', 'd', 'c']
alpha_list.sort()
print(alpha_list)

#Reverse list using the reverse() function, also in place. It replaces the original list with the sorted list

