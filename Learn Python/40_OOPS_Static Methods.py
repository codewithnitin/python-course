"""

staticmethod : If we wish to build the function or method which we were using earlier
in python in spite of taking input argument as self or cls so we can create it with
the help of staticmethod decorator and now we will study how we can do it.


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

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # return(cls(params[0],params[1],params[2]))
          return(cls(*string.split("-")))

    @staticmethod
    def printgood(string):
        print("This is a good", string)
        return("Thenga")


Harry = Employee("Harry",2000,"Instructor")
Rohan = Employee("Rohan",500,"Student")
Hamad = Employee.from_dash("Hamad-5000-Driver")

Harry.change_leaves(34)
# Employee.change_leaves(34)
# Rohan.change_leaves(34)
# print(Rohan.no_of_leaves)

# print(Hamad.printdetails())
# print(Hamad.no_of_leaves)

# Harry.printgood("boy")
# Employee.printgood("boy")

print(Rohan.printgood("boy"))
# print(Employee.printgood("boy"))



"""
First of all we applied builtin decorator of staticmethod which is used when we do
not want input self or cls as an argument and we wish to use function or method
under class as we were using earlier in python (Before OOPS matlab normal function
ki tarah kaam karega jaise humne phele padha hai function)

So first we applied builtin decorator of staticmethod like @staticmethod then type
method def printgood(): now we will not get self or cls as an argument automatically
and we can provide argument straight away here if we want to as per our ease like

    @staticmethod
    def printgood(string):
        print("This is a good", string)
    
    
Here we can call this static method by instances of the class or by class aswell

Harry.printgood("boy")
Employee.printgood("boy")

Once we call it so we will get an output : This is a good boy

Note : if we type print(Employee.printgood("boy")) so output would be

This is a good boy
None

This is because when method is called by Employee.printgood("boy") so it will print
output this is a good boy under declartion or definition of staticmethod printgood

Now question is why did this None came?

As we printed print(Employee.printgood("boy")) so first line this is a good boy
was printed due to method call Employee.printgood("boy") and we also printed by
print function like print(Employee.printgood("boy")) so this print function will
give new line charactor and the return value of staticmethod as we did not return
anything so it prints None and if we return something so that return value is
replaced by Employee.printgood("boy") so return value will be come up under
print(return value) as it is replaced by print(Employee.printgood("boy"))

For example : If we return "Thenga" so we will get output as Thenga instead of None
    


Note : static method is also accessible by instances or objects of the class as
well as by class



"""



