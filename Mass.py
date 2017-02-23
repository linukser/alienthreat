import pygame
from numpy import *

class Mass:
	x = 0
	y = 0
	offsetX = 0
	offsetY = 0
	energy = 100
	armor = 50
	speed = 2
	size = 128
	model = None
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
		self.movement_loop = 0
		
		choice = random.randint(0, 4)
		if choice == 0:
			self.model = pygame.image.load('data/images/monsters/mass/mass1.png')
			self.dead_model = pygame.image.load('data/images/monsters/mass/mass1.png')
			self.frozen_model = pygame.image.load('data/images/monsters/mass/mass1.png')
			self.fried_model = pygame.image.load('data/images/monsters/mass/mass1.png')
			self.size = 128
		elif choice == 1:
			self.model = pygame.image.load('data/images/monsters/mass/mass2.png')
			self.dead_model = pygame.image.load('data/images/monsters/mass/mass2.png')
			self.frozen_model = pygame.image.load('data/images/monsters/mass/mass2.png')
			self.fried_model = pygame.image.load('data/images/monsters/mass/mass2.png')
			self.size = 150
		elif choice == 2:
			self.model = pygame.image.load('data/images/monsters/mass/mass3.png')
			self.dead_model = pygame.image.load('data/images/monsters/mass/mass3.png')
			self.frozen_model = pygame.image.load('data/images/monsters/mass/mass3.png')
			self.fried_model = pygame.image.load('data/images/monsters/mass/mass3.png')
			self.size = 200
		elif choice == 3:
			self.model = pygame.image.load('data/images/monsters/mass/mass4.png')
			self.dead_model = pygame.image.load('data/images/monsters/mass/mass4.png')
			self.frozen_model = pygame.image.load('data/images/monsters/mass/mass4.png')
			self.fried_model = pygame.image.load('data/images/monsters/mass/mass4.png')
			self.size = 300
			
		self.frozen = False
		self.killed = False
		self.fried = False
		
		# self.center_x = 0
		# self.center_y = 0
		# self.colony = []
		
		# for i in range(0, size):
			# self.colony.append(Point(self.center_x + random.randint(0, 50), self.center_y + random.randint(0, 50), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
