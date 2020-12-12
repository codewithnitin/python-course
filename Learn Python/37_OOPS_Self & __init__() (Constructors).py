# class Employee:
#     no_of_leaves = 8
#     def printdetails(self):
#         return(f"The name is {self.name} salary is {self.salary} role is {self.role}")
# Harry = Employee()
# Rohan = Employee()
#
# Harry.name = "Harry"
# Harry.salary = 2000
# Harry.role = "Instructor"
# Rohan.name = "Rohan"
# Rohan.salary = 500
# Rohan.role = "Student"
#
# # print(Harry.salary,Rohan.role)
#
# print(Rohan.printdetails())

"""
Here we will study how we can create method under the class ?

we will declare or define method like def methodname(self): here object of class is 
assigned as an argument in place of self when we call method like object.methodname()
here paranthesis will be like () now question is we did not pass object into the ()
the beauty of python or convention comes up here which automatically pass object as
an argument under () which will be assigning further into self of methodname(self)
under declaration of method then we can return instance variables under it with the 
help of f string like {self.variable}

Now will explain above example we created method def printdetails(self): here object of
class is assigned into self as an argument so class object would be Harry or Rohan when
we call this method like Rohan.printdetails() here object which is Rohan will be come
up automatically and will be assginging further into the declaration of method in place
of self then we return f string f"the name is {self.name} salary is {self.salary} role
is {self.role} so

self.name will be replaced by "Rohan"
self.salary will be replaced by 500
self.role will be replaced by "Student"

so return f string will be assigned into Rohan.printdetails() and if we print it by
print(Rohan.printdetails()) to display as an output like

The name is Rohan salary is 500 role is Student

Similarly, we can print the details of any other object like Harry as well just by
changing print(Harry.printdetails()) so here Harry will be assigned as an argument
automatically and further will be under declaration and then so on.



Note : To prove object is assigned automatically as an argument we can omit out self
from the declaration so we will get an error which states 0 positional argument but
1 was given.

(self) means that object on which we are applying this function or method


"""

"""
In above approach we created object or instance variable manually if it is possible
to pass argument as an instance variable values under class name function while creating 
object like Harry = Employee("Harry",2000,"Instructor") toh kitna acha ho jaye and if we
run it as of now so it will given an error Employee() takes no arguments

An approach to provide arguments which are instances variables values to the 
Employee() is known as Constructor and these arguments are handled by __init__ method
like def __init__(self, arg1, arg2, arg3...) 

Here, An object which is creating will be passed as an argument into self and then
corresponding object or instance variables values into arg1,arg2,arg3,..... which
we have assigned under Employee("Harry",2000,"Instructor")

People will tell we did not call __init__ so how it is happening that is the convention
or beauty of python as __init__ will execute all the things which we wish to perform
while creating object automatically( Kehte haina Construction chal rha hai matlab kaam
ho rha hai waise he __init__ object bnate samay jo bhi kaam hum chahte hai woh kar deta
hai this is beauty of Python )


Note : If we are passing arguments into classname function which is Employee() in example
so these arguments will be handled by __init__ function only and this approach is known
as Constructor.

__init__ performs all the operations automatically which we wish to execute while creating 
object or instances as __init__ is not called here it works automatically.

"""

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return(f"The name is {self.name} salary is {self.salary} and role is {self.role}")

Harry = Employee("Harry",2000,"Instructor")
Rohan = Employee("Rohan",500,"Student")

print(Harry.salary,Rohan.role)

# print(Rohan.printdetails())


"""
We pass arguments into the Employee() like Harry = Employee("Harry",5000,"Instructor")
which are instance varibales values so if we run it we will get an error states 
Employee() takes no argument then we will use __init__ function to pass arguments
to the classname() which is Employee() like

def __init__(self, aname, asalary, arole) here self is the object which is creating
means Harry and aname, asalary, arole which are arguments means Harry variables values

After declaring method def __init__(self, aname, asalary, arole): we will enter into
it to type like

self.name = aname
self.salary = asalary
self.role = arole

Here, self.name, self.salary and self.role are instance varibale and aname, asalary,
arole are arguments means instance varibales values

Now beauty of python will come into role as __init__ function perform those operations
automatically which we wish to execute while creating object like self.name = aname,
self.salary = asalary, self.role = arole in spite of calling __init__

Finally we will print(Harry.salary) so we will get the value of this instance variable
which is 2000 and same will be doing for the others variables.





Note : methods having argument self is only accessible by objects or instances of the class


"""
