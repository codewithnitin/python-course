
Var1 = 10
Var2 = 5
Var3 = int(input())


"""
if Var3>Var2:                  #if reflects blue colour shows if keyword
    print("Greater")      
if Var3==Var2:
    print("Equal")             
else:                          #else reflects blue colour shows else keyword        
    print("Lesser")
"""

"""
if   condition:                : means enter into the if condition 
else condition:                : means enter into the else condition
#When we enter enter after : to move to second line so there will be tab before print is called Indentation
if we remove tab so output shows IndentationError so please make sure not to remove tab before print
> or < shows greater or lesser however equals to syntax is == double equals to to reflects equals to
in Python
"""

"""
Note : 

If we enter Var3 number greater than Var 2 so output comes up in first if statement however interpreter 
checks rest of if statement as well suppose we have 100 of if statement after first if statement and if 
first if statement is true so ideally no need to check rest of if statement in code so to avoid it we
have one keyword in Python called else if or elif
"""
"""
if Var3>Var2:
    print("Greater")
elif Var3==Var2:                #elif reflects blue colour shows elif keyword
    print("Equal")
else:
    print("Lesser")
"""

"""
Note : 

Here interpreter checks first if statement if it is true so it will not check rest of if statement in 
our code and if first statement is false so moves to elif statement and if elif is true so come out from
if else ladder and if elif is false so moves to else statement and then come out from if else ladder 
"""
"""
in                 in is the keyword in Python
not in             not in is the keyword in Python
"""
"""
List1 = [7,10,14,17]
# print(7 in List1)

if 10 in List1:
    print("Yes it is in list")
# print(15 not in List1)
if 15 not in List1:
    print("Yes it is not in list")
"""
"""
print("Enter your age")
Age = int(input())
if Age<18:
    print("You cannot drive")
elif Age==18:
    print("We will think about it")
else:
    print("You can drive")
"""

#Exercise2 : Age between 7 to 100

"""
print("Enter your age")
Age = int(input())
if Age<7:
    print("You cannot use computer")
elif Age==7:
    print("We will think about it")
elif 7<Age<101:
    print("You can use computer")
else:
    print("Please enter correct age")
"""

#Exercise 3 : Faulty calculator

"""
Design a faulty calculator which will solve all the problems except following computations :
45*3 = 555, 56+9 = 77, 56/6=4

and                 # and is the keyword in Python which shows blue colour

"""
"""
print("Enter your first number")
n1 = int(input())
print("Enter your second number")
n2 = int(input())
print("Enter your operator +,-,*,/")
n3 = input()
if n1==43 and n2==3 and n3=="*":
    print(555)
elif n3=="*":
    print(n1*n2)
elif n1==56 and n2==9 and n3=="+":
    print(77)
elif n3=="+":
    print(n1+n2)
elif n1==56 and n2==6 and n3=="/":
    print(4)
else:
    print(n1/n2)
"""











