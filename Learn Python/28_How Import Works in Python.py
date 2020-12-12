# How import statement works in python?

# import sklearn as sk
# print(sk.__version__)

"""
import, int , float etc are in global scope and we also have one data type __name__ which
we will study in next session.

Here we will use two files 28_How Import Works in Python.py and File_2.py to understand import statement working

"""
"""

Suppose we are executing one program in which we need to import module called sklearn so we
will study from where our python interpreter fetch the module then we use it accordingly into
the program with the help of import statement.

Here, we have one module sys which is inbuilt module so we will import this module and will run
one function of module sys is sys.path like

import sys
print(sys.path)

Output : It will give us the hierarchy how our python interpreter goes to find out any module
which we import into the program and here first directory would be the directory in which we
are present right now to find out the module and so on.

"""

# import sys
# print(sys.path)

"""
Now we will study how we can use content like variable, functions etc of another file into our
current file or program with the help of import statement which is given below :

"""
import File_2
print(File_2.a)
File_2.printjoke("This is me")

# import sklearn as sk                  # Here we have changed module name to sk via as keyword
# print(sk.__version__)

"""
Suppose we change the name of our current file to sklearn which is similar to module name
which we are using in our program so we will get an error because python interpreter will 
find out the module in first directory which has name sklearn itself so interpreter
will confuse if sklearn is module and getting module name in first directory and still
not getting module and will not move further in hierarchy of module which we had learnt
with the help of inbuilt module called sys above that is the reason we always ask to keep
filename different from the module name.

"""

