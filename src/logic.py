# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable

class Board:

    def __init__(self):
        """Initializes the board with index."""

        self.board = [['1', '2', '3'],
                      ['4', '5', '6'],
                      ['7', '8', '9']]

    def clear_board(self):
        """Clears the board."""

        self.board = [['1', '2', '3'],
                      ['4', '5', '6'],
                      ['7', '8', '9']]

    def get_winner(self):
        """Determines the winner of the given board.
                Returns 'X', 'O', or None."""

        # Check winner in rows
        for row in self.board:
            if row[0] == row[1] == row[2]:
                return row[0]

        col = 0

        # Check winner in columns
        while col < 3:
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.board[0][col]
            col += 1

        # Check winner in two diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None

    def get_character_from_index(self, index):
        """Given the index, returns the character on that board."""

        row = int((index - 1) / 3)
        col = int((index - 1) % 3)

        return self.board[row][col]

    def check_index(self, index):
        """Given the board and the index, check if the index from the player is valid or not."""

        if index < 1 or index > 9:
            return False
        if self.get_character_from_index(index) == 'X' or self.get_character_from_index(index) == 'O':
            return False

        return True

    def update_board(self, index, player):
        """Given the board, the index, and the player, updates the board."""

        if not self.check_index(index):
            return self.board

        row = int((index - 1) / 3)
        col = int((index - 1) % 3)

        self.board[row][col] = player

    def check_draw(self):
        """Given the board, check if the board is full and no winner can be determined.
        Returns True or False"""

        if self.get_winner() is not None:
            return False

        for row in self.board:
            for col in row:
                if col != 'O' and col != 'X':
                    return False

        return True


class Human:

    def __init__(self, player):
        """Initializes the player with O or X"""
        self.player = player

    def get_move(self, board, index):
        """Check whether the move is valid and update the board if true.
        Returns True if update successful, False if move is not valid."""

        if board.check_index(index) is False:
            return False
        else:
            board.update_board(index, self.player)
        return True

# TODO: Delete everything below
def make_empty_board():
    return [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']]


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


def update_board(board, index, player):
    """Given the board, the index, and the player, update and returns the board for the player."""

    if not check_index(board, index):
        return board

    row = int((index - 1) / 3)
    col = int((index - 1) % 3)

    board[row][col] = player

    return board


def check_draw(board):
    """Given the board, check if the board is full and no winner can be determined.
    Returns True or False"""

    if get_winner(board) is not None:
        return False

    for row in board:
        for col in row:
            if col != 'O' and col != 'X':
                return False

    return True
