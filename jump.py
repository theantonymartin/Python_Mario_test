from os import system
from colorama import Fore, Back

def Jump(mat, f, posx, posy, height):
	for x in range(posx, posx+6):
		if mat[x][height-posy+1] == 'W' or mat[x][height-posy+1] == Fore.GREEN +'W'+ Fore.RESET or mat[x][height-posy+1] == Fore.GREEN +'X'+ Fore.RESET or mat[x][height-posy+1] == '|' or mat[x][height-posy+1] == Fore.GREEN + '|' + Fore.RESET or mat[x][height-posy+1] == 'X' or mat[x][height-posy+1] == Fore.YELLOW + '|' + Fore.RESET or mat[x][height-posy+1] == Fore.YELLOW + 'W' + Fore.RESET or mat[x][height-posy+1] == Fore.YELLOW + 'X' + Fore.RESET:
			system('aplay smb_jump-super.wav&')
			return 'u'
	return f

def Grav(mat, f, posx, posy, height, objwidth,vdist=0):
	flag=1
	#flag1=1
	if f == 'u':
		for x in range(posx, posx+objwidth):
			if mat[x][height-posy-5] == 'X' or mat[x][height-posy-5] == Fore.GREEN + 'X' + Fore.RESET or mat[x][height-posy-5] == '|' or mat[x][height-posy-5] == Fore.GREEN + '|' + Fore.RESET or mat[x][height-posy-5] == Fore.YELLOW + '|' + Fore.RESET or mat[x][height-posy-5] == Fore.YELLOW + 'X' + Fore.RESET:
				f='d'
				system('aplay smb_bump.wav&')
				break
	for x in range(posx, posx+objwidth):
		if mat[x][height-posy+1] == Fore.GREEN+'W'+Fore.RESET or mat[x][height-posy+1] == Fore.GREEN+'|'+Fore.RESET or mat[x][height-posy+1] == Fore.GREEN+'X'+Fore.RESET or mat[x][height-posy+1] == 'W' or mat[x][height-posy+1] == '|' or mat[x][height-posy+1] == 'X'  or mat[x][height-posy+1] == Fore.YELLOW + '|' + Fore.RESET or mat[x][height-posy+1] == Fore.YELLOW + 'X' + Fore.RESET or mat[x][height-posy+1] == Fore.YELLOW + 'W' + Fore.RESET :
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