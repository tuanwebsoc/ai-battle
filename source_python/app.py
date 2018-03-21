from flask import Flask, request, jsonify, session, Response
from constant import Constant
from utils import place_ship, random_x, random_y, is_ocean, update_board
from copy import deepcopy
from random import randint
from pattern_shot import patternShot
import json as simplejson

app = Flask(__name__)
app.secret_key="my secret key"


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/invite", methods=["POST"])
def invite():
    session_id = request.headers['X-SESSION-ID']
    token = request.headers['X-TOKEN']
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

    js = simplejson.dumps({"message": "successful"})

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['X-SESSION-ID'] = session_id
    resp.headers['X-TOKEN'] = token
    return resp

@app.route("/place-ships", methods=["POST"])
def place_ships():
    session_id = request.headers['X-SESSION-ID']
    token = request.headers['X-TOKEN']

    # get information from request
    player1 = request.json["player1"]
    player2 = request.json["player2"]

    # get information from session
    board_width = session[Constant.SESSION_KEY_BOARD_WIDTH]
    board_height = session[Constant.SESSION_KEY_BOARD_HEIGHT]
    ships = session[Constant.SESSION_KEY_INVITE_SHIPS]
    print(type(ships), ships)

    #init board
    #TODO
    board = []
    for x in range(Constant.DEFAULT_BOARD_HEIGHT):
        board.append([Constant.OCEAN] * Constant.DEFAULT_BOARD_WIDTH)

    # store oppnent board
    opponent_board = deepcopy(board)
    session[Constant.SESSION_KEY_OPPONENT_BOARD] = opponent_board

    ret_ships = []
    for ship in ships:
        ret_ship = {}
        ret_ship["type"] = ship["type"]
        ret_ship["coordinates"] = []
        for quantity in range(ship["quantity"]):
            shipxy = place_ship(ship, board)
            board = shipxy["board"]

            ret_ship["coordinates"] = shipxy["ship_coordinates"]
            ret_ships.append(ret_ship)

    # store ai board in session
    session[Constant.SESSION_KEY_AI_BOARD] = board

    js = simplejson.dumps({"ships": ret_ships})

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['X-SESSION-ID'] = session_id
    resp.headers['X-TOKEN'] = token
    return resp


@app.route("/shot", methods=["POST"])
def shot():
    session_id = request.headers['X-SESSION-ID']
    token = request.headers['X-TOKEN']

    ai_board = session[Constant.SESSION_KEY_AI_BOARD]
    opponent_board = session[Constant.SESSION_KEY_OPPONENT_BOARD]
    # counter for turn in session
    turn = request.json["turn"]
    session["turn"] = turn

    try: 
        max_shots = request.json["maxShots"]
    except Exception:
        max_shots = 1

    orientation = -1    
    if "orientation" in session:
        orientation = session['orientation']

    ret_shots = []
    for i in range(max_shots):
        # no sunk ship
        if "target_ship_position" not in session:
            guess_x = randint(0, Constant.DEFAULT_BOARD_WIDTH - 1)
            guess_y = randint(0, Constant.DEFAULT_BOARD_HEIGHT - 1)
            while not is_ocean(guess_x, guess_y, opponent_board):
                guess_x = randint(0, Constant.DEFAULT_BOARD_WIDTH - 1)
                guess_y = randint(0, Constant.DEFAULT_BOARD_HEIGHT - 1)

            session["previous_guess_x"] = guess_x
            session["previous_guess_y"] = guess_y
        else:
            # based on previous hit
            ship_postion = session["target_ship_position"]
            target_x = ship_postion[0]
            target_y = ship_postion[1]
            # guess previous victim orientation
            if orientation == -1:
                if is_ocean(target_x, target_y + 1, opponent_board):
                    guess_x = target_x
                    guess_y = target_y + 1
                elif is_ocean(target_x, target_y - 1, opponent_board):
                    guess_x = target_x
                    guess_y = target_y - 1
                elif is_ocean(target_x - 1, target_y, opponent_board):
                    guess_x = target_x - 1
                    guess_y = target_y
                else:
                    guess_x = target_x + 1
                    guess_y = target_y

                session["previous_guess_x"] = guess_x
                session["previous_guess_y"] = guess_y
            elif orientation == Constant.VERTICAL:
                guess_x = session["previous_guess_x"]
                guess_y = session["previous_guess_y"]
                previous_status = session["previous_status"]
                if is_ocean(guess_x, guess_y + 1, opponent_board) and previous_status != Constant.SHOT_STATUS_MISS:
                    guess_y = guess_y + 1
                else:
                    guess_y = guess_y - 1
                    while not is_ocean(guess_x, guess_y, opponent_board):
                        guess_y = guess_y - 1
            else:
                guess_x = session["previous_guess_x"]
                guess_y = session["previous_guess_y"]
                previous_status = session["previous_status"]
                if is_ocean(guess_x - 1, guess_y, opponent_board) and previous_status != Constant.SHOT_STATUS_MISS:
                    guess_x = guess_y - 1
                else:
                    guess_x = guess_y + 1
                    while not is_ocean(guess_x, guess_y, opponent_board):
                        guess_x = guess_x + 1

        ret_shot = [guess_x, guess_y]
        ret_shots.append(ret_shot)

    session[Constant.SESSION_KEY_OPPONENT_BOARD] = opponent_board
    #session[Constant.SESSION_KEY_AI_BOARD] = ai_board

    js = simplejson.dumps({"coordinates" : ret_shots})

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['X-SESSION-ID'] = session_id
    resp.headers['X-TOKEN'] = token
    return resp


@app.route("/notify", methods=["POST"])
def notify():
    session_id = request.headers['X-SESSION-ID']
    token = request.headers['X-TOKEN']

    ai_board = session[Constant.SESSION_KEY_AI_BOARD]
    opponent_board = session[Constant.SESSION_KEY_OPPONENT_BOARD]

    player_id = request.json["playerId"]
    print("Player: ", player_id)
    shots = request.json["shots"]

    # analysis status shot
    for shot in shots:
        print(shot["coordinate"], shot["status"])
        coordinate = shot["coordinate"]
        status = shot["status"]
        session["previous_guess_x"] = coordinate[0]
        session["previous_guess_y"] = coordinate[1]

        if status == Constant.SHOT_STATUS_HIT:
            print('Good shot')
            ship_position = []
            if "target_ship_position" in session:
                ship_position = session["target_ship_position"]

            session["previous_status"] = Constant.SHOT_STATUS_HIT
            ship_position.extend(coordinate)
            session["target_ship_position"] = ship_position

            session["orientation"] = -1
            # update HIT value into board
            opponent_board[coordinate[1]][coordinate[0]] = Constant.HIT

            # in case of have sunk ship
            if "sunkShips" in request.json:
                sunk_ships = request.json["sunkShips"]
                # analysis sunk ship
                for sunk_ship in sunk_ships:
                    print(sunk_ship["type"], sunk_ship["coordinates"])
                    opponent_board = update_board(sunk_ship["type"], sunk_ship["coordinates"])
        elif status == Constant.SHOT_STATUS_MISS:
            print('Oh no, miss shot. Try again')
            opponent_board[coordinate[1]][coordinate[0]] = Constant.FIRE
            session["previous_status"] = Constant.SHOT_STATUS_MISS

    # return response to game engine
    js = simplejson.dumps({"message": "successful"})

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['X-SESSION-ID'] = session_id
    resp.headers['X-TOKEN'] = token
    return resp

@app.route("/game-over", methods=["POST"])
def game_over():
    return jsonify({"message": "game over !!!!"})

@app.route("/test", methods=["POST"])
def test():
    patternShot = patternShot()
    pattern = patternShot.getPattern(9, 2)

    print(pattern)

if __name__ == '__main__':
    app.run(debug=True)