import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (in pixels)
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("2048")

# Define the colors used in the game
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
red = (255, 0, 0)

# Define the font used in the game
font = pygame.font.Font(None, 32)

# Define the grid size and tile size
grid_size = 4
tile_size = 100

# Define the initial board state
board = [[0 for x in range(grid_size)] for y in range(grid_size)]
score = 0

# Add two random tiles to the board
def add_random_tile():
    empty_tiles = [(x, y) for x in range(grid_size) for y in range(grid_size) if board[x][y] == 0]
    if empty_tiles:
        x, y = random.choice(empty_tiles)
        board[x][y] = 2 if random.random() < 0.9 else 4

# Draw the board
def draw_board():
    screen.fill(black)
    for x in range(grid_size):
        for y in range(grid_size):
            tile = board[x][y]
            color = gray if tile == 0 else (255 - tile * 15, 255 - tile * 15, 255 - tile * 15)
            rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, color, rect)
            if tile > 0:
                text = font.render(str(tile), True, black)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.flip()

# Move the tiles in the specified direction
def move(direction):
    global score
    if direction == "left":
        for y in range(grid_size):
            for x in range(grid_size - 1):
                if board[x][y] == 0:
                    continue
                for i in range(x + 1, grid_size):
                    if board[i][y] == 0:
                        continue
                    if board[x][y] == board[i][y]:
                        board[x][y] *= 2
                        score += board[x][y]
                        board[i][y] = 0
                    break
                if board[x][y] != 0 and board[x+1][y] == 0:
                    board[x+1][y] = board[x][y]
                    board[x][y] = 0
    elif direction == "right":
        for y in range(grid_size):
            for x in range(grid_size - 1, 0, -1):
                if board[x][y] == 0:
                    continue
                for i in range(x - 1, -1, -1):
                    if board[i][y] == 0:
                        continue
                    if board[x][y] == board[i][y]:
                        board[x][y] *= 2
                        score += board[x][y]
                        board[i][y] = 0
                    break
                if board[x][y] != 0 and board[x-1][y]:
                    board[x-1][y] = board[x][y]
                    board[x][y] = 0
    elif direction == "up":
        for x in range(grid_size):
            for y in range(grid_size - 1):
                if board[x][y] == 0:
                    continue
                for i in range(y + 1, grid_size):
                    if board[x][i] == 0:
                        continue
                    if board[x][y] == board[x][i]:
                        board[x][y] *= 2
                        score += board[x][y]
                        board[x][i] = 0
                    break
                if board[x][y] != 0 and board[x][y+1] == 0:
                    board[x][y+1] = board[x][y]
                    board[x][y] = 0
    elif direction == "down":
        for x in range(grid_size):
            for y in range(grid_size - 1, 0, -1):
                if board[x][y] == 0:
                    continue
                for i in range(y - 1, -1, -1):
                    if board[x][i] == 0:
                        continue
                    if board[x][y] == board[x][i]:
                        board[x][y] *= 2
                        score += board[x][y]
                        board[x][i] = 0
                    break
                if board[x][y] != 0 and board[x][y-1] == 0:
                    board[x][y-1] = board[x][y]
                    board[x][y] = 0

# Check if the game is over
def game_over():
    for x in range(grid_size):
        for y in range(grid_size):
            if board[x][y] == 0:
                return False
            if x > 0 and board[x][y] == board[x-1][y]:
                return False
            if x < grid_size - 1 and board[x][y] == board[x+1][y]:
                return False
            if y > 0 and board[x][y] == board[x][y-1]:
                return False
            if y < grid_size - 1 and board[x][y] == board[x][y+1]:
                return False
    return True

# Main game loop
add_random_tile()
add_random_tile()
draw_board()
game_over_message = None
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move("left")
            elif event.key == pygame.K_RIGHT:
                move("right")
            elif event.key == pygame.K_UP:
                move("up")
            elif event.key == pygame.K_DOWN:
                move("down")
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_r:
                board = [[0 for x in range(grid_size)] for y in range(grid_size)]
                score = 0
                add_random_tile()
                add_random_tile()
                game_over_message = None
    draw_board()
    if game_over() and not game_over_message:
        game_over_message = font.render("Game Over!", True, red)
        game_over_rect = game_over_message.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(game_over_message, game_over)