class Constant:
    SHIP_TYPE_CARRIER = "CV"
    SHIP_TYPE_BATTLE_SHIP = "BB"
    SHIP_TYPE_CRUISER = "CA"
    SHIP_TYPE_DESTROYER = "DD"
    SHIP_TYPE_OIL_RIG = "OR"
    SHOT_STATUS_HIT = "HIT"
    SHOT_STATUS_MISS = "MISS"
    DEFAULT_BOARD_WIDTH = 20
    DEFAULT_BOARD_HEIGHT = 8
    SESSION_KEY_BOARD_WIDTH = "SESSION_KEY_BOARD_WIDTH"
    SESSION_KEY_BOARD_HEIGHT = "SESSION_KEY_BOARD_HEIGHT"
    SESSION_KEY_INVITE_SHIPS = "SESSION_KEY_INVITE_SHIPS"
    SESSION_KEY_AI_BOARD = "SESSION_KEY_AI_BOARD"
    SESSION_KEY_OPPONENT_BOARD = "SESSION_KEY_OPPONENT_BOARD"
    OCEAN = "O"
    FIRE = "X"
    HIT = "*"
    SHIPS_INFO = {"CV": {"width": 4, "height": 2}, "BB": {"width": 4, "height": 1},
                  "CA": {"width": 3, "height": 1}, "DD": {"width": 2, "height": 1}, "OR": {"width": 2, "height": 2}}
    VERTICAL = 0
    HORIZONAL = 1

