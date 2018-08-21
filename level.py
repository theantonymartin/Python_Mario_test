from ground import Ground
from mario import Mario
from enemy import Enemy1
from collision import *
import sys

def returnMap(maplength, height):
	grnd = Ground(maplength, height)
	grnd.renderBlocks(5*maplength/16 , height/4)
	grnd.renderPipe(maplength/5)
	grnd.renderClouds()
	return grnd.returnMatrix()

def renderMap(mapMatrix,length,height):
	map=""
	for y in range(0,height+9):
			for x in range(0,length):
				map += mapMatrix[x][y]
			map += '\n'
	return map

def updateMap(posx, posy, mappos, mat, length, height, direction, maplength,enempos,k,z, direction1,r):
	mapMatrix = []
	for i in range(0, length):
		mapMatrix.append([])
	for x in range(0,length):
		for y in range(0,height+9):
			mapMatrix[x].append(mat[mappos+x][y])
	for i in range(0, len(r)):
		if r[i]==0 :
			if mappos+length>=enempos[i]:
				x=collisionDetect(mat,direction1[i],int(k[i])+mappos,0,height,5,3)
				if x==0:
					if direction1[i]=='a':
						direction1[i]='d'
					else:
						direction1[i]='a'
				if direction1[i]=='a':
					k[i]=k[i]-0.5-z
				else :
					k[i]=k[i]+0.5-z
				enmy = Enemy1(int(k[i]),0)
				mat=enmy.renderEnemy(length, height, mapMatrix, direction1[i])
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
		if hitDetectEnemy(mat,posx,posy,height,6,5) == int(k[i]) and r[i]==0:
			r[i]=1
	return r,direction1,k,mapMatrix