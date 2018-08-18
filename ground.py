class Ground:
	#generating the ground for the level

	def __init__(self, length, height):
		self.length = length
		self.height = height
		self.matrix = []
		for i in range(0, self.length):
			self.matrix.append([])
			for j in range(0,self.height+1):
				self.matrix[i].append(' ')

	def renderGround(self,time):
		groundType=time%6;
		for i in range(0, self.length):
			if groundType == 0:
				self.matrix[i].extend(( 'W' , '.' , '.' , ' ' , '.', '.', 'x' , 'x' , 'x'))
			elif groundType == 1:
				self.matrix[i].extend(( 'W' , ' ' , ' ' , '.' , ' ', ' ', '.' , '.' , '.'))
			elif groundType == 2:
				self.matrix[i].extend(( 'W' , ' ' , '.' , ' ' , '.', '.', 'x' , 'x' , 'x'))
			elif groundType == 3:
				self.matrix[i].extend(( 'W' , '.' , ' ' , '.' , ' ', ' ', '.' , '.' , '.'))
			elif groundType == 4:
				self.matrix[i].extend(( 'W' , ' ' , '.' , ' ' , '.', '.', 'x' , 'x' , 'x'))
			elif groundType == 5:
				self.matrix[i].extend(( 'W' , ' ' , ' ' , '.' , ' ', ' ', '.' , '.' , '.'))
			groundType = groundType + 1
			if groundType == 6:
				groundType = 0

	def updateMap(self, newmap):
		self.matrix=newmap

	def renderPersons(self,posx, posy):
		self.matrix[posx][self.height-posy] = 'M'

	def returnMatrix(self):
		return self.matrix

	'''def returnString(self):
		map = ""
		for y in range(0,self.height+9):
			for x in range(0,self.length):
				map += self.matrix[x][y]
			map += '\n'
		return map
		'''


