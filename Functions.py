import pygame, math, sys, time, thread, os, random
from pygame.locals import *
from numpy import *

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data/sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound
	
def convert_angle(angle):
	if angle == 0: #up
		angle_conv = math.pi
	elif angle == 90: #right
		angle_conv = math.pi / 2
	elif angle == 180: #down
		angle_conv = 0
	elif angle == 270: #left
		angle_conv = 3 * math.pi / 2
	
	elif angle == 45:
		angle_conv = 3 * math.pi / 4
	elif angle == 135:
		angle_conv = math.pi / 4
	elif angle == 225:
		angle_conv = 7 * math.pi / 4
	elif angle == 315:
		angle_conv = 5 * math.pi / 4
	
	return angle_conv
