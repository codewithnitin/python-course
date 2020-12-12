"""

F-String is used to format the string by putting variable into the given string that
is all done by F-String

Here I will give some ways by which we can format the string first however these are
not that much readable if we have a long string where we will need to enter multiple
variable so this could be very confusing in code that is the reason we use F-String
which is very convenient in string formatting

#String ke beech variable ko lagana is string formatting and F-String is used to do it


"""
# var1 = "Nitin"
# x = "This is %s"%var1                   # This is for 1 variable string formatting
# print(x)

# var1 = "Nitin"
# var2 = 19
# import datetime
# z = datetime.datetime.now()
# x = "This is %s %s %s %s"%(var1,var2,z,24*5)       # Here we use tuple if we have more than 1 variable

# This is for more than 1 variable string formatting

# print(x)

# var1 = "Nitin"
# var2 = 19
# import datetime
# z = datetime.datetime.now()
# x = "This is {} {} {} {}"
# y = x.format(var1,var2,z,24*5)
# print(y)

# This is also for more than one variable
# These all formatting are not that much readable so we have very convenient F-string


# F-String way :


# var1 = "Nitin"
# var2 = 19
# import datetime
# z = datetime.datetime.now()
# x = f"This is {var1} {var2} {z} {24*5}"
# print(x)


