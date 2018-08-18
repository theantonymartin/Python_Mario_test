from os import system
import sys
#from ground import Ground
from level import * 
import time
from jump import *
from input import Get, input_to
from collision import *

length = 80
#height = 25

'''
class _Getch:

    def __init__(self):
    	self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()

class _GetchUnix:


    def __init__(self):
        import tty, sys


    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

_getch=_Getch()

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException


def get_input(timeout=0.1):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout, timeout)
    try:
        text = _getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
'''

'''
def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

getch = _find_getch()
'''
getch = Get()
posx = 0
posy = 0
mappos = 0
flag=0
flag1=0
direction='>'
travlength=0
maplength = 2
length = 80
height = 25
f = 's'
vdist = 0
x=0
while True:

	'''
	grnd = Ground( length, height )
	grnd.renderGround(mappos)
	grnd.renderMario(posx, posy)
	print(grnd.returnString())
	'''
	mat = returnMap(posx, posy, mappos, direction, length*maplength, height)
	print(renderMap(mat,length,height))

	button = input_to(getch)
	if button == 'q':
		system('clear')
		sys.exit()

	if button == 'd':
		x=collisionDetect(mat, button, posx, posy, height)
		direction = '>'
		travlength = travlength + x
		if travlength > ( (1/2 + maplength) * length):
			posx = posx + x
		else :
			if posx+1 < length/2:
				posx = posx + x
			else :
				mappos = mappos + x

	if button == 'a':
		x=collisionDetect(mat, button, posx, posy, height)
		direction = '<'
		if posx > 0:
			posx = posx - x
			travlength = travlength - x

	if button == 'w':
		f=Jump(mat, f, posx, posy, height)

	posy,f,vdist=Grav(mat, f,vdist,posx, posy, height)

	'''if button == 'w' and posy == 0:
		flag=1
		flag1 = 0

	if flag == 1:

		if posy < 7 and flag1 == 0:
			posy += 1
		else :
			posy -=1
		if posy == 7:
			flag1 = 1
		if posy == 0:
			flag = 0
			'''
	#time.sleep(0.25)
	system('clear')

'''while True:
	for i in range(0,pos):
		print(' ', end='')
	print("M")
	button=get_input()
	if button =='q':
		system('clear')
		sys.exit()

	if button == 'd':
		pos=pos+1

	if button == 'a':
		pos=pos-1

	system('clear')
	'''