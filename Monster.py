import pygame, math, sys, time, _thread, os, random
from pygame.locals import *
from numpy import *

from Spider import *
from Gigantula import *
from Robot import *
from Crane import *
from Hunter import *

class Monster:
	monsters = []
	gigantulas = []
	robots = []
	cranes = []
	hunters = []
	
	def add_monster(self, spider):
		self.monsters.append(spider)
	def add_spider(self, game):
		self.monsters.append(Spider(random.randint(100, game.map_size_x - 100), random.randint(100, game.map_size_y - 100 - game.screen_bottom)))
	def add_gigantula(self, game):
		self.gigantulas.append(Gigantula(random.randint(100, game.map_size_x - 100), random.randint(100, game.map_size_y - 100 - game.screen_bottom)))
	def add_robot(self, game):
		self.robots.append(Robot(random.randint(100, game.map_size_x - 100), random.randint(100, game.map_size_y - 100 - game.screen_bottom)))
	def add_crane(self, game):
		self.cranes.append(Crane(random.randint(100, game.map_size_x - 100), random.randint(100, game.map_size_y - 100 - game.screen_bottom)))
	def add_hunter(self, game):
		self.hunters.append(Hunter(random.randint(100, game.map_size_x - 100), random.randint(100, game.map_size_y - 100 - game.screen_bottom)))
	
	def kill_monster(self, game, new_x, new_y, range, weapon, global_player, player_name):
		for monster in self.monsters:
			if monster.energy > 0:
				if weapon == 'flamethrower':
					if new_x + range >= monster.x + 16 + game.x and new_x - range <= monster.x + 16 + monster.size + game.x and new_y + range >= monster.y + 16 + game.y and new_y - range <= monster.y + 16 + monster.size + game.y:
						monster.energy -= 50.0 / monster.armor
						if monster.energy <= 0:
							monster.fried = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 10
							game.points += 10
							if game.number_of_players > 1:
								global_player.players['george'].money += 10
							elif game.number_of_players > 2:
								global_player.players['james'].money += 10
							
				elif weapon == 'freezer':
					if new_x + range >= monster.x + 16 + game.x and new_x - range <= monster.x + 16 + monster.size + game.x and new_y + range >= monster.y + 16 + game.y and new_y - range <= monster.y + 16 + monster.size + game.y:
						#if global_player.players[player_name].has_freezer_upgrade1 == True:
						#	game.freezer_power_for_spider = 150
							
						monster.energy -= game.freezer_power_for_spider / monster.armor
						if monster.energy <= 0:
							monster.frozen = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 10
							game.points += 10
							if game.number_of_players > 1:
								global_player.players['george'].money += 10
							elif game.number_of_players > 2:
								global_player.players['james'].money += 10
							
				elif weapon == 'laser':
					if new_x + range >= monster.x + 16 + game.x and new_x - range <= monster.x + 16 + monster.size + game.x and new_y + range >= monster.y + 16 + game.y and new_y - range <= monster.y + 16 + monster.size + game.y:
						
						monster.energy -= game.laser_power / monster.armor
						
						if monster.energy <= 0:
							monster.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 10
							game.points += 10
							if game.number_of_players > 1:
								global_player.players['george'].money += 10
							elif game.number_of_players > 2:
								global_player.players['james'].money += 10
							
				elif weapon == 'plasma':
					if new_x + range >= monster.x + 16 + game.x and new_x - range <= monster.x + 16 + monster.size + game.x and new_y + range >= monster.y + 16 + game.y and new_y - range <= monster.y + 16 + monster.size + game.y:
						monster.energy -= game.plasma_power / monster.armor
						if monster.energy <= 0:
							monster.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 10
							game.points += 10
							if game.number_of_players > 1:
								global_player.players['george'].money += 10
							elif game.number_of_players > 2:
								global_player.players['james'].money += 10
							
				elif weapon == 'vortex':
					if new_x + range >= monster.x + 16 + game.x and new_x - range <= monster.x + 16 + monster.size + game.x and new_y + range >= monster.y + 16 + game.y and new_y - range <= monster.y + 16 + monster.size + game.y:
						#monster.energy -= 250.0 / monster.armor
						monster.energy -= game.vortex_power / monster.armor
						if monster.energy <= 0:
							monster.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 10
							game.points += 10
							if game.number_of_players > 1:
								global_player.players['george'].money += 10
							elif game.number_of_players > 2:
								global_player.players['james'].money += 10
							
		for gigantula in self.gigantulas:
			if gigantula.energy > 0:
				if weapon == 'flamethrower':
					if new_x + range >= gigantula.x + 16 + game.x and new_x - range <= gigantula.x + 16 + gigantula.size + game.x and new_y + range >= gigantula.y + 16 + game.y and new_y - range <= gigantula.y + 16 + gigantula.size + game.y:
						gigantula.energy -= 50.0 / gigantula.armor
						if gigantula.energy <= 0:
							gigantula.fried = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 50
							game.points += 50
							if game.number_of_players > 1:
								global_player.players['george'].money += 50
							elif game.number_of_players > 2:
								global_player.players['james'].money += 50
							
				elif weapon == 'freezer':
					if new_x + range >= gigantula.x + 16 + game.x and new_x - range <= gigantula.x + 16 + gigantula.size + game.x and new_y + range >= gigantula.y + 16 + game.y and new_y - range <= gigantula.y + 16 + gigantula.size + game.y:
						#if global_player.players[player_name].has_freezer_upgrade1 == True:
						#	gigantula.energy -= (game.freezer_power_for_gigantula + 30) / gigantula.armor
						#else:
						#	gigantula.energy -= game.freezer_power_for_gigantula / gigantula.armor

						gigantula.energy -= game.freezer_power_for_gigantula / gigantula.armor
												
						if gigantula.energy <= 0:
							gigantula.frozen = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 50
							game.points += 50
							if game.number_of_players > 1:
								global_player.players['george'].money += 50
							elif game.number_of_players > 2:
								global_player.players['james'].money += 50
							
				elif weapon == 'laser':
					if new_x + range >= gigantula.x + 16 + game.x and new_x - range <= gigantula.x + 16 + gigantula.size + game.x and new_y + range >= gigantula.y + 16 + game.y and new_y - range <= gigantula.y + 16 + gigantula.size + game.y:
						
						gigantula.energy -= game.laser_power / gigantula.armor
						
						if gigantula.energy <= 0:
							gigantula.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 50
							game.points += 50
							if game.number_of_players > 1:
								global_player.players['george'].money += 50
							elif game.number_of_players > 2:
								global_player.players['james'].money += 50
							
				elif weapon == 'plasma':
					if new_x + range >= gigantula.x + 16 + game.x and new_x - range <= gigantula.x + 16 + gigantula.size + game.x and new_y + range >= gigantula.y + 16 + game.y and new_y - range <= gigantula.y + 16 + gigantula.size + game.y:
						gigantula.energy -= game.plasma_power / gigantula.armor
						if gigantula.energy <= 0:
							gigantula.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 50
							game.points += 50
							if game.number_of_players > 1:
								global_player.players['george'].money += 50
							elif game.number_of_players > 2:
								global_player.players['james'].money += 50
							
				elif weapon == 'vortex':
					if new_x + range >= gigantula.x + 16 + game.x and new_x - range <= gigantula.x + 16 + gigantula.size + game.x and new_y + range >= gigantula.y + 16 + game.y and new_y - range <= gigantula.y + 16 + gigantula.size + game.y:
						gigantula.energy -= 250.0 / gigantula.armor
						if gigantula.energy <= 0:
							gigantula.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 50
							game.points += 50
							if game.number_of_players > 1:
								global_player.players['george'].money += 50
							elif game.number_of_players > 2:
								global_player.players['james'].money += 50

		for robot in self.robots:
			if robot.energy > 0:
				if weapon == 'flamethrower':
					if new_x + range >= robot.x + 16 + game.x and new_x - range <= robot.x + 16 + robot.size + game.x and new_y + range >= robot.y + 16 + game.y and new_y - range <= robot.y + 16 + robot.size + game.y:
						robot.energy -= game.flamethrower_power_for_robot / robot.armor
						if robot.energy <= 0:
							robot.fried = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 250
							game.points += 250
							if game.number_of_players > 1:
								global_player.players['george'].money += 250
							elif game.number_of_players > 2:
								global_player.players['james'].money += 250
							
				elif weapon == 'freezer':
					if new_x + range >= robot.x + 16 + game.x and new_x - range <= robot.x + 16 + robot.size + game.x and new_y + range >= robot.y + 16 + game.y and new_y - range <= robot.y + 16 + robot.size + game.y:
						#if global_player.players[player_name].has_freezer_upgrade1 == True:
						#	game.freezer_power_for_robot = 150
												
						robot.energy -= game.freezer_power_for_robot / robot.armor
						if robot.energy <= 0:
							robot.frozen = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 250
							game.points += 250
							if game.number_of_players > 1:
								global_player.players['george'].money += 250
							elif game.number_of_players > 2:
								global_player.players['james'].money += 250
							
				elif weapon == 'laser':
					if new_x + range >= robot.x + 16 + game.x and new_x - range <= robot.x + 16 + robot.size + game.x and new_y + range >= robot.y + 16 + game.y and new_y - range <= robot.y + 16 + robot.size + game.y:
						
						robot.energy -= game.laser_power / robot.armor
							
						if robot.energy <= 0:
							robot.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 250
							game.points += 250
							if game.number_of_players > 1:
								global_player.players['george'].money += 250
							elif game.number_of_players > 2:
								global_player.players['james'].money += 250
							
				elif weapon == 'plasma':
					if new_x + range >= robot.x + 16 + game.x and new_x - range <= robot.x + 16 + robot.size + game.x and new_y + range >= robot.y + 16 + game.y and new_y - range <= robot.y + 16 + robot.size + game.y:
						robot.energy -= game.plasma_power / robot.armor
						if robot.energy <= 0:
							robot.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 250
							game.points += 250
							if game.number_of_players > 1:
								global_player.players['george'].money += 250
							elif game.number_of_players > 2:
								global_player.players['james'].money += 250
							
				elif weapon == 'vortex':
					if new_x + range >= robot.x + 16 + game.x and new_x - range <= robot.x + 16 + robot.size + game.x and new_y + range >= robot.y + 16 + game.y and new_y - range <= robot.y + 16 + robot.size + game.y:
						robot.energy -= 1000.0 / robot.armor
						if robot.energy <= 0:
							robot.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 250
							game.points += 250
							if game.number_of_players > 1:
								global_player.players['george'].money += 250
							elif game.number_of_players > 2:
								global_player.players['james'].money += 250
								
		for crane in self.cranes:
			if crane.energy > 0:
				if weapon == 'flamethrower':
					if new_x + range >= crane.x + 16 + game.x and new_x - range <= crane.x + 16 + crane.size + game.x and new_y + range >= crane.y + 16 + game.y and new_y - range <= crane.y + 16 + crane.size + game.y:
						crane.energy -= game.flamethrower_power_for_crane / crane.armor
						if crane.energy <= 0:
							crane.fried = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 1000
							game.points += 1000
							if game.number_of_players > 1:
								global_player.players['george'].money += 1000
							elif game.number_of_players > 2:
								global_player.players['james'].money += 1000
							
				elif weapon == 'freezer':
					if new_x + range >= crane.x + 16 + game.x and new_x - range <= crane.x + 16 + crane.size + game.x and new_y + range >= crane.y + 16 + game.y and new_y - range <= crane.y + 16 + crane.size + game.y:
						#if global_player.players[player_name].has_freezer_upgrade1 == True:
						#	game.freezer_power_for_crane = 150
												
						crane.energy -= game.freezer_power_for_crane / crane.armor
						if crane.energy <= 0:
							crane.frozen = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 1000
							game.points += 1000
							if game.number_of_players > 1:
								global_player.players['george'].money += 1000
							elif game.number_of_players > 2:
								global_player.players['james'].money += 1000
							
				elif weapon == 'laser':
					if new_x + range >= crane.x + 16 + game.x and new_x - range <= crane.x + 16 + crane.size + game.x and new_y + range >= crane.y + 16 + game.y and new_y - range <= crane.y + 16 + crane.size + game.y:
						
						crane.energy -= game.laser_power / crane.armor
							
						if crane.energy <= 0:
							crane.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 1000
							game.points += 1000
							if game.number_of_players > 1:
								global_player.players['george'].money += 1000
							elif game.number_of_players > 2:
								global_player.players['james'].money += 1000
							
				elif weapon == 'plasma':
					if new_x + range >= crane.x + 16 + game.x and new_x - range <= crane.x + 16 + crane.size + game.x and new_y + range >= crane.y + 16 + game.y and new_y - range <= crane.y + 16 + crane.size + game.y:
						crane.energy -= game.plasma_power / crane.armor
						if crane.energy <= 0:
							crane.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 1000
							game.points += 1000
							if game.number_of_players > 1:
								global_player.players['george'].money += 1000
							elif game.number_of_players > 2:
								global_player.players['james'].money += 1000
							
				elif weapon == 'vortex':
					if new_x + range >= crane.x + 16 + game.x and new_x - range <= crane.x + 16 + crane.size + game.x and new_y + range >= crane.y + 16 + game.y and new_y - range <= crane.y + 16 + crane.size + game.y:
						crane.energy -= 1000.0 / crane.armor
						if crane.energy <= 0:
							crane.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 1000
							game.points += 1000
							if game.number_of_players > 1:
								global_player.players['george'].money += 1000
							elif game.number_of_players > 2:
								global_player.players['james'].money += 1000
		
		for hunter in self.hunters:
			if hunter.energy > 0:
				if weapon == 'flamethrower':
					if new_x + range >= hunter.x + 16 + game.x and new_x - range <= hunter.x + 16 + hunter.size + game.x and new_y + range >= hunter.y + 16 + game.y and new_y - range <= hunter.y + 16 + hunter.size + game.y:
						hunter.energy -= 50.0 / hunter.armor
						if hunter.energy <= 0:
							hunter.fried = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 2000
							game.points += 2000
							if game.number_of_players > 1:
								global_player.players['george'].money += 2000
							elif game.number_of_players > 2:
								global_player.players['james'].money += 2000
							
				elif weapon == 'freezer':
					if new_x + range >= hunter.x + 16 + game.x and new_x - range <= hunter.x + 16 + hunter.size + game.x and new_y + range >= hunter.y + 16 + game.y and new_y - range <= hunter.y + 16 + hunter.size + game.y:
						#if global_player.players[player_name].has_freezer_upgrade1 == True:
						#	game.freezer_power_for_hunter = 150
												
						hunter.energy -= game.freezer_power_for_spider / hunter.armor
						if hunter.energy <= 0:
							hunter.frozen = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 2000
							game.points += 2000
							if game.number_of_players > 1:
								global_player.players['george'].money += 2000
							elif game.number_of_players > 2:
								global_player.players['james'].money += 2000
							
				elif weapon == 'laser':
					if new_x + range >= hunter.x + 16 + game.x and new_x - range <= hunter.x + 16 + hunter.size + game.x and new_y + range >= hunter.y + 16 + game.y and new_y - range <= hunter.y + 16 + hunter.size + game.y:
						
						hunter.energy -= game.laser_power / hunter.armor
							
						if hunter.energy <= 0:
							hunter.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 2000
							game.points += 2000
							if game.number_of_players > 1:
								global_player.players['george'].money += 2000
							elif game.number_of_players > 2:
								global_player.players['james'].money += 2000
							
				elif weapon == 'plasma':
					if new_x + range >= hunter.x + 16 + game.x and new_x - range <= hunter.x + 16 + hunter.size + game.x and new_y + range >= hunter.y + 16 + game.y and new_y - range <= hunter.y + 16 + hunter.size + game.y:
						hunter.energy -= game.plasma_power / hunter.armor
						if hunter.energy <= 0:
							hunter.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 2000
							game.points += 2000
							if game.number_of_players > 1:
								global_player.players['george'].money += 2000
							elif game.number_of_players > 2:
								global_player.players['james'].money += 2000
							
				elif weapon == 'vortex':
					if new_x + range >= hunter.x + 16 + game.x and new_x - range <= hunter.x + 16 + hunter.size + game.x and new_y + range >= hunter.y + 16 + game.y and new_y - range <= hunter.y + 16 + hunter.size + game.y:
						hunter.energy -= 250.0 / hunter.armor
						if hunter.energy <= 0:
							hunter.killed = True
							
							global_player.players[player_name].experience += 1
							
							global_player.players['nash'].money += 2000
							game.points += 2000
							if game.number_of_players > 1:
								global_player.players['george'].money += 2000
							elif game.number_of_players > 2:
								global_player.players['james'].money += 2000

								
		if game.boss.energy > 0:
			if weapon == 'flamethrower':
				if new_x + range >= game.boss.x + 16 + game.x and new_x - range <= game.boss.x + 16 + game.boss.size + game.x and new_y + range >= game.boss.y + 16 + game.y and new_y - range <= game.boss.y + 16 + game.boss.size + game.y:
					game.boss.energy -= 50.0 / game.boss.armor
					if game.boss.energy <= 0:
						game.boss.fried = True
						
						global_player.players[player_name].experience += 1
						
						global_player.players['nash'].money += 5000 * game.stage
						game.points += 1000
						if game.number_of_players > 1:
							global_player.players['george'].money += 5000 * game.stage
						elif game.number_of_players > 2:
							global_player.players['james'].money += 5000 * game.stage
						
			elif weapon == 'freezer':
				if new_x + range >= game.boss.x + 16 + game.x and new_x - range <= game.boss.x + 16 + game.boss.size + game.x and new_y + range >= game.boss.y + 16 + game.y and new_y - range <= game.boss.y + 16 + game.boss.size + game.y:
					#if global_player.players[player_name].has_freezer_upgrade1 == True:
					#	game.freezer_power_for_boss = 150
											
					game.boss.energy -= game.freezer_power_for_boss / game.boss.armor

					if game.boss.energy <= 0:
						game.boss.frozen = True
						
						global_player.players[player_name].experience += 1
						
						global_player.players['nash'].money += 5000 * game.stage
						game.points += 1000
						if game.number_of_players > 1:
							global_player.players['george'].money += 5000 * game.stage
						elif game.number_of_players > 2:
							global_player.players['james'].money += 5000 * game.stage
						
			elif weapon == 'laser':
				if new_x + range >= game.boss.x + 16 + game.x and new_x - range <= game.boss.x + 16 + game.boss.size + game.x and new_y + range >= game.boss.y + 16 + game.y and new_y - range <= game.boss.y + 16 + game.boss.size + game.y:
					
					game.boss.energy -= game.laser_power / game.boss.armor
							
					if game.boss.energy <= 0:
						game.boss.killed = True
						
						global_player.players[player_name].experience += 1
						
						global_player.players['nash'].money += 5000 * game.stage
						game.points += 1000
						if game.number_of_players > 1:
							global_player.players['george'].money += 5000 * game.stage
						elif game.number_of_players > 2:
							global_player.players['james'].money += 5000 * game.stage
						
			elif weapon == 'plasma':
				if new_x + range >= game.boss.x + 16 + game.x and new_x - range <= game.boss.x + 16 + game.boss.size + game.x and new_y + range >= game.boss.y + 16 + game.y and new_y - range <= game.boss.y + 16 + game.boss.size + game.y:

					game.boss.energy -= game.plasma_power / game.boss.armor

					if game.boss.energy <= 0:
						game.boss.killed = True
						
						global_player.players[player_name].experience += 1
						
						global_player.players['nash'].money += 5000 * game.stage
						game.points += 1000
						if game.number_of_players > 1:
							global_player.players['george'].money += 5000 * game.stage
						elif game.number_of_players > 2:
							global_player.players['james'].money += 5000 * game.stage
						
			elif weapon == 'vortex':
				if new_x + range >= game.boss.x + 16 + game.x and new_x - range <= game.boss.x + 16 + game.boss.size + game.x and new_y + range >= game.boss.y + 16 + game.y and new_y - range <= game.boss.y + 16 + game.boss.size + game.y:

					game.boss.energy -= 1000.0 / game.boss.armor

					if game.boss.energy <= 0:
						game.boss.killed = True
						
						global_player.players[player_name].experience += 1
						
						global_player.players['nash'].money += 5000 * game.stage
						game.points += 1000
						if game.number_of_players > 1:
							global_player.players['george'].money += 5000 * game.stage
						elif game.number_of_players > 2:
							global_player.players['james'].money += 5000 * game.stage

	def kill_player(self, game, new_x, new_y, weapon_range, weapon, global_player, pain_sound, screen):
		for player in global_player.players.keys():
			if global_player.players[player].energy > 0:
				if weapon == 'robot_weapon':
					if new_x + weapon_range >= global_player.players[player].x + 16 + game.x and new_x - weapon_range <= global_player.players[player].x + 16 + 64 + game.x and new_y + weapon_range >= global_player.players[player].y + 16 + game.y and new_y - weapon_range <= global_player.players[player].y + 16 + 64 + game.y:
						global_player.players[player].energy -= 1.0 / global_player.players[player].armor
						pain_sound.play()
						global_player.players[player].being_attacked = True
						if global_player.players[player].energy <= 0:
							if game.lifes_pool > 0:
								game.lifes_pool -= 1
								global_player.players[player].energy = global_player.players[player].max_energy
								pain_sound.play()

								#draw player's death/explosion
								for i in range(0, 25):
									for angl in range(0, 100):
										#draw bloody vortex
										random_distortion = random.uniform(-0.2, 0.2)
										new_x = global_player.players[player].x + 32 + int(math.sin(angl * 3 + random_distortion) * 5 * i)
										new_y = global_player.players[player].y + 32 + int(math.cos(angl * 3 + random_distortion) * 5 * i)
										
										random_size = random.randint(2, 7)
										pygame.draw.circle(screen, (100, 0, 0), (new_x, new_y), random_size, 0)
											
										self.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, 'nash')
										
										random_distortion = random.uniform(-0.2, 0.2)
										new_x = global_player.players[player].x + 32 + int(math.sin(angl * 3 + random_distortion) * 5 * i)
										new_y = global_player.players[player].y + 32 + int(math.cos(angl * 3 + random_distortion) * 5 * i)
										
										random_size = random.randint(1, 5)
										pygame.draw.circle(screen, (155 + i * 4, 0, 0), (new_x, new_y), random_size, 0)
												
										self.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, 'nash')
										
									#pygame.display.flip()
									time.sleep(0.03)
								
							else:
								global_player.players[player].dead = True
								pain_sound.play()
				
				if weapon == 'boss_weapon':
					if new_x + weapon_range >= global_player.players[player].x + 16 + game.x and new_x - weapon_range <= global_player.players[player].x + 16 + 64 + game.x and new_y + weapon_range >= global_player.players[player].y + 16 + game.y and new_y - weapon_range <= global_player.players[player].y + 16 + 64 + game.y:
						global_player.players[player].energy -= 6.0 / global_player.players[player].armor
						pain_sound.play()
						global_player.players[player].being_attacked = True
						if global_player.players[player].energy <= 0:
							if game.lifes_pool > 0:
								game.lifes_pool -= 1
								global_player.players[player].energy = global_player.players[player].max_energy
								pain_sound.play()

								#draw player's death/explosion
								for i in range(0, 25):
									for angl in range(0, 100):
										#draw bloody vortex
										random_distortion = random.uniform(-0.2, 0.2)
										new_x = global_player.players[player].x + 32 + int(math.sin(angl * 3 + random_distortion) * 5 * i)
										new_y = global_player.players[player].y + 32 + int(math.cos(angl * 3 + random_distortion) * 5 * i)
										
										random_size = random.randint(2, 7)
										pygame.draw.circle(screen, (100, 0, 0), (new_x, new_y), random_size, 0)
											
										self.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, 'nash')
										
										random_distortion = random.uniform(-0.2, 0.2)
										new_x = global_player.players[player].x + 32 + int(math.sin(angl * 3 + random_distortion) * 5 * i)
										new_y = global_player.players[player].y + 32 + int(math.cos(angl * 3 + random_distortion) * 5 * i)
										
										random_size = random.randint(1, 5)
										pygame.draw.circle(screen, (155 + i * 4, 0, 0), (new_x, new_y), random_size, 0)
												
										self.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, 'nash')
										
									#pygame.display.flip()
									time.sleep(0.01)
								
							else:
								global_player.players[player].dead = True
								pain_sound.play()
						
