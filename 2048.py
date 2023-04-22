'''
This is the classic game 2048 where the user works with a 4x4 area to combine numbers to reach 2048
New numbers will be added to the board (2, 4, 8)
Only identical numbers can be combined
'''
#------------------------------------------------------------------------------------------------------------------------------------

from random import randint

#------------------------------------------------------------------------------------------------------------------------------------

def printBeginPrompt():
    print("Welcome to 2048!/n  This is the classic game where you will work with a 4x4 area of numbers!/nThe goal is to combine the number until you reach 2048!/n  Only like numbers can be combined.")

def gameOn():
    pass

def endPrompt():
    pass

#------------------------------------------------------------------------------------------------------------------------------------

printBeginPrompt()

play = True
while play:
    gameOn()

    play = endPrompt()