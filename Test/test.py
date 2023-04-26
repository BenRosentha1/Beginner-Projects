import numpy as np

def changeBoardRight(board):
    for line in board:
        zeros = line.count(0)
        for x in range(0, zeros):
            line.remove(0)
        for x in range (0, zeros):
            line.insert(0, 0)
    for line in board:
        for i in range(len(line)-1, 0, -1):
            if line[i] == line[i-1]:
                line[i] *= 2
                line[i-1] = 0

board = [[2, 0, 0, 2],
        [0, 0, 0, 2],
        [2, 0, 0, 0],
        [0, 0, 2, 2]]

lines = []
lines.insert

boardCopy = board.copy()
boardCopy = np.array(boardCopy).transpose().tolist()
changeBoardRight(boardCopy)
boardDoubleCopy = boardCopy.copy()
boardCopy = np.array(boardCopy).transpose().tolist()
for i in range(0, len(board)):
    boardCopy[i] = boardDoubleCopy[len(board)-i-1]
board = boardCopy

for line in board:
    print(line)
