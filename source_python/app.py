from flask import Flask, request, jsonify, session
from constant import Constant


app = Flask(__name__)
app.secret_key="my secret key"


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/invite", methods=["POST"])
def invite():
    # get request value from game engine

    try:
        board_width = request.json["boardWidth"]
    except Exception:
        board_width = Constant.DEFAULT_BOARD_WIDTH


    try:
        board_height = request.json["boardHeight"]
    except Exception:
        board_height = Constant.DEFAULT_BOARD_HEIGHT

    ships = request.json["ships"]
    print(type(ships), ships)

    # store init game informations to session
    session["board_width"] = board_width

    return jsonify({"boardWidth": board_width})

@app.route("/place-ships", methods=["POST"])
def place_ships():
    board_width = session["board_width"]
    print(type(board_width), board_width)

    return "ok"

if __name__ == '__main__':
    app.run(debug=True)