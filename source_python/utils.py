from random import randint
from constant import Constant
from ships import *


def random_y(is_vertical, size, height, ship_type):
    if is_vertical == Constant.VERTICAL:
        if ship_type == Constant.SHIP_TYPE_CARRIER  or ship_type == Constant.SHIP_TYPE_OIL_RIG:
            return randint(0, Constant.DEFAULT_BOARD_HEIGHT - size)
        else:
            return randint(0, Constant.DEFAULT_BOARD_HEIGHT - 1)
    else:
        if ship_type == Constant.SHIP_TYPE_CARRIER  or ship_type == Constant.SHIP_TYPE_OIL_RIG :
            return randint(height - 1, Constant.DEFAULT_BOARD_HEIGHT - height)
        else:
            return randint(0, Constant.DEFAULT_BOARD_HEIGHT - size)


def random_x(is_vertical, size, height, ship_type):
    if is_vertical == Constant.VERTICAL:
        if ship_type == Constant.SHIP_TYPE_CARRIER or ship_type == Constant.SHIP_TYPE_OIL_RIG:
            return randint(height - 1 , Constant.DEFAULT_BOARD_WIDTH - 1)
        else:
            return randint(0, Constant.DEFAULT_BOARD_WIDTH - size)
    else:
        if ship_type == Constant.SHIP_TYPE_CARRIER or ship_type == Constant.SHIP_TYPE_OIL_RIG:
            return randint(0 , Constant.DEFAULT_BOARD_WIDTH - size)
        else:
            return randint(size - 1, Constant.DEFAULT_BOARD_WIDTH - 1)

def is_ocean(x, y, b):  # true if ocean
    if y < 0 or y >= Constant.DEFAULT_BOARD_HEIGHT:
        return 0
    elif x < 0 or x >= Constant.DEFAULT_BOARD_WIDTH:
        return 0
    if b[y][x] == Constant.OCEAN:
        return 1
    else:
        return 0

def make_ship(ship_type):
    if ship_type == Constant.SHIP_TYPE_CARRIER:
        make_ship = Carrier()
    if ship_type == Constant.SHIP_TYPE_BATTLE_SHIP:
        make_ship = Battleship()
    if ship_type == Constant.SHIP_TYPE_CRUISER:
        make_ship = Cruiser()
    if ship_type == Constant.SHIP_TYPE_DESTROYER:
        make_ship = Destroyer()
    if ship_type == Constant.SHIP_TYPE_OIL_RIG:
        make_ship = Oilrig()

    return make_ship


def place_ship(ship, board):
    is_vertical = randint(0, 1) # vertical ship if true
    occupied = True
    ship_type = ship["type"]
    ship_info = Constant.SHIPS_INFO[ship_type]
    size = ship_info["width"]
    height = ship_info["height"]
    print("is_vertical=", is_vertical)
    print("shiptype=", ship_type)

    #TODO 
    if ship_type == Constant.SHIP_TYPE_CARRIER:
        make_ship = Carrier()
    if ship_type == Constant.SHIP_TYPE_BATTLE_SHIP:
        make_ship = Battleship()
    if ship_type == Constant.SHIP_TYPE_CRUISER:
        make_ship = Cruiser()
    if ship_type == Constant.SHIP_TYPE_DESTROYER:
        make_ship = Destroyer()
    if ship_type == Constant.SHIP_TYPE_OIL_RIG:
        make_ship = Oilrig()

    while occupied:
        occupied = False
        ship_x = random_x(is_vertical, size, height, ship_type)
        ship_y = random_y(is_vertical, size, height, ship_type)

        if (make_ship.canPlace(ship_x, ship_y, board, is_vertical) is False):
            occupied = True

    print("ship_x", ship_x, "ship_y", ship_y)
    #Place ship on boards
    ship_coordinates = make_ship.getShip(ship_x, ship_y, is_vertical)

    for ship_coordinate in ship_coordinates:
        board[ship_coordinate[1]][ship_coordinate[0]] = ship_type
    
    print(board)
    return {"ship_coordinates": ship_coordinates, "board": board, "is_vertical": is_vertical}

def update_board(ship_type, ship_coordinates, board):
    # uppdate HIT in board
    for coordinate in ship_coordinates:
        x = coordinate[0]
        y = coordinate[1]
        board[y][x] = Constant.HIT

    return board



