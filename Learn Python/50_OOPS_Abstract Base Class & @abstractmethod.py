# from abc import ABCMeta, abstractmethod
#
# class Shape(metaclass=ABCMeta):
#     @abstractmethod
#     def printarea(self):
#         return(0)


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return(0)



class Rectangle(Shape):
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return(self.length * self.breadth)

class Square(Shape):
    sides = 4

    def __init__(self):
        self.length = 6

    def printarea(self):
        return(self.length * self.length)

rect1 = Rectangle()
rect2 = Square()
# tryobj = Shape()              # Note:  We cannot create object of abstract base class
print(rect2.printarea())


"""
Abstract Base Class : That is the class which gives order to its derived class to define the same
method which is defined into the base class as derived class cannot be executed until they use the
same method which is defined into the base class. ( Matlab ye esi class hoti hai jo aadesh deti hai
apni child classes ko ki jo method base class me hai woh toh mandate hai aapko rakhna otherwise 
derived class or child class will not execute ).

In python we have one module called abc which has two classes ABC, ABCMeta and decorator of
abstractmethod so in above approach we created one class Shape which inherits (metaclass=ABCMeta)
and after that we applied the abstract method decorator over the method which we define under the
base class like

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return(0)
        
So here it is mandate for all the child classes which inherit this abstract base class Shape to
define the same method printarea inside them otherwise those classes will not run or execute.

( So yaha Shape hogi abstract base class jo adesh degi Rectangle class or Square class ko jo
abstract class hai ya child class hai ki aapko agar execute hona hai toh mera define method
apne andar define karna he padega ) 

Note : If we are using python version 3.4 or below so to make abstract base class we will use
(metaclass=ABCMeta) and if we have version above 3.4 so we can use the ABC class of module abc
which would be easier to remember syntax.


Ex : class Shape(ABC):       OR        class Shape(metaclass=ABCMeta):


"""




