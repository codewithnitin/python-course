# class Dad:
#     Basketball = 1
#
#
# class Son(Dad):
#     Dance = 1
#     Basketball = 4
#
#     def Isdance(self):
#         return(f"I dance {self.Dance} times")
#
#
# class Grandson(Son):
#     Dance = 6
#     Guitar = 1
#
#     def Isdance1(self):
#         return(f"Jackson Yeah, I dance very awesomly {self.Dance} times")
#
# Darry = Dad()
# Larry = Son()
# Harry = Grandson()
#
# print(Harry.Isdance())




class Electronic_device:
    no_of_devices = 20

    def __init__(self, abrand, aprice, awarranty):
        self.brand = abrand
        self.price = aprice
        self.warranty = awarranty

    def printdevice(self):
        return(f"The elctronice device is {self.brand}, price is {self.price} and warranty is {self.warranty}")


class Pocket_gadget(Electronic_device):
    no_of_devices = 12
    no_of_pgadgets = 10

    def printgadget(self):
        return(f"The pocket gadget is {self.brand}, price is {self.price} and warranty is {self.warranty}")

    @classmethod
    def from_dash(cls, string):
        return(cls(*string.split("-")))

    @classmethod
    def change_pgadgets(cls, newgadget):
        cls.no_of_pgadgets = newgadget


    @staticmethod
    def printgoods(str):
        print("This product is",str)
        return("Performance is incredible")



class Phone(Pocket_gadget):
    no_of_devices = 7
    Phones = ["Apple", "Nokia", "Samsung", "Vivo", "OnePlus"]


    def __init__(self, bbrand, bprice, bwarranty, bmodel):
        self.brand = bbrand
        self.price = bprice
        self.warranty = bwarranty
        self.model = bmodel

    def printmobile(self):
        return(f"The manufacturer is {self.brand}, price is {self.price} and warranty is {self.warranty} & model is {self.model}")

    def printphones(self):
        return(self.Phones)


TV = Electronic_device("Sony", 30000, "1yr")
Freeze = Electronic_device("Whirlpool", 20000, "2yr")
Cooler = Electronic_device("Bluestar", 9000, "1yr")
Walkman = Pocket_gadget("Boat", 2500, "1yr")
Pager = Pocket_gadget.from_dash("Philips-3500-2yr")
Apple = Phone("Apple", 50000, "1yr", "Iphone11")
Nokia = Phone("Nokia", 40000, "1yr", "N75")
Samsung= Phone("Samsung", 30000, "1yr", "Galaxy50")
Vivo = Phone("Vivo", 25000, "1yr", "VivoSmart")
OnePlus = Phone("OnePlus", 45000, "1yr", "Oneplus10")

print(Apple.printmobile())






"""

Multi-level Inheritance : When one class is derived from one class and then another class is derived
from the class which was derived from super class means class is deriving level by level.



First of all we created one class Electronic_device which has one class variable no_of_devices = 20 and 
three instances TV, Freeze, Cooler where each instance has instance variables brand, price and warranty so
we passed instance variables values or arguments like TV = Electronic_device("Sony", 30000, "1yr") and to
accepts these arguments we created one constructor then created one method printdevice which prints the
details of objects of the class Electronic_device.

Then we created one class Pocket_gadget(Electronic_device) which inherits the class Electronic_device
then created two class variables no_of_devices = 12 , no_of_pgadgets = 10 and instance of this class which
is Walkman which accepts three instance variables arguments for attributes brand, price and warranty as
it inherits class Electronic_device which has constructor which accepts three arguments brand , price and
warranty and then created one method printgadget to print the details of the object of class Pocket_gadget
then used classmethod decorator to create classmethod from_dash to use it as alternative constructor to
create an another instance of this class Pager which will accepts three instance attributes arguments like
brand, price and warranty then used classmethod decorator again to create classmethod change_pgadgets to
change the value of class variable no_of_pgadgets values then created one staticmethod printgoods.


Finially, we created another class Phone(Pocket_gadget) which has two class variables no_of_devices = 7
and Phones = ["Apple", "Nokia", "Samsung", "Vivo", "OnePlus"] then created five instances of this
class which has attributes brand, name, warranty and model and if we do not create constructor here
so we will get an error as we are passing one extra argument value for model here like

Apple = Phone("Apple", 50000, "1yr", "Iphone11") and this phone class will move to Pocket_gadget class
to find constructor and as there is no constructor so moves to Electronic_device which accepts only
brand, price and warranty so will get an error like 4 positional arguments take and 5 were given.

Due to which we created another constructor which accepts arguments brand, price and warranty and model
then created one method printmobile to print the details of the instances of the class Phone and one
method printphones so class Phone instances can use all the features of class Phone as well as class
Pocket_gadget and Electronic_device.



NOTE : Jaise Dad ke gunn Son ne inherit kiye and Son ke gunn Grandson ne toh indirectly Grandson ko Son
and Dad dono ke gunn mil gye ye hota hai Multi-level Inheritance jab inheritance level by level chalta
hai.









"""









