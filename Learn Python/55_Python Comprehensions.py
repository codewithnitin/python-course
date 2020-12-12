
# ls = []
# for i in range(50):
#     if i%2==0:
#         ls.append(i)

# ls = [i for i in range(50) if i%2==0]
#
# print(ls)


"""

List_Comprehension : It is an one liner approach to complete above scenario here for loop will
remain same and if statement would be optional if it requires in code and first i would be the
variable which is going as an input into list in every iteration means it is a replacement of
i in ls.append(i)

List comprehenstion code :

ls = [i for i in range(50) if i%2==0]


"""

# dict = {}
# for i in range(50):
#     if i%3==0:
#         dict[i] = f"item {i}"
#         # dict.update({i:f"item {i}"})
#
# print(dict)



# dict = {i:f"item {i}" for i in range(50) if i%3==0}
#
# dict1 = {i:f"item {i}" for i in range(5)}
#
# dict2 = {value:key for key,value in dict1.items()}    # Reverse the dictionary by comprehension

# print(dict)
# print(dict1,"\n",dict2)


"""

Dict_Comprehension : It is an one liner approach to complete above scenario here for loop will
remain same and if statement would be optional if it requires in code and first i:f"item{i}" 
would be the variable which is going as an input into dictionary in every iteration means it is
a replacement of i:f"item{i}" in dict.update({i:f"item{i}"}) or dict[i] = f"item {i}"

Dictionary comprehension code :

dict = {i:f"item {i}" for i in range(50) if i%3==0}

Dictionary comprehension is benificial for reverse the dictionary like :

dict2 = {value:key for key,value in dict1.items()}

"""

# s = set()
# for i in range(10):
#     if i%2!=0:
#         s.add(i)
#
# print(s)

# s = {i for i in range(10) if i%2!=0}
#
# print(s)

# Dresses = {dress for dress in ["dress1", "dress2", "dress2", "dress1"]}
#
# print(Dresses)
# print(type(Dresses))


"""

Set_Comprehension : It is an one liner approach to complete above scenario here for loop will
remain same and if statement would be optional if it requires in code and first i would be the
variable which is going as an input into set in every iteration means it is a replacement of i
in s.add(i)

Set comprehension code :

s = {i for i in range(10) if i%2!=0}

"""

# def disp(n):
#     for i in range(n):
#         if i%2!=0:
#             yield(i)
#
#
# n = int(input("Enter the number\n"))
# g = disp(n)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# If n is equal to 10

# g = (i for i in range(10) if i%2!=0)
# print(g)
# print(g.__next__())
# for i in g:
#     print(i)

"""

Gen_Comprehension : It is an one liner approach to complete above scenario here for loop will
remain same and if statement would be optional if it requires in code and first i would be the
variable which is going as an input into generator in every iteration means it is a replacement
of i in yield(i)

Generator comprehension code : 

g = (i for i in range(10) if i%2!=0)

"""

class Comprehensionn:


    def list_comp(self):
        list = [input("Enter the input\n") for i in range(5)]
        return(list)

    def dict_comp(self):
        dict = {input("Enter the input\n"):i+2 for i in range(5)}
        return(dict)

    def set_comp(self):
        s = {input("Enter the input\n") for i in range(5)}
        return(s)


Comp = Comprehensionn()
while(True):
    print("You will have 5 things to input")
    n = int(input("Type 1 for list_comp, 2 for dict_comp and 3 for set_comp"))
    if n == 1:
        print(Comp.list_comp())
    elif n == 2:
        print(Comp.dict_comp())
    elif n == 3:
        print(Comp.set_comp())
    else:
        print("Please enter the correct input details")




