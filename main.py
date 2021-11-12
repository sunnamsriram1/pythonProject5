# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Sunnam Sriram')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/ '''

'''
print("")
print("Exam Result's")
print("")
marks = 12

if marks >= 35:
    print("You Pass the Exam!", marks)
else:
    print("You are Failed:", marks) '''

'''
print("Exam Result:")

marks = 100

if marks == 35:
    print("YOu are Promoted", marks)
elif marks >= 35:
    print("You are Passed the Exam Marks!", marks)
else:
    print("You Failed! Marks", marks)  '''
'''
print("Exam Result'S")

marks = 46

if marks == 35:
    print("Promoted Marks:", marks)
    print("Congrates!")
elif marks > 35:
    print("")
    print("You are the Passed! Marks:", marks)
    if marks > 75 and marks <= 85:
        print("C garde the Marks:", marks)
    elif marks > 85 and marks < 90:
        print("B garde the Marks:", marks)
    elif marks > 98:
        print("A garde the Marks:", marks)
        print("#___Respect Boy_#")
    else:
        print("Devil Girl Better then Next Time")
else:
   print("You Failed! Dud: Marks", marks) '''



# Class 10 While Loop
'''
c = 0
while c <= 10:
     c += 1
     print(c, "Sprogram001")
     #if c == 3:
      #   print(" C value is 3 Now")
       #  continue
    # print(c, "Sprogram001")
         #break
    # c += 1 '''

# Class 11 For Loop
'''
for x in range(1, 50, 5):
    print(x)

person = ['Rafique', 'Samer', 'Vikram', 'Srikanth']
for user in person:
    print(user) '''



















# Class 22

# Types of Variables in Class
'''
print("Hello World")

class Bike:
   # Class or Static Variables
    tyres = 2
    def __init__(self):
        # Insttance Variables
        self.name = "Activa 6G"
        self.year = "2020"
        self.mileage = "40KMPL"


bike = Bike()
bike.tyres = 2
print(bike.name, bike.year, bike.mileage, Bike.tyres)
#print(bike.name)
#print(bike.year)
#print(bike.mileage)

bike2 = Bike()

bike2.name = "Unicorn"
bike2.year = "2021"
bike2.mileage = "50KMPL" 
Bike.tyres = 2
print(bike2.name, bike2.year, bike2.mileage, Bike.tyres) '''






# Class 23
'''
class Student:
    # Class or Static Vars
    school = "Sprogrm001"

    def __init__(self):
        # Instance Vars
        self.marks1 = "Marks 1"
        self.marks2 = "Marks 2"
        self.marks3 = "Marks 3"
        #Instance Methods #Class Methods # Static Methods

        # == Get Methods ===
    def get_m1(self):
            return  self.marks1  




s1 = Student()
s2 = Student()

#s1.marks1 = 81
#print(s1.marks1)

print(s1.get_m1())
print(s2.get_m1())   '''

# Python 23

# Types of Methods in Class
''''
class Student:
    # Class or Static Vars
    school = "Sprogram001"
    def __init__(self):
        # Instance Vars
        self.marks1 = 'Marks1'
        self.marks2 = 'Marks2'
        self.marks3 = 'Marks3'

    # Instance Methods (# Class Methods # Static Methods)

    # === Get Methods ===  Accesors
    def get_m1(self):
        return self.marks1

    def get_m2(self):
        return self.marks2

    def get_m3(self):
        return self.marks3

    # === Static Methods === Mutarors
    def set_m1(self,value):
        self.marks1 = value

    def set_m2(self,value):
        self.marks2 = value

    def set_m3(self,value):
        self.marks3 = value

    # Class Methods
    @classmethod
    def get_school(cls):
        return cls.school

    # Static Methods
    @staticmethod
    def sayhello():
        print("Hello, Student")

print("School_Name:", Student.get_school())

s1 = Student()

s2 = Student()

s1.set_m1(72)
s1.set_m2(92)
s1.set_m3(66)
print("Student 1 Marks")
print(s1.get_m1(), s1.get_m2(), s1.get_m3())

s2.set_m1(77)
s2.set_m2(91)
s2.set_m3(71)
print("Student 2 Marks")
print(s2.get_m1(), s2.get_m2(), s2.get_m3())  '''




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

class Apple:
    def john(self):
        print("From Apple")

class Orange:
    def fun2(self):
        print("From Orange")

class Banana(Orange):
    def fun3(self):
        print("From Banana")

fruit = Banana()
fruit.fun2()
fruit.fun3()











































