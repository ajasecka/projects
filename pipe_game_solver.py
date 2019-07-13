import pprint as pp
import time
import sys

'''
solves game to connect the dots with the same colors together
optimizations: pipes cannot be placed next to themselves
'''

# dictionary of different colors and their beginning and end positions on the board
color_dict = {'G': [[1, 3], [4, 4]],
              'Y': [[2, 1], [4, 1]],
              'B': [[1, 1], [4, 5]],
              'R': [[1, 0], [3, 5]],
              'O': [[5, 0], [3, 1]]}

# list of colors
color_list = list(color_dict.keys())

# size of board
b_size = 6

# time
t0 = time.time()

def main():
    # initializing board size and location of dots on board
    board = [['_'] * b_size for _ in range(b_size)]
    for color in color_list:
        for pos in color_dict[color]:
            board[pos[0]][pos[1]] = color

    # show original board
    pp.pprint(board)
    print('\n\n')

    # calls function initially
    board[color_dict[color_list[0]][0][0]][color_dict[color_list[0]][0][1]] = '_'
    colors(board, color_dict[color_list[0]][0], 0, None)

    print('No possible solution')


# finds path from one colored dot to the same colored dot
# can be optimized according to how the game works, but will do that later
def colors(board, tile, color, before):

    # other dot that is to be connected to
    end = color_dict[color_list[color]][1]

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
        if color < len(color_list) - 1:
            # goes to next color in the list
            board[color_dict[color_list[color + 1]][0][0]][color_dict[color_list[color + 1]][0][1]] = '_'
            colors(board, color_dict[color_list[color + 1]][0], color + 1, None)
            board[color_dict[color_list[color + 1]][0][0]][color_dict[color_list[color + 1]][0][1]] = color_list[color + 1]
        # all colors have been connected
        else:
            print('DONE!')
            print('time taken: {}'.format(time.time() - t0))
            pp.pprint(board)
            sys.exit(0)

    # checks if square is empty
    elif board[tile[0]][tile[1]] == '_':
        board[tile[0]][tile[1]] = color_list[color]
        colors(board, [tile[0] - 1, tile[1]], color, 'D')
        colors(board, [tile[0] + 1, tile[1]], color, 'U')
        colors(board, [tile[0], tile[1] - 1], color, 'R')
        colors(board, [tile[0], tile[1] + 1], color, 'L')

        board[tile[0]][tile[1]] = '_'

if __name__ == '__main__':
    main()
