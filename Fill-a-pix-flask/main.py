from flask import Flask, redirect, render_template, request
from werkzeug.utils import secure_filename
import game

app = Flask(__name__)

images = ['./images/heart.jpg', './images/house.jpg', './images/keylock.jpg']
player_name, board, game_saving_type = None, None, None
board_instance = None
correct_answer = True


@app.route("/", methods=['GET'])
def hello():
    return render_template('home.html')


@app.route("/game", methods=['GET', 'POST'])
def display_board():
    global player_name, board, board_instance, correct_answer, game_saving_type
    if request.method == 'POST':
        player_name = request.form.get('player')
        size = request.form.get('sizes')
        board = request.form.get('boards')
        game_saving_type = request.form.get('save-and-load')
        board_instance = game.Game(int(size), int(size), images[int(board)])
        if game_saving_type == "F":
            save_to_file(player_name, board, board_instance)
    return render_template('game.html', hints_array=board_instance.hints_array, height=len(board_instance.hints_array),
                           width=len(board_instance.hints_array[0]), player_name=player_name,
                           isDone=board_instance.isDone, correct_answer=correct_answer)


@app.route("/check", methods=['POST'])
def check():
    try:
        global player_name, board_instance, correct_answer
        row = request.form.get('row')
        column = request.form.get('column')
        correct_answer = board_instance.check_answer(int(row), int(column))
        if correct_answer and game_saving_type == "F":
            save_to_file(player_name, board, board_instance)
            load_from_file(player_name+'.txt')
    except IndexError:
        correct_answer = False
        pass
    except ValueError:
        correct_answer = False
        pass
    except AttributeError:
        correct_answer = False
        pass

    return redirect("/game")


@app.route("/load", methods=['POST'])
def load_from_memory():
    global player_name, correct_answer, board_instance, game_saving_type
    correct_answer = True
    game_saving_type = "M"
    return redirect("/game")


@app.route("/load-from-file", methods=['POST'])
def load_from_file_saved():
    global player_name, correct_answer, board_instance, game_saving_type
    correct_answer = True
    game_saving_type = "F"
    file = request.form.get('file')
    load_from_file(file)
    return redirect("/game")


def load_from_file(filename):
    global player_name, board, board_instance, correct_answer
    correct_answer = True
    with open('./saves/' + str(filename) , "r") as txt_file:
        player_name = txt_file.readline().replace('\n', "")
        size = txt_file.readline()
        board = txt_file.readline().replace('\n', "")
        board_instance = game.Game(int(size), int(size), images[int(board)])
        for i in range(len(board_instance.hints_array)):
            row = txt_file.readline().split()
            for j in range(len(board_instance.hints_array[0])):
                board_instance.hints_array[i][j][1] = row[j]


def save_to_file(player_name, board, board_instance):
    with open('./saves/' + player_name + ".txt", "w") as txt_file:
        txt_file.write(player_name + '\n')
        txt_file.write(str(len(board_instance.hints_array)) + '\n')
        txt_file.write(str(board) + '\n')
        for i in range(len(board_instance.hints_array)):
            for j in range(len(board_instance.hints_array[0])):
                txt_file.write(str(board_instance.hints_array[i][j][1]) + ' ')
            txt_file.write('\n')


if __name__ == '__main__':
    app.run(debug=True)
