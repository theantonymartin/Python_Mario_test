from colorama import Fore, Back,Style

def collisionDetect(mat, side, posx, posy, height, objwidth, objheight):
	
	if side == 'd':
		for y in range(0, objheight):
			if mat[posx+objwidth][height-posy-y] == '|' or mat[posx+objwidth][height-posy-y] == Fore.GREEN + '|' + Fore.RESET or mat[posx+objwidth][height-posy-y] == Fore.YELLOW + '|' + Fore.RESET :
				return 0
		return 1
	
	if side == 'a':
		for y in range(0, objheight):
			if mat[posx-1][height-posy-y] == '|' or mat[posx-1][height-posy-y] == Fore.GREEN + '|' + Fore.RESET or mat[posx-1][height-posy-y] == Fore.YELLOW + '|' + Fore.RESET :
				return 0

		return 1

def fallDetect(mat, posx, posy, height, objwidth, maplength):

		for x in range(0, objwidth):
			if mat[posx][height-posy+1]==Style.BRIGHT+Fore.RED + 'L' + Fore.RESET+Style.RESET_ALL:
				return 0
		return 1

def hitDetectMario(mat, posx, posy, height, objwidth, objheight):
	
		for y in range(0, objheight):
			if mat[posx+objwidth][height-posy-y] == '<' :
				return 1
			if mat[posx-1][height-posy-y] == '>' :
				return 1
		for x in range(0,objwidth):
			if mat[posx+x][height-posy+1]==Style.BRIGHT+Fore.RED + 'L' + Fore.RESET+Style.RESET_ALL:
				return 1
		return 0

def hitDetectEnemy(mat, posx, posy, height, objwidth, objheight):
	
		for x in range(0, objwidth):
			if mat[posx+x][height-posy+2] == 'H' :
				return posx+x-2, 400
			elif mat[posx+x][height-posy+2] == 'V' :
				return posx+x, posx+x-4
			elif mat[posx+x][height-posy+2] == 'T' :
				return posx +x-1, posx+x-3
		return 0, 0