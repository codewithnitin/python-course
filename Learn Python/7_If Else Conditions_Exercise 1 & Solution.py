# Write a program to show your age 18 plus which can get driving license?

print("Enter your age")
Age = int(input())
if Age<18:
    print("You cannot drive")
elif Age==18:
    print("We will think about it")
else:
    print("You can drive")