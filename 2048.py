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
    addNum(board, str(randint(1,2)*2))
    play = True
    while play:
        position = checkPosition(board)
        if position == 17:
            play = False
            play = checkAvailableMove(board)
            if play == False:
                printFailure()
        
        else:            
            printBoard(board)

            move = getMove()
            if move == "ESC":
                play = False
            else:
                changeBoard(board, move)
        
        
        addNum(board, str(position))
        play = checkWinner(board)

def checkAvailableMove(board):
    pass

def printFailure():
    print("I am sorry!  You have lost!")

def checkWinner(board):
    carryOn = True
    for line in board:
        for num in line:
            if num >= 2048:
                print("Congradulations!  You won!")
                CarryOn = False
    return carryOn

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
        result = possiblePosition[randint(0, possiblePosition.__len__()-1)]
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

def stripZeros(line):
    count = line.count(0)
    for i in range(0, count):
        line.remove(0)

def combineRight(line):
    for i in range(len(line)-1, 0, -1):
        if line[i] == line[i-1]:
            line[i] *=2
            line[i-1] = 0
    stripZeros(line)

def addZeros(line):
    for x in range(0, 4-len(line)):
        line.insert(0, 0)

def changeBoardUp(board):
    boardCopy = board
    boardCopy = np.array(boardCopy).transpose().tolist()
    changeBoardRight(boardCopy)
    for line in boardCopy:
        line.reverse()
    boardCopy = np.array(boardCopy).transpose().tolist()
    for i in range(0, len(boardCopy)):
        board[i] = boardCopy[i]

def changeBoardDown(board):
    boardCopy = board.copy()
    for line in boardCopy:
        line.reverse()
    boardCopy = np.array(boardCopy).transpose().tolist()
    changeBoardRight(boardCopy)
    boardCopy = np.array(boardCopy).transpose().tolist()
    for line in boardCopy:
        line.reverse()
    for i in range(0, len(boardCopy)):
        board[i] = boardCopy[i]

def changeBoardRight(board):
    for line in board:
        lineCopy = line
        stripZeros(lineCopy)
        combineRight(lineCopy)
        addZeros(lineCopy)
        line = lineCopy
         
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