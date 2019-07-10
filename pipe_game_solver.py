import pprint as pp

'''
solves game to connect the dots with the same colors together
no optimizations
'''

# dictionary of different colors and their beginning and end positions on the board
color_dict = {'G': [[0, 2], [3, 1]],
              'Y': [[0, 4], [3, 3]],
              'B': [[1, 2], [4, 2]],
              'R': [[0, 0], [4, 1]],
              'O': [[1, 4], [4, 3]]}

# list of colors
color_list = list(color_dict.keys())

# size of board
b_size = 5

# flag
win = False

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
    colors(board, color_dict[color_list[0]][0], 0)

    if not win:
        print('No possible solution')


# finds path from one colored dot to the same colored dot
# can be optimized according to how the game works, but will do that later
def colors(board, tile, color):

    # print(color_list[color])
    # pp.pprint(board)
    # print()

    # for modifying flag
    global win

    # checking if the current tile is out of bounds
    if (tile[0] < 0) or (tile[0] > (b_size - 1)) or (tile[1] < 0) or (tile[1] > (b_size - 1)):
        return

    # optimizations
    # if      (tile[0] - 1 > 0 and board[tile[0] - 1][tile[1]] == color_list[color]) or \
    #         (tile[0] + 1 < (b_size - 1) and board[tile[0] + 1][tile[1]] == color_list[color]) or \
    #         (tile[1] - 1 > 0 and board[tile[0]][tile[1] - 1] == color_list[color]) or \
    #         (tile[1] + 1 < (b_size - 1) and board[tile[0]][tile[1] + 1] == color_list[color]):
    #     return

    # getting color positions from dictionary
    # makes code more readable
    x1 = tile[0]
    y1 = tile[1]
    end = color_dict[color_list[color]][1]

    # if tile is the other colored dot
    if [x1, y1] == end:
        if color < len(color_list) - 1:
            # goes to next color in the list
            board[color_dict[color_list[color + 1]][0][0]][color_dict[color_list[color + 1]][0][1]] = '_'
            colors(board, color_dict[color_list[color + 1]][0], color + 1)
            board[color_dict[color_list[color + 1]][0][0]][color_dict[color_list[color + 1]][0][1]] = color_list[color + 1]
        # all colors have been connected
        else:
            print('DONE!')
            pp.pprint(board)
            win = True

    # checks if square is empty
    elif board[tile[0]][tile[1]] == '_':
        board[tile[0]][tile[1]] = color_list[color]
        colors(board, [tile[0] - 1, tile[1]], color)
        colors(board, [tile[0] + 1, tile[1]], color)
        colors(board, [tile[0], tile[1] - 1], color)
        colors(board, [tile[0], tile[1] + 1], color)

        board[tile[0]][tile[1]] = '_'

if __name__ == '__main__':
    main()