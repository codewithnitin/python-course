"""

Real life example of Public , Protected and Private access specifier

Suppose I have one page in which I write some information and paste it outside wall of the house
so if people want to read it they can means I have shared this information to all which is Public.

If I wish that information is read only by members of the house I we can paste it on the wall of
drawing room so that is an example of Protected means that information is only accessible by members
of the family.

If I paste that information inside my room where nobody can enter so it is an example of Private.


"""



class Employee:
    no_of_leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def __printdetails(self):
        return(f"The name is {self.name}, salary is {self.salary} and role is {self.role}")


class Programmer(Employee):
    no_of_leaves = 7
    language = ["python", "c++"]

    def printprog(self):
        return(f"The programmer name is {self.name}, salary is {self.salary} and role is {self.role}")

    @classmethod
    def change_leaves(cls):
        cls.no_of_leaves = 9

    @classmethod
    def from_slash(cls, string):
        return(cls(*string.split("/")))

    @staticmethod
    def printlanguage():
        print(f"The languages are {Carry.language}")




Harry = Employee("Harry", 55000, "Instructor")
Larry = Employee("Larry", 15000, "Student")
Carry = Programmer("Carry", 40000, "Programmer")
Marry = Programmer.from_slash("Marry/42000/Programmer")

print(Marry._Employee__printdetails())


"""
Access specifiers : These are the utilites by which we can enforce sort of protection to the access of 
the class variables and methods.

Why we are using the term sort of protection ?

This is because python is the language which does not enforce or apply restriction to access anything
means if something is designed to access in a specific area still this can be accessible from outside
this area.


So in short we learnt we do not have access specifiers in python (Kyunki python kisi kaam ko hone se
rokta nahi) like we have in c++ or java however python has some convention which acts with some sort
of protection like public, protected and private access specifiers.



Public : If class variables and methods are declared as Public then they can be accessible from
outside the class here outside means outside the class, derived class with the help of concept
Inheritance and outside anywhere ( chahe to aur bahar se bhi kar sakte hai )

Convention : If we do not use single or double underscore before class variables and methods so it
will be acted as Public.

All the members (normal variable outside OOPS, class variables and methods) in python are public 
by default.


Protected : It is as similar as public but little bit different.

Now the question how it is different ?

Suppose we are working in OOPS where we create class variables and methods and if we use one underscore
before variables and methods so we describe please use it outside class and by its dervied classes
only with the help of concept Inheritance (par chahe to aur bahar se bhi kar sakte hai python rokega nhi)



If class variables and methods are declared as Protected then they can be accessible from outside 
the class here outside means outside the class, derived class only with the help of concept Inheritance
(Optional bhar se bhi kar sakte hai access kyunki python rokega nahi )

Convention : Programmer uses single underscore _ before class variables and methods so it shows these
are protected means programmer describes to use it by outside class and by its derived class only however
this can also be accessible from outside more if somebody wants to.

Note : _ is using before class variables and methods to describe please use it outside class and by its
derived class only ( par chahe access karna aur bahar se toh rokega nahi python and _ yaha sirf class
variables and methods ko public se hatke dikhane ke liye lagaya hai waise syntactically koi protection
nahi lag jaati ese tbhi chahe to bahar kahi aur se bhi access kiya ja sakta hai)


Private : If class variables and methods are declared as Private so they can only be accessible under
the class & with the help of methods which are in public nature so we will be calling public method
and they will execute private variables accordingly and if we try to access it outside the class so
we will get an error class object has no such attribute even we would have that attribute.

Convention : __ before variable is used to show this variable or method is private.

Note : Generally, we cannot access private variables and methods outside the class however there is one
convention in python available by which we can also access it outside the class and this convention is
known as Name Mangling.

Syntax of Name Mangling : object._class__variable



Ex : 

class Player:
    no_of_games = 4
    
    def printplay(self):
        return(f"The Player name is {self.name} and games {self._game} and state is {self.__state}")
        


Rohan = Player()
Sohan = Player()
Rohan.name = "Rohan"
Rohan._game = ["Cricket", "Footbal"]
Rohan.__state = "Delhi"
Sohan.name = "Sohan"
Sohan._game = ["Cricket", "Tennis", "Football"]
Sohan.__state = "Haryana"

Note : Here name, _game, __state all are public variables as these are created outside the class
so inside or outside class variables without convention are called public but protected and private
are declared under class only.

Protected : By putting _ before variable and method name ( Kehne ke liye hai ki class se bahar and 
derived class me he use karna par chahe toh bahar se bhi kara ja sakta hai rokega nahi python 
interpreter and _ yaha sirf ye batane ke liye hai ki public nahi hai variable and method )  


Private : By putting __ before vairable and method name ( Ye sirf class ke andar he access hota hai
woh bhi kisi public ya protected method ki help se kyuki we will call to that method which is public
or protected so indirectly we will execute private ones and class ke bahar access nahi hota hai par
ek convention se bahar bhi kar sakte hai woh hai Name Mangling )







"""








