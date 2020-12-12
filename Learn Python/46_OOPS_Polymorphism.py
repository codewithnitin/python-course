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



class Programmer(Employee):
    no_of_leaves = 14

    def printdetails(self):
        return(f"The programmer name is {self.name}, salary is {self.salary} and role is {self.role}.")



Harry = Employee("Harry", 500, "Instructor")
Rohan = Employee("Rohan", 700, "Student")
Hamad = Employee.from_dash("Hamad-900-Monitor")
Shubham = Programmer("Shubham", 1100, "Programmer")
print(Shubham.printdetails())



"""

Polymorphism : It is an ability to take various forms ( matlab alag-alag rup dharan karna )

In above approach, we have class variable no_of_leaves and method printdetails are common in both the
classes super class Employee and the derived class Programmer here printdetails and no_of_leaves
gives different output when we call them with the help of object or classname of the class Programmer
that is known as Polymorphism ( Matlab classname Programmer and uske object ke liye new printdetails
method and new class variable no_of_leaves lagu hoga aur jo cheeze upar Employee class me hai class
variable no_of_leaves and printdetails method ko chodh ke woh sab bhi accessible hoga )


NOTE :  Ek se jayda rup dharan karne ki shakti ko Polymorphism kehte hai 



Example 1 :

print(5 + 6)                   Output 11
print("5" + "6")               Output 56

Here, I have two objects 5 & 6 when I use them as an integer with the help of + operator to print so gets 
an output 11 and when I use them in terms of string with the help of + operator so gets an output 56 ye
he hota hai Polymorphism alag alag rup dharan karna

Example 2 : Gangadhar ban jaana kbhi Skaktimaan ye he hota hai Polymorphism

Example 3 : Kabhi Peter Parker ban jaana toh kabhi Spider man ye he hota hai Polymorphism




Ways to achieve Polymorphism :

1) Over-riding
2) Super
3) Dunder method



"""