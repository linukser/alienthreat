import pygame, math, sys, time, _thread, os, random
from pygame.locals import *
from numpy import *

class Robot:
	x = 0
	y = 0
	offsetX = 0
	offsetY = 0
	movement_loop = 0
	size = 64
	energy = 100
	armor = 250.0
	speed = 2
	#base_decay = decay = 300 #time after robot corpse will disappear
	base_decay = decay = 150 #time after robot corpse will disappear
	model = None
	dead_model = None
	death_sound_played = False
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.model = pygame.image.load('data/images/monsters/robot/robot.png')
		self.dead_model = pygame.image.load('data/images/monsters/robot/dead_robot.png')
		self.frozen_model = pygame.image.load('data/images/monsters/robot/frozen_robot.png')
		self.fried_model = pygame.image.load('data/images/monsters/robot/roast_robot.png')
		self.frozen = False
		self.killed = False
		self.fried = False
