"""
# Create a program to guess the number n=18 ?
"""
n=18
guess = 1
print("You will have nine chances to guess the number")
while(guess<10):
    i = int(input("Enter the number"))
    if i<n:
        print("You entered the number lesser than guess number")
    elif i>n:
        print("You entered the number greater than guess number")
    else:
        print("You hit the guess number")
        print(guess, "You took chances to guess the number")
        break
    print("You have left chances to guess the number", 9-guess)
    if guess<10:
        guess = guess + 1
    if guess==10:
        print("Game over")
        continue
