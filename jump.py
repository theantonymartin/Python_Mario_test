def Jump(mat, f, posx, posy, height):
	for x in range(posx, posx+6):
		if mat[x][height-posy+1] == 'W' or mat[x][height-posy+1] == '|' or mat[x][height-posy+1] == 'X' :
			return 'u'
	return f

def Grav(mat, f, vdist, posx, posy, height):
	flag=1
	#flag1=1
	if f == 'u':
		for x in range(posx, posx+6):
			if mat[x][height-posy-5] == 'X' or mat[x][height-posy-5] == '|':
				f='d'
	for x in range(posx, posx+6):
		if mat[x][height-posy+1] == 'W' or mat[x][height-posy+1] == '|' or mat[x][height-posy+1] == 'X' :
			flag = 0
			if f == 'd' :
				f='s'
				vdist = 0
	if f =='s' and flag==1:
		f='d'

	if vdist == 12:
		#flag1=0
		if f=='u' :
			f='s'

	if f == 'u':
		vdist = vdist +1
		posy = posy+1
	
	if f == 'd':
		if vdist>0:
			vdist = vdist - 1
		posy = posy-1
	
	if f == 's':# and flag1==1:
		vdist = 0
		'''
	if f =='s':
		for x in range(posx, posx+6):
			if mat[x][height-posy+1] == 'W' or mat[x][height-posy+1] == '|' or mat[x][height-posy+1] == 'X' :
				vdist=0
'''

	return posy, f, vdist