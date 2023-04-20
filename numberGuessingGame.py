'''
This is a number guessing game where the user will specify a range and a random number will be selected for them to guess.
If they are above or below the game will give them a hint and ask them to continue.
The game will only end if they ask it to stop or they get the correct answer.
'''
from random import randint as getNum

def printBeginPrompt():
    print("Welcome to the Number Guessing Game!!!\nThe objective of the game is... well... just guessing the correct number\n")

def collectRange():
    print("To start we need to specify the range!")
    print("What is the minimum (must be a number)?: ", end="")
    min = input()
    # Check if min is a digit
    while not min.isdigit():
        print("Invalid response!  Please try again and keep in mind the accepted answers (must be a number)!: ", end="")
        min = input()
    min = int(min)
    print("And a maximum (must be a number greater than the minimum)?: ", end="")
    max = input()
    # Check if max is both a digit and greater than min
    while True:
        try:
            max = int(max)
            while min>max:
                print("Invalid Response!  Please try again and keep in mind the accepted answers (must be a number greater than the minimum)!: ", end="")
                max = int(input())
            if max>min:
                break
            else:
                print("Invalid Response!  Please try again and keep in mind the accepted answers (must be a number greater than the minimum)!: ", end="")
                max = input()
        except:
            print("Invalid Response!  Please try again and keep in mind the accepted answers (must be a number greater than the minimum)!: ", end="")
            max = input()
    return min, max

def guess(correctNum):
    guess = correctNum+1
    while correctNum!=guess:
        print("Take a guess: ", end="")
        guess = input()
        while not guess.isdigit():
            print("Invalid Response!  Please try again and keep in mind the accepted answers (must be a number)!: ", end="")
            guess = input()
        guess = int(guess)
        if guess > correctNum:
            print("Nope!  You were above the correct number.  Try again!")
        elif guess < correctNum:
            print("Nope!  You were below the correct number.  Try again!")
    print("Way to go!  You got it right!  The correct number was: ", correctNum, end="!\n")

def printEndPrompt():
    print("Would you like to play again? (Y/N): ", end="")
    response = input()
    while response != "Y" and response != "y" and response != "N"  and response != "n" and response != "":
        print("Invalid response!  Please try again and keep in mind the accepted answers (Y/N)!: ", end="")
        response = input()
    return response.capitalize()

def printSigniture():
    print("Thanks for playing!  Come back anytime!")


printBeginPrompt()

play = "Y"

while play == "Y":
    min, max = collectRange()

    randomNum = getNum(min, max)

    guess(randomNum)

    play = printEndPrompt()

printSigniture()

