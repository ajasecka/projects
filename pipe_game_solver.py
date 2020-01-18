import pprint as pp
import time
import sys
import pygame
from pygame.locals import *

'''
solves game to connect the dots with the same colors together
optimizations: pipes cannot be placed next to themselves
'''

# dictionary of different colors and their beginning and end positions on the board
# color_dict = {'G': [[1, 3], [4, 4]],
#               'Y': [[2, 1], [4, 1]],
#               'B': [[1, 1], [4, 5]],
#               'R': [[1, 0], [3, 5]],
#               'O': [[5, 0], [3, 1]]}

# list of colors

# size of board
b_size = 6

# time
t0 = time.time()


# colors
BLACK : (0, 0, 0)
WHITE = (255, 255, 255)
COLOR_DICT = {
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'orange': (255, 178, 102)
}
SIZE = 50
COLOR_LIST = ['blue', 'red', 'green', 'yellow', 'orange']

board = [['_'] * b_size for _ in range(b_size)]
color_dict = {}
color_list = None



# pygame board that allows user to pick where dots are located
# once the user closes the window, the current dots placed will be used in determining the paths
# INPUT: N/A
# OUTPUT: list (NxN list with locations of dots), integer (number of colors used)
def create_board():
    pygame.init()
    squares = 6
    x = SIZE * squares
    y = SIZE * squares
    display = pygame.display.set_mode((x, y))
    pygame.display.set_caption('Pipe Game')

    for xx in range(squares):
        pygame.draw.line(display, WHITE, (xx * SIZE, 0), (xx * SIZE, x), 4)
        pygame.draw.line(display, WHITE, (0, xx * SIZE), (y, xx * SIZE), 4)

    color_choice = [0, 0]

    flag = False
    xy = None
    while not flag:
        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                yy = int(pos[0] / SIZE)
                xx = int(pos[1] / SIZE)

                draw_x = int(pos[0] - ((pos[0]) % SIZE) + (SIZE / 2))
                draw_y = int(pos[1] - ((pos[1]) % SIZE) + (SIZE / 2))
                pygame.draw.circle(display, COLOR_DICT[COLOR_LIST[color_choice[0]]], (draw_x, draw_y), int(SIZE * .4))

                if color_choice[1] == 0:
                    color_dict[COLOR_LIST[color_choice[0]]] = [None, None]

                board[xx][yy] = COLOR_LIST[color_choice[0]]
                color_dict[COLOR_LIST[color_choice[0]]][color_choice[1]] = [xx, yy]
                print(xx, yy)

                # if color_choice[1] == 1:
                    # TODO MAKE SURE COORDINATES ARE STORING CORRECTLY
                    # coordinate_dict[COLOR_LIST[color_choice[0]]] = [xy, (x, y)]
                    # print(coordinate_dict[COLOR_LIST[color_choice[0]]])

                color_choice = [color_choice[0] + int((color_choice[1] + 1) / 2), (color_choice[1] + 1) % 2]
                print(color_choice)

            if event.type == QUIT:
                flag = True

        pygame.display.update()

    pygame.quit()
    return


def draw_board():
    pygame.init()
    squares = 6
    x = SIZE * squares
    y = SIZE * squares
    display = pygame.display.set_mode((x, y))
    pygame.display.set_caption('Finished Game')

    for xx in range(squares):
        pygame.draw.line(display, WHITE, (xx * SIZE, 0), (xx * SIZE, x), 4)
        pygame.draw.line(display, WHITE, (0, xx * SIZE), (y, xx * SIZE), 4)

    for y, row in enumerate(board):
        for x, color in enumerate(row):
            if color != '_':
                pygame.draw.circle(display, COLOR_DICT[color], (int(x * SIZE + (SIZE / 2)), int(y * SIZE + (SIZE / 2))), int(SIZE * .4))

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
    board[color_dict[color_list[0]][0][0]][color_dict[color_list[0]][0][1]] = '_'
    colors(color_dict[color_list[0]][0], 0, None)

    print('No possible solution')


# finds path from one colored dot to the same colored dot
# can be optimized according to how the game works, but will do that later
def colors(tile, color, before):
    # pp.pprint(board)
    # other dot that is to be connected to
    end = color_dict[color_list[color]][1]
    print(end, tile)

    # checking if the current tile is out of bounds
    if (tile[0] < 0) or (tile[0] > (b_size - 1)) or (tile[1] < 0) or (tile[1] > (b_size - 1)):
        return

    # optimizations
    # checks if out of bounds, an adjacent tile is the same color, it was not the previous tile, and it is not the end tile
    if      (tile[0] - 1 > 0 and board[tile[0] - 1][tile[1]] == color_list[color] and before != 'U' and [tile[0] - 1, tile[1]] != end) or \
            (tile[0] + 1 < (b_size - 1) and board[tile[0] + 1][tile[1]] == color_list[color] and before != 'D' and [tile[0] + 1, tile[1]] != end) or \
            (tile[1] - 1 > 0 and board[tile[0]][tile[1] - 1] == color_list[color] and before != 'L' and [tile[0], tile[1] - 1] != end) or \
            (tile[1] + 1 < (b_size - 1) and board[tile[0]][tile[1] + 1] == color_list[color] and before != 'R' and [tile[0], tile[1] + 1] != end):
        return

    # if tile is the other colored dot
    if [tile[0], tile[1]] == end:
        print('color here')
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
