
"""
while(True) or while(1) is the loop which always runs or continues and it is used to apply condition under it
with the help of break or continue statement.

Break : If we wish to break the while(True) loop so we will use break statement

Continue : It continues the current iteration and moves back to while(True) so whatever written in the code
below continue statement that will not be read by interpreter and it will go back to while(True) and once
the continue statement is false then it will move ahead in the code to read the further code and once
interpreter gets break statement so will break the while loop and move to line 25.


"""
"""
i = 0
while(True):
    if i+1<5:
        i = i + 1
        continue
    print(i+1, end =" ")
    if i==44:
        break
    i = i + 1
"""

#break the while loop

"""
Exercise5 : To assign input from your user from 1 to 100 so it will keep continuing and if we enter number 
greater than 100 so output should come up "Congrats you have entered the number greater than 100

"""
"""

while(True):
    print("Enter your number")
    i = int(input())
    if i>100:
        print("Congrats you have entered the number greater than 100")
        break
    else:
        print("Try again")
        i = i + 1
        continue
        
"""
"""
        
while(True):
    n1 = int(input("Enter the number"))
    if n1<101:
        print("Keep continuing")
        n1 = n1 + 1
        continue
    print("Congrats you have entered the number greater than 100")
    break
    
"""



"""
n = 16
guess = 1
print("You will have 5 chances to guess only")
while(guess<6):
    i = int(input("Enter the guess number"))
    if i>n:
        print("Entering the number greater than guess number")
    elif i<n:
        print("Entering the number lesser than guess number")
    else:
        print("You hit the guess number")
        print("You took guesses to complete the guess", guess)
        break
    print("no. of guesses left", 5-guess)
    if guess<6:
        guess = guess + 1
    if guess==6:
        guess = guess + 1
        print("Game over")
        continue
"""
"""
#Practice

while(True):
    print("Enter the number")
    i = int(input())
    if i<101:
        i = i + 1
        print("Try again")
        continue
    print("Congrats you have entered the number greater than 100")
    if i>100:
        break
    i = i + 1
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
"""

























# Create a program to guess the number n = 20 and you will have 10 guesses to guess the number ?

guess = 1
while(True):
    i = int(input("Enter your number"))
    if i<20:
        print("Your guess number is slightly greater")
    elif i>20:
        print("Your guess number is slightly lesser")
    else:
        print("You hit the target, Bingo!")
        print("You took chances to guess the number", guess)
        break
    print("Number of guesses you have", 10-guess)
    guess = guess + 1
    if guess>10:
        print("Gameover")
        break
    continue

























