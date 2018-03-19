class baseFleet:
	def __init__(numCol, numRow):
		self.numCol = numCol
		self.numRow = numRow
		
	def canPush(posX, posY)
		if (posX < 0 || posY < 0 || posX >= self.numCol || posY >= self.numRow)
			return false
		else
			return true
		
	def canPlace(startX, startY, type = 'v')
		ship = self.getShip(startX, startY, type)
		
		i = 0
		while i < len(ship):
			posX = ship[i].x
			posY = ship[i].y
			if (!self.canPush(posX, posY))
				return false
			
			i += 1
			
		return true

class Carrier(baseFleet):
	def getShip(startX, startY, type)
		if type == 'v'
			return [
				{'x': startX, 'y': startY},
				{'x': startX - 1, 'y': startY},
				{'x': startX - 1, 'y': startY - 1},
				{'x': startX - 2, 'y': startY},
				{'x': startX - 3, 'y': startY}
			]
		if type == 'h'
			return [
				{'x': startX, 'y': startY},
				{'x': startX, 'y': startY + 1},
				{'x': startX + 1, 'y': startY + 1},
				{'x': startX, 'y': startY + 2},
				{'x': startX, 'y': startY + 3}
			]

class Battleship(baseFleet):
	def getShip(startX, startY, type)
		if type == 'v'
			return [
				{'x': startX, 'y': startY},
				{'x': startX - 1, 'y': startY},
				{'x': startX - 2, 'y': startY},
				{'x': startX - 3, 'y': startY}
			]
		if type == 'h'
			return [
				{'x': startX, 'y': startY},
				{'x': startX, 'y': startY + 1},
				{'x': startX, 'y': startY + 2},
				{'x': startX, 'y': startY + 3}
			]
			
class Oilrig(baseFleet):
	def getShip(startX, startY, type)
		if type == 'v'
			return [
				{'x': startX, 'y': startY},
				{'x': startX - 1, 'y': startY},
				{'x': startX - 1, 'y': startY - 1},
				{'x': startX, 'y': startY + 1}
			]
		if type == 'h'
			return [
				{'x': startX, 'y': startY},
				{'x': startX - 1, 'y': startY},
				{'x': startX - 1, 'y': startY - 1},
				{'x': startX, 'y': startY + 1}
			]
			
class Destroyer(baseFleet):
	def getShip(startX, startY, type)
		if type == 'v'
			return [
				{'x': startX, 'y': startY},
				{'x': startX - 1, 'y': startY}
			]
		if type == 'h'
			return [
				{'x': startX, 'y': startY},
				{'x': startX, 'y': startY + 1}
			]
			
class Cruiser(baseFleet):
	def getShip(startX, startY, type)
		if type == 'v'
			return [
				{'x': startX, 'y': startY},
				{'x': startX - 1, 'y': startY},
				{'x': startX - 2, 'y': startY}
			]
		if type == 'h'
			return [
				{'x': startX, 'y': startY},
				{'x': startX, 'y': startY + 1},
				{'x': startX, 'y': startY + 2}
			]
			