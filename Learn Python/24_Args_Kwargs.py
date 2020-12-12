# def function1(a,b,c,d):
#     print(a,b,c,d)
# function1("Nitin","Pandey","Piyush","Sanjeev")



# def function_args(*args):
#     print(args)
#     print(args[0],args[1])
#     for item in args:
#         print(item)
# List = ["Nitin","Pandey","Piyush","Sanjeev","Anoop"]
# function_args(*List)

"""
Here our list elements passes under calling function_name(*Listname) and it converts into the
declaration as a tuple so whatever passes into function_name(*args) as a tuple so if we have
any iterable like list, tuple, dictionary etc all will be converted into the tuple under
declaration or definition of function


Note : If List = ["Nitin","Pandey","Piyush","Sanjeev","Anoop"] or tuple like that
Tuple = ("Nitin","Pandey","Piyush","Sanjeev","Anoop") and we pass these list or
tuple elements into args like that function_args(*List) or function_args(*Tuple)
so both list or tuple elements will be converted into declaration function_args(*args) as
a tuple that is convention of python like ("Nitin","Pandey","Piyush","Sanjeev","Anoop")

If List = [["Harry", 2],["Larry", 4], ["Carry", 8]] or Tuple like that
Tuple = (("Harry", 2), ("Larry", 4), ("Carry", 8)) so if we pass the elements of this
list or tuple into args like that function_args(*List) or function.args(*Tuple)
so both list or tuple elements will be converted into declaration function_args(*args) as
a tuple that is convention of python like (("Harry", 2), ("Larry", 4), ("Carry", 8))

List of List or Tuple of Tuple have same syntax to unpack key value pair like

for item, lollypop in args:
    print(item,lollypop)

If Dict = {"Harry" : 2, "Larry" : 4, "Carry" : 8} and we pass this dictionary key
value pairs into the function_args like function_args(*dict) so here in the
declaration function_args(*args) we will have tuple which is python convention
but tuple having keys only like that ("Harry", "Larry", "Carry") instead of tuple
having key value pairs which we were getting when we were passing List of List or
Tuple of Tuple so here syntax will be

for item in args:
    print(item)

So, if we wish to pass dictionary key value pairs so we can do it with the help
of **kwargs only as it accepts dictionary key value pairs only not list or tuple
elements and on the other hand we can pass list or tuple elements to *args and it
changes into tuple but if we pass dict key value pairs to args so we will get tuple
of keys only which is not our desired output.



Nature : def function_name(normal,*args,**kwargs)
*args and **kwargs both are optional

"""


# def function_args(normal,*args):
#     print(normal)
#     for item in args:
#         print(item)
# normal = "These are the students which are under below:"
# List = ["Nitin","Pandey","Piyush","Sanjeev"]
# function_args(normal,*List)

"""
Note : Please make sure not to change the nature or order def function_name(normal,*args,**kwargs)
like def function_name(*args,normal,**kwargs) so we will get an error as we cannot change it.
"""


def function_args(normal,*args,**kwargs):
    print(normal)
    # print(type(normal))
    for item in args:
        print(item)
    # print(type(args))
    print("\nNow I would like to introduce these students:")
    for key,value in kwargs.items():
        print(f"{key} is {value}")
    # print(type(kwargs))
normal = "These are the students which are under below:"
List = ["Nitin","Pandey","Piyush","Sanjeev"]
List2 = {"Nitin":"Technical guy","Pandey":"Medical technician","Piyush":"Reporter"}
function_args(normal,*List,**List2)



