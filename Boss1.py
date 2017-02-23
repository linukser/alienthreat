import pygame, math, sys, time, thread, os, random
from pygame.locals import *
from numpy import *

class Boss1:
	x = 0
	y = 0
	offsetX = 0
	offsetY = 0
	size = 300
	energy = 100
	armor = 10000.0
	# armor = 500.0
	speed = 13
	
	movement_loop = 0
	movement_loop_max = 5
	fire_loop = 0
	fire_loop_max = 2
	
	base_decay = 250
	decay = 250
	model = None
	dead_model = None
	death_sound_played = False
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.model = pygame.image.load('data/images/bosses/boss1/alienog.png')
		self.dead_model = pygame.image.load('data/images/bosses/boss1/alienog.png')
		self.frozen_model = pygame.image.load('data/images/bosses/boss1/alienog.png')
		self.fried_model = pygame.image.load('data/images/bosses/boss1/alienog.png')
		self.frozen = False
		self.killed = False
		self.fried = False
