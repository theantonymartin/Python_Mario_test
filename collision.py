from colorama import Fore, Back,Style
from os import system

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
			if posx+x<90 :
				if mat[posx+x][height-posy+1]==Style.BRIGHT+Fore.RED + 'L' + Fore.RESET+Style.RESET_ALL:
					return 0
		return 1

def hitDetectMario(mat, posx, posy, height, objwidth, objheight,mappos,level):
		
		if posx+mappos==800 and level ==1:
			return -1
		if posx+mappos==890 and level ==2:
			return -1
		for y in range(0, objheight):
			if mat[posx+objwidth][height-posy-y] == '<' :
				return 1
			if mat[posx-1][height-posy-y] == '>' :
				return 1
		for x in range(0,objwidth):
			if mat[posx+x][height-posy+1]==Style.BRIGHT+Fore.RED + 'L' + Fore.RESET+Style.RESET_ALL:
				return 1
		return 0

def hitDetectEnemy(mat, posx, posy,posxe,posye,height, objwidth, objheight):
	flag1=0
	flag2=0
	for x in range(0, objwidth+10):
			if posxe+x-5==posx:
				flag1=1
				break
	if objheight+posye==posy:
		flag2=1
	if flag1==1 and flag2==1:
		return 1
	else:
		return 0