import pygame, math, sys, time, thread, os, random
from pygame.locals import *
from numpy import *

class Crane:
	x = 0
	y = 0
	offsetX = 0
	offsetY = 0
	movement_loop = 0
	size = 200
	energy = 100
	armor = 2000.0
	speed = 2
	base_decay = decay = 1000 #time after crane corpse will disappear
	model = None
	dead_model = None
	death_sound_played = False
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.model = pygame.image.load('data/images/monsters/crane/crane.png')
		self.dead_model = pygame.image.load('data/images/monsters/crane/dead_crane.png')
		self.frozen_model = pygame.image.load('data/images/monsters/crane/frozen_crane.png')
		self.fried_model = pygame.image.load('data/images/monsters/crane/roast_crane.png')
		self.frozen = False
		self.killed = False
		self.fried = False
