#Exercise 3 : Faulty calculator

"""
Design a faulty calculator which will solve all the problems except following computations :
45*3 = 555, 56+9 = 77, 56/6=4

and                 # and is the keyword in Python which shows blue colour

"""

print("Enter your first number")
n1 = int(input())
print("Enter your second number")
n2 = int(input())
print("Enter your operator +,-,*,/")
n3 = input()
if n1==43 and n2==3 and n3=="*":
    print(555)
elif n3=="*":
    print(n1*n2)
elif n1==56 and n2==9 and n3=="+":
    print(77)
elif n3=="+":
    print(n1+n2)
elif n1==56 and n2==6 and n3=="/":
    print(4)
else:
    print(n1/n2)
