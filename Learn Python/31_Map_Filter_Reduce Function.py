# Type casting of list elements


Numbers = ["5", "34", "64"]
# for i in range(len(Numbers)):               # Type casting of list into integer by len keyword
#     Numbers[i] = int(Numbers[i])
# print(Numbers[2] + 1)


                                 # OR

"""
map() : It is not a good habbit to run for loop all the time if we can perform the operation
with the help of one liner function map() which is useful to apply function to all the elements
of list
"""

# print(map(int, Numbers))

"""
Here, map function has a syntax : map(function, listname) so in above statement map function
puts int function to all the elements of listname Numbers and return the output which is not
in desired format so we typecast map into list by list(map(int, Numbers) and store it into one
variable called Num which is a new list which has an elements in integer form.

"""
# Num = list(map(int, Numbers))
# print(Num[2] + 1)




List = [2, 4, 9, 22, 6, 7]
#
# def sq(a):
#     return(a*a)
#
# List1 = list(map(sq, List))
# print(List1)

# List1 = list(map(lambda x:x*x, List))
# print(List1)






# def sq(a):
#     return(a*a)
#
# def cu(a):
#     return(a*a*a)
#
# Func = [sq,cu]
#
# for i in range(5):
#     var1 = list(map(lambda x:x(i), Func))
#     print(var1)







"""
filter() : It is used to apply function to all the elements of list as per our need
"""

L1 = [1,2,3,4,5,6,7,8,9]

# def num_greater_5(num):
#     return(num>5)
#
# num_greater = list(filter(num_greater_5, L1))
# print(num_greater)





"""
reduce() : 
"""

List_1 = [1,2,3,4]

# num = 0
# for item in List_1:
#     num = num + item
# print(num)



"""

We cannot use reduce() straight away like map() and filter() so we import reduce() which is
function of module functools which is given below :

"""

from functools import reduce

# Sum = reduce(lambda x,y:x+y, List_1)          # x,y : x+y in commulative form
# print(Sum)

Prod = reduce(lambda x,y:x*y, List_1)
print(Prod)


























"""

#Practice


# List = ["5","15","25","64","1"]
# List1 = []
#
#
# for i in range(len(List)):
#     a = int(List[i])
#     List1.append(a)
# print(List1)
# print(List1[3] + List1[4])


# a = list(map(int, List))
# print(type(a))
#
# print(a[3] + a[4])




List = [2,4,7,3,6,5]
# List1 = []
# for item in List:
#     List1.append(item*item)
# print(List1)


# def sq(n):
#     return(n*n)
#
# # a = list(map(sq, List))
# # print(a)



# def sq(n):
#     return(n*n)
#
# def cu(n):
#     return(n*n*n)
#
# Func = [sq,cu]
#
# for i in range(5):
#     print(list(map(lambda x:x(i), Func)))



# List = [3,5,7,2,10]
# List1 = []
# for item in List:
#     if item>=5:
#         List1.append(item)
# print(List1)

# def num(n):
#     if n>=5:
#         return(n)

# a = list(filter(num,List))
# # print(type(a))
#
# print(a)

# b = 0
# for i in a:
#     b = b + i
# print(b)




# from functools import reduce
#
# print(reduce(lambda x,y : x+y, a))         # Cumulative form



"""