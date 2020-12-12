List = ["Roti", "Sabzi", "Chawal"]

for item in List:
    print(item)

else:
    print("For loop ended properly")

               # OR

# for item in List:
#     if item == "Omellete":
#         break
#
# else:
#     print("For loop ended properly")


"""

Using else with for loop :

1) We can use else with for loop only when for loop is iterated completely like if we have list
when all the items are iterated after that else condition can be used , if we have string to 
iterate when all the characters are iterated then we can use the else condition.

2) We can also use else condition by using if statement in for loop.





In first approach for loop is iterated completely so else condition is executed.

In second approach we have if condition in for loop like 

if item == "Omellete":
    break
    
However we have no item omellete in List so for loop will be iterated completely and else 
condition will be executed.

Suppose if we have statement in for loop like 

if item == "Sabzi"
    break
    
Here once for loop will run so if item would be "Sabzi" which is the second element of List
so for loop will break and due to which for loop did not execute completely as we have one
more element "Chawal" present in List that is the reason else condition will not be executed.


"""