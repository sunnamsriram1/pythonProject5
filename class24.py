'''
class A:
    x = 'Something'

class B:
    y = 'Nothing'


o1 = A()
print(o1.x)

o1=B()
print(o1.y) '''

''''
class A:  # Parent class or Base class
    x = 'Somthing'

class B(A): # Child class or Derived class
    y = 'Nothing'

obj = B()
print(obj.x) '''


# Single Inheritance
'''
class Parent:
    def fun1(self):
        print("From Parent")
class Child(Parent):
    def fun2(self):
        print("From Child")

obj=Child()
obj.fun1()
obj.fun2() '''


# Multiple Inheritance

class Mother:

    mother_name =" "
    def mom(self):
        print(self.mother_name)

class Father:
    father_name =" "
    def dad(self):
        print(self.father_name)

class Son(Mother,Father):
    son_name =" "
    def shownames(self):
        print(self.son_name,'s/oMr.@Mrs.',self.mother_name,'_',self.father_name)

obj = Son()
obj.son_name = "Ram Charn"
obj.mother_name = "K.Surekha"
obj.father_name = "Chiranjeeve"
obj.shownames()