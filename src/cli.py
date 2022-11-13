# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import logic


class Game:
    def __init__(self, playerO, playerX):
        """Initializes the Game with player O, player X, and an empty board."""
        self.playerO = playerO
        self.playerX = playerX
        self.board = logic.Board()
        self.winner = None
        self.current_player = playerO

    def print_board(self):
        """Prints the current board."""

        for row in self.board.board:
            print('  | ' + row[0] + ' | ' + row[1] + ' | ' + row[2] + ' |')

    def print_winner(self):
        """Prints the winner."""

        self.print_board()
        if self.winner is None:
            print('It is a draw!')
        else:
            print('Player ' + self.winner + ' won!')

    def other_player(self):
        """Changes the current player to the other player."""

        if self.current_player == self.playerO:
            self.current_player = self.playerX
        else:
            self.current_player = self.playerO

    def run(self):

        while self.winner is None and self.board.check_draw() is False:
            self.print_board()
            self.current_player.get_move(self.board)
            self.winner = self.board.get_winner()
            self.other_player()

        self.print_winner()


if __name__ == '__main__':

    print('Tic Tac Toe Game!')
    print('Game Modes')
    print('1. Human vs. Human')
    print('2. Human vs. Bot')
    print('3. Bot   vs. Bot')
    print('Please Select Game Mode (1-3): ', end='')
    game_mode = input()

    while not str.isnumeric(game_mode) or int(game_mode) < 1 or int(game_mode) > 3:
        print('Error! Input Invalid! Please Try Again!')
        print('Please Select Game Mode: ', end='')
        game_mode = input()

    game_mode = int(game_mode)

    if game_mode == 1:
        player1 = logic.Human('O')
        player2 = logic.Human('X')
    elif game_mode == 2:
        player1 = logic.Human('O')
        player2 = logic.Bot('X')
    else:
        player1 = logic.Bot('O')
        player2 = logic.Bot('X')

    game = Game(player1, player2)
    game.run()
