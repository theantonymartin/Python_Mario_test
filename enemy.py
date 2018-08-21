class Enemy1 :
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.matrix = [ [ 'V', 'T', 'H', 'T', 'V'], [ '<', 'H', 'H', 'H', '>'], [ ' ', '|', ' ', '|', ' '] ]
	
	def renderEnemy(self, length, height, mapMatrix, direction):
		for y in range(0, 3):
			for x in range(0, 5):
				if int(self.x+x)<length and int(self.x+x)>=0:
					mapMatrix[int(self.x + x)][height-2+y-self.y] = self.matrix[y][x] 
		return mapMatrix

	def showPosition(self):
		return [ self.x, self.y ]