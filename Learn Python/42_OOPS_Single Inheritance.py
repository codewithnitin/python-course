"""
Inheritance : In real life, those similarities are got by child from his/her parents is known
as Inheritance.

Ex : 1)  Aap ke papa gore hai toh aap bhi gore ho sakte hai
     2)  kisi ke papa ki nose lambi hai toh unke bache ki nose bhi lambi ho sakti hai



Similarly in OOPS : If we copy one class A into class B so class B will inherit class A means
class B will have all the features of class A like class variables, instance variables,
methods, classmethod and staticmethod etc along with the features of class B itself.

Example which is given below :

We have base or main or super class Employee & class Programmer which inherits the class
Employee features in terms of class variables, instance variables, methods, classmethod &
statocmethod etc along wth the features of itself.

( Matlab Programmer class me jo uske features hai woh toh hai he aur woh Employee class ke
features or sare gunn ko bhi use kar sakti hai ye he hota hai Inheritance )


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




Harry = Employee("Harry", 500, "Instructor")
Rohan = Employee("Rohan", 700, "Student")
Hamad = Employee.from_dash("Hamad-900-Monitor")


# print(Harry.salary, Rohan.role)
# print(Rohan.no_of_leaves)

# print(Hamad.printdetails())

# Harry.change_leaves(34)
# Employee.change_leaves(34)
# print(Hamad.no_of_leaves)

# print(Rohan.printgood("boy"))

class Programmer(Employee):
    no_of_holidays = 14


    def __init__(self, aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguages


    def printprog(self):
        return(f"The programmer's name is {self.name}, salary is {self.salary}, role is {self.role} and languages {self.language}")


    @classmethod
    def change_holidays(cls, newholidays):
        cls.no_of_holidays = newholidays


    @classmethod
    def from_slash(cls, string):
        return(cls(*string.split("/")))


    @staticmethod
    def printgood1(string):
        print("This is me", string)
        return("baba ji ka thulu")


Shubham = Programmer("Shubham", 800, "Programmer", ["python"])
Karan = Programmer("Karan", 900, "Programmer", ["python", "c++"])
Ayush = Programmer.from_slash("Ayush/950/Programmer/[python]")

# print(Karan.printprog())
# print(Karan.printdetails())

# print(Shubham.no_of_leaves)
# print(Karan.no_of_holidays)

# Shubham.change_holidays(15)
# Programmer.change_holidays(15)
# print(Shubham.no_of_holidays)
# print(Programmer.no_of_holidays)

# print(Ayush.printprog())
# print(Ayush.printdetails())

# print(Ayush.printgood1("Nitin"))
# print(Ayush.printgood("guy"))


"""

Single Inheritance : When one class inherits one class or one class is derived from one class is known
as Single Inheritence.



First of all we created one class Programmer now the question how to inherit class Employee
by class Programmer

There is one way we can copy the whole code from no_of_leaves till instance formation 
Hamad = Employee.from_dash("Hamad-900-Monitor") like

class Programmer:
    whole code copied of class Employee
    
If we do so we will loose code reuse ability as we do not wish to repeat ourselves ( Hum
code reuse ability ko kho denge agar copy karenge kyuki hum repeat nahi karna chahte )

So we will do like this

class Programmer(Employee):
    pass
    
Due to which we created class Programmer which inherits the class Employee all the features or
gunn like class variables, instances variables, method, classmethod & staticmethod etc.

Suppose we have two programmer Shubham and Karan which have attributes name, salary, role and
languages they know so if we are using the constructor of class Employee we can use it as
constructor of class Employee has instance attributes name, salary and role but we are passing
one more argument here which is language so there will be a problem.

To avoid this problem we will create a new constructor under class Programmer which accepts
name, salary, role and language as an instance attributes of this class then we created a
method printprog which prints the details of the objects of class Programmer like print
print(Karan.printprog()) which will be showing name, salary, role and language as well as 
Karan can use the printdetails() like print print(Karan.printdetails()) which will be showing
name, salary and role so here Karan will have access of printdetails as well which comes from
class Employee this is called Inheritance

Shubham can print no_of_leaves like print(Shubham.no_of_leaves) which is class variable of 
class Employee but can change the class variables of Programmer with the help of classmethod
of programmer class as well as change class variable of super class as Programmer class
inherit the base or super class Employee after that if we are going to change class variable
directly with the help of instance like Shubham.no_of_holidays = 15 so it will create a new 
instance variable in spite of changing to the no_of_holidays)

Then I used classmethod as Alternative method to build one instance of Programmer class which
is Ayush by above approach and then we can apply printdetails as well as printprog method on
Ayush easily and last I created one static method printgood1 above




Note : When I created a new constructor which will have instance variables name, salary, role 
and language so copied Employee class code like

       self.name = aname
       self.salary = asalary
       self.role = arole
       self.language = alanguages
       
So we lost code reuse ability concept here as we do not wish to repeat ourselves.

To avoid it we have one feature called super by which we can call __init__ of super class to
perform it in spite of copying so we will study use of super later.


To prove this test :


If we keep the cursor on __init__ of class Programmer so it tells call to __init__ of super 
is missed means it gives an alert use super to call super class __init__ instead of 
copying and lossing the code reuse ability.




One most important thing which needs to be noted if we made object of class Programmer like
Shubham and Karan and we know object is made due to constructor so that object must try to
use base or main or super class constructor first of all if we would have same attributes
name, salary and role in object of class Programmer so there will no need to build a new
constructor however we are having one more attribute which is language and constructor of
super class accepts 3 attrbutes name, salary and role that is the reason we created a new
constructor of class Programmer which accepts one more attribute which is language and there
is a warning as this is not a right approach as we are loosing code reuse ability concept
here so we will use super here which will be studied later. ( Ab base class ka nahi Shubham
constructor use krega instance variables name, salary, role ke liye bhi Programmer class
ka constructor he jo ki code reusebility ko kho deta hai agar super use krte toh ye common
instance attributes super class ke constructor se utha lete and programmer class ke constructor
me sirf ek extra language instance attribute rkhte toh code reuse ability kharab nhi hoti ) 


Similarly goes to method suppose Shubham is using printdetaiils method and we know printdetails
return(f"The name is {self.name}, salary is {self.salary} and role is {self.role}") so there 
will be need of three instance attributes are Shubham.name,Shubham.salary and Shubham.role
so here constructor will be used by Programmer class as it accepts instance variables name,
salary and role and this concept will work on all the methods , classmethods, staticmethods
etc.

NOTE : Always check the constructor of the class which is present or current class if do not
get the instance attributes so can use super class constructor with the help of super for
common instance attributes and rest instance attributes we can create in current class constructor
and if we do not use super and we have one more argument in current classname function rather
than super class constructor so we will need to create current class constructor and it will 
loose code reuse ability concept.

       




"""










