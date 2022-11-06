# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable

def make_empty_board():
    return [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""

    # Check winner in rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    col = 0

    # Check winner in columns
    while col < 3:
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
        col += 1

    # Check winner in two diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def other_player(player):
    """Given the character for a player, returns the other player."""

    if player == 'O':
        return 'X'

    return 'O'


def get_board_from_index(board, index):
    """Given the board and the index, returns the character on that board."""

    row = int((index - 1) / 3)
    col = int((index - 1) % 3)

    return board[row][col]


def check_index(board, index):
    """Given the board and the index, check if the index from the player is valid or not."""

    if index < 1 or index > 9:
        return False
    if get_board_from_index(board, index) == 'X' or get_board_from_index(board, index) == 'O':
        return False

    return True
