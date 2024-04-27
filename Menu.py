import pygame, math, sys, time, _thread, os, random
from pygame.locals import *
from numpy import *

#menu functions

def start_game(screen, game):
	exit_menu = False
	y = 0
	
	while(exit_menu == False):
		screen.fill((0, 0, 0))
		font = pygame.font.SysFont("Courier New", 60)
		
		start_game_label = font.render('Start game', True, (0, 255, 100))	
		one_player_label = font.render('1 Player', True, (0, 255, 100))
		two_players_label = font.render('2 Players', True, (0, 255, 100))
		three_players_label = font.render('3 Players', True, (0, 255, 100))
		return_label = font.render('return', True, (0, 255, 100))
		
		screen.blit(start_game_label, (150, 150))
		screen.blit(one_player_label, (150, 250))
		screen.blit(two_players_label, (150, 350))
		screen.blit(three_players_label, (150, 450))
		screen.blit(return_label, (150, 550))
		
		pygame.draw.rect(screen, (0, 255, 100), (100, 240 + y * 100, 1050, 100), 10)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_DOWN:
				if y < 3:
					y += 1
			elif event.type == KEYDOWN and event.key == K_UP:
				if y > 0:
					y -= 1
			elif event.type == KEYDOWN and event.key == K_RETURN:
				if y == 0:
					game.number_of_players = 1
					choose_character(screen, game, 'Nash')
					return True
				elif y == 1:
					game.number_of_players = 2
					choose_character(screen, game, 'Nash')
					choose_character(screen, game, 'George')
					return True
				elif y == 2:
					game.number_of_players = 3
					choose_character(screen, game, 'Nash')
					choose_character(screen, game, 'George')
					choose_character(screen, game, 'James')
					return True
				elif y == 3:
					#return to menu
					return False
			elif event.type == KEYDOWN and event.key == K_BACKSPACE:
				exit_menu = True
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				exit_menu = True

	
	pygame.mixer.music.stop()
	time.sleep(0.2)
	return exit_menu

def choose_character(screen, game, character_name):
	exit_menu = False
	y = 0
	
	while(exit_menu == False):
		screen.fill((0, 0, 0))
		font = pygame.font.SysFont("Courier New", 60)
		
		character = 'Choose character: ' + character_name
		start_game_label = font.render(character, True, (0, 255, 100))	
		commando_label = font.render('Commando', True, (0, 255, 100))
		robot_label = font.render('Robot', True, (0, 255, 100))
		doctor_label = font.render('Doctor', True, (0, 255, 100))
		scientist_label = font.render('Scientist', True, (0, 255, 100))
		return_label = font.render('return', True, (0, 255, 100))
		
		screen.blit(start_game_label, (150, 150))
		screen.blit(commando_label, (150, 250))
		screen.blit(robot_label, (150, 350))
		screen.blit(doctor_label, (150, 450))
		screen.blit(scientist_label, (150, 550))
		screen.blit(return_label, (150, 650))
		
		pygame.draw.rect(screen, (0, 255, 100), (100, 240 + y * 100, 1050, 100), 10)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_DOWN:
				if y < 4:
					y += 1
			elif event.type == KEYDOWN and event.key == K_UP:
				if y > 0:
					y -= 1
			elif event.type == KEYDOWN and event.key == K_RETURN:
				if y == 0:
					if character_name == 'Nash':
						game.nash_character = 1
					elif character_name == 'George':
						game.george_character = 1
					elif character_name == 'James':
						game.james_character = 1
					return True
				elif y == 1:
					if character_name == 'Nash':
						game.nash_character = 2
					elif character_name == 'George':
						game.george_character = 2
					elif character_name == 'James':
						game.james_character = 2
					return True
				elif y == 2:
					if character_name == 'Nash':
						game.nash_character = 3
					elif character_name == 'George':
						game.george_character = 3
					elif character_name == 'James':
						game.james_character = 3
					return True
				elif y == 3:
					if character_name == 'Nash':
						game.nash_character = 4
					elif character_name == 'George':
						game.george_character = 4
					elif character_name == 'James':
						game.james_character = 4
					return True
				elif y == 4:
					#return to menu
					return False
			elif event.type == KEYDOWN and event.key == K_BACKSPACE:
				exit_menu = True
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				exit_menu = True

	
	pygame.mixer.music.stop()
	time.sleep(0.2)
	return exit_menu

	
def options(screen, game):
	exit_menu = False
	y = 0
	
	while(exit_menu == False):
		screen.fill((0, 0, 0))
		font = pygame.font.SysFont("Courier New", 60)
		
		start_game_label = font.render('Choose difficulty', True, (0, 255, 100))	
		easy_label = font.render('Easy', True, (0, 255, 100))
		medium_label = font.render('Medium', True, (0, 255, 100))
		hard_label = font.render('Hard', True, (0, 255, 100))
		return_label = font.render('return to menu', True, (0, 255, 100))
		
		screen.blit(start_game_label, (150, 150))
		screen.blit(easy_label, (150, 250))
		screen.blit(medium_label, (150, 350))
		screen.blit(hard_label, (150, 450))
		screen.blit(return_label, (150, 550))
		
		pygame.draw.rect(screen, (0, 255, 100), (100, 240 + y * 100, 1050, 100), 10)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_DOWN:
				if y < 3:
					y += 1
			elif event.type == KEYDOWN and event.key == K_UP:
				if y > 0:
					y -= 1
			elif event.type == KEYDOWN and event.key == K_RETURN:
				if y == 0:
					game.difficulty = 'easy'
					game.spider_attack = 1.0
					exit_menu = True
				elif y == 1:
					game.difficulty = 'medium'
					game.spider_attack = 2.0
					exit_menu = True
				elif y == 2:
					game.difficulty = 'hard'
					game.spider_attack = 3.0
					exit_menu = True
				elif y == 3:
					#return to menu
					return False
			elif event.type == KEYDOWN and event.key == K_BACKSPACE:
				exit_menu = True
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				exit_menu = True

	
	pygame.mixer.music.stop()
	time.sleep(0.2)
	return exit_menu

	
def menu(screen, game):

	exit_menu = False
	exit_game = False
	y = 0
	
	while(exit_menu == False):
		screen.fill((0, 0, 0))
		font = pygame.font.SysFont("Courier New", 60)
		alien_threat_label = font.render('Alien Threat ' + game.version, True, (0, 255, 100))
		
		if game.started == False:
			start_game_label = font.render('Start new game', True, (0, 255, 100))
		elif game.started == True:
			start_game_label = font.render('Resume game', True, (0, 255, 100))
			
		load_game_label = font.render('Load game', True, (0, 255, 100))
		options_label = font.render('Options', True, (0, 255, 100))
		exit_game_label = font.render('Exit game', True, (0, 255, 100))
		screen.blit(alien_threat_label, (150, 150))
		screen.blit(start_game_label, (150, 250))
		screen.blit(load_game_label, (150, 350))
		screen.blit(options_label, (150, 450))
		screen.blit(exit_game_label, (150, 550))
		
		pygame.draw.rect(screen, (0, 255, 100), (100, 240 + y * 100, 1050, 100), 10)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_DOWN:
				if y < 3:
					y += 1
			elif event.type == KEYDOWN and event.key == K_UP:
				if y > 0:
					y -= 1
			elif event.type == KEYDOWN and event.key == K_RETURN:
				if y == 0:
					if game.started == False:
						exit_menu = start_game(screen, game)
					else:
						exit_menu = True
				elif y == 1:
					pass
				elif y == 2:
					y = 0
					options(screen, game)
				elif y == 3:
					sys.exit()
			elif event.type == KEYDOWN and event.key == K_BACKSPACE:
				exit_menu = True
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				exit_menu = True
