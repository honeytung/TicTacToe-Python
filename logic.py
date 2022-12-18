# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable

import pandas as pd
import numpy as np


class DataSave:
    def __init__(self, filename):
        """Initializes the database with the csv filename."""

        self.filename = filename
        self.games = None
        self.load_game()

    def load_game(self):
        """Tries the load game from the filename. If file not found then create a new database."""

        try:
            self.games = pd.read_csv(self.filename, index_col=0)
        except FileNotFoundError:
            self.games = pd.DataFrame(columns=[
                "Game ID",
                "Player 1",
                "Player 2",
                "Player 1 Type",
                "Player 2 Type",
                "Winner",
            ])

    def record_game(self, playerO, playerX, winner):
        """Records the game and winner of the match and writes to the csv file."""

        self.games.loc[len(self.games)] = {
            "Game ID": len(self.games) + 1,
            "Player 1": playerO.name,
            "Player 2": playerX.name,
            "Player 1 Type": playerO.type,
            "Player 2 Type": playerX.type,
            "Winner": winner,
        }

        self.games.to_csv(self.filename)

    def print_statistics(self, player1, player2):
        """Prints the current games and player stats."""

        player1_games = self.games.loc[
            (self.games['Player 1'] == player1.name) | (self.games['Player 2'] == player1.name)]
        player1_wins = len(player1_games.loc[(player1_games['Winner'] == player1.name)])
        player1_loses = len(
            player1_games.loc[(player1_games['Winner'] != player1.name) & (player1_games['Winner'] != 'Draw')])
        player1_ratio = player1_wins / max(1, player1_loses + player1_wins)

        player2_games = self.games.loc[
            (self.games['Player 1'] == player2.name) | (self.games['Player 2'] == player2.name)]
        player2_wins = len(player2_games.loc[(player2_games['Winner'] == player2.name)])
        player2_loses = len(
            player2_games.loc[(player2_games['Winner'] != player2.name) & (player2_games['Winner'] != 'Draw')])
        player2_ratio = player2_wins / max(1, player2_loses + player2_wins)

        print()
        print('=== Statistics ===')
        print('Player: ' + player1.name + '\tPlayer Type: ' + player1.type + '\tWins: ' + str(
            player1_wins) + '\tLoses: ' + str(player1_loses) + '\tW/L Ratio: ' + str(player1_ratio))
        print('Player: ' + player2.name + '\tPlayer Type: ' + player2.type + '\tWins: ' + str(
            player2_wins) + '\tLoses: ' + str(player2_loses) + '\tW/L Ratio: ' + str(player2_ratio))


class Game:
    def __init__(self, playerO, playerX, cli):
        """Initializes the Game with player O, player X, and an empty board."""

        self.playerO = playerO
        self.playerX = playerX
        self.board = Board()
        self.save = DataSave('GameSave.csv')
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

    def print_statistic(self):
        """Prints the statistics of the game."""
        self.save.print_statistics(self.playerO, self.playerX)

    def other_player(self):
        """Changes the current player to the other player."""

        if self.current_player == self.playerO:
            self.current_player = self.playerX
        else:
            self.current_player = self.playerO

    def run(self):
        """Run function to start the game."""

        while self.winner is None and self.board.check_draw() is False:
            self.print_board()
            self.current_player.get_move(self.board)
            self.winner = self.board.get_winner()
            self.other_player()

        if self.winner == 'O':
            self.save.record_game(self.playerO, self.playerX, self.playerO.name)
        elif self.winner == 'X':
            self.save.record_game(self.playerO, self.playerX, self.playerX.name)
        else:
            self.save.record_game(self.playerO, self.playerX, 'Draw')

        self.print_winner()
        self.print_statistic()


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

    def __init__(self, player, name):
        """Initializes the player with O or X."""

        self.player = player
        self.next_move = 1
        self.name = name
        self.type = 'Human'

    def get_next_move(self, board):
        """Gets the next mode from player and return"""

        print('Player ' + self.player + ' enter the location for your move (1-9): ', end='')
        self.next_move = input()

        while str.isnumeric(self.next_move) is False or board.check_index(int(self.next_move)) is False:
            print('Error! Input Invalid! Please Try Again!')
            print('Player ' + self.player + ' enter the location for your move (1-9): ', end='')
            self.next_move = input()

        self.next_move = int(self.next_move)
        return self.next_move

    def get_move(self, board):
        """Gets the next best move and updates the board."""

        self.next_move = self.get_next_move(board)
        board.update_board(self.next_move, self.player)

    def get_move_flask(self, board, move):
        """Gets the next move for flask web interface and updates the board."""
        while str.isnumeric(move) is False or board.check_index(int(move)) is False:
            raise Exception('Error! Input Invalid!')
        board.update_board(move, self.player)


class Bot:
    def __init__(self, player, name):
        """Initializes the player with O or X."""

        self.player = player
        self.next_move = 1
        self.name = name
        self.type = 'Bot'

    def get_next_move(self, board):
        """Bot logic for compute next best move.
        Returns the index of the next move."""

        for i in range(1, 9):
            if board.check_index(i) is True:
                print('Player ' + self.player + ' plays at position (1-9): ' + str(i))
                return i

    def get_move(self, board):
        """Gets the next best move and updates the board."""

        self.next_move = self.get_next_move(board)
        board.update_board(self.next_move, self.player)
