import sys
import pprint as pp

'''
solves game in which you connect the dots with the same colors together
'''

# dictionary of different colors and their beginning and end positions on the board
color_dict = {'G': [[0, 2], [3, 1]],
              'Y': [[0, 4], [3, 3]],
              'B': [[1, 2], [4, 2]],
              'R': [[0, 0], [4, 1]],
              'O': [[1, 4], [4, 3]]}

color_list = list(color_dict.keys())

# size of board
b_size = 5


def main():
    # initializing board size and location of dots on board
    board = [['_'] * b_size for _ in range(b_size)]
    for color in color_list:
        for pos in color_dict[color]:
            board[pos[0]][pos[1]] = color

    # pp.pprint(board)
    for x in board:
        print(x)
    print('\n\n')

    board[color_dict[color_list[0]][0][0]][color_dict[color_list[0]][0][1]] = '_'
    colors(board, color_dict[color_list[0]][0], 0)

    # currently only doing this for the 'G' dot
    # check_area(board, [1, 0], board[1][0])

    # pp.pprint(board)

# goes through the list of colors and calls check_area to connect them
# finds path from one colored dot to the same colored dot
# can be optimized according to how the game works, but will do that later
def colors(board, tile, color):

    # checking if the current tile is out of bounds
    if (tile[0] < 0) or (tile[0] > (b_size - 1)) or (tile[1] < 0) or (tile[1] > (b_size - 1)):
        return

    # getting color positions from dictionary
    # makes code more readable
    x1 = tile[0]
    y1 = tile[1]
    end = color_dict[color_list[color]][1]

    # if tile is the other colored dot
    if [x1, y1] == end:
        if color < len(color_list) - 1:
            board[color_dict[color_list[color + 1]][0][0]][color_dict[color_list[color + 1]][0][1]] = '_'
            colors(board, color_dict[color_list[color + 1]][0], color + 1)
            board[color_dict[color_list[color + 1]][0][0]][color_dict[color_list[color + 1]][0][1]] = color_list[color + 1]
            # something to do with here
        else:
            print('DONE! (HOPEFULLY)')
            pp.pprint(board)

    #fix this - can go back into the original square
    elif board[tile[0]][tile[1]] == '_':
        board[tile[0]][tile[1]] = color_list[color]
        # print('up')
        colors(board, [tile[0] - 1, tile[1]], color)
        # print('down')
        colors(board, [tile[0] + 1, tile[1]], color)
        # print('left')
        colors(board, [tile[0], tile[1] - 1], color)
        # print('right')
        colors(board, [tile[0], tile[1] + 1], color)

        board[tile[0]][tile[1]] = '_'

if __name__ == '__main__':
    main()