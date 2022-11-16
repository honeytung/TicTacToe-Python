# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':

    # Display welcome message and game modes selection
    print('Tic Tac Toe Game!')
    print('Game Modes')
    print('1. Human vs. Human')
    print('2. Human vs. Bot')
    print('3. Bot   vs. Bot')
    print('Please Select Game Mode (1-3): ', end='')
    game_mode = input()

    # Check input is valid and ask again if not
    while not str.isnumeric(game_mode) or int(game_mode) < 1 or int(game_mode) > 3:
        print('Error! Input Invalid! Please Try Again!')
        print('Please Select Game Mode: ', end='')
        game_mode = input()

    game_mode = int(game_mode)

    if game_mode == 1:
        player1 = Human('O')
        player2 = Human('X')
    elif game_mode == 2:
        player1 = Human('O')
        player2 = Bot('X')
    else:
        player1 = Bot('O')
        player2 = Bot('X')

    # Initialize game with appropriate game mode
    game = Game(player1, player2)
    # Run the game
    game.run()
