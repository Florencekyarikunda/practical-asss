# class Student:
#     school = "AkiraChix"

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age 
    
#     def speak(self):
#         return f"Hello my name is {self.name}, I am {self.age} years old and I love {self.school}."

# class Employee:
#     school="AkiraChix"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def __repr__(self):
#         return f" Hello,{self.name}, you are age {self.age} years old and welcome to school {self.school}"


# ja=Employee("James",29)
# print(ja)

# class Dog:
#     def bark(self):
#         print("Ham-Ham")

# charlie=Dog()
# charlie.bark()

# class Car:
#     pass
# ferrari=Car()

class my_class:
    message="I am a student from lovelace"

x= my_class()
y=my_class()

print(x.message)
print(y.message)

class Animal:
    def __init__(self,voice):
        self.voice=voice

cat=Animal(voice="Meow")
print(cat.voice)

dog=Animal(voice="Woo")
print(dog.voice)

a=2
print(type(a))

a=1.9
print(type(a))

a='b'
print(type(a))


class Employee:
    def __init__(self,name):
        self.name=name

    def print_name(self):
        print("Hi, i am" +self.name)        

print(dir())
print(dir(Employee))

class Person:
    def __init__(self,message,name,fees):
        self.message=message
        self.name=name
        self.fees=fees


str1=Person("Hello you","Maina",3900)
print(str1.message)
print(str1.name)
print(str1.fees)

class People:
    def you(self,country,salary):
        self.country=country
        self.salary=salary
        
    print("Uganda", 560000)

class Child(People):
    def child(self):
        print("Child")

    
childr=Child()
childr.you("Uganda", 560000)

class Animal:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs

class Dog(Animal):
    def sound(self):
        print("woof")

ky=Dog("Yoki",5)
print(ky.name)
print(ky.legs)
ky.sound()

        
def findArea(r):
    PI=3.14
    return PI*(r*r)

print("Area of a circle= %.6f"%findArea(6))
        

def Area(r):
    PI=3.14
    return PI*(r*r)

print("Area of the circle=%.6f" %Area(6))


class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.14*(self.radius **2)
    def perimeter(self):
        return 2*3.14*self.radius



obj=Circle(7)
print("Area of the circle:",obj.area())
print("Perimeter of a circle:",obj.perimeter())



class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.14* (self.radius**2)
    

are=Circle(4)
print("Area of the circle:",Area.area())


Num=5
Factorial=1
if Num < 0:
    print("Factorial does not exist for negative numbers")
elif Num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,Num+1):
        Factorial=Factorial*1
    print("The factorial of ",Num,"is", Factorial)


def sub(self,num1,num2):
    self.num1=num1
    self.num2=num2
    return (num1,num2)

print(sub(num2=90,num1=23)) 


year=2024
if(year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is a leap year ".format(year))
else:
    print("{0} is not a leap year".format(year))            
