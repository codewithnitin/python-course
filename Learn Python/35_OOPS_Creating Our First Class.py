class Student:
    pass
Harry = Student()
Larry = Student()

# print(Harry, Larry)

Harry.name = "Harry"
Harry.std = 12
Harry.section = "A"
Larry.std = 10
Larry.subjects = ["Hindi","English","Math","Science"]

print(Harry.std, Larry.subjects)
# print(Harry.std, Larry.name)

"""
Here, we created class name student generally we will have template in class but this 
is our first class program so we are using empty class or template naming student and
once we enter into it so there will be indentation we will write pass which tells there
is nothing or kuch nahi to aage chalo then we will drive instance of the class means
object Harry and Larry by above syntax and if we print instances of the class so we get
an output as class object at location

After creating instances or objects of the class we created instance variable or object
variable name, std and section etc then we print the instance variables by print function
to get an output of instance variables accordingly and if we pass invalid instance
variable into the print function so we will get an error which states class object has no
such attribute like we are passing Larry.name above but we did not create Larry.name 
instance so we will get an error.

Note : 

1 :  Generally we will have some blueprint or template in our class however we made
empty class here so to tell python interpreter this class is okay so please provide
approval to move ahead for further operation or task in program we type pass if we do
not write it so we will get an error here.

2 :  Instance variable could be nothing like string, integer, float number, List,
tuple etc.


"""