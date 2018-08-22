from ground import Ground
from mario import Mario
from enemy import Enemy1
from collision import *
import sys
from init import *
from jump import *

def returnMap(maplength, height):
	grnd = Ground(maplength, height)
	placeBlocks(grnd, maplength, height)
	placePipe(grnd, maplength)
	placeHole(grnd,maplength)
	grnd.renderClouds()
	return grnd.returnMatrix()

def renderMap(mapMatrix,length,height):
	map=""
	for y in range(0,height+9):
			for x in range(0,length):
				map += mapMatrix[x][y]
			map += '\n'
	return map

def updateMap(posx, posy, mappos, mat, length, height, direction, maplength,enempos,kx,ky,z, direction1,r,fe):
	o=[]
	mapMatrix = []
	for i in range(0, length):
		mapMatrix.append([])
	for x in range(0,length):
		for y in range(0,height+9):
			mapMatrix[x].append(mat[mappos+x][y])
	for i in range(0, len(r)):
		if r[i]==0:
			if mappos+length>=enempos[i]:
				ky[i],fe[i],v=Grav(mat, fe[i], int(kx[i])+mappos, int(ky[i]), height,5)
				l=collisionDetect(mat,direction1[i],int(kx[i])+mappos,int(ky[i]),height,5,3)
				o.append(l)
		else :
			o.append(-1)
	for i in range(0, len(r)):
		if r[i]==0 and mappos+length>=enempos[i]:
			enmy = Enemy1(int(kx[i]),int(ky[i]))
			mat=enmy.renderEnemy(length, height, mapMatrix, direction1[i])
			if o[i]==0:
				if direction1[i]=='a':
					direction1[i]='d'
				else:
					direction1[i]='a'
			if direction1[i]=='a':
				kx[i]=kx[i]-0.5-z
			else :
				kx[i]=kx[i]+0.5-z			
	mrio = Mario(posx, posy)
	#if mappos+posx == int(maplength/2):
		#renderEnemy(maplength)
	'''
	if mappos >= 2:
		mapMatrix=renderBlocks(length-(mappos-2), 7, grnd)
		grnd.updateMap(mapMatrix)
	'''
	mapMatrix = mrio.renderMario(height, mapMatrix, direction)
	for i in range(0,len(r)):
		if r[i] == 0 and mappos+length>=enempos[i]:
			a,b=hitDetectEnemy(mapMatrix,posx,posy,height,6,5)
			c=fallDetect(mapMatrix,int(kx[i]),int(ky[i]),height,5,maplength)
			if (a == int(kx[i]) or b== int(kx[i])) or c ==0 :
				r[i]=1
	return r,direction1,kx,ky,mapMatrix