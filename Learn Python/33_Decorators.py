# def welcome():
#     print("Nitin is a good boy")
# welcome()



# def welcome():
#     print("Nitin is a good boy")
# wel = welcome
# del welcome
# wel()

"""
Here we did not call the welcome() so not to apply paranthesis () and assign welcome function into
the variable wel and then we deleted the function welcome so if we call welcome() now we will not
get output as welcome function has been deleted

here we will have the copy of welcome function into the vairbale wel so when we call wel() it calls
welcome() indirectly to get the desired output which we were getting earlier

"""

# How to return functions under function?

# def funcret(num):
#     if num == 0:
#         return(print)
#     elif num == 1:
#         return(int)
# a = funcret(0)
# print(a)

# How we can pass function as an argument in function?

# def func(func1):
#     func1("This is awesome weather")
# func(print)

"""
Here we created one function called func and passing argument func1 so when we call func(print) means
passing argument print function so print will assign into func1 then func1("Statement") will act as 
print("statement")

"""

# Decorators are those functions which are used to enhance the functionality of the others functions
# It takes one function as an argument to enhance the functionality of that function which is passed
# as an argument and returns the other function.

# (Matlab jo function as an argument pass krte hai decorator function me uski functionality ko enhance
# karta hai ese ki uss function ke execute hone se phele kuch execute ho jaye and phr woh function
# execute ho jo as an argument pass kiya ho and phr kuch aur execute ho jaye uske baad)

def dec1(func1):
    def nowexec():
        print("Executing before func1 call")
        func1()
        print("Executed after func1 call")
    return(nowexec)

@dec1
def who_is_Nitin():
    print("Nitin is a technical guy")
# who_is_Nitin = dec1(who_is_Nitin)
who_is_Nitin()


"""
Working of decorators :

First of wll we will create decorator function dec1 in which we will assign one argument func1
which would be the function that needs to be enhanced in terms of their functionality after
that we will create another function nowexec under dec1 and we will print Executing before func1 call
then calling func1 then print Executed after func1 call under nowexec function then return(nowexec)
 
Note : It could be anything before calling func1 in nowexec function like any computation, print
statement which we used or any remote server execution etc and same after calling func1 too

Till now we created decorator function only

Now we will create another function who_is_Nitin which prints Nitin is a technical guy and when we
call who_is_Nitin() here so we will get the output as usual Nitin is a technical guy

Note : Here we will change who_is_Nitin before calling it like who_is_Nitin = dec1(who_is_Nitin)
means who_is_Nitin is changed to call dec1 function by passing argument as a function who_is_Nitin
which returns nowexec function it means who_is_Nitin has been changed to return(nowexec) so when we
will call who_is_Nitin() now so we will call nowexec() indirectly and then we will get output as
first print statement Exeuting before func1 call and then call func1() means calling who_is_Nitin
which was earlier Nitin is a technical guy and then another print statement Executed after func1
call

so we sandwiched our who_is_Nitin function here with the help of decorator function dec1

Note : we can avoid who_is_Nitin = dec1(who_is_Nitin) by putting @dec1 just above who_is_Nitin
function as well both are same.

"""