"""
Exercise : To assign input from your user from 1 to 100 so it will keep continuing and if we enter number
greater than 100 so output should come up "Congrats you have entered the number greater than 100

"""


while(True):
    n1 = int(input("Enter the number"))
    if n1<101:
        print("Keep continuing")
        n1 = n1 + 1
        continue
    print("Congrats you have entered the number greater than 100")
    break