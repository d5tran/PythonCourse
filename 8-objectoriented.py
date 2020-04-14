#by convention classes are capitlized
class Dog():
    #Class object attribute are defined above init method.
    #These are the same for any instance of a classs
    #don't need to use the self keyword because it's the same for all classes therefor all instances
    species = 'mammal'

    
    #Paramters passed in when creating the object
    #Init gets called automatically when creating a new object (contructor)
    #self is the instance of the object itself00
    def __init__(self,breed,name,spots):
        #Attributes are characteristics of the object
        #Assign the argument using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

    #Methods are functions of a class
    #Operations/actions
    #self refers to the particular instance of the ojbect created
    def bark(self):
        print(F"WOOF My name is {self.name}")

my_dog = Dog('lab','Rex',True)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
my_dog.bark()

class Circle():
    #Class object attribute (Should always be true regardless of the instance)
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
    
    #Method
    def get_circumference(self):
        return self.radius * self.pi * 2
        #OR instead of using self.pi you can use Circle.pi

my_circle = Circle()
my_circle3 = Circle()

Circle.pi = 3
print(my_circle.get_circumference())
print(my_circle.pi)

#Inheritance

class Animal():
    def __init__(self):
        print('Animal created')
    def who_am_i(self):
        print('I am an animal')
    def eat(self):
        print ('I am eating')

#Inherit by using the original class
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat Created")
    #overwrite methods of the base class
    def who_am_i(self):
        print("I am a cat")

cat = Cat()
cat.eat()
cat.who_am_i()

#Polymorphism
#When each class share a specific method name, you can leverage it by passing in different objects but call the same method on it
class Bird():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says tweet"

class Hamster():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says squeek"

tweety = Bird("Tweety")
print(tweety.speak())
hamtaro = Hamster("Hamtaro")
print(hamtaro.speak())

for pet in [tweety,hamtaro]:
    print(type(pet))
    print(type(pet.speak()))


def pet_speak(pet):
    print(pet.speak())

pet_speak(hamtaro)

#abstract classes pretty much only serve as a base class
#example: Animal() class


class Animal2():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract Method")

#Special Methods

mylist = [1,2,3]
len(mylist)


class Sample():
    pass
mysample = Sample()
#This won't work
#len(mysample)

#Special methods/Dunder methonds

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    #Special method that returns a string representation 
    def __str__(self):
        return f"{self.title} by {self.author}"
    #Special method that returns a length representation
    def __len__(self):
        return self.pages
b = Book('Python rocks', 'Jose', 200)
print(b)
print(len(b))

#Homework
#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return (((self.coor1[0] - self.coor2[0])**2) + ((self.coor1[1] - self.coor2[1])**2))**(1/2)
    
    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
line = Line((3,2),(8,10))
print(line.distance())
print(line.slope())


#Fill in the class
class Cylinder:
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (self.pi)*(self.radius**2)*(self.height)
    
    def surface_area(self):
        return (2*(self.pi)*(self.radius)*(self.height))+((2*self.pi)*(self.radius**2))
    
cylinder = Cylinder(2,3)
print(cylinder.volume())
print(cylinder.surface_area())


#Challenge Problem

# Object Oriented Programming Challenge

# For this challenge, create a bank account class that has two attributes:

#     owner
#     balance

# and two methods:

#     deposit
#     withdraw

# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit Accepted")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable")

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}"

myaccount = Account("Dave",100)
print(myaccount)

myaccount.deposit(100)
print(myaccount)
myaccount.withdraw(10)
print(myaccount)
myaccount.withdraw(1000)
    


