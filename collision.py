def collisionDetect(mat, side, posx, posy, height, objwidth, objheight):
	
	if side == 'd':
		for y in range(0, objheight):
			if mat[posx+objwidth][height-posy-y] == '|' :
				return 0
		return 1
	
	if side == 'a':
		for y in range(0, objheight):
			if mat[posx-1][height-posy-y] == '|' :
				return 0
		return 1

def hitDetectMario(mat, posx, posy, height, objwidth, objheight):
	
		for y in range(0, objheight):
			if mat[posx+objwidth][height-posy-y] == '<' :
				return 1

		for y in range(0, objheight):
			if mat[posx-1][height-posy-y] == '>' :
				return 1
		return 0

def hitDetectEnemy(mat, posx, posy, height, objwidth, objheight):
	
		for x in range(0, objwidth):
			if mat[posx+x][height-posy+1] == 'H' :
				return posx+x-2
		return 0