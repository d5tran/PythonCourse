#Three key words
#try: , except: , finally:
#finall is always executed wheter or not there was an error

def add(n1,n2):
    print(n1+n2)

add(10,20)

number1 = 10
#number2 = input("please provide a number: ")
#add(number1,number2)
#print("Something happened")


try:
    #I want to attempt this code
    #May have an error
    result = 10 + '10'
except:
    #What I want to happen if there is an error
    print("Hey looks like you arent adding correctly")
else:
    #if there are no errors
    print(result)

try:
    f = open('testfile','w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("You have an OS error")
finally:
    #always executes no matter what
    print("I always run")

def ask_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops thats not a number")
            continue
        else:
            print("yes thank you")
            break
        finally:
            print("I will always run at the end")

ask_int()

