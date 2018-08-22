from os import system
import sys
#from ground import Ground
from level import * 
import time
from jump import *
from input import Get, input_to
from collision import *
from init import *


getch = Get()
posx = 1
posy = 0
mappos = 0
flag=0
flag1=0
direction='>'
direction1=[]
travlength=0
mapsize = 9
screenlength = 90
height = 35
f = 's'
vdist = 0
fe=[]
kx=[]
ky=[]
enempos=[]
r=[]
placeEnemies(direction1, r,kx,ky,height, enempos, screenlength, screenlength*mapsize,fe)
mat = returnMap(screenlength*mapsize, height)
z=0

while True:

	r,direction1,kx,ky,mapMatrix=updateMap(posx, posy, travlength-posx, mat, screenlength, height, direction,screenlength*mapsize,enempos,kx,ky,z,direction1,r,fe)
	print(renderMap(mapMatrix,screenlength,height))
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
	x=hitDetectMario(mapMatrix,posx, posy, height, 6,5)
	if x==1:
		system('clear')
		print("Game Over")
		time.sleep(2)
		sys.exit()

	posy,f,vdist=Grav(mapMatrix, f,posx, posy, height, 6,vdist)
	time.sleep(0.028)
	system('clear')