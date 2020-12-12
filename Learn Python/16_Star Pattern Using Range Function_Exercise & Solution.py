"""
Create a pattern in which we will take input as a number from user to display
pattern
                    *
                    **
                    ***
                    ****
                    *****

if boolean user input is True and if it is False then display a pattern

                    *****
                    ****
                    ***
                    **
                    *
?
"""

n = int(input("Enter the number of rows"))
b = bool(int(input("Type 1 for True or 0 for False")))
print(b)
if b == True:
    for i in range(1,n+1):
        for j in range(i):
            print("*", end=" ")
        print()
elif b == False:
    for i in range(1,n+1):
        for j in range((n+1)-i):
            print("*", end=" ")
        print()






