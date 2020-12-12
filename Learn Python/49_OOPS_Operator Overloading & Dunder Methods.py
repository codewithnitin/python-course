"""
Dunder method : These are some special methods which execute their work inside itself means we do not
need to call them and it starts from __ and ends with __

Example : __init__           ( Dunder init or constructor as we know whatever we want to perform while
creating object __init__ execute it automatically)

__truediv__       ( Dunder truediv it gives division of two objects )

__add__           ( Dunder add it gives addition of two objects )

Operator overloading : In OOPS, Operator overloading can be achieved only with the help of special
methods called Dunder methods and two objects of the class.


"""

class Employee:
    no_of_leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return(f"The name is {self.name}, salary is {self.salary} and role is {self.role}")

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # return(cls(params[0],params[1],params[2]))
        return(cls(*string.split("-")))

    @staticmethod
    def printgood(string):
        print("This is a good", string)
        return("Thenga")

    def __add__(self, other):
        return(self.salary + other.salary)

    def __truediv__(self, other):
        return(self.salary / other.salary)

    def __repr__(self):
        # return(f"The name is {self.name}, salary is {self.salary} and role is {self.role}")
        return(f"Employee('{self.name}',{self.salary},'{self.role}')")

    def __str__(self):
        return(f"The name is {self.name}, salary is {self.salary} and role is {self.role}")

    def __mul__(self, other):
        return(self.salary * other.salary)

    def __sub__(self, other):
        return( self.salary - other.salary )

    def __pow__(self, power, modulo=None):
        return(self.salary ** emp2.salary)




emp1 = Employee("Harry", 500, "Programmer")
emp2 = Employee("Rohan", 100, "Cleaner")
# emp3 = Employee.from_dash("Hamad-320-Accountant")

# print(emp1 + emp2)
# print(emp1 - emp2)
# print(emp1 * emp2)
# print(emp1 / emp2)
# print(emp1 ** emp2)
# print(emp1)

"""
We created two objects emp1 and emp2 if we print print(emp1 + emp2) so python interpreter will confuse
how to add these two objects emp1 and emp2 ( bhokhla jayega ki kaise add krun inki salary inke naam
inke role ) due to which we have dunder add method by which we can easily add two objects like

    def __add__(self, other):
        return(self.salary + other.salary)
    
so once we print print(emp1 + emp2) so here emp1 will be assigned to self and emp2 in other which returns
self.salary so we know what would be the output of self.salary in constructor and similary emp2 will
also follow constructor to get the output other.salary and result would be 600.

Similar process will be held for __truediv__ which gives division of two objects, __sub__ which gives
substraction of two objects and __mul__ gives multiplication of two objects.

We also have one dunder exponential __pow__ which gives power with the help of two objects like

    def __pow__(self, power, modulo=None):
        return(self.salary ** emp2.salary)
        
so once we print print (emp1 ** emp2) so here emp1 will be assigned to self then power will come and
then module=None here None will be replaced by emp2 ) so this method returns 
return(self.salary ** emp2.salary) so in above approach if self.salary = 5 and emp2.salary = 3 then
output would be 125.

"""

"""

Note : Dunder methods can be used for operator overloading as well as for others use like __init__,
__repr__, __str__ etc here we did not use operator actually however these are dunder methods.


Suppose we print print(emp1) so it gives an output <__main__.Employee object at 0x008AC1A8> ( Ye 
location deta hai class Employee ke object emp1 ki bhot he bhadha sa lagta hai ye so to print
it in a meaningful manner we use dunder repr __repr__ which can return anything but generally it is
returned like 

    def __repr__(self):
        # return(f"The name is {self.name}, salary is {self.salary} and role is {self.role}")
        return(f"Employee('{self.name}',{self.salary},'{self.role}')")
        
so if we print print(emp1) now so will get an output Employee('Harry',500,'Programmer') in a systematic
manner.



If we want to define the object emp1 so we have dunder str __str__ like

    def __str__(self):
        return(f"The name is {self.name}, salary is {self.salary} and role is {self.role}")
        
so if we print print(emp1) it will give an output like The name is Harry, salary is 500 and role is
Programmer even repr method is present in the code.


Note : If __repr__ and __str__ both are present in the code so if we print object like print(emp1)
it will print __str__ output until we call repr like print(repr(emp1)) ( Matlab str hai toh str he print
hoga jabtak ki keh kar call na kare repr ko like print(repr(emp1)) agar str nhi hai toh phr chahe
print(emp1) kare ya print(str(emp1)) kare ya phr print(repr(emp1)) kare repr ka output he print hoga )


Very important : __init__, __repr__, __str__ executes one object at a time and doest not use any operator
however __add__, __sub__, __truediv__ , __mul__,  __pow__ gives output with the help of two objects
along with operator (Operator overloading hoti hai yaha )

WE CAN ALSO OVERRIDE DUNDER METHODS IN DERIVED CLASS

"""



