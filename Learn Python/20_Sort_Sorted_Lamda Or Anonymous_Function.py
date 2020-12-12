"""
Nature or Syntax of sort() : listname.sort(key = none, reverse = False)

sort() :  It is used to sort the list only and by default it sorts the list in increasing
order

Note : It sorts the original list which means if you have a list x = [3, 5, 2] and x.sort()
so output will be [2, 3, 5] in terms of changes into the original list

sort(reverse=True) : It sorts the original list by decreasing order

Note : If we wish to do further sorting so we can use key of sort()

Note : sort() changes the original list if we have list of numbers only or strings only
means if we have list which is a collection of numbers and strings so sort() will not
perform the operation

"""
"""
a = []
for i in range(5):
    x = int(input("Enter the number"))
    a.append(x)
#print(a)                      #Printing list items which is user defined
#a.sort()                      #It sorts the original list in terms of increasing order
#print(a)
#a.sort(reverse=True)          #It sorts the original list in terms of descending order
#print(a)
"""


a = [[2,9],[1,3],[11,7]]
#print(a)                       #Printing list which is list of list
#a.sort()                       #It sorts first element of each indexing of list a
#print(a)
#a.sort(reverse=True)           #It sorts first element of each indexing of list a
#print(a)
""""
def a_list(element):
    return(element[1])
a.sort(key=a_list)       
print(a)
"""

"""
Sorting is done via key which is assigned by function a_list so here a_list will check all
the indexing of list a and will return element[1] for each indexing and then sort() comes
into a role to sort each return elements to give the desired output which is to sort list
of list in terms of increasing order for second element
"""
"""
def a_list(element):
    return(element[1])
a.sort(key=a_list, reverse=True)
print(a)
"""

"""
Sorting is done via key which is assigned by function a_list so here a_list will check all
the indexing of list a and will return element[1] for each indexing and then sort() comes
into a role to sort each return elements to give the desired output which is to sort list
of list in terms of decreasing order for second element
"""
b = ["aa", "b", "eeee", "ccc"]
#print(b)
#b.sort()                #It sorts the list by alphabet order in terms of increasing order
#print(b)
#b.sort(reverse=True)     #It sorts the list by alphabet order in terms of decreasing order
#print(b)
#b.sort(key=len)           #It sorts the list by length of the elements in list
#print(b)


b = [["aa", "cccc"], ["ccc", "aa"], ["b","d"]]
"""
def b_list(element):
    return(element[1])
b.sort(key=b_list)
print(b)
"""
"""
def b_list(element):
    return(element[1])
b.sort(key=b_list, reverse=True)
print(b)
"""

# Nature or Syntax of sorted() : sorted(iterable, key=none, reverse=False)
# We can use it for all the iterables list, set, dictionary, tuple and string
# It returns output in the form of new list means does not change the original list which
# were changing in previous listname.sort()

"""
Lamda or Anonymous function : It is used for convenience means if we do not use it still
we can perform our task

Now question is what is lamda function ?

Whatever we write under the definition or declaration of function till return in user
defined function we can replace it by one line function called lamda function

let us take an example of addition :

def addition(x,y):
    return(x+y)
    
    OR
    
addition = lamda x,y : x+y

# Both are same here
"""

# def add(a,b):
#     return(a + b)

add = lambda a,b: a + b
# print(add(4,5))

# def minus(x,y):
#     return(x-y)

minus = lambda x,y : x-y
# print(minus(9,4))


d = [[5,8],[11,2],[3,7]]
# def d_list(element):
#     return(element[1])

d_list = lambda element : element[1]
d.sort(key=d_list)
print(d)