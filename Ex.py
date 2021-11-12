# Class 22
'''
class Bike:
    tyres = 2
    def __init__(self):
        self.name = "Activa 6G"
        self.year = "2023"
        self.mileage = "30KMPL"

bike = Bike()
Bike.tyres = 400
print(bike.name, bike.year, bike.mileage, Bike.tyres)

bike1 = Bike()
bike1.name = "HONODA"
bike1.year = "2020"
bike1.mileage = "50KMPL"
Bike.tyres =30
print(bike1.name, bike1.year, bike1.mileage, Bike.tyres) '''

'''
person = ['Ram', 'John001', 'Don', 'Suri', 'Siri']

for user in person:
    print(user) '''
'''
BestFriends = ['Ram', 'Akhil', 'M_B', 'Venkat']

for x in BestFriends:
    print(x)
    if x == 'Akhil':
        break
    #print(x)  '''

# Class 23

#Types of Methods in Class
'''
class Student:
    # Class or Static Vars

    school = "Sprogram001"
    def __init__(self):
        # Instance Vars
        self.marks1 = "Marks1"
        self.marks2 = "Marks2"
        self.marks3 = "Marks3"
    # Instance Methods (# Class Methods  # Static Methods  )
    # === Get Methods ==== Accessors
    def get_m1(self):
        return self.marks1

    def get_m2(self):
        return self.marks2

    def get_m3(self):
        return self.marks3



    # === Set Methods ===   Mutators

    def set_m1(self, value):
        self.marks1 = value

    def set_m2(self, value):
        self.marks2 = value

    def set_m3(self, value):
        self.marks3 = value

    # Class Methods
    @classmethod
    def get_school(cls):
        return cls.school

    # Static Methods
    @staticmethod
    def sayhello():
        print("Hello Student")




print("School_Name:", Student.get_school())
#Student.sayhello()

s1 = Student()

s2 = Student()

s1.set_m1(72)
s1.set_m2(92)
s1.set_m3(66)
print('Student 1 Marks:')
print(s1.get_m1(), s1.get_m2(), s1.get_m3())



s2.set_m1(77)
s2.set_m2(91)
s2.set_m3(71)
print('Student 2 Marks :')
print(s2.get_m1(), s2.get_m2(), s2.get_m3())
#s1.set_m1(72)
#print(s1.get_m1())

#s2.set_m1(55)
#print(s2.get_m1()) '''



# Types of Methos or static Vars
'''
class Student:
    school = 'Sprogram001'

    def __init__(self):
        self.marks1 = 'Marks1'
        self.marks2 = 'Marks2'
        self.marks3 = "Marks3"
    def get_m1(self):
        return self.marks1

    def get_m2(self):
        return self.marks2

    def get_m3(self):
        return self.marks3

    def set_m1(self,value):
        self.marks1 = value

    def set_m2(self,value):
        self.marks2 = value

    def set_m3(self,value):
        self.marks3 = value


s1 = Student()

s2 = Student()

s1.set_m1(89)
s1.set_m2(34)
s1.set_m3(43)
print(s1.get_m1(), s1.get_m2(), s1.get_m3())


s2.set_m1(89)
s2.set_m2(34)
s2.set_m3(343)
print(s2.get_m1(), s2.get_m2(), s2.get_m3()) '''

''''
# Types of Inheritance

class A:
    x = "How are you Due!"

class B:
    y = "Nothing"

class Z:
    z = "Dud!"

class Name:
    r = "SriRam"

print(" ")
obj = Name()
print(obj.r)
print(" ")
obj = A()
print(obj.x)
print(" ")
obj = B()
print(obj.y)
print(" ")
obj = Z()
print(obj.z)
print(" ")  '''


# Types of Inheritance
'''
class A:
    x = "Something"

class B:
    y = "Nothing"

class S:
    a = "Sunnam.Sriram"

o1 = S()
print(o1.a)
o1 = A()
print(o1.x)
o1 = B()
print(o1.y) '''





''''

class A: # Parent Class or Base Class
    x = "Something"

class B(A): # Child Class or Derived Class
    y = "Nothing"

obj = B()
print(obj.x) '''







''''
class A:  # Parent Class or Base Class
    x = "Something"

class B(A):  # Child Class or Dervived Class
    y = "Nothing"

obj = B()
print(obj.y)  '''


# Single Inheritance
''''
class Parent:
    def fun1(self):
        print("From Parent")

class Child(Parent):
    def fun2(self):
        print("From Child")

obj = Child()
obj.fun1()
obj.fun2() '''


# Multipule Inheritance

''''
class Mother:
    mother_name = " "
    def mom(self):
        print(self.mother_name)

class Father:
    father_name = " "
    def dad(self):
        print(self.father_name)

class Son(Mother,Father):
    son_name = " "
    def Shownames(self):
        print(self.son_name,'Mr','_',self.mother_name,"_",'Mrs',self.father_name)

obj = Son()
obj.son_name = "Ram"
obj.mother_name = "Subhadra"
obj.father_name = "Veerraju"
obj.Shownames()  '''

# Multilevel Inheritance
''''
class Apple:
    def john(self):
        print("From Apple")

class Orange(Apple):
    def fun2(self):
        print("From Orange")

class Banana(Orange):
    def fun3(self):
        print("From Banana")

fruit = Banana()
fruit.fun2()
fruit.fun3() '''


# Class 25
#
# Comments and Boolen
#
# print('Comment and Boolen')
#

# text = '''
# Theis is a comment written in three lines'''
#
# print(text)

#   Boolean

print('Boolean')

 # True or False

# print(0==99)
# print(9<10)


# if True:
#     print("This is True")
#
# else:
#     print('This is False')



# if 10 < 9:
#     print("This is True")
#
# else:
#     print('This is False')


# a = 99
#
# b = 12
#
# if a > b:
#     print("This is True")
#
# else:
#     print("This is False")

# a = 1
#
# x = " "
#
# print(bool(x))

mylist = {22 }


print(bool(mylist))







