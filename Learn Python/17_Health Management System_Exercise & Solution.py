"""
Health Management System  ( Helpful program for trainer or nutritionist for their client )
"""


def getdate():
    import datetime
    return datetime.datetime.now()
date = getdate()
def take(client):
    if client == 1:
        print("Harry")
        n2 = int(input("Type 1 for Harry's diet, 2 for Harry's exercise"))
        if n2 == 1:
            f = open("Harry_diet.txt", "a")
            f.write(str([str(date)]) + input("Enter the Harry's diet") + "\n")
            print("Successfully written")
        elif n2 == 2:
            f = open("Harry_exercise.txt", "a")
            f.write(str([str(date)]) + input("Enter the Harry's exercise") + "\n")
            print("Successfully written")
    elif client == 2:
        print("Rohan")
        n2 = int(input("Type 1 for Rohan's diet, 2 for Rohan's exercise"))
        if n2 == 1:
            f = open("Rohan_diet.txt", "a")
            f.write(str([str(date)]) + input("Enter the Rohan's diet") + "\n")
            print("Successfully written")
        elif n2 == 2:
            f = open("Rohan_exercise.txt", "a")
            f.write(str([str(date)]) + input("Enter the Rohan's exercise") + "\n")
            print("Successfully written")
    elif client == 3:
        print("Hammad")
        n2 = int(input("Type 1 for Hammad's diet, 2 for Hammad's exercise"))
        if n2 == 1:
            f = open("Hammad_diet.txt", "a")
            f.write(str([str(date)]) + input("Enter the Hammad's diet") + "\n")
            print("Successfully written")
        elif n2 == 2:
            f = open("Hammad_exercise.txt", "a")
            f.write(str([str(date)]) + input("Enter the Hammad's exercise") + "\n")
            print("Successfully written")
def retrieve(client):
    if client == 1:
        print("Harry")
        n2 = int(input("Type 1 for Harry's diet, 2 for Harry's exercise"))
        if n2 == 1:
            f = open("Harry_diet.txt", "r")
            print(f.read())
        elif n2 == 2:
            f = open("Harry_exercise.txt", "r")
            print(f.read())
    elif client == 2:
        print("Rohan")
        n2 = int(input("Type 1 for Rohan's diet, 2 for Rohan's exercise"))
        if n2 == 1:
            f = open("Rohan_diet.txt", "r")
            print(f.read())
        elif n2 == 2:
            f = open("Rohan_exercise.txt", "r")
            print(f.read())
    elif client == 3:
        print("Hammad")
        n2 = int(input("Type 1 for Hammad's diet, 2 for Hammad's exercise"))
        if n2 == 1:
            f = open("Hammad_diet.txt", "r")
            print(f.read())
        elif n2 == 2:
            f = open("Hammad_exercise.txt", "r")
            print(f.read())
print("Welcome to Health Management System")
n1 = int(input("What would you like to do ? Type 1 for log or 2 for retrieve the client's data"))
if n1 == 1:
    print("Log the client's data")
    client = int(input("Enter the client : Type 1 for Harry, 2 for Rohan, 3 for Hammad"))
    take(client)
elif n1 == 2:
    print("Retrieve the client's data")
    client = int(input("Enter the client : Type 1 for Harry, 2 for Rohan, 3 for Hammad"))
    retrieve(client)















