from random import randint
from constant import Constant
from utils import *


def random_shot(board):
    guess_x = randint(0, Constant.DEFAULT_BOARD_WIDTH - 1)
    guess_y = randint(0, Constant.DEFAULT_BOARD_HEIGHT - 1)
    while not is_ocean(guess_x, guess_y, board):
        guess_x = randint(0, Constant.DEFAULT_BOARD_WIDTH - 1)
        guess_y = randint(0, Constant.DEFAULT_BOARD_HEIGHT - 1)
    return [guess_x, guess_y]


def circle_shot(board, start_x, start_y):
    directions = [0,1,2,3] # 0: above, 1: right, 2: bottom, 3: left

    if start_x == 0:
        directions.remove(3)
    elif board[start_y][start_x - 1] == Constant.FIRE:
        directions.remove(3)

    if start_x == Constant.DEFAULT_BOARD_WIDTH - 1:
        directions.remove(1)
    elif board[start_y][start_x + 1] == Constant.FIRE:
        directions.remove(1)

    if start_y == 0:
        directions.remove(0)
    elif board[start_y - 1][start_x] == Constant.FIRE:
        directions.remove(0)

    if start_y == Constant.DEFAULT_BOARD_HEIGHT - 1:
        directions.remove(2)
    elif board[start_y + 1][start_x] == Constant.FIRE:
        directions.remove(2)

    direction = -1
    guess_x = start_x
    guess_y = start_y

    if len(directions) > 0:
        guess_spot = randint(0, len(directions))
        direction = direction[guess_spot]

    if direction == 0:
        guess_y = start_y - 1
    elif direction == 1:
        guess_x = start_x + 1
    elif direction == 2:
        guess_y = start_y + 1
    elif direction == 3:
        guess_x = start_x - 1

    return [guess_x, guess_y]

def line_shot(board, start_x, start_y):
    guess_x = 0
    guess_y = 0
    return [guess_x, guess_y]

def opposite_shot(board, start_x, start_y, direction):
    guess_x = 0
    guess_y = 0
    # TODO consider later
    line_x = start_x
    line_y = start_y

    if direction == 0:
        guess_y = start_y + 1
        line_y += 1
    elif direction == 1:
        guess_x = start_x - 1
        line_x -= 1
    elif direction == 2:
        guess_y = start_y - 1
        line_y -= 1
    elif direction == 3:
        guess_x = start_x + 1
        line_x += 1

    if guess_x < 0 or guess_x > Constant.DEFAULT_BOARD_WIDTH or guess_y < 0 or guess_y > Constant.DEFAULT_BOARD_HEIGHT:
        guess_pos = random_shot(board)
        guess_x = guess_pos[0]
        guess_y = guess_pos[1]
    elif board[guess_y][guess_x] == Constant.FIRE:
        guess_pos = random_shot(board)
        guess_x = guess_pos[0]
        guess_y = guess_pos[1]

    return [guess_x, guess_y]
