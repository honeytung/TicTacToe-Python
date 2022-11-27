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
        print('Please Enter Player O Name: ', end='')
        player1_name = input()

        while len(player1_name) <= 0:
            print('Error! Input Invalid! Please Try Again!')
            print('Please Enter Player O Name: ', end='')
            player1_name = input()

        print('Please Enter Player X Name: ', end='')
        player2_name = input()

        while len(player2_name) <= 0:
            print('Error! Input Invalid! Please Try Again!')
            print('Please Enter Player X Name: ', end='')
            player2_name = input()

        player1 = Human('O', player1_name)
        player2 = Human('X', player2_name)
    elif game_mode == 2:
        print('Please Enter Player O Name: ', end='')
        player1_name = input()

        while len(player1_name) <= 0:
            print('Error! Input Invalid! Please Try Again!')
            print('Please Enter Player O Name: ', end='')
            player1_name = input()

        player1 = Human('O', player1_name)
        player2 = Bot('X', 'Bot 2')
    else:
        player1 = Bot('O', 'Bot 1')
        player2 = Bot('X', 'Bot 2')

    # Initialize game with appropriate game mode
    game = Game(player1, player2)
    # Run the game
    game.run()
