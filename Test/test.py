import numpy as np

def changeBoardRight(board):
    for line in board:
        lineCopy = line
        stripZeros(lineCopy)
        combineRight(lineCopy)
        addZeros(lineCopy)
        line = lineCopy

def stripZeros(line):
    count = line.count(0)
    for i in range(0, count):
        line.remove(0)

def combineRight(line):
    for i in range(len(line)-1, 0, -1):
        if line[i] == line[i-1]:
            line[i] *=2
            del line[i-1]

def addZeros(line):
    for x in range(0, 4-len(line)):
        line.insert(0, 0)

board = [[2, 0, 0, 0],
        [0, 0, 2, 0],
        [2, 0, 0, 2],
        [0, 0, 2, 0]]

lines = []
lines.remove

board = np.array(board).transpose().tolist()
changeBoardRight(board)
for line in board:
    line.reverse()
board = np.array(board).transpose().tolist()

for line in board:
    print(line)
