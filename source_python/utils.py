from random import randint
from constant import Constant


def random_y(is_vertical, size, height, ship_type):
    if is_vertical:
        return randint(0, Constant.DEFAULT_BOARD_HEIGHT - 1)
    else:
        if ship_type == Constant.SHIP_TYPE_CARRIER:
            return randint(height, Constant.DEFAULT_BOARD_HEIGHT - 1)
        return randint(0, Constant.DEFAULT_BOARD_HEIGHT - size)


def random_x(is_vertical, size, height, ship_type):
    if is_vertical:
        if ship_type == Constant.SHIP_TYPE_CARRIER:
            return randint(height, Constant.DEFAULT_BOARD_WIDTH - 1)
        return randint(0, Constant.DEFAULT_BOARD_WIDTH - 1)
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

def place_ship(ship, board, ship_x, ship_y):
    is_vertical = randint(0, 1) # vertical ship if true
    occupied = True
    ship_type = ship["type"]
    ship_info = Constant.SHIPS_INFO[ship_type]
    size = ship_info["width"]
    height = ship_info["height"]
    while occupied:
        occupied = False
        ship_x = random_x(is_vertical, size, height, ship_type)
        ship_y = random_y(is_vertical, size, height, ship_type)
        #TODO
        if is_vertical:
            for p in range(size):
                if not is_ocean(ship_x, ship_y + p, board):
                    occupied = True
            if ship_type == Constant.SHIP_TYPE_CARRIER:
                if not is_ocean(ship_x - 1, ship_y + 1, board):
                    occupied = True
                else:
                    occupied = False
        else:
            for p in range(size):
                if not is_ocean(ship_x + p, ship_y, board):
                    occupied = True
            if ship_type == Constant.SHIP_TYPE_CARRIER:
                if not is_ocean(ship_x, ship_y - 1, board):
                    occupied = True
                else:
                    occupied = False

    #Place ship on boards
    if is_vertical:
        board[ship_y][ship_x] = "^"
        board[ship_y + size - 1][ship_x] = "v"
        # if set_ship is not None:
        #     number_board[ship_row][ship_col] = set_ship
        #     number_board[ship_row+size-1][ship_col] = set_ship
        for p in range(size -2):
            board[ship_y + p +1][ship_x] = "+"
            # if set_ship != None:
            #     number_board[ship_row+p+1][ship_col] = set_ship
        if ship_type == Constant.SHIP_TYPE_CARRIER:
            board[ship_x - 1][ship_y + 1] = "+"
    else:
        board[ship_y][ship_x] = ">"
        board[ship_y][ship_x - size + 1] = "<"
        # if set_ship != None:
        #     number_board[ship_row][ship_col] = set_ship
        #     number_board[ship_row][ship_col-size+1] = set_ship
        for p in range(size -2):
            board[ship_y][ship_x - p - 1] = "+"
            # if set_ship != None:
            #     number_board[ship_row][ship_col-p-1] = set_ship
        if ship_type == Constant.SHIP_TYPE_CARRIER:
            board[ship_x][ship_y - 1] = "+"
    return {"ship_x": ship_x, "ship_y": ship_y}