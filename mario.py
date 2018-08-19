class Mario :
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.matrix = [ [ ' ', ' ', '_', '_', ' ', ' '], [ ' ', '|', '_', '_', '|', '_' ], [ ' ', '(', '^', '^', ')', ' ' ], [ '/', '|', 'M', 'M', '|', '\\' ],[ ' ', '|', ' ', ' ', '|', ' ' ], [ '_', '|', '_', '_', '|', ' ' ]]
	
	def renderMario(self, height, mapMatrix, direction):
		for y in range(0, 5):
			for x in range(0, 6):
				mapMatrix[self.x + x][height-4+y-self.y] = self.matrix[y][x] 
		if direction == '<':
			for x in range(0, 6):
				mapMatrix[self.x + x][height-3-self.y] = self.matrix[5][x]
		return mapMatrix

	def showPosition(self):
		return [ self.x, self.y ]