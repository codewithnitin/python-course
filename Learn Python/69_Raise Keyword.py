"""

As we know if we have code in try and except block so try blocks try to execute that code and if it
works that is fine and if does not work so except catches the error and print it and if we have further
code after except statement so it will be executed (Matlab try block me code hai toh usse execute krne
ki koshish kro hota hai toh thik nhi hota toh error or exception ko pakdo except ke duara and uske aage
jo important code likha hai jo hume run krna he hai woh run ho jaata hai)


Sometimes we have some code or program which takes some input and if we put wrong input which is not
suitable for our code and there is some further code in the program after input from user which takes
almost an hour to execute so what is the point to run further code if we have provided wrong input
here we can use the keyword raise by which we explains if we put wrong input so stop the program then
and there instead of wasting time of user, user resources and server load by executing further code.

(
Matlab esa code jb hum chahte hai ki kuch wrong input hua toh sidha code ruk jaye kyunki uske aage
jo code hai woh kaafi time leta hai jo hmare user ka time, resources and server per load bhi dalta
hai jo ki unnecassary hoga kyuki hume pta hai output nhi aayega toh iske liye hum raise keyword use
krte hai taaki agr wrong input mile toh code wahi ruk jaye and aage proceed na kre
)

raise keyword : It is used to raise exceptions in code here exceptions could be built in exceptions
or user defined exceptions. (Exceptions tab occur hoti hai jb kuch error ya galti hoti hai program
me )

We will take some examples to learn this keyword raise now.

"""


# a = input("Enter your name")
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowed as input.")
#
# print(f"Hello {a}")




# a = int(input("Computation takes 10 secs to give result as a number"))
#
# if a==0:
#     raise ZeroDivisionError("Number cannot be divided by zero")
#
# b = int(input("Computation takes 30 secs to give result as a number"))
#
# print("Result", b/a)





# a = input("Enter your name")
#
# try:
#     if a == "Harry":
#         raise Exception("Access denied to this person to our website")
# except Exception as e:
#     raise ValueError("Harry is not allowed to access our website")
#
# print(f"Welcome to our website {a}")





# dict = {"Harry" : 2, "Larry" : 4, "Carry" : 8}
#
# try:
#     print(dict["Marry"])
#
# except Exception as e:
#     raise KeyError("Key Marry is not found in the dictionary dict")
#
# print("This is important line to print")





# List = [1,2,3,4,5]
#
# try:
#     print(List[5])
#
# except Exception as e:
#     raise IndexError("Out of range is accessing in list sequence")
#
# print("Exception handled")




# a = "Harry"
#
# try:
#     print(b)
#
# except Exception as e:
#     raise NameError("Variable b is not defined")
#
# print("Important stuff to print")





"""
a = input("Enter your name")                              
if a.isnumeric():                                         
    raise Exception("Numbers are not allowed as input.")  
print(f"Hello {a}") 

In this approach we are taking input as a string and we know name will be made up with alphabets
only so if in case we enter wrong input number in a form of string then there is a function
isnumeric() which are applying on the variable a which detects we are entering number as an input
in a form of string so once it is find out by isnumeric() input is number then raise an Exception
which is user defined in spite of built in exceptions that numbers are not allowed so further code
will not run and if input is a string in a form of alphabets so no exception will be raised and
further code print print(f"Hello {a}) will be executed.




                                                                       
a = int(input("Computation takes 10 secs to give result as a number"))                                                                                                                                                                                      
if a==0:                                                                                                                                       
    raise ZeroDivisionError("Number cannot be divided by zero")                                                                                                                                                                                                                              
b = int(input("Computation takes 30 secs to give result as a number"))                                                                                                                                                 
print("Result", b/a)                                                    

In this approach we are doing some computation which takes 10 secs to give result as a number
and we are assigning it into a variable a and if a is equal to zero so we do not wish to execute
the further code which is also a computation which takes 30 secs to give a result as a number
then print b/a as a result which will give us Zero division error in python.

Due to which we raised an exception ZeroDivisionError("Number cannot be divided by zero") for
variable a so it will not run further code and it will save our time and resources and server 
load and whatever we write here under raise Exception("Number cannot be divided by zero") or 
raise ZeroDivisionError("Number cannot be divided by zero") is our custom script which we can
show in console for the user.

Note : raise Exception("Number cannot be divided by zero") or raise ZeroDivisionError("Number 
cannot be divided by zero") both can be used ( Matlab built in exceptions name likhe ya simple
keyword Exception likhe dono se kaam chal jayega bs farak itna sa hai built in exceptions ke
liye pre defined exceptions name hai jaha Exception keyword use kr bhi skte hai but user defined
exceptions me Exception keyword he role play krta hai )





a = input("Enter your name")                                         
try:                                                                 
    if a == "Harry":                                                 
        raise Exception("Access denied to this person to our website")
except Exception as e:                                               
    raise ValueError("Harry is not allowed to access our website")   
print(f"Welcome to our website {a}")                                 

In this approach we are taking input a string in a form of alphabets only into a variable a and
then we created a try block which states if input into a variable a is equals to "Harry" so raise
Exception("Access denied to this person to our website") then defined except statement to catch
this exception or error which is user defined then raised ValueError Exception is used to opt out
the specific value as raise ValueError("Harry is not allowed to access our website") it means a 
person name "Harry" is not allowed to access the website and apart from this if input into  var
a would be any other person name so no exception will be raised and further code will run which is
print(f"Welcome to our website {a}")

Note : raise ValueError("Harry is not allowed to access our website")  or   raise Exception("Harry
is not allowed to access our website")  both are same which we had discussed above already.




dict = {"Harry" : 2, "Larry" : 4, "Carry" : 8}                          
try:                                                                   
    print(dict["Marry"])                                               
except Exception:                                                 
    raise KeyError("Key Marry is not found in the dictionary dict")    
print("This is important line to print")                               

In this approach we are trying to print a key "Marry" which is not present in the dictionary
dict so there will be an error or exception will be come up which will be Key Error in try
block then we have except statement to catch that exception and then we raised an exception
like  raise KeyError("Key Marry is not found in the dictionary dict")  so further code will 
not be run and if in try block print(dict["Harry"]) which is a key defined into a dictionary
dict so no exception will be come up and rest of further code will be executed easily.




List = [1,2,3,4,5]                                                                                                                                  
try:                                                              
    print(List[5])                                                
except Exception:                                                 
    raise IndexError("Out of range is accessing in list sequence")
print("Exception handled")                                        

In this approach we are trying to print print(List[5]) which is an element which is not
present in the list naming List in a try block so whenever we are accessing for those
index which is not present in a sequence so there will be an exception comes up which is
Index error so here exception will be raised when we print print(List[5]) in try block
and we have except statement to catch that exception and then in except block we raised
raise IndexError("Out of range is accessing in list sequence") so it will not execute
further code and if in try block print print(List[4]) so this index is present in a list
so no exception will be raised and rest of code in a program print("Exception handled")
will be run easily.




a = "Harry"                                                      
try:                             
    print(b)                                                     
except Exception:                
    raise NameError("Variable b is not defined")                                                                                                     
print("Important stuff to print")

In this approach we are trying to print(b) in try block as we know we have a variable a not
b so there will be a name error or exception will occur for sure and we have except state-
ment to catch this exception and then we raised this exception which is NameError in except
block like this raise NameError("Variable b is not defined") so no further code will run but
if we have code print(a) in try block so there will be no exception and rest of code which 
is print("Important stuff to print") will also be executed easily.




Built in exceptions in python :

ZeroDivisionError : Jab denominator zero hota hai
NameError : Jab local or global scope me koi variable define nhi ho aur usse execute kre
KeyError : Jab dictionary me key define na ho jo key search kre
IndexError : Jab kisi sequence me jaise list ke woh element ko access kre jo present nhi
ValueError : Jab kisi specific value ko opt out krna ho jaise koi user ko block krna kisi
website me value kuch bhi ho sakti hai jaise username ya koi number anything.
ModuleNotFoundError : Jab module ka name he galat input krde program me
FileNotFoundError: Jab koi esi file ko access kre jo exist nhi krti
SyntaxError : Jab koi syntax he galat ho jaise for loop ya if statement ke end me colon :
nhi lagaya ho
IndentationError: Jab kahi code me galat indentation or tab de di jaati hai






"""











