from constant import Constant
class BaseShip:
    def __init__(self):
        self.numCol = Constant.DEFAULT_BOARD_WIDTH
        self.numRow =  Constant.DEFAULT_BOARD_HEIGHT
        
    def canPush(self, posX, posY, board):
        if posX < 0 or  posX >= self.numCol:
            return False
        elif posY < 0  or posY >= self.numRow:
            return False
        if board[posY][posX] == Constant.OCEAN:
            return True
        return False
        
    def canPlace(self, startX, startY, board, type = Constant.HORIZONAL):
        ship = self.getShip(startX, startY, type)
        
        for i in range(len(ship)):
            posX = ship[i][0]
            posY = ship[i][1]
            if self.canPush(posX, posY, board) is False:
                return False

        # i = 0
        # while i < len(ship):
        #   posX = ship[i].x
        #   posY = ship[i].y
        #   if not self.canPush(posX, posY):
        #       return false
            
        #   i += 1
            
        return True

    def getMergePosition(self, startX, startY)
        ship1 = self.getShip(startX, startY, Constant.VERTICAL)
        ship2 = self.getShip(startX, startY, Constant.HORIZONAL)

        return ship1 + ship2 # merge array

class Carrier(BaseShip):
    def __init__(self):
        BaseShip.__init__(self)

    def getShip(self, startX, startY, orientation):
        if orientation == Constant.VERTICAL:
            return [
                [startX,startY],
                [startX, startY + 1],
                [startX - 1, startY + 1],
                [startX, startY + 2],
                [startX, startY + 3]
            ]
        elif orientation == Constant.HORIZONAL:
            return [
                [startX, startY],
                [startX + 1, startY],
                [startX + 1, startY - 1],
                [startX + 2, startY],
                [startX + 3, startY]
            ]

class Battleship(BaseShip):
    def __init__(self):
        BaseShip.__init__(self)

    def getShip(self, startX, startY, orientation):
        if orientation == Constant.VERTICAL:
            return [
                [startX, startY],
                [startX, startY + 1],
                [startX, startY + 2],
                [startX, startY + 3]
            ]
        elif orientation == Constant.HORIZONAL:
            return [
                [startX, startY],
                [startX + 1, startY],
                [startX + 2, startY],
                [startX + 3, startY]
            ]

class Oilrig(BaseShip):
    def __init__(self):
        BaseShip.__init__(self)

    def getShip(self, startX, startY, orientation):
        return [
                [startX, startY],
                [startX, startY + 1],
                [startX - 1, startY],
                [startX - 1, startY + 1]]

class Destroyer(BaseShip):
    def __init__(self):
        BaseShip.__init__(self)

    def getShip(self, startX, startY, orientation):
        if orientation == Constant.VERTICAL:
            return [
                [startX, startY],
                [startX, startY + 1]
            ]
        elif orientation == Constant.HORIZONAL:
            return [
                [startX, startY],
                [startX + 1, startY]
            ]

class Cruiser(BaseShip):
    def __init__(self):
        BaseShip.__init__(self)

    def getShip(self, startX, startY, orientation):
        if orientation == Constant.VERTICAL:
            return [
                [startX, startY],
                [startX, startY + 1],
                [startX, startY + 2]
            ]
        elif orientation == Constant.HORIZONAL:
            return [
                [startX, startY],
                [startX + 1, startY],
                [startX + 2, startY]
            ]           