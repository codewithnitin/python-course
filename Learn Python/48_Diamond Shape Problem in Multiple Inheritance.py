"""
Diamond shape problem in Multiple Inheritance :

                                         A

                                    B         C

                                         D


We observe confusion to judge method from which class that belongs to if we have Diamond shape
problem in Multiple inheritance when we are using language like c++ & java even does not support
Multiple Inheritance that is why Multi-Level Inheritance is recommended.

In python we do not face any confusion or difficulty to judge the methods of classes in Diamond
shape problem in Multiple Inheritance because syntax or resolution of python is crystal clear
however Multi-Level-Inheritance is suggested to the Programmer as it is good to use as compared to
Multiple Inheritance as it avoids chances of confusion to judge methods of different classes.


"""

class A:
    def met(self):
        print("This is the method of class A")


class B(A):
    def met(self):
        print("This is the method of class B")


class C(A):
    def met(self):
        print("This is the method of class C")


class D(B, C):
    def met(self):
        print("This is the method of class D")



a = A()
b = B()
c = C()
d = D()

d.met()

"""
We know first d will search the method inside class D if does not find it out so will move to
class B which is first inherited by order of Inheritance and if does not find out then moves to
class C and if does not find there so moves to class A which is inherited by B and C.

So we observed we did not face much difficulty to find out method in python but overriding has 
been done alot here which creates confusion so we always recommend to use Single or Multi-Level
Inheritance.

"""