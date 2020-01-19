import pprint as pp
import time
import sys
import pygame
from pygame.locals import *

'''
solves game to connect the dots with the same colors
GUI allows user to input where the dots are placed
press the X button once finished with drawing the board to solve

optimizations: pipes cannot be placed next to themselves
'''

# size of board
B_SIZE = 7

# physical size of blocks
SIZE = 50

# time
t0 = None

# colors
WHITE = (255, 255, 255)
COLOR_DICT = {
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'orange': (255, 128, 0),
    'teal': (51, 255, 255),
    'pink': (255, 0, 255),
    'maroon': (153, 0, 0)
}
COLOR_LIST = ['blue', 'red', 'green', 'yellow', 'orange', 'teal', 'pink', 'maroon']

# empty board
board = [['_'] * B_SIZE for _ in range(B_SIZE)]

# dictionary of color locations, along with list of used colors
color_dict = {}
color_list = None


# pygame board that allows user to pick where dots are located
# once the user closes the window, the current dots placed will be used in determining the paths
# INPUT: N/A
# OUTPUT: N/A
def create_board():
    x = SIZE * B_SIZE
    y = SIZE * B_SIZE

    # initializing game
    pygame.init()
    display = pygame.display.set_mode((x, y + SIZE))
    pygame.display.set_caption('Pipe Game')

    # drawing board
    for i in range(B_SIZE):
        pygame.draw.line(display, WHITE, (i * SIZE, 0), (i * SIZE, x), 4)
        pygame.draw.line(display, WHITE, (0, i * SIZE), (y, i * SIZE), 4)

    # management of which color and how many are on board
    color_choice = [0, 0]
    flag = False

    # running pygame and waiting until X box is clicked
    while not flag:
        pygame.draw.rect(display, COLOR_DICT[COLOR_LIST[color_choice[0]]], (0, y, x, SIZE))

        for event in pygame.event.get():
            # if board is clicked
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                yy = int(pos[0] / SIZE)
                xx = int(pos[1] / SIZE)

                draw_x = int(pos[0] - ((pos[0]) % SIZE) + (SIZE / 2))
                draw_y = int(pos[1] - ((pos[1]) % SIZE) + (SIZE / 2))
                pygame.draw.circle(display, COLOR_DICT[COLOR_LIST[color_choice[0]]], (draw_x, draw_y), int(SIZE * .4))

                # initializing list in dictionary
                if color_choice[1] == 0:
                    color_dict[COLOR_LIST[color_choice[0]]] = [None, None]

                # setting location of color on board
                board[xx][yy] = COLOR_LIST[color_choice[0]]
                color_dict[COLOR_LIST[color_choice[0]]][color_choice[1]] = [xx, yy]
                print(xx, yy)

                color_choice = [color_choice[0] + int((color_choice[1] + 1) / 2), (color_choice[1] + 1) % 2]
                print(color_choice)

            if event.type == QUIT:
                flag = True
        pygame.display.update()

    pygame.quit()
    return


# draws completed board once the game has been solved
def draw_board():
    # initializing game
    pygame.init()
    x = SIZE * B_SIZE
    y = SIZE * B_SIZE
    display = pygame.display.set_mode((x, y))
    pygame.display.set_caption('Finished Game')

    # drawing board
    for xx in range(B_SIZE):
        pygame.draw.line(display, WHITE, (xx * SIZE, 0), (xx * SIZE, x), 4)
        pygame.draw.line(display, WHITE, (0, xx * SIZE), (y, xx * SIZE), 4)

    # drawing circles on board
    for y, row in enumerate(board):
        for x, color in enumerate(row):
            if color != '_':
                pygame.draw.circle(display, COLOR_DICT[color], (int(x * SIZE + (SIZE / 2)), int(y * SIZE + (SIZE / 2))), int(SIZE * .4))

    # displaying board until X button is pushed
    flag = False
    while not flag:
        for event in pygame.event.get():
            pygame.display.update()

            if event.type == QUIT:
                flag = True
    pygame.quit()

def main():
    # initializing board size and location of dots on board
    create_board()
    # changing global variable
    global color_list
    color_list = list(color_dict.keys())

    # show original board
    pp.pprint(board)
    print('\n\n')

    # calls function initially
    global t0
    t0 = time.time()
    board[color_dict[color_list[0]][0][0]][color_dict[color_list[0]][0][1]] = '_'
    colors(color_dict[color_list[0]][0], 0, None)

    print('No possible solution')


# finds path from one colored dot to the same colored dot
# can be optimized according to how the game works, but will do that later
def colors(tile, color, before):

    # other dot that is to be connected to
    end = color_dict[color_list[color]][1]

    # checking if the current tile is out of bounds
    if (tile[0] < 0) or (tile[0] > (B_SIZE - 1)) or (tile[1] < 0) or (tile[1] > (B_SIZE - 1)):
        return

    # optimizations
    # checking if an adjacent tile is the same color
    if      (tile[0] - 1 >= 0 and board[tile[0] - 1][tile[1]] == color_list[color] and before != 'U' and [tile[0] - 1, tile[1]] != end) or \
            (tile[0] + 1 <= (B_SIZE - 1) and board[tile[0] + 1][tile[1]] == color_list[color] and before != 'D' and [tile[0] + 1, tile[1]] != end) or \
            (tile[1] - 1 >= 0 and board[tile[0]][tile[1] - 1] == color_list[color] and before != 'L' and [tile[0], tile[1] - 1] != end) or \
            (tile[1] + 1 <= (B_SIZE - 1) and board[tile[0]][tile[1] + 1] == color_list[color] and before != 'R' and [tile[0], tile[1] + 1] != end):
        return

    # if tile is the other colored dot
    if [tile[0], tile[1]] == end:
        if color < len(color_list) - 1:
            # goes to next color in the list
            board[color_dict[color_list[color + 1]][0][0]][color_dict[color_list[color + 1]][0][1]] = '_'
            colors(color_dict[color_list[color + 1]][0], color + 1, None)
            board[color_dict[color_list[color + 1]][0][0]][color_dict[color_list[color + 1]][0][1]] = color_list[color + 1]
        # all colors have been connected
        else:
            print('DONE!')
            print(f'time taken: {time.time() - t0}')
            pp.pprint(board)
            draw_board()
            sys.exit(0)

    # checks if square is empty
    elif board[tile[0]][tile[1]] == '_':
        board[tile[0]][tile[1]] = color_list[color]

        colors([tile[0] - 1, tile[1]], color, 'D')
        colors([tile[0] + 1, tile[1]], color, 'U')
        colors([tile[0], tile[1] - 1], color, 'R')
        colors([tile[0], tile[1] + 1], color, 'L')

        board[tile[0]][tile[1]] = '_'

if __name__ == '__main__':
    main()
