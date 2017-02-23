import pygame, math, sys, time, thread, os, random
from pygame.locals import *
from numpy import *

class Spider:
	x = 0
	y = 0
	offsetX = 0
	offsetY = 0
	size = 32
	energy = 100
	armor = 15
	speed = 7
	base_decay = decay = 300 #time after spider corpse will disappear
	model = None
	dead_model = None
	death_sound_played = False
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.model = pygame.image.load('data/images/monsters/spider/spider.png')
		self.dead_model = pygame.image.load('data/images/monsters/spider/dead_spider.png')
		self.frozen_model = pygame.image.load('data/images/monsters/spider/frozen_spider.png')
		self.fried_model = pygame.image.load('data/images/monsters/spider/roasted_spider.png')
		self.frozen = False
		self.killed = False
		self.fried = False
