
"""
Difference between == vs is in python ?


==    : It checks equality
        Two objects have the same value

is    : It checks memory location or identities
        Two references refer to the same object


Now I will take an example to elaborate these above statements which will clear
the concept how they are different to each other

"""

a = [4,5,8,9]
b = a
# print(type(a), type(b))
# print(a, b)

# b[1] = 10
# print(a, b)

# print(a == b)
# print(a is b)

c = a.copy()
# print(c)
# print(a == c, b == c)
# print(a is c, b is c)
# print(id(a), id(b), id(c))

"""
First of all we created one list [4,5,8,9] into a variable a means a = [4,5,8,9]
then we created another variable b in which we are pointing variable a it clears
both a and b variable are associated with same list object (Matlab a & b variable  
alag alag hai pr unki list ek he hai means b ke liye koi new list create nhi ki
a aur b same list use kr rhe hai so in memory location of python there will be
only one list object [4,5,8,9] which is applicable for both the variables a & b)

Then we printed print(type(a), type(b)) so will get an output class list class
list then we printed print (a, b) so will get an output [4,5,8,9] [4,5,8,9] so
got two list here ( par internally python memory location me ek he list object
hai [4,5,8,9] for both the variable a and b same list use kr rhe hai )

If we change b[1] = 10 so it will change a[1] automatically ( kyunki vastav me
list object toh ek he hai dono variable ke liye matlab ek list share kr rhe hai
dono object so if we printed print(a, b) so will get an output [4,10,8,9] [4,10
8,9] ( ye dono variable a and b ki list same hai kyunki actual me dono ek he
list object ko use kr rhe hai )

Then comment out b[1] = 10

if we print print(a == b)  so we will get an output TRUE because there are two
objects which are having same value ( Dono object bhale he different hai par
unki value same hai jo ki list hai [4,5,8,9] and if we print print(a is b) so
still will get an output TRUE because two objects or references having the same
list object ( Ye bhi True aayega because alag alag hai dono refrences a and b
par list object [4,5,8,9] toh ek he use kr rhe hai kyunki humne b variable ke
liye koi new list create nhi ki sirf a wali list ko he point kiya b variable me
jisse do variable hai pr list object same hai )

Then we created another variable c which is a copy list of variable a like this
c = a.copy() as we created copy list but it will be different list in memory
location of python ( Yaha c variable me jo list aayi beshak a variable me jo
list hai uski he copy hai lekin ye new list hai kyunki a me padi list ko c var
me point na karke humne a var me padi list ki copy banai c variable me toh ye
nee list hogi jo alag memory location me store hogi python ke )

We printed print(c) so will get an out [4,5,8,9] but it is a new list which is
located at different memory location.

If we print print(a == c, b == c) so output would be TRUE TRUE as we have diff
objects but their values are same which is [4,5,8,9] 

If we print print(a is c, b is c) so output would be FALSE FALSE this is because
references a and b having same list object [4,5,8,9] as they are sharing the same
list object due to pointing case but c is a copy list of variable a so even list
looks similar [4,5,8,9] but actually it is stored in a different memory location
so it is different list object ( yaha a and b variables toh same list object ko
share kr rhe hai pr c variable jisme copy list hai variable a ki woh actual me
different list hai jo different memory location me store hui hai so a & c and b
& c references ke list object alag hai aur hum jante hai jb 2 alag alag variables
or references refer krte hai same object ko toh unke bich is TRUE hota hai par 
yaha 2 references a & c, b & c ke object same nahi hai dono alag list hai isliye
output FALSE FALSE hai) 


As we learnt in object introspection if we print(id(obj)) so it gives unique id
so we printed print(id(a), id(b), id(c)) output would be like

41671656 41671656 42763176

This happened because a and b variable are sharing the same list object so their
id would be same ( kyunki b ke liye toh koi new list create he nhi ki thi a aur
b toh same he list use kr rhe hai toh id same hogi but c ki id alag hogi kyunki
usme jo list hai woh different list hai jo different memory location pe store hai)


Quiz :

a = [1,5,7,"34"]
b = [1,5,7,"34"]

print(a == b)      TRUE    ( Due to same value of two diff objects )
print(a is b)      FALSE   ( Due to not same object as two references having diff
list object )

"""

