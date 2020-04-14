mylist = [1,2,3]

for num in range(3,10,2):
    print(num)

#ennumerate

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1
index_count = 0
word ='abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

for index,letter in enumerate(word):
    print(f'At index {index} the letter is {letter}')

#zip
mylist1= [1,2,3]
mylist2= ['a','b','c']

for item in zip(mylist1,mylist2):
    print(item)

#in operator

myx = 'x' in ['x','y','z']
print(myx)
