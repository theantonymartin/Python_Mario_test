from ground import Ground
from mario import Mario

def returnMap(length, height):
	grnd = Ground(length, height)
	grnd.renderBlocks(3*length/8 , height/4)
	grnd.renderPipe(length/5)
	return grnd.returnMatrix()

def renderMap(mapMatrix,length,height):
	map=""
	for y in range(0,height+9):
			for x in range(0,length):
				map += mapMatrix[x][y]
			map += '\n'
	return map

def updateMap(posx, posy, mappos, mat, length, height, direction):
	mapMatrix = []
	for i in range(0, length):
		mapMatrix.append([])
	for x in range(0,length):
		for y in range(0,height+9):
			mapMatrix[x].append(mat[mappos+x][y])
	mrio = Mario(posx, posy)
	'''
	if mappos >= 2:
		mapMatrix=renderBlocks(length-(mappos-2), 7, grnd)
		grnd.updateMap(mapMatrix)
	'''
	mapMatrix = mrio.renderMario(height, mapMatrix, direction)
	return mapMatrix