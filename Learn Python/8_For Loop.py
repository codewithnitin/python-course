List1 = [["Harry", 2], ["Larry", 4], ["Carry", 7], ["Harpic", 10],
         ["Vim Bar", 50], [10, 5], [5.5, 8]]
"""
# List of list
print(List1[0], List1[1], List1[2], List1[3], List1[4], List1[5], List1[6])

# For loop performs iteration until our list, string, dictionary and set content is completed.

for item in List1:
    print(item)
"""

# Printing all the items in the List1 like ["", ] and so on
# Iteration occurs for each item like in "Harry" in 9 line and then print Harry
# in line 10 and then it goes back to line 9 for item 2 which is "Larry" and
# then print Larry in line 10 and then goes back to line 9 for next item and so on.
"""
for item, lollypop in List1:
    print(item, lollypop)               # item = "Harry", lollypop = 2 then iteration so on
#Printing all the items with unpack in the List1 like "",  and so on

#If we wish to print anything like and lolly is in each iteration while
# printing output.
"""
"""
for item, lollypop in List1:
    print(item, "and lolly is", lollypop)
"""
"""
Dict1 = dict(List1)
for item, lollypop in Dict1:  
    print(item, lollypop)  
"""
"""    
# Does not give the output like in List as it is Dict data type so to access
# the items in terms of key value pairs we will use items() here so code will
# be doing iteration and will also provide the correct output along with unpack.
"""
"""
Dict1 = dict(List1)
for item, lollypop in Dict1.items():
    print(item, "and lolly is", lollypop)
"""

# Now we are getting the same output which we were getting above via list.

# Syntax to use boolean functions : String.isaplha(), String.isnumeric(), String.isalnum(), String.endswith()

#Exercise3 : To print the items of list which are collection of alphabets and ends with rry

"""
Mylist= ["Harry", "Larry", "Carry", "Harpic", "Vim Bar", 2, 5, 7, 10]
for item in Mylist:
    if str(item).isalpha() and item.endswith("rry"):
        print(item)
"""

#Exercise4 : To print the items of list which are collection of numbers and greater than equal to 6
"""
Mylist= ["Harry", "Larry", "Carry", "Harpic", "Vim Bar", 2, 5, 6, 7, 10, 1, 15]
for item in Mylist:
    if str(item).isnumeric() and item>=6:
        print(item)
"""
