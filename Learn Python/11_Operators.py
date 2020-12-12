"""
Operators in Python :

Arithmetic Operators
Assignment Operators
Comparision Operators
Logical Operators
Identity Operators
Membership Operators
Bitwise Operators

"""
"""
print("Arithmetic Operators")
print("5 + 6 is", 5 + 6)               # + operator adds the numbers
print("5 - 6 is", 5 - 6)               # - operator subtracts the numbers
print("5 * 6 is", 5 * 6)               # * operator multiply the numbers
print("5 / 6 is", 5 / 6)               # / operator divides the numbers
print("17 // 4 is", 17 // 4)           # // operator gives floor integer value except decimal one.
print("5 ** 3 is", 5 ** 3)             # ** operator exponential the number
print("15 % 2 is", 15 % 2)             # % (Modulus) operator gives the remainder
"""
"""
print("Assignment Operators")
x = 5
#x +=8                                 #x +=8 or x = x + 8
#x -=4                                 #x -=4 or x = x - 4
#x *=7                                 #x *=7 or x = x * 7
#x /=4                                 #x /=4 or x = x / 4
#x **=3                                #x **=3 or x = x**3
#x //=2                                #x //=2 or x = x//2
#x %=3                                 #x %=3 or x = x % 3
print(x)
"""
"""
print("Comparision Operator")
x = 5
#print(x == 2)            # == comparing the variable x values and gives output true or false
#print(x != 6)            # != not equal sign and gives output in true or false
#print(x > 4)             # > greater than sign and gives the output in true or false
#print(x < 4)             # < lesser than sign and gives the output in true or false
#print(x >= 4)   # >= greater than equal to sign and gives the output true either one condition is true
#print(x <= 8)   # <= less than equal to sign and gives the output true either one condition is true
"""


"""
print("Logical Operators")

Boolean table of and logical operator :

True and True           True
True and False          False
False and True          False
False and False         False

Boolean table of or logical operator :

True and True           True
True and False          True
False and True          True
False and False         False

Boolean table of not logical operator :

If original expression is true so output will be false or original one is false so output will be true

print(8>=9 and 4>3)
print(5>6 or 10<=9)
print(not(9<=5))
"""

"""
print("Identity Operators")
x = 9
y = 15
print(x is y)
print(x is not y)
"""

"""
print("Membership operator")

L1 = [1,5,7,12]
if 7 in L1:
    print("Yes, it is L1")
if 15 not in L1:
    print("Yes, it is not in L1")
"""

"""
print("Bitwise Operators")

0    00
1    01
2    10
3    11
4   100
5   101
6   110
7   111
8  1000
9  1001
10 1010
11 1011
12 1100
13 1101
14 1110
15 1111
"""
"""

& (AND) bitwise operator : If both the operand and its corresponding bits are 1 so return 
the value 1 otherwise 0

| (OR)  bitwise operator : If any operand value is 1 so return the value 1 otherwise 0

^ (XOR) bitwise operator : If both the operand along with the corresponding bits are opposite 
so return the value 1 otherwise 0

~ (NOT) or complement operator : Complement bitwise operator is an uniary operator so it works
on one operand and it returns one's complement of the number like 

Addition rule of binary :
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10 so here we return 0 and carry 1 to the next coloumn

Example of NOT operator :

x = 10 = 1010 (Binary)

~x = ~1010
   = -(1010 + 1)
   = -(1011)
   = -11
print(~x)            Output :      -11


print(6 & 10)
print(5 | 9)
print(6 ^ 12)
print(~9)

"""








