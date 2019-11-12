x=0
while x < 5:
    print(f'The current value of {x}')
    x = x + 1
else:
    print("x is not less than 5")

#Break, continue, pass
#Break breaks out of the current closest enclosing loop.
#Conintue: Goes to the top of the closest enclosing loop.
#Pass: does nothing at all.

x= [1,2,3]
for item in x:
    #comment, if i had nothing here, pythong will error out. It needs something in the for loop. pass can be use as a place holder
    pass

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)



mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        break
    print(letter)