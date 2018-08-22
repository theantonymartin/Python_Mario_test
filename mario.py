from colorama import Fore, Back
class Mario :
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.matrix = [ [ ' ', ' ', '_', '_', ' ', ' '], [ ' ', '|', '_', '_', '|', '_' ], [ ' ', '(', '^', '^', ')', ' ' ], [ '/', '|', 'M', 'M', '|', '\\' ],[ ' ', '|', ' ', ' ', '|', ' ' ], [ '_', '|', '_', '_', '|', ' ' ]]
	
	def renderMario(self, height, mapMatrix, direction):
		for y in range(0, 5):
			for x in range(0, 6):
				if y==1 and (x==2 or x==3):
					mapMatrix[self.x + x][height-4+y-self.y] = Back.RED+Fore.RED+self.matrix[y][x]+Back.RESET+Fore.RESET
				else: 
					mapMatrix[self.x + x][height-4+y-self.y] = Fore.RED+self.matrix[y][x]+Fore.RESET 
		if direction == '<':
			for x in range(0, 6):
				if x==2 or x==3:
					mapMatrix[self.x + x][height-3-self.y] = Back.RED+Fore.RED+self.matrix[y][x]+Back.RESET+Fore.RESET
				else: 
					mapMatrix[self.x + x][height-3-self.y] = Fore.RED+self.matrix[5][x]+Fore.RESET
		return mapMatrix

	def showPosition(self):
		return [ self.x, self.y ]