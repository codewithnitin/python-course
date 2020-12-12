"""

class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithnitin.com"

    def explain(self):
        return(f"The employee is {self.fname} {self.lname}")

    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return("Email is not set..Please set email using setter")
        else:
            return(f"{self.fname}.{self.lname}@codewithnitin.com")

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

SkillF = Employee("Skill", "F")
# print(SkillF.email)

# print(type(SkillF))
# print(type("This is a string"))

# print(id("This is a string"))

o = "This is a string"
# print(dir(o))
# print(dir(SkillF))

import inspect
print(inspect.getmembers(SkillF))



"""

"""

Object introspection : That is the term by which we can explain the object means which class
that object belongs to and what is the unique id of that object and what are the members which
can be used by this object. 


There are some data types which explain object introspection like type(), id(), dir() and one 
module inspect.



type() : It is used to show from which class that object belongs to.


print(type(SkillF))   
Output : <class '__main__.Employee'>  It shows class Employee of main method ( main method ki
class Employee se aaya ye object )

print(type("This is a string")
Output : <class 'str'> It shows class str ( string class se aaya ye object )



id() : It gives unique id to every object on each run time ( Matlab same object bhi jitni baar
run krenge toh ek unqiue id show krega )


print(id("This is a string"))        Output : 12806096
print(id("This is a string"))        Output : 14968736

So we ran same object but id() gives unique id on each run time.


dir() : It gives members of the object in a list ( Matlab woh attributes , methods jinke sath ye
object khilwad kar sakta hai )


o = "This is a string"
print(dir(o))

output : ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__',
'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__'
, '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode'
, 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle'
, 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
'swapcase', 'title', 'translate', 'upper', 'zfill']


print(dir(SkillF))

Output : ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__'
, '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'email', 'explain', 'fname', 'lname']

( We got all the members of SkillF object jinke sath khilwad kr sakte hai included those which we
define manually jaise fname, lname, explain and email method )


Similarly, we have one module inspect which also plays a huge role in object introspection.

import inspect
print(inspect.getmembers(SkillF))

Here we imported module inspect and then used getmembers() of inspect module to show what are the
members of object SkiilF.




"""




