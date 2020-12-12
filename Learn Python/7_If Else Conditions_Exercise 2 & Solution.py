#Exercise2 : Age between 7 to 100

print("Enter your age")
Age = int(input())
if Age<7:
    print("You cannot use computer")
elif Age==7:
    print("We will think about it")
elif 7<Age<101:
    print("You can use computer")
else:
    print("Please enter correct age")