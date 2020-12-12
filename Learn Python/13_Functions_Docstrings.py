"""
a = 5
b = 9

sum() built in function which is iterable so it works on list and tuple only
Here, we have integer only a and b so if we write c = sum(a,b) so we do not
get output here ( sum() ek built in python function hai jo iterable jaise
list, tuple ko argument ke tor par leta hai isliye agar hum sum(a,b) pass
karenge toh output nhi aayega kyunki yaha argument list or tuple nhi balki
integer values hai )

To avoid this error we will use iterable like this c = sum([a,b]) or c = sum((a,b))
to get an output if we print print(c)

c = sum((a,b))
print(c)                  Output : 14
"""


"""
User defined function:

Declare the user defined function by keyword def like

Syntax : 

def function name():
    print(Statement)

Call a function

Syntax : 

function name()

"""



def welcome():
    print("Nitin is a technical guy")
welcome()
welcome()
welcome()
welcome()

def sum(x,y):
    print("Sum of x and y", x + y)
sum(5,4)


def average(a,b):
    """This is a function which calculates average of two numbers only"""
    c = (a+b)/2
    print(c)
average(5,10)
print(average.__doc__)       # Syntax to print docstring : print(function name.__doc__)
# Docstring is the first line as a string statement under function which we write as """string"""
# it is not read by Python interpreter and if we wish to print the docstring so we use syntax
# print(function name.__doc__)

def exponential(x):
    return(x**3)
v = exponential(5)
print(v)

def add_sub(x,y):
    c = x + y
    d = x - y
    return(c,d)
V1,V2 = add_sub(5,4)
print(V1,V2)




