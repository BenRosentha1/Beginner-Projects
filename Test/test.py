from msvcrt import getch

run = True
while run:
    char = str(getch())
    if char == "b'q'":
        run = False
    else:
        print(char)