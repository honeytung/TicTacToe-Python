from flask import Flask, render_template, request, redirect, url_for, flash
from logic import *

app = Flask(__name__)
board = Board()
bot = Bot('X', 'Bot 2')


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        playername = request.form['player_name']
        if len(playername) == 0:
            error = 'Invalid Player Name!'
            return render_template('index.html', error = error)
        else:
            return play_game(playername)
    else:
        return render_template('index.html', error = error)


def play_game(playername):
    board.clear_board()
    return redirect(f'/play/{playername}')


@app.route('/stats/')
def stats():
    return render_template('stats.html')


@app.route('/play/<playername>', methods=['GET', 'POST'])
def game(playername):
    error = None
    message = None
    if request.method == 'POST':

        if board.check_draw() is True:
            message = 'Game Over: Its a Draw!'
            return render_template('play.html', error = error, board = board, playername = playername, message = message)
        elif board.get_winner() is not None:
            winner = board.get_winner()
            message = 'Game Over: Player ' + winner + ' Won!'
            return render_template('play.html', error = error, board = board, playername = playername, message = message)

        if request.form.get('position1') == 'Play Here':
            board.update_board(1, 'O')
        if request.form.get('position2') == 'Play Here':
            board.update_board(2, 'O')
        if request.form.get('position3') == 'Play Here':
            board.update_board(3, 'O')
        if request.form.get('position4') == 'Play Here':
            board.update_board(4, 'O')
        if request.form.get('position5') == 'Play Here':
            board.update_board(5, 'O')
        if request.form.get('position6') == 'Play Here':
            board.update_board(6, 'O')
        if request.form.get('position7') == 'Play Here':
            board.update_board(7, 'O')
        if request.form.get('position8') == 'Play Here':
            board.update_board(8, 'O')
        if request.form.get('position9') == 'Play Here':
            board.update_board(9, 'O')

        if board.check_draw() is True:
            message = 'Game Over: Its a Draw!'
            return render_template('play.html', error = error, board = board, playername = playername, message = message)
        elif board.get_winner() is not None:
            winner = board.get_winner()
            message = 'Game Over: Player ' + winner + ' Won!'
            return render_template('play.html', error = error, board = board, playername = playername, message = message)

        bot.get_move(board)

        return redirect(f'/play/{playername}')
    else:
        return render_template('play.html', error = error, board = board, playername = playername, message = message)
