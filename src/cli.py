# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import logic


def print_board(board):
    """Prints the current board"""

    for row in board:
        print('  | ' + row[0] + ' | ' + row[1] + ' | ' + row[2] + ' |')


if __name__ == '__main__':
    board = logic.make_empty_board()
    winner = None
    player = 'X'
    print('Tic Tac Toe Game!')

    while winner is None:
        player = logic.other_player(player)
        print_board(board)
        print('Player ' + player + ' enter the location for your move (1-9): ', end='')
        index = int(input())

        # Check if player input is valid
        while not logic.check_index(board, index):
            print('Error! Input Invalid! Please Try Again!')
            print('Player ' + player + ' enter the location for your move (1-9): ', end='')
            index = int(input())

        # Update the board with player input
        logic.update_board(board, index, player)

        # Check if there is a winner
        winner = logic.get_winner(board)
        print('')

        # If there is no winner and the board is full, end the game
        if logic.check_draw(board):
            break

    # Print current board and the result of the game
    print_board(board)
    if winner is None:
        print('It is a draw!')
    else:
        print('Player ' + winner + ' won!')
