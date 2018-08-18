def collisionDetect(mat, side, posx, posy, height):
	
	if side == 'd':
		for y in range(0, 5):
			if mat[posx+6][height-posy-y] == '|' :
				return 0
		return 1
	
	if side == 'a':
		for y in range(0, 5):
			if mat[posx-1][height-posy-y] == '|' :
				return 0
		return 1
