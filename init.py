def placeEnemies(direction1, r,k, enempos,screenlength,maplength):
	k.append(3*screenlength/8)
	k.append(screenlength)
	enempos.append(0)
	enempos.append(3*maplength/4)
	for i in range(0,2):
		r.append(0)
		direction1.append('a')