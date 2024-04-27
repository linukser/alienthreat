import pygame, math, sys, time, _thread, os, random
from pygame.locals import *
from numpy import *

class Shop:

	def __init__(self):
		self.flamethrower_ammo = 0
		self.laser_ammo = 0
		self.plasma_ammo = 0
		self.freezer_ammo = 0

	def armor_shop(self, screen, game, global_player, customer):
		exit_shop = False
		exit = False
		y = 0
		shop_background = pygame.image.load('data/images/backgrounds/shop_background.png').convert()
		
		super_regeneration_price = 150000
		body_armor_price = 100000
		light_armor_price = 50000
		vortex_enhancer_price = 35000
		add_life_price = 25000
		#add_life_price = 400
		force_field_price = 15000
		
		font = pygame.font.SysFont("Courier New", 30)
		
		while(exit_shop == False and exit == False):
			money = global_player.players[customer].money
			
			screen.fill((0, 0, 0))
			screen.blit(shop_background, (0, 0))
			
			money_label = font.render('money: ' + str(money), True, (0, 255, 100))
			
			if money >= super_regeneration_price and global_player.players[customer].has_super_regeneration_upgrade == False:
				super_regeneration_upgrade_label   = font.render('super regeneration:  ' + str(super_regeneration_price), True, (0, 255, 100))
			elif money < super_regeneration_price and global_player.players[customer].has_super_regeneration_upgrade == False:
				super_regeneration_upgrade_label   = font.render('super regeneration:  ' + str(super_regeneration_price), True, (150, 0, 0))
			elif global_player.players[customer].has_super_regeneration_upgrade == True:
				super_regeneration_upgrade_label   = font.render('super regeneration:  ' + str(super_regeneration_price), True, (0, 80, 0))
			
			if money >= body_armor_price and global_player.players[customer].has_body_armor_upgrade == False:
				body_armor_upgrade_label           = font.render('body armor:          ' + str(body_armor_price), True, (0, 255, 100))
			elif money < body_armor_price and global_player.players[customer].has_body_armor_upgrade == False:
				body_armor_upgrade_label           = font.render('body armor:          ' + str(body_armor_price), True, (150, 0, 0))
			elif global_player.players[customer].has_body_armor_upgrade == True:
				body_armor_upgrade_label           = font.render('body armor:          ' + str(body_armor_price), True, (0, 80, 0))
				
			if money >= light_armor_price and global_player.players[customer].has_light_armor_upgrade == False:
				light_armor_upgrade_label          = font.render('light armor:          ' + str(light_armor_price), True, (0, 255, 100))
			elif money < light_armor_price and global_player.players[customer].has_light_armor_upgrade == False:
				light_armor_upgrade_label          = font.render('light armor:          ' + str(light_armor_price), True, (150, 0, 0))
			elif global_player.players[customer].has_light_armor_upgrade == True:
				light_armor_upgrade_label          = font.render('light armor:          ' + str(light_armor_price), True, (0, 80, 0))
			
			if money >= vortex_enhancer_price and global_player.players[customer].has_enhanced_vortex_upgrade == False:
				vortex_enhancer_upgrade_label = font.render('vortex enhancer:      ' + str(vortex_enhancer_price), True, (0, 255, 100))
			elif money < vortex_enhancer_price and global_player.players[customer].has_enhanced_vortex_upgrade == False:
				vortex_enhancer_upgrade_label = font.render('vortex enhancer:      ' + str(vortex_enhancer_price), True, (150, 0, 0))
			elif global_player.players[customer].has_enhanced_vortex_upgrade == True:
				vortex_enhancer_upgrade_label = font.render('vortex enhancer:      ' + str(vortex_enhancer_price), True, (0, 80, 0))
			
			if money >= add_life_price:
				additional_life_label = font.render('additional life:      ' + str(add_life_price), True, (0, 255, 100))
			elif money < add_life_price:
				additional_life_label = font.render('additional life:      ' + str(add_life_price), True, (150, 0, 0))
			#if money >= add_life_price and global_player.players[customer].has_level2_force_field_upgrade == False:
			#	level2_force_field_upgrade_label   = font.render('additional life:   ' + str(add_life_price), True, (0, 255, 100))
			#elif money < add_life_price and global_player.players[customer].has_level2_force_field_upgrade == False:
			#	level2_force_field_upgrade_label   = font.render('additional life:   ' + str(add_life_price), True, (150, 0, 0))
			#elif global_player.players[customer].has_level2_force_field_upgrade == True:
			#	level2_force_field_upgrade_label   = font.render('additional life:   ' + str(add_life_price), True, (0, 80, 0))
			
			if money >= force_field_price and global_player.players[customer].has_force_field == False:
				force_field_label          = font.render('force field:          ' + str(force_field_price), True, (0, 255, 100))
			elif money < force_field_price and global_player.players[customer].has_force_field == False:
				force_field_label          = font.render('force field:          ' + str(force_field_price), True, (150, 0, 0))
			elif global_player.players[customer].has_force_field == True:
				force_field_label          = font.render('force field:          ' + str(force_field_price), True, (0, 80, 0))
			
			exit_shop_label = font.render('return', True, (0, 255, 100))
			screen.blit(money_label, (150, 150))
			screen.blit(super_regeneration_upgrade_label, (150, 250))
			screen.blit(body_armor_upgrade_label, (150, 300))
			screen.blit(light_armor_upgrade_label, (150, 350))
			screen.blit(vortex_enhancer_upgrade_label, (150, 400))
			#screen.blit(level2_force_field_upgrade_label, (150, 450))
			screen.blit(additional_life_label, (150, 450))
			screen.blit(force_field_label, (150, 500))
			screen.blit(exit_shop_label, (150, 550))
			
			pygame.draw.rect(screen, (0, 255, 100), (100, 240 + y * 50, 1050, 50), 10)

			pygame.display.flip()
			
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_DOWN:
					if y < 6:
						y += 1
				elif event.type == KEYDOWN and event.key == K_UP:
					if y > 0:
						y -= 1
				elif event.type == KEYDOWN and event.key == K_RETURN:
					if y == 0:
						#buy super regeneration
						if money >= super_regeneration_price and global_player.players[customer].has_super_regeneration_upgrade == False:
							global_player.players[customer].has_super_regeneration_upgrade = True
							global_player.players[customer].money -= super_regeneration_price
					elif y == 1:
						#buy powerful armor
						if money >= body_armor_price and global_player.players[customer].has_body_armor_upgrade == False:
							global_player.players[customer].has_body_armor_upgrade = True
							global_player.players[customer].money -= body_armor_price
							global_player.players[customer].base_armor *= 3
					elif y == 2:
						#buy light armor
						if money >= light_armor_price and global_player.players[customer].has_light_armor_upgrade == False:
							global_player.players[customer].has_light_armor_upgrade = True
							global_player.players[customer].money -= light_armor_price
							global_player.players[customer].base_armor *= 2
					elif y == 3:
						if money >= vortex_enhancer_price and global_player.players[customer].has_enhanced_vortex_upgrade == False:
							global_player.players[customer].has_enhanced_vortex_upgrade = True
							global_player.players[customer].money -= vortex_enhancer_price
							global_player.players[customer].vortex_loop = 0
							global_player.players[customer].vortex_loop_max = 10
							global_player.players[customer].ammo['vortex'] = 1
					elif y == 4:
						#buy additional life
						if money >= add_life_price:
							global_player.players[customer].money -= add_life_price
							game.lifes_pool += 1
					elif y == 5:
						#faster player
						if money >= force_field_price and global_player.players[customer].has_force_field == False:
							global_player.players[customer].has_force_field = True
							global_player.players[customer].money -= force_field_price
							global_player.players[customer].has_force_field = True
					elif y == 6:
						exit_shop = True
				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					exit_shop = True
				# elif event.type == KEYDOWN and event.key == K_ESCAPE:
					# exit = True
					
		return exit
			
	def weapon_shop(self, screen, game, global_player, customer):
		exit_shop = False
		exit = False
		y = 0
		shop_background = pygame.image.load('data/images/backgrounds/shop_background.png').convert()

		flamethrower_upgrade_price = 10000
		plasma_upgrade_price = 15000
		freezer_upgrade_price = 20000
		laser_upgrade_price = 30000
		
		font = pygame.font.SysFont("Courier New", 60)
		
		while(exit_shop == False and exit == False):
			money = global_player.players[customer].money
			
			screen.fill((0, 0, 0))
			screen.blit(shop_background, (0, 0))
			
			money_label = font.render('money: ' + str(money), True, (0, 255, 100))
			
			if money >= flamethrower_upgrade_price and global_player.players[customer].has_flamethrower_upgrade1 == False:
				flamethrower_upgrade_label = font.render('combat flamethrower: ' + str(flamethrower_upgrade_price), True, (0, 255, 100))
			elif money < flamethrower_upgrade_price and global_player.players[customer].has_flamethrower_upgrade1 == False:
				flamethrower_upgrade_label = font.render('combat flamethrower: ' + str(flamethrower_upgrade_price), True, (150, 0, 0))
			elif global_player.players[customer].has_flamethrower_upgrade1 == True:
				flamethrower_upgrade_label = font.render('combat flamethrower: ' + str(flamethrower_upgrade_price), True, (0, 80, 0))
				
			if money >= plasma_upgrade_price and global_player.players[customer].has_plasma_upgrade1 == False:
				plasma_upgrade_label       = font.render('upgrade plasma:      ' + str(plasma_upgrade_price), True, (0, 255, 100))
			elif money < plasma_upgrade_price and global_player.players[customer].has_plasma_upgrade1 == False:
				plasma_upgrade_label       = font.render('upgrade plasma:      ' + str(plasma_upgrade_price), True, (150, 0, 0))
			elif global_player.players[customer].has_plasma_upgrade1 == True:
				plasma_upgrade_label       = font.render('upgrade plasma:      ' + str(plasma_upgrade_price), True, (0, 80, 0))
			
			if money >= freezer_upgrade_price and global_player.players[customer].has_freezer_upgrade1 == False:
				freezer_upgrade_label      = font.render('upgrade freezer:     ' + str(freezer_upgrade_price), True, (0, 255, 100))
			elif money < freezer_upgrade_price and global_player.players[customer].has_freezer_upgrade1 == False:
				freezer_upgrade_label      = font.render('upgrade freezer:     ' + str(freezer_upgrade_price), True, (150, 0, 0))
			elif global_player.players[customer].has_freezer_upgrade1 == True:
				freezer_upgrade_label      = font.render('upgrade freezer:     ' + str(freezer_upgrade_price), True, (0, 80, 0))
				
			if money >= laser_upgrade_price and global_player.players[customer].has_laser_upgrade1 == False:
				laser_upgrade_label        = font.render('laser power boost:   ' + str(laser_upgrade_price), True, (0, 255, 100))
			elif money < laser_upgrade_price and global_player.players[customer].has_laser_upgrade1 == False:
				laser_upgrade_label        = font.render('laser power boost:   ' + str(laser_upgrade_price), True, (150, 0, 0))
			elif global_player.players[customer].has_laser_upgrade1 == True:
				laser_upgrade_label        = font.render('laser power boost:   ' + str(laser_upgrade_price), True, (0, 80, 0))
			
			exit_shop_label = font.render('return', True, (0, 255, 100))
			screen.blit(money_label, (150, 150))
			screen.blit(flamethrower_upgrade_label, (150, 250))
			screen.blit(plasma_upgrade_label, (150, 350))
			screen.blit(freezer_upgrade_label, (150, 450))
			screen.blit(laser_upgrade_label, (150, 550))
			screen.blit(exit_shop_label, (150, 650))
			
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
						#upgrade flamethrower
						if money >= flamethrower_upgrade_price and global_player.players[customer].has_flamethrower_upgrade1 == False:
							global_player.players[customer].has_flamethrower_upgrade1 = True
							global_player.players[customer].money -= flamethrower_upgrade_price
							#global_player.players[customer].flamethrower_range_upgrade = 3
							global_player.players[customer].flamethrower_range_upgrade = 4
					elif y == 1:
						#upgrade plasma
						if money >= plasma_upgrade_price and global_player.players[customer].has_plasma_upgrade1 == False:
							global_player.players[customer].has_plasma_upgrade1 = True
							global_player.players[customer].money -= plasma_upgrade_price
							global_player.players[customer].plasma_range_upgrade = 3
					elif y == 2:
						#upgrade freezer
						if money >= freezer_upgrade_price and global_player.players[customer].has_freezer_upgrade1 == False:
							global_player.players[customer].has_freezer_upgrade1 = True
							global_player.players[customer].money -= freezer_upgrade_price
							global_player.players[customer].freezer_range_upgrade = 1
					elif y == 3:
						#upgrade laser
						if money >= laser_upgrade_price and global_player.players[customer].has_laser_upgrade1 == False:
							global_player.players[customer].has_laser_upgrade1 = True
							global_player.players[customer].money -= laser_upgrade_price
							game.laser_power_boost += game.laser_additional_power_boost
							#global_player.players[customer].laser_diameter_upgrade = 4
						
					elif y == 4:
						exit_shop = True
				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					exit_shop = True
				# elif event.type == KEYDOWN and event.key == K_ESCAPE:
					# exit = True
					
		return exit		

	def weapon_slots_shop(sefl, screen, game, global_player, customer):
		exit_shop = False
		exit = False
		y = 0
		shop_background = pygame.image.load('data/images/backgrounds/shop_background.png').convert()
		
		font = pygame.font.SysFont("Courier New", 60)
		
		while(exit_shop == False and exit == False):
			money = global_player.players[customer].money
			screen.fill((0, 0, 0))
			screen.blit(shop_background, (0, 0))			
		
			title_label = font.render('slots', True, (0, 255, 100))
			
			slot1_label = font.render('slot1', True, (0, 255, 100))
			
			if global_player.players[customer].slot1 == 0:
				slot1_label = font.render('freezer', True, (0, 255, 100))
			elif global_player.players[customer].slot1 == 1:
				slot1_label = font.render('long range freezer', True, (0, 255, 100))
			
			slot2_label = font.render('slot2', True, (0, 255, 100))
			slot3_label = font.render('slot3', True, (0, 255, 100))
			slot4_label = font.render('slot4', True, (0, 255, 100))
			exit_shop_label = font.render('return', True, (0, 255, 100))

			screen.blit(title_label, (150, 150))
			screen.blit(slot1_label, (150, 250))
			screen.blit(slot2_label, (150, 350))
			screen.blit(slot3_label, (150, 450))
			screen.blit(slot4_label, (150, 550))
			screen.blit(exit_shop_label, (150, 650))
			
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
						if global_player.players[customer].slot1 == 0:
							global_player.players[customer].slot1 = 1
						elif global_player.players[customer].slot1 == 1:
							global_player.players[customer].slot1 = 0
					elif y == 1:
						pass
					elif y == 2:
						pass
					elif y == 3:
						pass
					elif y == 4:
						exit_shop = True
				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					exit_shop = True
					
		return exit
	
	def experience_shop(self, screen, game, global_player, customer):
		exit_shop = False
		exit = False
		y = 0
		shop_background = pygame.image.load('data/images/backgrounds/shop_background.png').convert()
		
		font = pygame.font.SysFont("Courier New", 60)
		
		while(exit_shop == False and exit == False):
			money = global_player.players[customer].money
			screen.fill((0, 0, 0))
			screen.blit(shop_background, (0, 0))			
		
			#medkit_xp_price = 50
			medkit_xp_price = 40
			#speed_xp_price = 50
			speed_xp_price = 40
			
			#additional_energy = 2
			additional_energy = 4
			#additional_speed = 1
			additional_speed = 2
		
			title_label = font.render('experience: ' + str(global_player.players[customer].experience), True, (0, 255, 100))
			
			life_label = font.render('+' + str(additional_energy) + ' to medkit [' + str(medkit_xp_price) + ' xp]', True, (0, 255, 100))
			speed_label = font.render('+' + str(additional_speed) + ' to speed  [' + str(speed_xp_price) + ' xp]', True, (0, 255, 100))			
			exit_shop_label = font.render('return', True, (0, 255, 100))

			screen.blit(title_label, (150, 150))
			screen.blit(life_label, (150, 250))
			screen.blit(speed_label, (150, 350))
			screen.blit(exit_shop_label, (150, 450))
			
			pygame.draw.rect(screen, (0, 255, 100), (100, 240 + y * 100, 1050, 100), 10)

			pygame.display.flip()
			
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_DOWN:
					if y < 2:
						y += 1
				elif event.type == KEYDOWN and event.key == K_UP:
					if y > 0:
						y -= 1
				elif event.type == KEYDOWN and event.key == K_RETURN:
					if y == 0:
						#add +1 to armor
						if global_player.players[customer].experience >= medkit_xp_price:
							global_player.players[customer].experience -= medkit_xp_price
							global_player.players[customer].add_energy_booster += additional_energy
					elif y == 1:
						#add +1 to speed
						if global_player.players[customer].experience >= speed_xp_price:
							global_player.players[customer].experience -= speed_xp_price
							global_player.players[customer].base_speed += additional_speed
							global_player.players[customer].player_speed += additional_speed
					elif y == 2:
						exit_shop = True
				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					exit_shop = True
					
		return exit

	def ammo_shop(self, screen, game, global_player, customer):
		exit_shop = False
		exit = False
		y = 0
		shop_background = pygame.image.load('data/images/backgrounds/shop_background.png').convert()
		
		font = pygame.font.SysFont("Courier New", 60)
		
		self.flamethrower_ammo = global_player.players[customer].get_ammo('flamethrower')
		self.laser_ammo = global_player.players[customer].get_ammo('laser')
		self.plasma_ammo = global_player.players[customer].get_ammo('plasma')
		self.freezer_ammo = global_player.players[customer].get_ammo('freezer')
		
		while(exit_shop == False and exit == False):
			money = global_player.players[customer].money
			screen.fill((0, 0, 0))
			screen.blit(shop_background, (0, 0))			
		
			money_label = font.render('money: ' + str(money), True, (0, 255, 100))
			
			if money >= 5000:
				gasoline_label = font.render('gasoline:     5000 (' + str(self.flamethrower_ammo) + '/' + str(global_player.players[customer].get_max_ammo("flamethrower")) + ')', True, (0, 255, 100))
			else:
				gasoline_label = font.render('gasoline:     5000 (' + str(self.flamethrower_ammo) + '/' + str(global_player.players[customer].get_max_ammo('flamethrower')) + ')', True, (150, 0, 0))
						
			if money >= 5000:
				cell_label       = font.render('plasma cells: 5000 (' + str(self.plasma_ammo) + '/' + str(global_player.players[customer].get_max_ammo('plasma')) + ')', True, (0, 255, 100))
			else:
				cell_label       = font.render('plasma cells: 5000 (' + str(self.plasma_ammo) + '/' + str(global_player.players[customer].get_max_ammo('plasma')) + ')', True, (150, 0, 0))
			
			if money >= 5000:
				refrigerant_label      = font.render('refrigerant:  5000 (' + str(self.freezer_ammo) + '/' + str(global_player.players[customer].get_max_ammo('freezer')) + ')', True, (0, 255, 100))
			else:
				refrigerant_label      = font.render('refrigerant:  5000 (' + str(self.freezer_ammo) + '/' + str(global_player.players[customer].get_max_ammo('freezer')) + ')', True, (150, 0, 0))
			
			exit_shop_label = font.render('return', True, (0, 255, 100))
			screen.blit(money_label, (150, 150))
			screen.blit(gasoline_label, (150, 250))
			screen.blit(cell_label, (150, 350))
			screen.blit(refrigerant_label, (150, 450))
			screen.blit(exit_shop_label, (150, 550))
			
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
						#upgrade flamethrower
						if money >= 5000 and self.flamethrower_ammo < global_player.players[customer].get_max_ammo('flamethrower'):
							self.flamethrower_ammo += 50
							global_player.players[customer].money -= 5000
							global_player.players[customer].add_ammo('flamethrower', 100)
							if self.flamethrower_ammo > global_player.players[customer].get_max_ammo('flamethrower'):
								self.flamethrower_ammo = global_player.players[customer].get_max_ammo('flamethrower')
					elif y == 1:
						#plasma
						if money >= 5000 and self.plasma_ammo < global_player.players[customer].get_max_ammo('plasma'):
							self.plasma_ammo += 5
							global_player.players[customer].money -= 5000
							global_player.players[customer].add_ammo('plasma', 10)
							if self.plasma_ammo > global_player.players[customer].get_max_ammo('plasma'):
								self.plasma_ammo = global_player.players[customer].get_max_ammo('plasma')
					elif y == 2:
						#freezer
						if money >= 5000 and self.freezer_ammo < global_player.players[customer].get_max_ammo('freezer'):
							self.freezer_ammo += 25
							global_player.players[customer].money -= 5000
							global_player.players[customer].add_ammo('freezer', 50)
							if self.freezer_ammo > global_player.players[customer].get_max_ammo('freezer'):
								self.freezer_ammo = global_player.players[customer].get_max_ammo('freezer')
					elif y == 3:
						exit_shop = True
				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					exit_shop = True
				# elif event.type == KEYDOWN and event.key == K_ESCAPE:
					# exit = True
					
		return exit
		
	def buy(self, screen, game, global_player, customer):
		exit_shop = False
		exit = False
		y = 0
		shop_background = pygame.image.load('data/images/backgrounds/shop_background.png').convert()

		font = pygame.font.SysFont("Courier New", 60)
		
		self.flamethrower_ammo = global_player.players[customer].get_ammo('flamethrower')
		self.laser_ammo = global_player.players[customer].get_ammo('laser')
		self.plasma_ammo = global_player.players[customer].get_ammo('plasma')
		self.freezer_ammo = global_player.players[customer].get_ammo('freezer')
		
		while(exit_shop == False and exit == False):
			money = global_player.players[customer].money
			screen.fill((0, 0, 0))
			screen.blit(shop_background, (0, 0))

			money_label = font.render('money: ' + str(money), True, (0, 255, 100))
			armor_upgrades_label = font.render('armor upgrades', True, (0, 255, 100))
			weapon_upgrades_label = font.render('weapon upgrades', True, (0, 255, 100))
			weapon_slots_label = font.render('weapon slots', True, (0, 255, 100))
			experience_label = font.render('experience', True, (0, 255, 100))
			ammo_shop_label = font.render('ammo shop', True, (0, 255, 100))
			exit_shop_label = font.render('return', True, (0, 255, 100))
			screen.blit(money_label, (150, 150))
			screen.blit(armor_upgrades_label, (150, 250))
			screen.blit(weapon_upgrades_label, (150, 350))
			screen.blit(weapon_slots_label, (150, 450))
			screen.blit(experience_label, (150, 550))
			screen.blit(ammo_shop_label, (150, 650))
			screen.blit(exit_shop_label, (150, 750))
			
			pygame.draw.rect(screen, (0, 255, 100), (100, 240 + y * 100, 1050, 100), 10)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_DOWN:
					if y < 5:
						y += 1
				elif event.type == KEYDOWN and event.key == K_UP:
					if y > 0:
						y -= 1
				elif event.type == KEYDOWN and event.key == K_RETURN:
					if y == 0:
						exit = self.armor_shop(screen, game, global_player, customer)
					elif y == 1:
						exit = self.weapon_shop(screen, game, global_player, customer)
					elif y == 2:
						exit = self.weapon_slots_shop(screen, game, global_player, customer)
					elif y == 3:
						exit = self.experience_shop(screen, game, global_player, customer)
					elif y == 4:
						exit = self.ammo_shop(screen, game, global_player, customer)
					elif y == 5:
						exit_shop = True
				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					exit_shop = True
				# elif event.type == KEYDOWN and event.key == K_ESCAPE:
					# exit = True
					
		return exit
		
	def enter_shop(self, screen, game, global_player):

		pygame.mixer.music.stop()
		pygame.mixer.music.load('data/music/shop.ogg')
		pygame.mixer.music.play()
		shop_background = pygame.image.load('data/images/backgrounds/shop_background.png').convert()
		
		exit_shop = False
		exit = False
		y = 0
		
		font = pygame.font.SysFont("Courier New", 60)
		
		while(exit_shop == False and exit == False):
			screen.fill((0, 0, 0))
			screen.blit(shop_background, (0, 0))
			
			money_label = font.render('money: ' + str(global_player.players['nash'].money), True, (0, 255, 100))
			
			if game.number_of_players > 1:
				money_label = font.render('money: ' + str(global_player.players['nash'].money + global_player.players['george'].money), True, (0, 255, 100))
			if game.number_of_players > 2:
				money_label = font.render('money: ' + str(global_player.players['nash'].money + global_player.players['george'].money + global_player.players['james'].money), True, (0, 255, 100))
				
			armor_upgrades_label = font.render('Nash upgrades', True, (0, 255, 100))
			
			if game.number_of_players > 1:
				weapon_upgrades_label = font.render('George upgrades', True, (0, 255, 100))
			else:
				weapon_upgrades_label = font.render('George upgrades', True, (0, 80, 0))
				
			if game.number_of_players > 2:
				other_upgrades_label = font.render('James upgrades', True, (0, 255, 100))
			else:
				other_upgrades_label = font.render('James upgrades', True, (0, 80, 0))
				
			exit_shop_label = font.render('exit shop', True, (0, 255, 100))
			screen.blit(money_label, (150, 150))
			screen.blit(armor_upgrades_label, (150, 250))
			screen.blit(weapon_upgrades_label, (150, 350))
			screen.blit(other_upgrades_label, (150, 450))
			screen.blit(exit_shop_label, (150, 550))
			
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
						exit = self.buy(screen, game, global_player, 'nash')
					elif y == 1:
						if game.number_of_players > 1:
							exit = self.buy(screen, game, global_player, 'george')
					elif y == 2:
						if game.number_of_players > 2:
							exit = self.buy(screen, game, global_player, 'james')
					elif y == 3:
						exit_shop = True
						time.sleep(0.2)
						pygame.mixer.music.stop()
				# elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					# exit_shop = True
				# elif event.type == KEYDOWN and event.key == K_ESCAPE:
					# exit = True
		
		screen.fill((0, 0, 0))
		loading_label = font.render('Loading...', True, (0, 255, 100))
		screen.blit(loading_label, (400, 300))
		pygame.display.flip()
		
