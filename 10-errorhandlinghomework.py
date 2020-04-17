#
#Problem 1

#Handle the exception thrown by the code below by using try and except blocks.
#for i in ['a','b','c']:
#    print(i**2)


try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("not a number")


#Problem 2

#Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

#x = 5
#y = 0

#z = x/y

try:
    x = 5
    y = 0

    z = x/y
except:
    print("can't divide by 0")
finally:
    print("All Done.")


#Problem 3

#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            result = int(input("Please enter an integer: "))
        except:
            print("Not an integer")
            continue
        else:
            break
    print(result**2)    
ask()
