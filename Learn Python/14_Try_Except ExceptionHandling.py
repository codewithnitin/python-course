#try except exception handling :
"""
try is the keyword like if so try keyword tries to execute the statement which is written under it
if it executes so it prints the output and moves further in the program and if try statement is not
right and we do not want to stop rest of the program so we use another keyword called except in Python
like we have catch in c or c++ so except catches the error comes up while executing the try statement
and prints the error and then moves further in the program without stopping the program.

Syntax :

try:
    print(Statement)
except Exception as e:
    print(e)
print(Further statement)
"""

n1 = input("Enter the first number\n")
n2 = input("Enter the second number\n")
try:
    print("Sum of these two numbers is", int(n1) + int(n2))
except Exception as e:
    print(e)
print("This line is very important")



