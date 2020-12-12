"""
Module : Basically these are those programs or codes which are already designed by
someone and they are in the perfect form so we just import it into our code and do
further task instead of writing code for the module.

In short it saves our time and make our life easier.

External Module : If we download it from outside python means internet so such
modules are called as External Module.

In Built Module : Those are shipped with python already called In Built Module.


"""


import random                         # Importing random module which is built in module
#Functions of random module :

# random_number = random.randint(0,8)
# print(random_number)
# Generating random integer in range (0,8) includes both 0 and 8

# random_number = random.random()
# print(random_number)                  # Output (float number)

# random_number = random.random() * 50
# print(random_number)

# Generating number in between 0 to 1 by calling .random() so if we wish to generate
# number in between 0 to 50 so we will write .random() * 50 so output will come up with
# number in between 0 to 50

#.choice(list or tuple or string) is used to select an element from non empty sequence

# List = ["Star Plus", "DD1", "Sony Six", "Aaj Tak", 50, 4.2]
# Random_Channel_Choice = random.choice(List)
# print(Random_Channel_Choice)

# List2 = (17, 3, 6, 1)
# Random_Channel_Choice = random.choice(List2)
# print(Random_Channel_Choice)

# Mystr = "Awesome"
# Random_Channel_Choice = random.choice(Mystr)
# print(Random_Channel_Choice)

import math                                # Importing math module which is built module

# Function of math module :

# x = math.ceil(2.4)
# print(x)

# It gives integer which is nearest greater to this float value

# x = math.floor(2.4)
# print(x)

# It gives integer which is nearest smaller to this float value

# x = math.sqrt(16)
# print(x)

# It gives square root of the integer which we passes into sqrt(16)

# x = math.pi
# print(x)

# It gives the constant value of pi in mathematics which is 22/7 or 3.14

import os                                 # Importing math module which is built module

# Functions of os module :

# y = "date"
# x = os.system(y)              # system commands like "date", "time" , "calc" etc
# print(x)

# Creating a variable cmd and storing "date" in string notation and then .system(cmd)
# gives an output by displaying today's date

# y = "time"
# x = os.system(y)
# print(x)

# Creating a variable cmd and storing "time" in string notation and then .system(cmd)
# gives an output by displaying today's time


# y = "calc"
# x = os.system(y)
# print(x)

# Creating a variable cmd and storing "calc" in string notation and then .system(cmd)
# gives an output by displaying today's calc

# x = os.getlogin()
# print(x)

# It gives an output by reflecting the name of administrator


import datetime                     # Importing datetime module which is built in module

# Functions of datetime module :

x = datetime.date(2020,8,1)
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.isoweekday())

# Here .date(YYYY,MM,DD) gives an output as assigning date and we can print it individualy
# as well

# x = datetime.time(19,40,50,345235)
# print(x)
# print(x.hour)
# print(x.minute)
# print(x.second)
# print(x.microsecond)

# Here .time(HH,MM,SS,SSSSSS) gives an output as assigning time and we can print it
# individualy as well

# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.isoweekday())
# print(x.hour)
# print(x.minute)
# print(x.second)
# print(x.microsecond)

# Here .datetime.now() gives an output as date and times both means all together and
# we can print it individualy as well

import calendar                   # Importing calender module which is built in module

# Function of calender module :

# x = calendar.calendar(1990)
# print(x)

# .calender(YYYY) gives an output of full year calender of particular year which we assign

x = calendar.month(2020,8)
print(x)

# .month(YYYY, MM) gives an output of particular month of a particular year which we assign






