'''
This is the classic game 2048 where the user works with a 4x4 area to combine numbers to reach 2048
New numbers will be added to the board (2 or 4)
Only identical numbers can be combined
'''
#------------------------------------------------------------------------------------------------------------------------------------

from random import randint
from random import randomrange
from msvcrt import getch

#------------------------------------------------------------------------------------------------------------------------------------

def printBeginPrompt():
    print("Welcome to 2048!\nThis is the classic game where you will work with a 4x4 area of numbers!\nThe goal is to combine the number until you reach 2048!\nOnly like numbers can be combined.")

def gameOn():
    board = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    play = True
    while play:
        position = checkPosition(board)
        if position == 17:
            play = False

        addNum(board, str(position))

        printBoard(board)

        move = getMove()
        if move == "esc":
            play = False
        else:
            changeBoard(move)

def checkPosition(board):
    possiblePositionCopy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    possiblePosition = []
    result = 17
    for line in board:
        for pos in line:
            if pos == 0:
                possiblePosition.append(possiblePositionCopy.pop(0))
            else:
                possiblePositionCopy.remove(0)
    if possiblePosition.__len__() > 0:
        result = possiblePosition[randint(0, possiblePosition.__len__()-1)]
    return result
        

def addNum(board, position):
    num = randint(1,3)*2
    match position:
        case "0":
            board[0][0] = num
        case "1":
            board[0][1] = num
        case "2":
            board[0][2] = num
        case "3":
            board[0][3] = num
        case "4":
            board[1][0] = num
        case "5":
            board[1][1] = num
        case "6":
            board[1][2] = num
        case "7":
            board[1][3] = num
        case "8":
            board[2][0] = num
        case "9":
            board[2][1] = num
        case "10":
            board[2][2] = num
        case "11":
            board[2][3] = num
        case "12":
            board[3][0] = num
        case "13":
            board[3][1] = num
        case "14":
            board[3][2] = num
        case "15":
            board[3][3] = num

def printBoard(board):
    for line in board:
        for num in line:
            print(num, end= "  ")
        print("\n", end="")

def getMove():
    pass

def changeBoard(move):
    pass

def endPrompt():
    pass

#------------------------------------------------------------------------------------------------------------------------------------

printBeginPrompt()

gameOn()

play = endPrompt()