#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶ 

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2==0:
        if a > b:
            return b
        else:
            return a
    elif a%2 != 0 or b%2 != 0:
        if a > b:
            return a
        else:
            return b

print(lesser_of_two_evens(3,4))

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    mytext = text.split()
    firstwordletter = mytext[0][0].lower()
    secondwordletter = mytext[1][0].lower()
    if firstwordletter == secondwordletter:
        return True
    else:
        return False

print(animal_crackers('sexy Same'))

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    myname = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return myname
print(old_macdonald('abcdefgh'))

#MASTER YODA: Given a sentence, return a sentence with the words reversed 
def master_yoda(text):
    mystring = ''
    for x in text.split():
        mystring = x + ' ' + mystring
    return mystring

print(master_yoda('I am home'))

#Find 33 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    y = False
    for x in nums:
        if y == True:
            if x == 3:
                return True
            else:
                y = False
        else:
            if x == 3:
                y = True
            else:
                y= False
    return False
        #if y == True:
         #   if x == 3:
          #      return True
           # else:
            #    y == False
        #else:
         #   if x == '3':
          #      print(x)
           #     print(y)
           # else:
            #    y == False

mynums = [3,4,3]
print(has_33(mynums))