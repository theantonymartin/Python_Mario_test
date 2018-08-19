from os import system
import sys
#from ground import Ground
from level import * 
import time
from jump import *
from input import Get, input_to
from collision import *

getch = Get()
posx = 0
posy = 0
mappos = 0
flag=0
flag1=0
direction='>'
travlength=0
maplength = 2
length = 90
height = 35
f = 's'
vdist = 0
x=0

mat = returnMap(length*maplength, height)

while True:

	mapMatrix=updateMap(posx, posy, travlength-posx, mat, length, height, direction)
	print(renderMap(mapMatrix,length,height))

	button = input_to(getch)
	if button == 'q':
		system('clear')
		sys.exit()

	if button == 'd':
		x=collisionDetect(mapMatrix, button, posx, posy, height)
		direction = '>'
		travlength = travlength + x
		if travlength > ( (maplength-1/2) * length):
			posx = posx + x
		else :
			if posx < length/2:
				posx = posx + x
			else :
				mappos = mappos + x

	if button == 'a':
		x=collisionDetect(mapMatrix, button, posx, posy, height)
		direction = '<'
		if posx > 0:
			posx = posx - x
			travlength = travlength - x

	if button == 'w':
		f=Jump(mapMatrix, f, posx, posy, height)

	posy,f,vdist=Grav(mapMatrix, f,vdist,posx, posy, height)

	#time.sleep(0.01)
	system('clear')