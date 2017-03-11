from Functions import *

#================================== FLAMETHROWER =====================================================
		
def flamethrower(threadName, delay, screen, flamethrower_sound, x, y, angle, ammo, monster, game, global_player, player_name):
	disable = 10
	
	flamethrower_sound.play()
	if ammo['flamethrower'] > 0:
		
		for j in range(1, 2 + global_player.players[player_name].flamethrower_range_upgrade):
			# for i in range(0, 35 + global_player.players[player_name].flamethrower_range_upgrade * 3):
			for i in range(0, int((global_player.players[player_name].ammo['flamethrower']) / 500 + 5 + global_player.players[player_name].flamethrower_range_upgrade * 3)):
				if ammo['flamethrower'] > 0:
					# ammo['flamethrower'] -= 1
					ammo['flamethrower'] -= 0.3 #effectiveness of flamethrower
					# if smaller value then slower gasoline consumption
			
					angle_conv = convert_angle(angle)

					#draw flames
					random_distortion = random.uniform(-0.2, 0.2)
					new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * (i + 2))
					new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * (i + 2))

					if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
						if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
							if disable > 0:
								disable -= 1
							else:
								return

					# red
					#pygame.draw.circle(screen, (70 + i * 3, 0, 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
					pygame.draw.circle(screen, (236, 0, 6), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)

					# pygame.draw.circle(screen, (70 + int(i / 5.0), 0, 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
					# pygame.draw.circle(screen, (70 + int(i / 2), 0, 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
					# pygame.draw.circle(screen, (70 + i, 0, 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
					
					monster.kill_monster(game, new_x, new_y, i, 'flamethrower', global_player, player_name)
					
					time.sleep(delay * j)
					
					random_distortion = random.uniform(-0.2, 0.2)
					new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * (i + 2))
					new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * (i + 2))
					
					if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
						if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
							if disable > 0:
								disable -= 1
							else:
								return
					
					# yellow
					#pygame.draw.circle(screen, (255 - i * 2, 70 + i * 3, 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
					pygame.draw.circle(screen, (255, 228, 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)

					# pygame.draw.circle(screen, (255 - int(i * 3.0), 70 + int(i / 5.0), 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
					# pygame.draw.circle(screen, (255 - int(i/2), 70 + int(i/2), 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
					# pygame.draw.circle(screen, (255 - i, 70 + i, 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
					
					monster.kill_monster(game, new_x, new_y, i, 'flamethrower', global_player, player_name)
					
					time.sleep(delay * j)
					
					if global_player.players[player_name].has_flamethrower_upgrade1 == True:
						random_distortion = random.uniform(-0.2, 0.2)
						new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * (i + 2))
						new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * (i + 2))
						
						if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
							if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
								if disable > 0:
									disable -= 1
								else:
									return
						
						pygame.draw.circle(screen, (255 - i * 3, 0, 70 + i * 3), (new_x, new_y), 7 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
						
						monster.kill_monster(game, new_x, new_y, i, 'flamethrower', global_player, player_name)
						
						time.sleep(delay * j)
	else:
		for j in range(1, 2 + global_player.players[player_name].flamethrower_range_upgrade):
			# for i in range(0, 35 + global_player.players[player_name].flamethrower_range_upgrade * 3):
			for i in range(0, 1 + global_player.players[player_name].flamethrower_range_upgrade * 3):
			
				angle_conv = convert_angle(angle)

				#draw flames
				random_distortion = random.uniform(-0.2, 0.2)
				new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * (i + 2))
				new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * (i + 2))

				if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
					if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
						if disable > 0:
							disable -= 1
						else:
							return

				pygame.draw.circle(screen, (70 + i * 3, 0, 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
				
				monster.kill_monster(game, new_x, new_y, i, 'flamethrower', global_player, player_name)
				
				time.sleep(delay * j)
				
				random_distortion = random.uniform(-0.2, 0.2)
				new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * (i + 2))
				new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * (i + 2))
				
				if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
					if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
						if disable > 0:
							disable -= 1
						else:
							return
				
				pygame.draw.circle(screen, (255 - i * 2, 100 + i * 3, 0), (new_x, new_y), 5 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
				
				monster.kill_monster(game, new_x, new_y, i, 'flamethrower', global_player, player_name)
				
				time.sleep(delay * j)
				
				if global_player.players[player_name].has_flamethrower_upgrade1 == True:
					random_distortion = random.uniform(-0.2, 0.2)
					new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * (i + 2))
					new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * (i + 2))
					
					if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
						if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
							if disable > 0:
								disable -= 1
							else:
								return
					
					pygame.draw.circle(screen, (255 - i * 3, 0, 100 + i * 3), (new_x, new_y), 7 + i + global_player.players[player_name].flamethrower_range_upgrade, 0)
					
					monster.kill_monster(game, new_x, new_y, i, 'flamethrower', global_player, player_name)
					
					time.sleep(delay * j)
				
#==================================== freezer ==========================================================================
	
def freezer(threadName, delay, screen, freezer_sound, x, y, angle, ammo, monster, game, global_player, player_name):
	disable = 10
	
	if ammo['freezer'] > 0:
		freezer_sound.play()
	for i in range(2, 5 + global_player.players[player_name].freezer_range_upgrade):
		if ammo['freezer'] > 0:
			ammo['freezer'] -= 0.5
			for angl in range(0, 18):
				
				random_distortion = random.uniform(-0.2, 0.2)
										
				new_x = x + 32 + int(math.sin(angl * 20 * random_distortion) * 25 * i)
				new_y = y + 32 + int(math.cos(angl * 20 * random_distortion) * 25 * i)
				
				if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
					if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
						if disable > 0:
							disable -= 1
						else:
							return
						
				random_size = random.randint(5, 16)
				#pygame.draw.circle(screen, (0, 0, 100 + i * 3), (new_x, new_y), 110 + global_player.players[player_name].freezer_range_upgrade * 40 - i * 25, random.randint(1, 6))
				pygame.draw.circle(screen, (0, 0, 100 + i * 3), (new_x, new_y), 100 + global_player.players[player_name].freezer_range_upgrade * 40 - i * 25, random.randint(1, 6))
						
				monster.kill_monster(game, new_x, new_y, i, 'freezer', global_player, player_name)
						
				new_x = x + 32 + int(math.sin(angl * 20 * random_distortion) * 25 * i)
				new_y = y + 32 + int(math.cos(angl * 20 * random_distortion) * 25 * i)

				if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
					if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
						if disable > 0:
							disable -= 1
						else:
							return
					
				random_size = random.randint(5, 16)
				#pygame.draw.circle(screen, (0, 100 + i * 5, 255 - i * 5), (new_x, new_y), 110 + global_player.players[player_name].freezer_range_upgrade * 40 - i * 25, random.randint(1, 6))
				pygame.draw.circle(screen, (0, 100 + i * 5, 255 - i * 5), (new_x, new_y), 100 + global_player.players[player_name].freezer_range_upgrade * 40 - i * 25, random.randint(1, 6))
						
				monster.kill_monster(game, new_x, new_y, i, 'freezer', global_player, player_name)
				
				#time.sleep(delay)
	
#==================================== long range freezer ============================================================================	
def long_range_freezer(threadName, delay, screen, freezer_sound, x, y, angle, ammo, monster, game, global_player, player_name):
	disable = 10
	
	freezer_sound.play()
	if ammo['freezer'] > 0:
		
		for j in range(1, 5):
			for i in range(1, 50):
				if ammo['freezer'] > 0:
					ammo['freezer'] -= 0.1
			
					angle_conv = convert_angle(angle)

					#draw ice circles
					random_size = random.randint(6, 12)
					random_distortion = random.uniform(-0.1, 0.1)
					new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * (i + 2))
					new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * (i + 2))

					if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
						if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
							if disable > 0:
								disable -= 1
							else:
								return

					pygame.draw.circle(screen, (0, 100 + i * 3, 255 - i * 3), (new_x, new_y), random_size, random.randint(3, 6))
					
					monster.kill_monster(game, new_x, new_y, i, 'freezer', global_player, player_name)
					
					time.sleep(delay * j)
					
#=============================== PLASMA ==========================================================================
				
def plasma(threadName, delay, screen, plasma_sound, x, y, angle, ammo, monster, game, global_player, player_name):
	disable = 10
		
	if ammo['plasma'] > 0:
		ammo['plasma'] -= 0.5
		angle_conv = convert_angle(angle)

		for i in range(2, 20 + global_player.players[player_name].plasma_range_upgrade):
			#draw plasma
			for j in range(1, 2):
				random_distortion = random.uniform(-0.15 * global_player.players[player_name].plasma_range_upgrade, 0.15 * global_player.players[player_name].plasma_range_upgrade)
				new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 25 * i)
				new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 25 * i)
				
				if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
					if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
						if disable > 0:
							disable -= 1
						else:
							return

				random_size = random.randint(5, 21)
				# pygame.draw.circle(screen, (255, 100 + i * 3, 0), (new_x, new_y), 22 - i, 0)
				pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (new_x, new_y), 22 - i, 0)
				
				monster.kill_monster(game, new_x, new_y, 100, 'plasma', global_player, player_name)
				
			time.sleep(delay)
				
			for j in range(1, 2):
				random_distortion = random.uniform(-0.15 * global_player.players[player_name].plasma_range_upgrade, 0.15 * global_player.players[player_name].plasma_range_upgrade)
				new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 25 * i)
				new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 25 * i)

				if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
					if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
						if disable > 0:
							disable -= 1
						else:
							return
					
				random_size = random.randint(5, 16)
				# pygame.draw.circle(screen, (255 - i * 3, 0, 0), (new_x, new_y), 22 - i, 0)
				pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (new_x, new_y), 22 - i, 0)
					
				monster.kill_monster(game, new_x, new_y, 100, 'plasma', global_player, player_name)
				
			time.sleep(delay)
		plasma_sound.play()
		
	
				
#=============================== LASER ==========================================================================
			
def laser(threadName, delay, screen, laser_sound, x, y, angle, ammo, monster, game, global_player, player_name):
	disable = 10
	
	# if ammo['laser'] > 0 or global_player.players[player_name].laser_time_upgrade == True:
		# laser_sound.play()
		
		# if ammo['laser'] > 0:
			# ammo['laser'] -= 1
		
	if ammo['laser'] > 0:
		laser_sound.play()
		
		if ammo['laser'] > 0:
			ammo['laser'] -= 1
			
		angle_conv = convert_angle(angle)
				
		for i in range(0, 400):
			new_x = x + 32 + int(math.sin(angle_conv) * (i + 3) * 5)
			new_y = y + 32 + int(math.cos(angle_conv) * (i + 3) * 5)
			
			if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
				if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
					if disable > 0:
						disable -= 1
					else:
						return
			
			# if global_player.players[player_name].laser_time_upgrade > 0:
				# pygame.draw.circle(screen, (0, 0, 255), (new_x, new_y), 2 + global_player.players[player_name].laser_diameter_upgrade + global_player.players[player_name].laser_time_upgrade)
				
			# else:
				# pygame.draw.circle(screen, (255, 0, 0), (new_x, new_y), 2 + global_player.players[player_name].laser_diameter_upgrade)

			pygame.draw.circle(screen, (255, 0, 0), (new_x, new_y), 1 + int(game.laser_power / 30.0))
			
			monster.kill_monster(game, new_x, new_y, 1 + int(game.laser_power / 10.0), 'laser', global_player, player_name)
						
			# monster.kill_monster(game, new_x, new_y, 20 + 5 * global_player.players[player_name].laser_diameter_upgrade, 'laser', global_player, player_name)
			
#================================ VORTEX ==========================================================================
		
def vortex(threadName, delay, screen, x, y, angle, ammo, monster, game, global_player, player_name):
	if global_player.players[player_name].has_enhanced_vortex_upgrade == False:
		for i in range(0, 20):
		
			for angl in range(0, 100):
				#draw vortex
				random_distortion = random.uniform(-0.2, 0.2)
				new_x = x + int(math.sin(angl * 3 + random_distortion) * 30 * i)
				new_y = y + int(math.cos(angl * 3 + random_distortion) * 30 * i)
				
				random_size = random.randint(10, 21)
				pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (new_x, new_y), random_size, 0)
					
				monster.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, player_name)
				
				random_distortion = random.uniform(-0.2, 0.2)
				new_x = x + int(math.sin(angl * 3 + random_distortion) * 30 * i)
				new_y = y + int(math.cos(angl * 3 + random_distortion) * 30 * i)
				
				random_size = random.randint(15, 26)
				pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (new_x, new_y), random_size, 0)
						
				monster.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, player_name)
				
			time.sleep(0.01)

	else:
		for i in range(0, 50):
		
			for angl in range(0, 100):
				#draw vortex
				random_distortion = random.uniform(-0.2, 0.2)
				new_x = x + int(math.sin(angl * 3 + random_distortion) * 30 * i)
				new_y = y + int(math.cos(angl * 3 + random_distortion) * 30 * i)
				
				random_size = random.randint(10, 21)
				pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (new_x, new_y), random_size, 0)
					
				monster.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, player_name)
				
				random_distortion = random.uniform(-0.2, 0.2)
				new_x = x + int(math.sin(angl * 3 + random_distortion) * 30 * i)
				new_y = y + int(math.cos(angl * 3 + random_distortion) * 30 * i)
				
				random_size = random.randint(15, 26)
				pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (new_x, new_y), random_size, 0)
						
				monster.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, player_name)
				
			time.sleep(0.01)
		

#================================ ROBOT WEAPON ==========================================================================		
		
def robot_weapon(threadName, delay, screen, laser_sound, x, y, monster, game, global_player, pain_sound):
	disable = 10
	
	laser_sound.play()

	angle_conv = random.randint(0, 2 * math.pi)
	
	for i in range(0, 40):
		
		for j in range(1, 3):
			# random_distortion = random.uniform(-0.15)
			# new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * i)
			new_x = x + 32 + int(math.sin(angle_conv) * 10 * i)
			# new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * i)
			new_y = y + 32 + int(math.cos(angle_conv) * 10 * i)
			
			if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
				if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
					if disable > 0:
						disable -= 1
					else:
						return

			random_size = random.randint(5, 10)
			pygame.draw.circle(screen, (100 + i * 3, 0, 0), (new_x, new_y), random_size, random.randint(0, random_size))
			
			monster.kill_player(game, new_x, new_y, i, 'robot_weapon', global_player, pain_sound, screen)
			
		time.sleep(delay)
			
		for j in range(1, 3):
			# random_distortion = random.uniform(-0.15)
			# new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * i)
			new_x = x + 32 + int(math.sin(angle_conv) * 10 * i)
			# new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * i)
			new_y = y + 32 + int(math.cos(angle_conv) * 10 * i)
			
			if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
				if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
					if disable > 0:
						disable -= 1
					else:
						return
			
			random_size = random.randint(5, 10)
			pygame.draw.circle(screen, (255 - i * 3, 0 , 0), (new_x, new_y), random_size, random.randint(0, random_size))
				
			monster.kill_player(game, new_x, new_y, i, 'robot_weapon', global_player, pain_sound, screen)
			
		time.sleep(delay)

#================================ BOSS WEAPON ====================================================================		
		
def boss_weapon(threadName, delay, screen, laser_sound, x, y, monster, game, global_player, pain_sound):
	disable = 10
	
	laser_sound.play()

	angle_conv = random.randint(0, 2 * math.pi)
	
	# for i in range(0, 75):
	for i in range(0, game.boss_fire_range):
		
		# for j in range(1, 3):
		for j in range(1, 5):
			# random_distortion = random.uniform(-0.15)
			# new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * i)
			new_x = x + game.boss.size / 2 + int(math.sin(angle_conv) * 10 * i)
			# new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * i)
			new_y = y + game.boss.size / 2 + int(math.cos(angle_conv) * 10 * i)
			
			if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
				if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
					if disable > 0:
						disable -= 1
					else:
						return

			random_size = random.randint(15, 30)
			pygame.draw.circle(screen, (100 + i * 2, 100 + i * 2, 0), (new_x, new_y), random_size, random.randint(0, random_size))
			
			monster.kill_player(game, new_x, new_y, i, 'boss_weapon', global_player, pain_sound, screen)
			
		time.sleep(delay)
			
		# for j in range(1, 3):
		for j in range(1, 5):
			# random_distortion = random.uniform(-0.15)
			# new_x = x + 32 + int(math.sin(angle_conv + random_distortion) * 10 * i)
			new_x = x + game.boss.size / 2 + int(math.sin(angle_conv) * 10 * i)
			# new_y = y + 32 + int(math.cos(angle_conv + random_distortion) * 10 * i)
			new_y = y + game.boss.size / 2 + int(math.cos(angle_conv) * 10 * i)
			
			if new_x - game.x - 32 >= 0 and new_y - game.y - 32 >= 0:
				if game.pixel_table[new_x - game.x - 32][new_y - game.y - 32] != 0:
					if disable > 0:
						disable -= 1
					else:
						return
			
			random_size = random.randint(10, 35)
			pygame.draw.circle(screen, (255 - i * 2, 0, 0), (new_x, new_y), random_size, random.randint(0, random_size))
				
			monster.kill_player(game, new_x, new_y, i, 'boss_weapon', global_player, pain_sound, screen)
			
		time.sleep(delay)

