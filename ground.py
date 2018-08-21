class Ground:
	#generating the ground and stationary objects for the level

	def __init__(self, length, height):
		self.length = length
		self.height = height
		self.matrix = []
		for i in range(0, self.length):
			self.matrix.append([])
			for j in range(0,self.height+1):
				self.matrix[i].append(' ')
		groundType=0
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


	def renderPipe(self,posx,posy=6):
		Pipe=[" __________ ","|XXXXXXXXXX|","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  "]
		pipeMat=[]
		
		for x in range(0,7):
			pipeMat.append([])
			for y in range(0,12):
				pipeMat[x].append(Pipe[x][y])

		for y in range (0, 7):
			for x in range(0, 12):
				self.matrix[int(posx+x)][int(self.height-posy+y)] = pipeMat[y][x]

	def renderBlocks(self, posx, posy):
		Blocks=["|WWWW|","|XXXX|","|XXXX|"]
		blockMat=[]

		for x in range(0,3):
			blockMat.append([])
			for y in range(0,6):
				blockMat[x].append(Blocks[x][y])

		for y in range (0, 3):
			for x in range(0, 6):
					self.matrix[int(posx+x)][int(self.height+y-posy)] = blockMat[y][x]

	def renderClouds(self):
		Clouds=["  __________             ____________               _________________           ",
" ///////////\           /////////////\__           //////////////////\          ",
"/////////////\         /////////////////\          \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\         ",
"\////////////|        ///////////////////        \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\      ",
" \\\\\\\\\\\\\\\\\\\\\/         |//////////////////         \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\      ",
"                       \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/           \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\      ",
"                                                     \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\       ",
"                                                           \\\\\\\\\\\\\\\\\\\\\\\\\\\        "]				
		cloudMat=[]

		for x in range(0,8):
			cloudMat.append([])
			for y in range(0,len(Clouds[x])):
				cloudMat[x].append(Clouds[x][y])

		i = 0
		while(1):
			length = 80 * i
			if length>self.length:
				return
			for y in range (0, 8):
				for x in range(0, len(Clouds[y])):
					if x+length<self.length:
						self.matrix[x+length][y+1] = cloudMat[y][x]
			i = i+1


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


