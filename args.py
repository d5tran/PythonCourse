#*args and **kwargs

def myfunc(a,b):
    #returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

#*args will be treated as a tuple after passed in
def myfunc2(*args):
    return sum (args) * 0.05

print(myfunc2(4,5,6,76,8,9))

#**kwargs builds a dictionary of keyword arguments

def myfunc3(**kwargs):
    if 'fruit' in kwargs:
        print(f"my fruit of choise is {kwargs['fruit']}")
    else:
        print('I did not find any fruit here')

myfunc3(fruit = 'apple')

def myfunc4(*args,**kwargs):
    print (f"I would like {args[0]} {kwargs['food']} ")

myfunc4(10,20,30,fruit='organge',food='eggs',animal='dog')


#