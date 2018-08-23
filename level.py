from ground import Ground
from mario import Mario
from enemy import Enemy1
from boss import Boss
from collision import *
import sys
from os import system
from init import *
from jump import *
from random import randint

def returnMap(maplength, height,level):
	grnd = Ground(maplength, height)
	grnd.renderClouds()
	placeBlocks(grnd, maplength, height)
	placePipe(grnd, level, maplength)
	placeHole(grnd,maplength)
	return grnd.returnMatrix()

def renderMap(mapMatrix,length,height):
	map=""
	for y in range(0,height+9):
			for x in range(0,length):
				map += mapMatrix[x][y]
			map += '\n'
	return map

def updateMap(boss,level, posx, posy, mappos, mat, length, height, direction, maplength,enempos,kx,ky,z, direction1,r,fe,score,bosspos,direction2):
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
				if level==1:
					kx[i]=kx[i]-0.5-z
				else:
					kx[i]=kx[i]-0.8-z
			else :
				if level==1:
					kx[i]=kx[i]+0.5-z
				else:
					kx[i]=kx[i]+0.8-z					
	if level==2 :
		if mappos+length>=bosspos:
			mat=boss.renderBoss(length, height, mapMatrix)
			if direction2=='a':
				boss.x=boss.x-1
			elif direction2 =='d':
				boss.x=boss.x+1
			if boss.x == 50:
				direction2='d'
			elif boss.x== 85:
				direction2='a'

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
			a=hitDetectEnemy(mapMatrix,posx,posy,int(kx[i]),int(ky[i]),height,5,3)
			if a==1:
				score=score+20
			b=fallDetect(mapMatrix,int(kx[i]),int(ky[i]),height,5,maplength)
			if a == 1 or b ==0 or int(kx[i])<0:
				#if int(kx[i])+5>=0:
				system('aplay smb_stomp.wav&')
				r[i]=1
	return score,r,direction1,kx,ky,mapMatrix