class Employee:
    Var = 8
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



class Player:
    Var = 9
    no_of_games = 4

    def __init__(self, bname, bgame):
        self.name = bname
        self.game = bgame

    def printplay(self):
        return(f"The Player's name is {self.name} and game {self.game}")


class Coolprogrammer(Employee, Player):
    Var = 10
    language = "python"

    def __init__(self, cname, csalary, crole, cgame):
        self.name = cname
        self.salary = csalary
        self.role = crole
        self.game = cgame


    def printlanguage(self):
        print(self.language)

    def printprog(self):
        return(f"The coolprogrammer's name is {self.name}, salary is {self.salary}, role is {self.role} and game {self.game}")


Harry = Employee("Harry", 500, "Instructor")
Rohan = Employee("Rohan", 700, "Student")
Shubham = Player("Shubham", ["Cricket"])
Karan = Coolprogrammer("Karan", 2999, "Programmer", ["Cricket, Football"])
print(Karan.Var)



"""

Multiple Inheritance : When one class inherits two or more classes or a class is dervied from two or more
classes so this is called Multiple Inheritance.



We created two class Employee which we had created earlier in OOPS with all the class variables, object 
variables , classmethod and staticmethod etc and then we created another class Player which is separate
class means this is not inheriting class Employee which has two object attributes name and game, one
one class variable no_of_games and method printplay to print the details of the object of class Player.

After that we created a class Coolprogrammer which inherits above two class Employee and Player means
Coolprogrammer has access of all the features of both class Employee and Player and now when we create
an object Karan = Coolprgrammer() so if run it so it will give an error states Coolprogrammer accepts
4 positional arguments and none was provided.

We know class function Coolprogrammer() takes no argument which we had read earlier and to pass arguments
to it we have constructor with the help of __init__ and now the question is we did not create any constructor
under class Coolprogrammer so after that it will find constructor in the class which we will assign under
Coolprogrammer(Employee, Player) means it will find constructor into the class Employee and if we pass
arguments name, salary and role only so it will get approval from constructor of Employee and then can
print method printdetails here easily like Karan.printdetails() as it accepts three object attributes which
are name, salary and role.

If we type Karan.printplay() so same Karan has three attributes name, salary and role and first it will find
constructor under its class Coolprogrammer where we did not create constructor and then it will follow order
to find consturctor so will move to class Employee and where it will get constructor which accepts three
instance variables like name, salary and role and then it will find method printplay under class Employee
if it will not get it under it then it will move to class Player where printplay method is present but it
will give an error printplay accepts two arguments name and game and we had provided three instance
variables values or arguments name, salary and role and if we change the order of inherit class like
Coolprogrammer(Player, Employee) so if we run it now so we will get an error like Coolprogrammer has no
constructor so it will use constructor of Player class which accepts two arguments and we are passing
three so we will need to change arguments of Coolprogrammer like Coolprogrammer("Karan", ["Cricket"] so
Player class constructor will give approval and we can use all the methods of class Player now and
if we print Karan.printdetails() so we will get an error as it accepts three attributes name, salary
and role and we are passing two arguments name and game to Coolprogrammer("Karan", ["Cricket"].


To avoid it we will create constructor of Coolprogramer which accepts arguments like name, salary,
role and game so we created one method printprog to print the details of the object of Coolprogrammer
which accepts attributes name, salary, role and game so we can use this method like Karan.printprog()
now and we can use printdetails method of class Employee as we have arguments name, salary and role and
game in Coolprogrammer and printdetails accepts attributes name, salary and role only which is present
in Coolprogrammer already so we will get an output easily and similarly goes to class Player method
printplay etc.


NOTE : A class which inherits more classes so if we are finding constructor, class attributes, object
variables, classmethod and staticmethod first it will check under itself and if did not find then
moves to the class which comes first in the order of inherit classes and if did not find then moves to
second class in order of inherit classes and so on.



Ex : We have one class variable Var which is present in all three classes like Var = 8 in class Employee,
Var = 9 in class Player and Var = 10 in class Coolprogrammer so if we type print(Karan.Var) and Karan is
the object of class Coolprogrammer so Karan will check its variables if not found then will check its
class variables once it found so it will give an output 10.

If there will be no Var present in Coolprogrammer and we type print(Karan.Var) so first Karan will check
its attributes and then its class variables once Karan did not find it so it will move to that class which
comes in order of inherit classes so Karan will move to class Employee and will check it and if found
so will provide an output 8 and if in case Karan did not find Var variable in Employee so it will move to
next class Player and if found so will give an output 9









"""




