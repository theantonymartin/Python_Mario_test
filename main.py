from os import system
import sys
#from ground import Ground
from level import * 
import time
from jump import *
from input import Get, input_to
from collision import *
from init import *
from boss import Boss
lives=3
level=1
score1=0
score=0
while lives>0:
	boss=Boss()
	getch = Get()
	posx = 1
	posy = 0
	mappos = 0
	flag=0
	flag1=0
	direction='>'
	direction1=[]
	travlength=0
	mapsize = 10
	screenlength = 90
	height = 35
	f = 's'
	bosspos=900
	direction2='a'
	vdist = 0
	fe=[]
	kx=[]
	ky=[]
	enempos=[]
	r=[]
	placeEnemies(direction1, r,kx,ky,height, enempos, screenlength, screenlength*mapsize,fe)
	mat = returnMap(screenlength*mapsize, height,level)
	z=0

	while True:

		score,r,direction1,kx,ky,mapMatrix=updateMap(boss,level,posx, posy, travlength-posx, mat, screenlength, height, direction,screenlength*mapsize,enempos,kx,ky,z,direction1,r,fe,score,bosspos, direction2)
		print(renderMap(mapMatrix,screenlength,height))
		if level==1 :
			print('Score:', score, '   Lives:',lives)
		else :
			print('Score:', score1+score, '   Lives:',lives)
		z=0
		button = input_to(getch)
		if button == 'q':
			system('clear')
			sys.exit()
		if button == 'd':
			x=collisionDetect(mapMatrix, button, posx, posy, height,6,5)
			direction = '>'
			travlength = travlength + x
			if travlength > ( (mapsize-1/2) * screenlength):
				posx = posx + x
			else :
				if posx < screenlength/2:
					posx = posx + x
				else :
					z=x
					mappos = mappos + x

		if button == 'a':
			x=collisionDetect(mapMatrix, button, posx, posy, height,6,5)
			direction = '<'
			if posx > 0:
				posx = posx - x
				travlength = travlength - x

		if button == 'w':
			f=Jump(mapMatrix, f, posx, posy, height)
		score=score+z
		x=hitDetectMario(mapMatrix,posx, posy, height, 6,5,mappos,level)
		if x==1:
			lives=lives-1
			if lives>0:
				score=0
				system('aplay smb_mariodie.wav&')
			system('clear')
			break
		elif x==-1:
			system('aplay smb_stage_clear.wav&')
			system('clear')
			score=score+10*posy
			if level==1:
				level=level+1
				score1=score
				score=0
				break
			print("You Won\nFinal Score is:",score1+score)
			time.sleep(2)
			sys.exit()
		posy,f,vdist=Grav(mapMatrix, f,posx, posy, height, 6,vdist)
		time.sleep(0.028)
		system('clear')
system('aplay smb_gameover.wav&')
system('clear')
print("Game Over\nFinal Score is:",score)
time.sleep(2)
sys.exit()