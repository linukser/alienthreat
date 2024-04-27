import pygame, math, sys, time, _thread, os, random
from pygame.locals import *
from numpy import *

class Gigantula:
	x = 0
	y = 0
	offsetX = 0
	offsetY = 0
	movement_loop = 0
	size = 64
	energy = 100
	armor = 200
	speed = 5
	#base_decay = decay = 500 #time after gigantula corpse will disappear
	base_decay = decay = 150 #time after gigantula corpse will disappear
	model = None
	dead_model = None
	death_sound_played = False
	
	breed_loop = 0
	breed_loop_max = 50 #bigger number - less spiders
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.model = pygame.image.load('data/images/monsters/gigantula/gigantula.png')
		self.dead_model = pygame.image.load('data/images/monsters/gigantula/dead_gigantula.png')
		self.frozen_model = pygame.image.load('data/images/monsters/gigantula/frozen_gigantula.png')
		self.fried_model = pygame.image.load('data/images/monsters/gigantula/roasted_gigantula.png')
		self.frozen = False
		self.killed = False
		self.fried = False
