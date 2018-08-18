

'''class Platforms :
		blockMat.append([])
		for y in range(0,5):
			blockMat[i].append(Blocks[i][y])
	def __init__(self):
		self.matrix = blockMat'''
Blocks=["|WWWW|","|XXXX|","|XXXX|"]
blockMat=[]
for i in range(0,3):
	blockMat.append([])
	for y in range(0,6):
		blockMat[i].append(Blocks[i][y])
#rint(blockMat)
def renderBlocks(posx, posy, grnd):
	newMatrix = grnd.returnMatrix()
	for y in range (0, 3):
		for x in range(0, 6):
			if (posx -1 + x) < grnd.length and posx -1 + x >= 0:
				newMatrix[posx-1+x][grnd.height+y-posy] = blockMat[y][x]
	return newMatrix