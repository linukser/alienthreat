import pygame, math, sys, time, _thread, os, random
from pygame.locals import *
from numpy import *

class Boss2:
	x = 0
	y = 0
	offsetX = 0
	offsetY = 0
	size = 64
	energy = 100
	armor = 4000.0
	# armor = 500.0
	speed = 7

	movement_loop = 0
	movement_loop_max = 5
	fire_loop = 0
	fire_loop_max = 4
	
	base_decay = 250
	decay = 250
	model = None
	dead_model = None
	death_sound_played = False
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.model = pygame.image.load('data/images/bosses/boss2/hunter.png')
		self.dead_model = pygame.image.load('data/images/bosses/boss2/hunter.png')
		self.frozen_model = pygame.image.load('data/images/bosses/boss2/hunter.png')
		self.fried_model = pygame.image.load('data/images/bosses/boss2/hunter.png')
		self.frozen = False
		self.killed = False
		self.fried = False
