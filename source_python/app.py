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
    session[Constant.SESSION_KEY_BOARD_WIDTH] = board_width
    session[Constant.SESSION_KEY_BOARD_HEIGHT] = board_height
    session[Constant.SESSION_KEY_INVITE_SHIPS] = ships

    return jsonify({"message": "successful"})

@app.route("/place-ships", methods=["POST"])
def place_ships():
    # get information from request
    player1 = request.json["player1"]
    player2 = request.json["player2"]

    # get information from session
    board_width = session[Constant.SESSION_KEY_BOARD_WIDTH]
    board_height = session[Constant.SESSION_KEY_BOARD_HEIGHT]
    ships = session[Constant.SESSION_KEY_INVITE_SHIPS]
    print(type(ships), ships)
    ret_ships = []
    for ship in ships:
        for quantity in range(ship["quantity"]):
            ret_ship = {}
            ret_ship["type"] = ship["type"]
            ret_ship["coordinates"] = [[1,2], [2,1]]
            ret_ships.append(ret_ship)
    #TODO

    return jsonify(ret_ships)

@app.route("/shot", methods=["POST"])
def shot():
    # counter for turn in session
    turn = request.json["turn"]

    max_shots = request.json["maxShots"]

    if max_shots > 1:
        print("Combo")

    coordinates = []
    for shot in range(max_shots):
        coordinate = [1,2]
        coordinates.append(coordinate)
    return jsonify({"coordinates" : coordinates})

@app.route("/notify", methods=["POST"])
def notify():
    player_id = request.json["playerId"]
    shots = request.json["shots"]
    # analysis status shot
    for shot in shots:
        print(shot["coordinate"], shot["status"])

    sunk_ships = request.json["sunkShips"]
    # analysis sunk ship
    for sunk_ship in sunk_ships:
        print(sunk_ship["type"], sunk_ship["coordinates"])

    return jsonify({"message": "successful"})

if __name__ == '__main__':
    app.run(debug=True)