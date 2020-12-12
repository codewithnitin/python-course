"""
Global variable : This can be used by all the functions (Single or Nested) as well as outside
functions ( Sarkari paisa ) means we can use it under or outside the function easily

Local variable : This can only be used under the function ( Apna paisa ) however if there
will be no local variable so function can use global variable to perform the operation by
reading global variable from outside the function

Note: Suppose we have nested function Rohan() and main function Harry() and we do not have any
local variable under Rohan() so Rohan() will try to fetch global variable outside main
function in spite of under the Harry()

Note : If we have local variable so we can easily change the value of local variable but
we do not have local variable and function got the global variable so if we are changing
the value of global variable we cannot change it directly under the function as Python does
not allow the function to change the value of global variable directly so

Here we have one keyword called global to change the value of global variable x

global x             #Changing the value of global variable
x = x + 10

"""


# b = 10 # Global Variable
# def function1(n):
#     x = 5 # Local
#     a = 10 # Local
#     global b
#     b = b + 9
#     print(a,x)
#     print(b)   # Global
#     print("I have created this", n)
# function1("Nitin")
# print(b)  #Global


# y = 4
# def harry():
#     x = 10
#     def rohan():
#         global y
#         y = 25
#         print("Before calling rohan", y)
#     rohan()
#     print("After calling rohan", x)
# harry()
# print(y)



# Practice

x = 45
def func1():
    y = 25
    def func2():
        d = 19
        d -=1
        print("Before calling func2()", d)
        global x
        x = x + 5
        print(x)
    func2()
    print("After calling func2()", y)
func1()
print(x)














