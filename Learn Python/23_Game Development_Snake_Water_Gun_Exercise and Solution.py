# Snake water gun using random module


import random
turn = 1
Count_user = 0
Count_computer = 0
Tie_breaker = 0
print("Welcome into the game SnakeWaterGun for 5 turns")
while(True):
    i = int(input("Type 1 for Snake, 2 for Water, 3 for Gun\n"))
    List = ["Snake", "Water", "Gun"]
    Computer_choice = random.choice(List)
    if i == 1:
        print("Snake")
        print(Computer_choice)
        if Computer_choice == "Snake":
            Tie_breaker = Tie_breaker + 1
            print("Same choice")
        elif Computer_choice == "Water":
            Count_user = Count_user + 1
            print("You won")
        else:
            Count_computer = Count_computer + 1
            print("Computer won")
    elif i == 2:
        print("Water")
        print(Computer_choice)
        if Computer_choice == "Snake":
            Count_computer = Count_computer + 1
            print("Computer won")
        elif Computer_choice == "Water":
            Tie_breaker = Tie_breaker + 1
            print("same choice")
        else:
            Count_user = Count_user + 1
            print("You won")
    elif i == 3:
        print("Gun")
        print(Computer_choice)
        if Computer_choice == "Snake":
            Count_user = Count_user + 1
            print("You won")
        elif Computer_choice == "Water":
            Count_computer = Count_computer + 1
            print("Computer won")
        else:
            Tie_breaker = Tie_breaker + 1
            print("Same choice")
    print("Number of turns left", 5 - turn)
    print(f"Total score : User : {Count_user} Computer : {Count_computer} and Tie : {Tie_breaker}")
    turn = turn + 1
    if turn>5:
        print("Game over")
        break





# Snake Water Gun Practice

"""

import random

print("Welcome into our childhood game Snake Water Gun")
turns = 1
Cc = 0
Cu = 0
Ct = 0
while(True):
    n1 = int(input("Enter the user input : Type 1 for Snake, 2 for Water, 3 for Gun"))
    n2 = random.choice(["Snake","Water","Gun"])
    if n1 == 1 and n2 == "Snake":
        print("Tie")
        Ct += 1
    elif n1 == 1 and n2 == "Water":
        print("You won")
        Cu += 1
    elif n1 == 1 and n2 == "Gun":
        print("Computer won")
        Cc += 1
    elif n1 == 2 and n2 == "Snake":
        print("Computer won")
        Cc += 1
    elif n1 == 2 and n2 == "Water":
        print("Tie")
        Ct += 1
    elif n1 == 2 and n2 == "Gun":
        print("You won")
        Cu += 1
    elif n1 == 3 and n2 == "Snake":
        print("You won")
        Cu += 1
    elif n1 == 3 and n2 == "Water":
        print("Computer won")
        Cc += 1
    else:
        print("Tie")
        Ct += 1
    print("Number of turns left in the game", 10-turns)
    print(f"Number of wins by user : {Cu} and computer : {Cc} and tie-breaker : {Ct}")
    turns = turns + 1
    if turns > 10:
        print("Game over")
        break

"""