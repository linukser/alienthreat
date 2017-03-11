import pygame, math, sys, time, thread, os, random
from pygame.locals import *
from numpy import *

class Hunter:
	x = 0
	y = 0
	offsetX = 0
	offsetY = 0
	movement_loop = 0
	size = 64
	energy = 100
	armor = 700.0
	speed = 7
	fire_loop = 0
	base_decay = decay = 500
	model = None
	dead_model = None
	death_sound_played = False
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.model = pygame.image.load('data/images/monsters/hunter/hunter.png')
		self.dead_model = pygame.image.load('data/images/monsters/hunter/hunter.png')
		self.frozen_model = pygame.image.load('data/images/monsters/hunter/hunter.png')
		self.fried_model = pygame.image.load('data/images/monsters/hunter/hunter.png')
		self.frozen = False
		self.killed = False
		self.fried = False
