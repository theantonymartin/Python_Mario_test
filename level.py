from ground import Ground
from mario import Mario
from blocks import renderBlocks

def renderMap(mapMatrix,length,height):
	map=""
	for y in range(0,height+9):
			for x in range(0,length):
				map += mapMatrix[x][y]
			map += '\n'
	return map

def returnMap(posx, posy, mappos, direction, length, height):
	grnd = Ground( length, height)
	grnd.renderGround(mappos)
	mrio = Mario(posx, posy)

	if mappos >= 2:
		mapMatrix=renderBlocks(grnd.length-(mappos-2), 7, grnd)
		grnd.updateMap(mapMatrix)
	mapMatrix = mrio.renderMario(grnd, direction)
	return mapMatrix