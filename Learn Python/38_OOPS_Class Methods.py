"""
What we will study in this session ?

How to build class method with the help of built in classmethod decorator which
changes self into cls

(Agar hum class ke sath khilwad krna chahte hai generally hum class method bnate
hai toh self automatically aata hai to uski jagah cls matlab class ko la sakte hai
built in decorator classmethod ki help se ye padhenge hum isme)

"""



"""
Ex :

We know we can access class variables by instances of that class as well as by class
and if we wish to change the class variable so we can get it done by class only as
if we are going to change it with instances like Rohan.no_of_leaves so here we will
create one instance variable of Rohan in spite of changing the class variable

so we know we can change class variable by class only

If I want to change the class variable with the help of class method so we can also
do it and we will study how we can change the class variable with the help of
classmethod.


"""


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return(f"The name is {self.name} salary is {self.salary} and role is {self.role}")

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

Harry = Employee("Harry",2000,"Instructor")
Rohan = Employee("Rohan",500,"Student")

# print(Harry.salary,Rohan.role)
# print(Harry.printdetails())

# print(Employee.no_of_leaves)
# print(Rohan.no_of_leaves)

Harry.change_leaves(34)
print(Employee.no_of_leaves)

"""
In above approach we applied one built in decorator classmethod like @classmethod
and we know decorator enhances the functionality of function on which it is applied
so we applied it over the function or method def change_leaves(cls): 

Here cls comes up automatically in place of self due to @classmethod it changes
self into cls which is a class whose instances are Harry and Rohan means Employee

Now we know how we call method Harry.change_leaves(34) as we changed self into cls
due to @classmethod so Harry.change_leaves() will not pass object Harry as an argument
so we will give manual argument which is 34 and it will be assigned into the position
argument in declaration of method def change_leaves(cls, newleaves): so 34 will be
passed to new leaves and then we type cls.no_of_leaves = newleaves under this method
due to which we will change the class variable value with the help of class method
and if we print print(Harry.no_of_leaves) so will get an output 34 now.

Note : Here we learnt how we can pass argument into the class method by instances
or by class as well like 

Harry.change_leaves(34)
We could have written it by class as well Employee.change_leaves(34)





Note : classmethod is accessible by instances or objects of the class as well as
by class


"""


