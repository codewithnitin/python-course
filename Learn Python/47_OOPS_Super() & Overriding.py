class A:
    classvar1 = "I am a class variable of class A"

    def __init__(self):
        self.var1 = "I am inside constructor of class A"
        self.classvar1 = "I am inside class A"
        self.special = "Special"

    def printdetails(self):
        return(f"var1 is {self.var1}, classvar1 is {self.classvar1} & special is {self.special}")


class B(A):
    classvar1 = "I am a class variable of class B"

    def __init__(self):
        super().__init__()
        self.var1 = "I am inside constructor of class B"
        self.classvar1 = "I am inside class B"
        self.salary = 5000


    def printdetails(self):
        print(super().printdetails())
        print(super().classvar1)
        return(f"var1 is {self.var1}, classvar1 is {self.classvar1}, special is {self.special} & salary is {self.salary}")



a = A()
b = B()
print(b.special, b.var1, b.classvar1, b.salary)
# print(b.printdetails())





"""

Super() : Suppose for some reason we need to execute the instance attributes or constructor, class
variables and methods of super class from derived classname or object of the derived class even
there is a concept of polymorphism ( jo kehta ki same name ke attributes, class variables ya phir
method he kyu na ho new wale lagun ho jaate hai phir bhi hum super class ke members ko access karna
chahte hai ) then we have a power of the function called Super().

So, Super() is used to access members of super class even there is a concept of polymorphism under
derived class.

"""


"""
In above approach, we created one class A which has one class variable classvar1 and created 
constructor which has one instance attribute var1 then created another class B which inherits
class A which has same class variable naming classvar1 and then made two instances a of class A
& b of class B.

So if we print print(b.var1) so it will search instance attrbute inside class B and if does not
find it out so will move to class A which is inherited to check instance attribute there and if 
finds it out so print it accordingly and now I created one more instance variable classvar1 in
constructor of class A and if we print print(b.classvar1) so b will search it inside class B
first and if does not find it out so will move to check instance attribute in class A and if finds
it out so will print it accordingly and if in case it does not find it out in class A constructor
so will move down in class B to check its class variable and if find it out so print it accordingly
and if does not so wil move again to check the class variable in class A to print it accordingly.

Means we learnt, instance of derived class will search instance attribute first inside derived class
if does not find it out so will move to super class to check instance attribute and if does not find
it out so will move down to derived class to check its class variable and if does not find it out
so will move further to super class to check the class variable accordingly.

Now I created one constructor inside derived class which accepts two instance attributes var1 and
classvar1 which are as similar as instance attributes of class A so if we print print(b.classvar1)
so instance b of derived class will search it under constructor of class B and print it accordingly
and if we comment it out so it will not move to super class to check it due to overriding case
or polymorphism ( jb same constructor niche bhi hai toh new wala lagu hoga and upar wala constructor
null and void ho jayega ) after that it will search class variable inside class B if finds it out
so will print and if does not so will move further to check class variable inside super class A.

Now for some reason I need to execute constructor of super class as well (par kyunki polymorphism
allow nhi karta hai phir bhi me chahta hu karna toh kaise krun ) suppose we have one important
instance attribute special in constructor of class A

To perform this we have a power of super() which is used to access members of super class even there
is a concept of polymorphism and now we will study how we can use this function called super()

We will type super().__init__() inside constructor of derived class like 

    def __init__(self):
        super().__init__()
        self.var1 = "I am inside constructor of class B"
        self.classvar1 = "I am inside class B"
        self.salary = 5000
        
if we print print(b.special) so b will search it inside constructor of class B & we have initialise
super().__init__() so it will move to constructor of super class where self.var1, self.classvar1
will execute and then will execute self.special to print it accordingly.

if we print print(b.special, b.var1, b.classvar1, b.salary) so b will search it inside constructor
of class B and we have initialise super().__init__() so it will move to the constructor of class A
to execute self.var1, self.classvar1, b.special ( halaki super class me jaake var1 and classvar1 
ka output different hai par kyunki var1 and classvar1 set bhi hai class B me toh use hoga self.var1
& self.classvar1 super class ka he par output replace ho jayega class B ke output se & self.special
class A ka he hoga and phir super class se out hoke self.salary print ho jayega derived class se)

if we type like this :

    def __init__(self):
        self.var1 = "I am inside constructor of class B"
        self.classvar1 = "I am inside class B"
        self.salary = 5000
        super().__init__()
          
          
if we print print(b.special, b.var1, b.classvar1, b.salary) so b will search instance attributes
inside constructor of class B so will execute self.var1, self.classvar1, self.salary and then moves
to super class constructor where will execute self.var1, self.classvar1, self.special so ye tino
kyunki super() ke initialise hone ke baad set maane jayenge toh inke output super class wale
print honge and self.salary print hoga class B ke hisab se )


Similarly, we created one method printdetails in class A which returns like
return(f"var1 is {self.var1}, classvar1 is {self.classvar1} & special is {self.special}") and we
created one method in class B which has same name printdetails as similar as class A which returns
return(f"var1 is {self.var1}, classvar1 is {self.classvar1}, special is {self.special} & salary is
{self.salary}")

so if we print print(b.printdetails()) so b will search method printdetails inside class B first
and as it is present here which returns instance variables self.var1, self.classvar1, self.special
and self.salary so it will find out these attributes inside class B constructor first and we have
initialise super() class constructor first like super().__init__() so will move to constructor
os super class to execute self.var1, self.classvar1 and self,special ( halaki super me jaake
self.var1 and self.classvar1 ke output different hai par kyunki ye variables set hai class B me
so self.var1, self.classvar1 ka output honge class B ke hisab se special ka class A ke hisab se phr
super ke constructor se out hoke self.salary print hoga class B ke hisab se )


if we created one method printdetails in derived class and we initialise method like 

    def printdetails(self):
        print(super().printdetails())
        print(super().classvar1)
        return(f"var1 is {self.var1}, classvar1 is {self.classvar1}, special is {self.special} & salary is {self.salary}")



if we print print(b.printdetails()) so first printdetails of super class will be printed and we
know printdetails of super class will use three instance attributes self.var1, self.classvar1 &
self.special so will search these instance attriutes inside class B constructor first and where
we have initialise constructor of super class so will move to constructor of class A to execute
self.var1, self.classvar1 and self.special ( halaki super me jaake self.var1, self.classvar1 &
self.special ke output different hai par self.var1 and self.classvar1 set hai class B me toh
self.var1 and self.classvar1 chalange super ke he par output replace ho jayenge inke class B ke
hisab se special ka output class A ke hisab se print hoga ) after that class variable of super
class will print and then return return(f"var1 is {self.var1}, classvar1 is {self.classvar1}, 
special is {self.special} & salary is {self.salary}") will print as per same above approach.




"""


