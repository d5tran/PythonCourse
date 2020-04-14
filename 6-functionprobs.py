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


def lesser_of_two_evens2(a,b):
    if a%2 == 0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
print(lesser_of_two_evens2(3,4))

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

#Given Two integers, return True if the sum of the i ntegers is 20 or if one of the ingeters is 20. If not, return False

def makes_twenty(a,b):
    if a == 20 or b == 20:
        return True
    else:
        if (a+b) == 20:
            return True
        else:
            return False
def makes_twenty2(a,b):
    return (a+b)==20 or a == 20 or b ==20
print(makes_twenty(10,20))
print(makes_twenty2(10,21))

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    myname = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return myname
print(old_macdonald('abcdefgh'))

def old_macdonald2(name):
    first_half = name[:3]
    second_half = name[3:]
    
    return first_half.capatlize()+second_half.capatlize()
print(old_macdonald('abcdefgh'))
#MASTER YODA: Given a sentence, return a sentence with the words reversed 
def master_yoda(text):
    mystring = ''
    for x in text.split():
        mystring = x + ' ' + mystring
    return mystring

print(master_yoda('I am home'))

#Given an integer n, return True if n is within 10 of either 100, 0r 200

def almost_there(n):
    if abs(n-100) <= 10:
        return True
    elif abs(n-200) <= 10:
        return True
    else:
        return False
print(almost_there(200))


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
def has_33_2(nums):

    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

mynums = [3,4,3]
print(has_33(mynums))


#Given a string, return a string where for every character in the original there are three characters
#Hello -> HHHeeellllllooo
def paper_doll(text):
    result = ""
    for i in text:
        result = result + i*3
    return result
print(paper_doll("Hello"))

#Given three integers between 1 and 11, if their sum is less than or equal to 21,
#return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
#Finall, if the sum (even after the adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    sum = a + b + c
    if sum <= 21:
        return sum
    else:
        if (a==11) or (b==11) or (c==11):
            sum = sum - 10
            if sum <= 21:
                return sum
            else:
                return 'BUST'
        else:
            return 'BUST'
print(blackjack(9,9,9))

#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
#and  extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    y = False
    sum = 0
    for x in arr:
        if x == 6:
            y = True
        elif x == 9:
            y = False
        elif y == False:
            sum = sum + x
    return sum

print(summer_69([2,1,6,9,11]))


#write a function that akes in a list of integers and returns True if it contains 007 in Order

def spy_games(nums):

    code = [0,0,7,'x']

    for x in nums:
        if x == code[0]:
            code.pop(0)
    return len(code) == 1
        
print(spy_games([1,2,3,0,3,0,7,8]))

#Write a function that returns the number of prime numbers that exiist up to and including a given number

def count_primes(num):

    #check for 0 or 1 input
    if num < 2:
        return 0
    # 2 or greater
    primes = [2]
    #Counter going up to inpute num
    x = 3

    while x <= num:
        #Check if x is prime
        for y in range (3,x,2):
            if x%y ==0:
                x += 2
                break
        else:
            primes.append(x)
            x +=2
    print(primes)
    return len(primes)

print(count_primes(100))