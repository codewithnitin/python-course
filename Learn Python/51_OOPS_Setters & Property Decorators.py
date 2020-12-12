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

Hindustani_supporter = Employee("Hindustani", "Supporter")
print(Hindustani_supporter.email)
Hindustani_supporter.fname = "US"
print(Hindustani_supporter.email)
Hindustani_supporter.email = "this.that@codewithnitin.com"
print(Hindustani_supporter.email)
del Hindustani_supporter.email
print(Hindustani_supporter.email)


"""
In other languages, we have getter() to change the identity of a method to instance attribute
similarly we have property decorator in python to change the identity of a method to instance
attribute.

In other languages, we have setter() to set the instance attribute similarly, we have setter
decorator in python to set an instance attribute which has been created by property decorator.


In above approach, we created one class which has one constructor having instance attributes
self.fname, self.lname and self.email and one method explain which defines the object of class
Employee and then created one object Hindustani_Supporter which accepts two arguments Hindustani
and Supporter so if we print print(Hindustani_Supporter.email) so will get an output like

Hindustani.Supporter@codewithnitin.com 

then we changed the instance attribute Hindustani_Supporter.fname = "US" ( Kyunki ab Hindustani
supporter ki job US me lag gayi hai and woh keh rha hai mera first name change krdo Hindustani se
US kyunki ab me US ko support karunga )

if we print now print(Hindustani_Supporter.email) so will get the same output like 

Hindustani.Supporter@codewithnitin.com
Hindustani.Supporter@codewithnitin.com 

Hindustani.Supporter@codewithnitin.com ( Kyunki jab object bana toh constructor run ho gya toh
self.fname, self.lname and self.email run ho gye and yaha self.email already set ho jayega uss
fname and lname ke sath jo object bante time use hue toh hum fname ko change kre halaki
ab print(Hindustani_Supporter.fname) to output dega US par phr bhi self.email phele wala he set
print(Hindustani_Supporter.email) same output dega )

To avoid this problem we will not create instance attribute self.email inside constructor here
we will create a new method called email like

  def email(self):
      return(f"{self.fname}.{self.lname}@codewithnitin.com")
      
so if we print(Hindustani_Supporter.email()) then Hindustani_Supporter.fname = "US" then print again
print(Hindustani_Supporter.email()) so output would like :


Hindustani.Supporter@codewithnitin.com
US.Supporter@codewithnitin.com

(Kyuki phele toh Hindustani.Supporter@codewithnitin.com ye print hoga fname and lname use honge 
object bante time ke phr fname change hua toh ab print hoyega US.Supporter@codewithnitin.com )

Now we got the output but still I wish not to create email method I just want to use email as an
instant attribute so we have power of property decorator in python like :

  @property
  def email(self):
      return(f"{self.fname}.{self.lname}@codewithnitin.com")
      
Due to which we can call this method as an instant attribute by print(Hindustani_Supporter.email)
instead of print(Hindustani_Supporter.email()) then changed the instance attribute Hindustani_Sup
porter.fname = "US" then print(Hindustani_Supporter.email) so output would be like :

Hindustani.Supporter@codewithnitin.com
US.Supporter@codewithnitin.com

Note : We did not use paranthesis () here due to property decorator which changed the email
method to instance attribute of Hindustani_Supporter     

( Yeh Abstraction hai kyunki humne method ko instant attribute me change kra and hum nhi chahte
ki Programmer inh sb me worry ho ki kaise kya class me likha hai woh sidha instant attriute ki 
tarah email method ko use kre aur jo technique use hui method ko instant attribute bnane me
woh hai Encaplusation matlab setter decorator yha par )


Here, if we wish to change value of attribute email like we can change Hindustani_Supporter.fname
or Hindustani_Supporter.lname so we cannot change Hindustani_Supporter.email directly here like

Hindustani_Supporter.email = "this.that@codewithnitin.com" it will give an error Can't set attribute

So to set the instant attribute which has been created via property decorator we have one power of
setter decorator in python like

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
        
we will type @attribute.setter here attribute would be the attribute which we are unable to set
directly then define the method with the same name of attribute which takes two argument self
and string here self would the object of this attrbute means Hindustani_Supporter and string 
argument would be "this.that@codewithnitin.com" now we splited this string string.split("@")
and assgined it to the variable names and we know split function gives list so we will have
names = ["this.that", "codewithnitin.com"] now we need to change fname and lname only so we will
write names = string.split("@")[0] so we will have list names = "this.that" then further
self.fname = names.split(".")[0] so self.name = "this" and self.lname = names.split(".")[1] so
self.lname = "that"

Now we will not get any error while run because we have @email.setter available to set the instant
attribute Hindustani_Supporter.email = "this.that@codewithnitin.com" so if we print(Hindustani_Su
pporter.email) then Hindustani_Supporter.fname = "US" then print(Hindustani_Supporter.email) then
set Hindustani_Supporter.email = "this.that@codewithnitin.com" then print(Hindustani_Supporter.
email) now email attribute is set due to @email.setter so output would be like

Hindustani.Supporter@codewithnitin.com
US.Supporter@codewithnitin.com
this.that@codewithnitin.com


Suppose we wish to delete this instant attribute email because we do not have requirement of this
now so we have one power decorator deleter in python like

  @email.deleter
  def email(self):
      self.fname = None
      self.lname = None
      
We will type @attribute.deleter then defines method with the same name of attribute def email(self):
then self.fname = None and self.lname = None if we print(Hindustani_Supporter.email) then Hindustani
_Supporter.fname = "US" then print(Hindustani_Supporter.email) then set Hindustani_Supporter.email =
"this.that@codewithnitin.com" then print(Hindustani_Supporter.email) then del(Hinustani.Supporter.
email) then print(Hindustani_Supporter.email) so output will be like


Hindustani.Supporter@codewithnitin.com
US.Supporter@codewithnitin.com
this.that@codewithnitin.com
None.None@codewithnitin.com

However we do not want this None.None@codewithnitin.com in output so we will go to property email
and type like

    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return("Email is not set..Please use setter to set email")
        else:
            return(f"{self.fname}.{self.lname}@codewithnitin.com")
            
If self.fname = None and self.lname is None so return("Email is not set..Please use setter to set
email") otherwise return(f"{self.fname}.{self.lname}@codewithnitin.com")

Now we print(Hindustani_Supporter.email) then Hindustani_Supporter.fname = "US" then print(Hindustan
i_Supporter.email) then set Hindustani_Supporter.email = "this.that@codewithnitin.com" then print(H
industani_Supporter.email) then del(Hinustani.Supporter.email) then print(Hindustani_Supporter.email)
so output will be like


Hindustani.Supporter@codewithnitin.com
US.Supporter@codewithnitin.com
this.that@codewithnitin.com
Email is not set..Please use setter to set email


Note : We learnt actually we do not have any deleter in python we just initialise instant attribute
self.fname and self.lname is equal to None for the instance attribute email.











 













"""