from constant import Constant
from ships import *

class patternShot:
	#def __init__(self, board)
    def __init__(self)
		#self.board = board
        self.numCol = Constant.DEFAULT_BOARD_WIDTH
        self.numRow =  Constant.DEFAULT_BOARD_HEIGHT

	def getBoard()
		return self.board

	def whereShouldIShoot(startX, startY)
		board = self.board
        pattern = self.getPattern(startX, startY)

        # Loop all parten and check where can we should Next shot

	def getPattern(startX, startY)
		# Get array of carrier
		carrier = Carrier()
		battleship = Battleship()
        cruiser = Cruiser()
        destroyer = Destroyer()
        oilrig = Oilrig()

        pattern = carrier.getMergePosition(startX, startY) + battleship.getMergePosition(startX, startY) + cruiser.getMergePosition(startX, startY) + destroyer.getMergePosition(startX, startY) + oilrig.getMergePosition(startX, startY)

        return pattern






