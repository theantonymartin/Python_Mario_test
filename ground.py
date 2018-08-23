from colorama import Fore, Back,Style
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
				self.matrix[i].extend(( Fore.GREEN + 'W' + Fore.RESET, '.' , '.' , ' ' , '.', '.', 'x' , 'x' , 'x'))
			elif groundType == 1:
				self.matrix[i].extend(( Fore.GREEN + 'W' + Fore.RESET, ' ' , ' ' , '.' , ' ', ' ', '.' , '.' , '.'))
			elif groundType == 2:
				self.matrix[i].extend(( Fore.GREEN + 'W' + Fore.RESET, ' ' , '.' , ' ' , '.', '.', 'x' , 'x' , 'x'))
			elif groundType == 3:
				self.matrix[i].extend(( Fore.GREEN + 'W' + Fore.RESET, '.' , ' ' , '.' , ' ', ' ', '.' , '.' , '.'))
			elif groundType == 4:
				self.matrix[i].extend(( Fore.GREEN + 'W' + Fore.RESET, ' ' , '.' , ' ' , '.', '.', 'x' , 'x' , 'x'))
			elif groundType == 5:
				self.matrix[i].extend(( Fore.GREEN + 'W' + Fore.RESET, ' ' , ' ' , '.' , ' ', ' ', '.' , '.' , '.'))
			groundType = groundType + 1
			if groundType == 6:
				groundType = 0


	def renderHole(self, posx,posy=0):
		Hole=["          ","          ","          ","          ","          ","          ","LLLLLLLLLL","LLLLLLLLLL",]
		holeMat=[]

		for x in range(0,8):
			holeMat.append([])
			for y in range(0,10):
				holeMat[x].append(Hole[x][y])

		for y in range (0, 8):
			for x in range(0, 10):
				if y==6 or y==7:
					self.matrix[int(posx+x)][int(self.height-posy+y+1)] = Style.BRIGHT+Fore.RED+holeMat[y][x]+Fore.RESET+Style.RESET_ALL
				else:
					self.matrix[int(posx+x)][int(self.height-posy+y+1)] = holeMat[y][x]

	def renderPipe3(self, posx ,posy=9):
		Pipe=[" __________ ","|XXXXXXXXXX|","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  "]
		pipeMat=[]
		
		for x in range(0,10):
			pipeMat.append([])
			for y in range(0,12):
				pipeMat[x].append(Fore.GREEN+Pipe[x][y]+Fore.RESET)

		for y in range (0, 10):
			for x in range(0, 12):
				self.matrix[int(posx+x)][int(self.height-posy+y)] = pipeMat[y][x]


	def renderPipe2(self,posx,posy=6):
		Pipe=[" __________ ","|XXXXXXXXXX|","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  "]
		pipeMat=[]
		
		for x in range(0,7):
			pipeMat.append([])
			for y in range(0,12):
				pipeMat[x].append(Fore.GREEN+Pipe[x][y]+Fore.RESET)

		for y in range (0, 7):
			for x in range(0, 12):
				self.matrix[int(posx+x)][int(self.height-posy+y)] = pipeMat[y][x]


	def renderPipe1(self,posx,posy=4):
		Pipe=[" __________ ","|XXXXXXXXXX|","  |XXXXXX|  ","  |XXXXXX|  ","  |XXXXXX|  "]
		pipeMat=[]
		
		for x in range(0,5):
			pipeMat.append([])
			for y in range(0,12):
				pipeMat[x].append(Fore.GREEN+Pipe[x][y]+Fore.RESET)

		for y in range (0, 5):
			for x in range(0, 12):
				self.matrix[int(posx+x)][int(self.height-posy+y)] = pipeMat[y][x]
		

	def renderBlocks(self, posx, posy):
		Blocks=["|WWWW|","|XXXX|","|XXXX|"]
		blockMat=[]

		for x in range(0,3):
			blockMat.append([])
			for y in range(0,6):
				blockMat[x].append(Fore.YELLOW+Blocks[x][y]+Fore.RESET)

		for y in range (0, 3):
			for x in range(0, 6):
					self.matrix[int(posx+x)][int(self.height+y-posy)] = blockMat[y][x]

	def renderClouds(self):
		Clouds=["  __________             ____________               _________________           ",
" ///////////\           /////////////\__           //////////////////\          ",
"/////////////\         /////////////////\          \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\         ",
"\/////////////        ///////////////////        \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\      ",
" \\\\\\\\\\\\\\\\\\\\\/         ///////////////////         \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\      ",
"                       \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/           \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\      ",
"                                                     \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\       ",
"                                                           \\\\\\\\\\\\\\\\\\\\\\\\\\\        "]				
		cloudMat=[]

		for x in range(0,8):
			cloudMat.append([])
			for y in range(0,len(Clouds[x])):
				cloudMat[x].append(Fore.CYAN + Clouds[x][y] + Fore.RESET )

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

	def renderFlag(self, posx,posy=29):
		Flag=["      ___ o",
"       \  || ",
"        \ ||",
"         \||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"          ||",
"        __||__",
"       |______|"]
		
		FlagMat=[]
		i=0
		for x in Flag:
			FlagMat.append([])
			for y in x:
				FlagMat[i].append(Fore.CYAN + y + Fore.RESET )
			i=i+1

		for y in range (0, i):
			for x in range(0, len(FlagMat[y])):
				self.matrix[int(posx+x)][int(self.height-posy+y)] = FlagMat[y][x]

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


