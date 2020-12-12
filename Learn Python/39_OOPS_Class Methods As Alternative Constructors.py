"""
What we will study in this session?

classmethod as Alternative constructors and will study how we can create instance
with the help of classmethod


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

Harry = Employee("Harry",2000,"Instructor")
Rohan = Employee("Rohan",500,"Student")
Hamad = Employee.from_dash("Hamad-5000-Driver")

Harry.change_leaves(34)
# Employee.change_leaves(34)
# Rohan.change_leaves(34)
# print(Rohan.no_of_leaves)

print(Hamad.printdetails())
print(Hamad.no_of_leaves)


"""
We created one class method def from_str(cls): with the help of built in classmethod
decorator then we call method from_str like Employee.from_str("Hamad-5000-Driver")
so we passed argument into the declaration def from_str(cls, string) so string is
assigned by argument "Hamad-5000-Driver" then under declaration like

def from_str(cls, string):
      params = string.split("-")
      return(cls(params[0],params[1],params[2])
      
Here we are applying split function on string so it spits the string by dash and
gives an output in the form of list so we will get list [Hamad 5000 Driver] then
return(cls(params[0],params[1],params[2]) means Employee(Hamad,5000,Driver) so
it will be replaced by calling function Employee.from_str("Hamad-5000-Driver")
which we are assigning into the instance or object Hamad like

Hamad = Employee.from_str("Hamad-5000-Driver") means Hamad = Employee(Hamad,5000,Driver)

so we made instance Hamad now and then we can print print(Hamad.role) so will get
an output Driver with the above __init__ as per concept as __init__ handles arguments
of class function or Employee()

we can also print print(Hamad.printdetails()) to print the details of Hamad in terms
of name, salary and role which are instance variables of Hamad object or instance.


Note : we can use the concept of args here if we wish to pass the elements of list 
as an argument so we can simply type return(cls(*string.split("-"))) Pythonic approach

cls(*string.split("-")) or Employee(*params) or Employee(*string.split("-"))

That is one liner return(cls(*string.split("-")) as we can save two lines like 

params = string.split("-")
return(cls(params[0],params[1],params[2])




Note : classmethod is accessible by instances or objects of the class as well as
by class


"""