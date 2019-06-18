import sys
import pprint as pp

'''
solves game in which you connect the dots with the same colors together
'''

# dictionary of different colors and their position on the board
color_dict = {'G': [1, 0],
              'Y': [0, 6],
              'B': [6, 2],
              'R': [6, 3],
              'T': [1, 4],
              'O': [8, 6]}

# size of board
b_size = 9

def main():
    # initializing board size and location of dots on board
    board = [['_'] * b_size for _ in range(b_size)]
    board[1][0] = 'G'
    board[3][5] = 'G'
    board[0][6] = 'Y'
    board[2][5] = 'Y'
    board[6][2] = 'B'
    board[3][4] = 'B'
    board[6][3] = 'R'
    board[1][7] = 'R'
    board[1][4] = 'T'
    board[8][8] = 'T'
    board[8][6] = 'O'
    board[7][7] = 'O'

    colors(board, ['G', 'Y', 'B', 'R', 'T', 'O'], 0)

    # currently only doing this for the 'G' dot
    # check_area(board, [1, 0], board[1][0])

    pp.pprint(board)

# goes through the list of colors and calls check_area to connect them
# need to keep track of last "seen" dot placed so if color path does not exist, the path before it can be redone***
def colors(board, color_list, pos):
    # getting color positions from dictionary
    # makes code more readable
    x = color_dict[color_list[pos]][0]
    y = color_dict[color_list[pos]][1]

    if check_area(board, [x, y], board[x][y]):
        if pos < len(color_list):
            colors(board, color_list, (pos + 1))
        else:
            print('WE MADE IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    else:
        return





# finds path from one colored dot to the same colored dot
# can be optimized according to how the game works, but will do that later
# should also be able to be optimized code-wise, but will do that later
# returns True if color is placed, False if not (not implemented yet)
def check_area(board, tile, label):
    # initialization
    seen = 'X'
    board[tile[0]][tile[1]] = seen

    # checking if the next tile has the corresponding colored dot
    if         ((tile[0] > 0) and (board[tile[0] - 1][tile[1]] == label)) \
            or ((tile[0] < 8) and (board[tile[0] + 1][tile[1]] == label)) \
            or ((tile[1] > 0) and (board[tile[0]][tile[1] - 1] == label)) \
            or ((tile[1] < 8) and (board[tile[0]][tile[1] + 1] == label)):
        board[tile[0]][tile[1]] = label
        return True

    # checks if in bounds
    if tile[0] > 0:
        # checks if empty tile
        if board[tile[0] - 1][tile[1]] == '_':
            check_area(board, [tile[0] - 1, tile[1]], label)
            # if colored dot was reached, convert 'seen' dots to the initial colored dot
            if board[tile[0] - 1][tile[1]] == label:
                board[tile[0]][tile[1]] = label
                return True

    # all if statements follow pattern above
    if tile[0] < 8:
        if board[tile[0] + 1][tile[1]] == '_':
            check_area(board, [tile[0] + 1, tile[1]], label)
            if board[tile[0] + 1][tile[1]] == label:
                board[tile[0]][tile[1]] = label
                return True

    if tile[1] > 0:
        if board[tile[0]][tile[1] - 1] == '_':
            check_area(board, [tile[0], tile[1] - 1], label)
            if board[tile[0]][tile[1] - 1] == label:
                board[tile[0]][tile[1]] = label
                return True

    if tile[1] < 8:
        if board[tile[0]][tile[1] + 1] == '_':
            check_area(board, [tile[0], tile[1] + 1], label)
            if board[tile[0]][tile[1] + 1] == label:
                board[tile[0]][tile[1]] = label
                return True

    # if there is no place to go, reset
    board[tile[0]][tile[1]] = '_'

if __name__ == '__main__':
    main()