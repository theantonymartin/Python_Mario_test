class Boss :
	def __init__(self):
		self.x = 75
		self.y = 0
		self.matrix=[]
		bossmat = [" ......... ",
" ;(6) (6); ",
' \   \"   / ',
"  ( HHH )  ",
"  _)   (_  ",
".'  '_'  '.",
": .       :",
": :_____: :",
"<_:__Z__:_\\",
"<(|     |))",
"< :     :  ",
"< |     |  ",
"< \ / \ /  ",
"< L_) (_7  "]

		i=0
		for x in bossmat:
			self.matrix.append([])
			for y in x:
				self.matrix[i].append(y)
			i=i+1
	
	def renderBoss(self, length, height, mapMatrix):
		for y in range(0, 14):
			for x in range(0, 11):
				if int(self.x+x)<length and int(self.x+x)>=0:
					mapMatrix[int(self.x + x)][height-13+y-self.y] = self.matrix[y][x] 
		return mapMatrix

	def showPosition(self):
		return [ self.x, self.y ]