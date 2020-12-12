
def addition(x,y):
    add = x + y
    return(add)

def subtraction(x,y):
    sub = x - y
    return(sub)

try:
    x = int(input("Enter the first number\n"))
    y = int(input("Enter the second number\n"))
    print("Sum of these two numbers :", addition(x,y))

except Exception as e:
    print(e)

else:
    print("Subtraction of these two numbers :", subtraction(x,y))

finally:
    print("It must be done")

print("This is the important line to print")


"""


In above approach, we are learning how we can use else and finally block in try and
except.

We know it very well if try is executed our further program is executed without any
problem and if try is not executed and still we do not want to stop the rest of execution
in further code so we use except block which catch the error and print it accordingly
and executed further program.

else : This block is executed only if except is not running.

finally : That is the block which will be executed all the time either try,except,else
are executed or not. ( Hmesha chalta rhega chahe try, exception occur ho na ho, else 
chale nhi chale tbhi iska naam finally hai matlab kuch bhi ho isse to chalna he hai hai )

It is used to clean up the code suppose if we have open up some of the files so we can
close those files under finally block ( ye kaam aata hai sameta batoli ke liye )

We will see one example of this sameta batoli below :



"""


"""

try:
    f = open("Harry_diet.txt")

except Exception as e:
    print(e)

else:
    print("This is executed only if except is not running")

finally:
    print("Run this anyway..run hone he hona hai sameta batoli ke liye")
    f.close()

print("This is important stuff to execute")


"""
