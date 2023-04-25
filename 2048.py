'''
This is the classic game 2048 where the user works with a 4x4 area to combine numbers to reach 2048
New numbers will be added to the board (2 or 4)
Only identical numbers can be combined
'''
#------------------------------------------------------------------------------------------------------------------------------------

from random import randint
from msvcrt import getch
import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------

def printBeginPrompt():
    print("Welcome to 2048!\nThis is the classic game where you will work with a 4x4 area of numbers!\nThe goal is to combine the number until you reach 2048!\nOnly like numbers can be combined.")

def gameOn():
    board = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    addNum(board, str(randint(1,2)*2))
    play = True
    while play:
        position = checkPosition(board)
        if position == 17:
            play = False
        else:
            addNum(board, str(position))

            printBoard(board)

            move = getMove()
            if move == "ESC":
                play = False
            else:
                changeBoard(board, move)

def checkPosition(board):
    possiblePositionCopy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    possiblePosition = []
    result = 17
    for line in board:
        for num in line:
            if num == 0:
                possiblePosition.append(possiblePositionCopy.pop(0))
            else:
                possiblePositionCopy.pop(0)
    if possiblePosition.__len__() > 0:
        result = possiblePosition[randint(1, possiblePosition.__len__()-1)]
    return result
        
def addNum(board, position):
    num = randint(1,2)*2
    match position:
        case "1":
            board[0][0] = num
        case "2":
            board[0][1] = num
        case "3":
            board[0][2] = num
        case "4":
            board[0][3] = num
        case "5":
            board[1][0] = num
        case "6":
            board[1][1] = num
        case "7":
            board[1][2] = num
        case "8":
            board[1][3] = num
        case "9":
            board[2][0] = num
        case "10":
            board[2][1] = num
        case "11":
            board[2][2] = num
        case "12":
            board[2][3] = num
        case "13":
            board[3][0] = num
        case "14":
            board[3][1] = num
        case "15":
            board[3][2] = num
        case "16":
            board[3][3] = num

def printBoard(board):
    for line in board:
        for num in line:
            print(num, end= "  ")
        print()
    print()

def getMove():
    move = "AGAIN"
    while move == "AGAIN":
        move = str(getch())
        if move == "b'q'":
            move = "ESC"
        elif move == "b'w'":
            move = "UP"
        elif move == "b'a'":
            move = "LEFT"
        elif move == "b's'":
            move = "DOWN"
        elif move == "b'd'":
            move = "RIGHT"
        else:
            move = "AGAIN"
    return move

def changeBoard(board, move):
    match move:
        case "UP":
            changeBoardUp(board)
        case "DOWN":
            changeBoardDown(board)
        case "RIGHT":
            changeBoardRight(board)
        case "LEFT":
            changeBoardLeft(board)

def changeBoardUp(board):
    boardCopy = board.copy()
    for i in range(0, 3):
        for j in range(0, 3):
            boardCopy[i][j] = board[-i][j]

    changeBoardRight(boardCopy)
    boardDoubleCopy = boardCopy.copy()
    for i in range(0, 3):
        for j in range(0, 3):
            boardCopy[-i][-j] = boardDoubleCopy[i][j]
    board = boardCopy

def changeBoardDown(board):
    pass

def changeBoardRight(board):
    for line in board:
        for i in range(0, 3):
            if line[i+1] == 0:
                line[i+1] = line[i]
                line[i] = 0
            elif line[i+1] == line[i]:
                line[i+1] *= 2
                line[i] = 0


def changeBoardLeft(board):
    boardCopy = board.copy()
    for line in boardCopy:
        line.reverse()
    changeBoardRight(boardCopy)
    for line in boardCopy:
        line.reverse()
    board = boardCopy


def printEndPrompt():
    response = "!"
    while response != "Y" and response != "y" and response != "N" and response != "n" and response != "":
        print("Thanks for playing 2048!\nWould you like to play again? (Y/N): ", end="")
        response = input()
    return response.upper()

def printSigniture():
    print("Thanks for playing!  Come back anytime!")

#------------------------------------------------------------------------------------------------------------------------------------

play = "Y"
while play == "Y":    
    printBeginPrompt()

    gameOn()

    play = printEndPrompt()

printSigniture()