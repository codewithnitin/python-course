class Employee:
    no_of_leaves = 8
    pass
Harry = Employee()
Rohan = Employee()

Harry.name = "Harry"
Harry.salary = 2000
Harry.role = "Instructor"
Rohan.name = "Rohan"
Rohan.salary = 500
Rohan.role = "Student"

# print(Harry.role,Rohan.salary)

# print(Employee.no_of_leaves)
# print(Harry.no_of_leaves)
# print(Rohan.no_of_leaves)
# Rohan.no_of_leaves = 9
# print(Rohan.no_of_leaves)
# print(Rohan.__dict__)

# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Harry.no_of_leaves)


"""
We created one class naming Employee which is an empty class or template so we will type
pass to let the python interpreter know this class is okay so provide approval to move
further in the program or code and after that we created instances of the class Employee
naming Harry and Rohan by above syntax then we created instances variables like name,
salary, role etc and then printed instances variables by print function so nothing is
changed as of now as we have already studied it in last session.

Here we will create one class variable named no_of_leaves = 8 under class Employee means
no_of_leaves will be same for each and every instances of that class so this class variable
can be printed by class itself like print(Employee.no_of_leaves) or this can also be
accessed by any instance of that class like print(Harry.no_of leaves) or print(Rohan.no_
of_leaves) etc means class variable is accessible by class itself as well as instances of
that class.

( class variable = Sarkari Property )

( instances varibales = Private Property jo virasat me nahi mili mtlb class se nahi mili) 

Now the question can we change the class variable value with the help of instances of that
class ?

Rohan.no_of_leaves = 9 it will create another instance variable means will increment
Rohan variable in spite of changing value of the class variable so if we print
print(Rohan.no_of_leaves) so output will 9 which is another instance variable so class
variable no_of_leaves will as same as 8 and if we print(Rohan.__dict__) so it will
print the attribute or variable of instance named Rohan which are name, salary, role and
no_of_leaves

We printed print(Employee.no_of_leaves) so will get an output same 8 and then printed
print(Employee.__dict__) to print attributes of the class Employee and then changed the
value of class varibale no_of_leaves like Employee.no_of_leaves = 9 and then we printed
print(Employee.__dict__) to print attributes of the class Employee we will get no_of_leaves
is 9 now as we have changed it and then printed print(Employee.no_of_leaves) which is 9
now so if we access no_of_leaves by class instances like print(Harry.no_of_leaves) still
will get an output as 9 as no_of_leaves which is class variable has been chnaged now.


Note : Class variable can be accessed by class as well as its instances and class variable
can be changed by class itself only.

print(classname.__dict__) gives an output attributes or variables of the class in the
form of dictionary.

Similarly, print(instancename.__dict__) gives an output attributes or variables of the 
instance in the form of dictionary.

Note : When we print print(Harry.no_of_leaves) so first instance Harry will check
no_of_leaves variable exits under Harry or not and if not so will move to class
variable as instances can access the class variable as well.


"""
