import pygame, math, sys, time, _thread, os, random
from pygame.locals import *
from numpy import *
from tableMazeModel import *
from Game import *
from Player import *
from Monster import *

import ctypes

from Point import *
from Mass import *

from Bonus import *
from Players import *
from Functions import *
from Menu import *
from Shop import *
from Weapons import *
from Labirynth import *
from Boss1 import *
from Boss2 import *
from Boss3 import *
from Boss4 import *
from Boss5 import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# resolution = (640, 480)		
# resolution = (1024, 576)
# resolution = (1152, 648)
# resolution = (1280, 1024)

#resolution = (1366, 768)
resolution = (1920, 1080)

#resolution = (2560, 1440)
#resolution = (3440, 1440)
#resolution = (3840, 2160)

#user32 = ctypes.windll.user32
#width = user32.GetSystemMetrics(0)
#height = user32.GetSystemMetrics(1)
#print "width = ", width
#print "height = ", height

#resolution = (width, height) # auto

#==================================== INITIALIZE GAME =================================================
	
game = Game(resolution)
game.level = 1
game.next_level = False
game.bonus_loop = 0

for arg in sys.argv:
	if arg == '1':
		game.number_of_players = 1
	elif arg == '2':
		game.number_of_players = 2
	elif arg == '3':
		game.number_of_players = 3
		
	# if arg == 'np':
		# game.nash_pad = True
	# elif arg == 'nk':
		# game.nash_pad = False
		
	# if arg == 'gp':
		# game.george_pad = True
	# elif arg == 'gk':
		# game.george_pad = False

if game.difficulty == 'easy':
	game.safety_border = 150
elif game.difficulty == 'medium':
	game.safety_border = 150
elif game.difficulty == 'hard':
	game.safety_border = 150
	
pygame.init()
pygame.mouse.set_visible(False)

if game.mute == False:
	pygame.mixer.music.set_volume(1.0)
elif game.mute == True:
	pygame.mixer.music.set_volume(0.0)

joy1 = None
joy2 = None

#initialize pad/joystick
if game.nash_pad == True:
	joy1 = pygame.joystick.Joystick(0)
	joy1.init()

if game.number_of_players > 1 and game.george_pad == True:
	joy2 = pygame.joystick.Joystick(1)
	joy2.init()
	
#test joy1
# print 'Initialized Joystick : %s' % joy1.get_name()
# try:
	# while True:
		# pygame.event.pump()
		# for i in range(0, joy1.get_numaxes()):
			# if joy1.get_axis(i) != 0.00:
				# print 'Axis %i reads %.2f' % (i, joy1.get_axis(i))
				# time.sleep(1.5)
		# for i in range(0, joy1.get_numbuttons()):
			# if joy1.get_button(i) != 0:
				# print 'Button %i reads %i' % (i, joy1.get_button(i))
				# time.sleep(1.5)
# except KeyboardInterrupt:
	# joy1.quit()

#test joy2
# print 'Initialized Joystick : %s' % joy2.get_name()
# try:
	# while True:
		# pygame.event.pump()
		# for i in range(0, joy2..get_numaxes()):
			# if joy2..get_axis(i) != 0.00:
				# print 'Axis %i reads %.2f' % (i, joy2..get_axis(i))
				# time.sleep(1.5)
		# for i in range(0, joy2..get_numbuttons()):
			# if joy2..get_button(i) != 0:
				# print 'Button %i reads %i' % (i, joy2..get_button(i))
				# time.sleep(1.5)
# except KeyboardInterrupt:
	# joy2..quit()

#screen = pygame.display.set_mode(resolution, FULLSCREEN | DOUBLEBUF | HWSURFACE)
#screen = pygame.display.set_mode(resolution, FULLSCREEN | DOUBLEBUF)
screen = pygame.display.set_mode(resolution, FULLSCREEN)

screen.fill((0, 0, 0))
loading_font = pygame.font.SysFont("Courier New", 60)
loading_label = loading_font.render('Loading...', True, (0, 255, 100))
screen.blit(loading_label, (400, 300))
pygame.display.flip()

clock = pygame.time.Clock()

game.pixel_table = zeros( (4000, 4000) )

#pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
#pygame.mixer.init(frequency=44100, size=-16, channels=64, buffer=4096)
pygame.mixer.init(frequency = 44100, size = -16, channels = 8, buffer = 16384)
pygame.mixer.set_num_channels(256)
# pygame.mixer.set_num_channels(1024)

volume = 0.05

# death_sound = load_sound('die.wav')
# death_sound.set_volume(volume)

pain_sound = load_sound('players/pain.ogg')
pain_sound.set_volume(0.1)

spider_death_sound = load_sound('monsters/spider_death.ogg')
gigantula_death_sound = load_sound('monsters/gigantula_death.ogg')
#robot_death_sound = load_sound('monsters/robot_death.wav')
#crane_death_sound = load_sound('monsters/crane_death.wav')
#hunter_death_sound = load_sound('monsters/crane_death.wav')

robot_death_sound = load_sound('monsters/gigantula_death.ogg')
crane_death_sound = load_sound('monsters/gigantula_death.ogg')
hunter_death_sound = load_sound('monsters/gigantula_death.ogg')

# spider_death_sound.set_volume(volume)
spider_death_sound.set_volume(0.7)
gigantula_death_sound.set_volume(1.5)
robot_death_sound.set_volume(0.5)
crane_death_sound.set_volume(0.5)
hunter_death_sound.set_volume(0.5)
laser_sound = load_sound('weapons/laser.ogg')
laser_sound.set_volume(0.3)
flamethrower_sound = load_sound('weapons/flamethrower.ogg')
flamethrower_sound.set_volume(volume)
freezer_sound = load_sound('weapons/freezer.ogg')
freezer_sound.set_volume(volume * 5)
plasma_sound = load_sound('weapons/plasma.ogg')
plasma_sound.set_volume(0.3)
#roar_sound = load_sound('roar.wav')
#roar_sound.set_volume(0.02)
# applause_sound = load_sound('applause.wav')
# applause_sound.set_volume(volume)
vortex_sound = load_sound('weapons/vortex.ogg')
#vortex_sound.set_volume(volume * 10)
vortex_sound.set_volume(4.0)

if game.mute == True:
	spider_death_sound.set_volume(0.0)
	gigantula_death_sound.set_volume(0.0)
	robot_death_sound.set_volume(0.0)
	crane_death_sound.set_volume(0.0)
	hunter_death_sound.set_volume(0.0)
	laser_sound.set_volume(0.0)
	flamethrower_sound.set_volume(0.0)
	freezer_sound.set_volume(0.0)
	plasma_sound.set_volume(0.0)
	roar_sound.set_volume(0.0)
	vortex_sound.set_volume(0.0)
	pain_sound.set_volume(0.0)

# applause_sound_played = False

game.level_type = "arena" #first stage will be "outside", so arena type

game.boss = Boss1(resolution[0] / 2, 300)
game.boss.energy = 0

if game.level_type == "labirynth":
	labirynth = TableMazeModel(rowsNum = game.labirynth_dim_x, colsNum = game.labirynth_dim_y)
	labirynth.genMaze()
	print(str(labirynth))
	# f = open('d:/prg/AlienThreat/logs/labirynth', 'w')
	# # f = open('f:/prg/at/AlienThreat/logs/labirynth', 'w')
	# # print f
	# f.write(str(labirynth))
	# f.close()
	set_labirynth(game, labirynth, game.labirynth_dim_x, game.labirynth_dim_y)
elif game.level_type == "arena":
	pass

game.x = 0
game.y = 0

nash = Player(100, 100, 'data/images/players/nash/nash-0.png', 'data/images/players/nash/nash_pain-0.png', game)
george = Player(200, 100, 'data/images/players/george/george-0.png', 'data/images/players/george/george_pain-0.png', game)
james = Player(100, 200, 'data/images/players/james/james-0.png', 'data/images/players/james/james_pain-0.png', game)
rxvt = Player(200, 200, 'data/images/players/rxvt/rxvt-0.png', 'data/images/players/rxvt/rxvt-0.png', game)

def define_character():
	if game.nash_character == 1: # commando
		nash.base_speed = nash.player_speed = game.commando_speed
		nash.base_armor = nash.armor = game.commando_armor
		
	elif game.nash_character == 2: # robot
		nash.base_speed = nash.player_speed = game.robot_speed
		nash.base_armor = nash.armor = game.robot_armor
		
	elif game.nash_character == 3: # doctor
		nash.base_speed = nash.player_speed = game.doctor_speed
		nash.base_armor = nash.armor = game.doctor_armor
		nash.doctor_energy_regeneration = True
		
	elif game.nash_character == 4: # scientist
		nash.base_speed = nash.player_speed = game.scientist_speed
		nash.base_armor = nash.armor = game.scientist_armor
	
	# george
	if game.george_character == 1: # commando
		george.base_speed = george.player_speed = game.commando_speed
		george.base_armor = george.armor = game.commando_armor
		
	elif game.george_character == 2: # robot
		george.base_speed = george.player_speed = game.robot_speed
		george.base_armor = george.armor = game.robot_armor
		
	elif game.george_character == 3: # doctor
		george.base_speed = george.player_speed = game.doctor_speed
		george.base_armor = george.armor = game.doctor_armor
		george.doctor_energy_regeneration = True
		
	elif game.george_character == 4: # scientist
		george.base_speed = george.player_speed = game.scientist_speed
		george.base_armor = george.armor = game.scientist_armor

	# james
	if game.james_character == 1: # commando
		james.base_speed = james.player_speed = game.commando_speed
		james.base_armor = james.armor = game.commando_armor
		
	elif game.james_character == 2: # robot
		james.base_speed = james.player_speed = game.robot_speed
		james.base_armor = james.armor = game.robot_armor
		
	elif game.james_character == 3: # doctor
		james.base_speed = james.player_speed = game.doctor_speed
		james.base_armor = james.armor = game.doctor_armor
		james.doctor_energy_regeneration = True
		
	elif game.james_character == 4: # scientist
		james.base_speed = james.player_speed = game.scientist_speed
		james.base_armor = james.armor = game.scientist_armor


define_character()

background_earth = pygame.image.load('data/images/backgrounds/earth.jpg').convert()
background_moon = pygame.image.load('data/images/backgrounds/moon.png').convert()
background_mars = pygame.image.load('data/images/backgrounds/mars.png').convert()
background_venus = pygame.image.load('data/images/backgrounds/venus.png').convert()
background_neptune = pygame.image.load('data/images/backgrounds/neptune.png').convert()

surface = background_earth

game.medkit_model = pygame.image.load('data/images/powerups/medkit.png')
game.gasoline_model = pygame.image.load('data/images/powerups/gasoline.png')
game.refrigerant_model = pygame.image.load('data/images/powerups/refrigerant.png')
game.laser_model = pygame.image.load('data/images/powerups/laser.png')
game.plasma_model = pygame.image.load('data/images/powerups/plasma.png')
game.vortex_model = pygame.image.load('data/images/powerups/vortex.png')
game.money_green_model = pygame.image.load('data/images/powerups/money_green.png')
game.money_yellow_model = pygame.image.load('data/images/powerups/money_yellow.png')

game.blue_key_model = pygame.image.load('data/images/items/blue_key.png')
game.red_key_model = pygame.image.load('data/images/items/red_key.png')
game.green_key_model = pygame.image.load('data/images/items/green_key.png')
game.yellow_key_model = pygame.image.load('data/images/items/yellow_key.png')

alien_egg = pygame.image.load('data/images/monsters/alien_eggs/alien_egg.png')

floor = pygame.image.load('data/images/floors/nasa_hq_floor.png').convert()
wall1 = pygame.image.load('data/images/walls/nasa_hq_wall.png').convert()
wall2 = pygame.image.load('data/images/walls/moon_base_wall.png').convert()
wall3 = pygame.image.load('data/images/walls/mars_colony_wall.png').convert()
wall4 = pygame.image.load('data/images/walls/alpha_labs_wall.png').convert()
wall5 = pygame.image.load('data/images/walls/neptune_corridors_wall.png').convert()

mass1 = Mass(random.randint(200, game.map_size_x - 200), random.randint(200, game.map_size_y - 200 - game.screen_bottom))
mass2 = Mass(random.randint(200, game.map_size_x - 200), random.randint(200, game.map_size_y - 200 - game.screen_bottom))

monster = Monster()

for i in range(0, game.number_of_spiders):
	monster.add_spider(game)
		
for i in range(0, game.number_of_gigantulas):
	monster.add_gigantula(game)
	
for i in range(0, game.number_of_robots):
	monster.add_robot(game)
	
for i in range(0, game.number_of_cranes):
	monster.add_crane(game)
	
for i in range(0, game.number_of_hunters):
	monster.add_hunter(game)
	
game_loop = 0
nash_regeneration_loop = 0
george_regeneration_loop = 0
james_regeneration_loop = 0
nash_ff_regeneration_loop = 0
george_ff_regeneration_loop = 0
james_ff_regeneration_loop = 0
chase_loop = 0
robot_fire_loop = 0

title_screen = pygame.image.load('data/images/title_screen/title_screen.png')
end_screen = pygame.image.load('data/images/end_screen/end_screen.png')
game_over_screen = pygame.image.load('data/images/end_screen/game_over.png')

pygame.mixer.music.load('data/music/intro.ogg')
pygame.mixer.music.play()

game.when_new_bonus = random.randint(game.new_bonus_min_time, game.new_bonus_max_time)	

#add "solid" objects
#alien eggs
if game.level_type == "arena":
	add_object(game, 300, 400, 48, 48)	
	add_object(game, 320, 440, 48, 48)	
	add_object(game, 370, 400, 48, 48)	
	add_object(game, 800, 600, 48, 48)	
	add_object(game, 820, 690, 48, 48)	
	add_object(game, 970, 650, 48, 48)	

	w1 = (600, 400)
	w2 = (664, 400)
	w3 = (472, 400)
	w4 = (536, 400)
	w5 = (472, 464)
	w6 = (664, 464)
	w7 = (472, 528)
	w8 = (664, 528)

	#walls
	add_object(game, w1[0], w1[1], 64, 64)
	add_object(game, w2[0], w2[1], 64, 64)	
	add_object(game, w3[0], w3[1], 64, 64)
	add_object(game, w4[0], w4[1], 64, 64)
	add_object(game, w5[0], w5[1], 64, 64)
	add_object(game, w6[0], w6[1], 64, 64)
	add_object(game, w7[0], w7[1], 64, 64)
	add_object(game, w8[0], w8[1], 64, 64)

# add_object(game, resolution[0], resolution[1] - 64 - 30, 64, 64)

elif game.level_type == "labirynth":
	#add bonuses
	game.bonuses = []
	game.bonus_count = 0

	for game.bonus_count in range(0, game.bonuses_per_level):
		#remember to increase this after adding new bonus to the game !!!
		which_one = random.randint(0, 8)
		
		if which_one == 5: #vortex
			game.add_new_bonus(which_one, random.randint(150, game.map_size_x - 150), random.randint(150, game.map_size_y - 150 - game.screen_bottom), 100)
		elif which_one == 7: #yellow money
			game.add_new_bonus(which_one, random.randint(150, game.map_size_x - 150), random.randint(150, game.map_size_y - 150 - game.screen_bottom), 100)
		else: #all other bonuses
			game.add_new_bonus(which_one, random.randint(150, game.map_size_x - 150), random.randint(150, game.map_size_y - 150 - game.screen_bottom), 500)

#load start and exit places for labirynth mode
start_place = pygame.image.load('data/images/textures/start.png')
exit_place = pygame.image.load('data/images/textures/exit.png')
# start_place_x = random.randint(0, game.labirynth_dim_x)
# start_place_y = random.randint(0, game.labirynth_dim_y)

exit_place_x = 0
exit_place_y = 0

# Create a font
font = pygame.font.SysFont("Comic Sans MS", 20)
story_font = pygame.font.SysFont("Comic Sans MS", 30)

while exit_place_x == 0 and exit_place_y == 0:
	exit_place_x = random.randint(0, game.labirynth_dim_x)
	exit_place_y = random.randint(0, game.labirynth_dim_y)

while True:
	#display title screen
	if game.started == False:
		screen.blit(title_screen, ( -( (1920 - resolution[0]) / 2), -( (1080 - resolution[1]) / 2)))
		pygame.display.flip()
		
	else:
		if game.level_type == "arena" or game.level_type == "boss_level":
			screen.blit(surface, (game.x, game.y))
		elif game.level_type == "labirynth":
			screen.fill((0, 0, 0))
				
			# screen.blit(start_place, (128 + game.x + 320 * start_place_x, 128 + game.y + 320 * start_place_y))
			screen.blit(start_place, (128 + game.x, 128 + game.y))
		
		if mass1.movement_loop == 150:
				mass1.movement_loop = 0
				mass1.offsetX += random.randint(-1, 2)
				mass1.offsetY += random.randint(-1, 2)
		else:
			mass1.movement_loop += 1
		
		if (mass1.x + mass1.offsetX) >= 200 and (mass1.x + mass1.offsetX) < (game.map_size_x - 200):
			mass1.x += mass1.offsetX
			
		if (mass1.y + mass1.offsetY) >= 200 and (mass1.y + mass1.offsetY) < (game.map_size_y - 200 - game.screen_bottom):
			mass1.y += mass1.offsetY
		
		screen.blit(mass1.model, (mass1.x + game.x, mass1.y + game.y))
		
		if mass2.movement_loop == 150:
			mass2.movement_loop = 0
			mass2.offsetX += random.randint(-1, 2)
			mass2.offsetY += random.randint(-1, 2)
		else:
			mass2.movement_loop += 1
		
		if (mass2.x + mass2.offsetX) >= 200 and (mass2.x + mass2.offsetX) < (game.map_size_x - 200):
			mass2.x += mass2.offsetX
			
		if (mass2.y + mass2.offsetY) >= 200 and (mass2.y + mass2.offsetY) < (game.map_size_y - 200 - game.screen_bottom):
			mass2.y += mass2.offsetY
			
		if game.level_type == "labirynth":
			if game.stage == 2:
				for x in range(0, game.labirynth_dim_x * 6):
					for y in range(0, game.labirynth_dim_y * 6):
						screen.blit(floor, (y * 64 + game.x, x * 64 + game.y))
			
				draw_labirynth(screen, game, labirynth, wall1, game.labirynth_dim_x, game.labirynth_dim_y)
			elif game.stage == 5:
				for x in range(0, game.labirynth_dim_x * 6):
					for y in range(0, game.labirynth_dim_y * 6):
						screen.blit(floor, (y * 64 + game.x, x * 64 + game.y))
			
				draw_labirynth(screen, game, labirynth, wall2, game.labirynth_dim_x, game.labirynth_dim_y)
			elif game.stage == 8:
				for x in range(0, game.labirynth_dim_x * 6):
					for y in range(0, game.labirynth_dim_y * 6):
						screen.blit(floor, (y * 64 + game.x, x * 64 + game.y))
			
				draw_labirynth(screen, game, labirynth, wall3, game.labirynth_dim_x, game.labirynth_dim_y)
			elif game.stage == 11:
				for x in range(0, game.labirynth_dim_x * 6):
					for y in range(0, game.labirynth_dim_y * 6):
						screen.blit(floor, (y * 64 + game.x, x * 64 + game.y))
			
				draw_labirynth(screen, game, labirynth, wall4, game.labirynth_dim_x, game.labirynth_dim_y)
			elif game.stage == 14:
				for x in range(0, game.labirynth_dim_x * 6):
					for y in range(0, game.labirynth_dim_y * 6):
						screen.blit(floor, (y * 64 + game.x, x * 64 + game.y))
			
				draw_labirynth(screen, game, labirynth, wall5, game.labirynth_dim_x, game.labirynth_dim_y)
				
			if game.exit_opened == True:
				screen.blit(exit_place, (128 + game.x + 320 * exit_place_x, 128 + game.y + 320 * exit_place_y))

		screen.blit(mass2.model, (mass2.x + game.x, mass2.y + game.y))
				
		if game.level_type == "arena":
			screen.blit(alien_egg, (300 + game.x, 400 + game.y))
			screen.blit(alien_egg, (320 + game.x, 440 + game.y))
			screen.blit(alien_egg, (370 + game.x, 400 + game.y))
			screen.blit(alien_egg, (800 + game.x, 600 + game.y))
			screen.blit(alien_egg, (820 + game.x, 690 + game.y))
			screen.blit(alien_egg, (970 + game.x, 650 + game.y))

			if game.stage <= 2:
				wall = wall1
			elif game.stage <= 4:
				wall = wall2
			elif game.stage <= 6:
				wall = wall3
			elif game.stage <= 8:
				wall = wall4
			screen.blit(wall, (600 + game.x, 400 + game.y))
			screen.blit(wall, (664 + game.x, 400 + game.y))
			screen.blit(wall, (472 + game.x, 400 + game.y))
			screen.blit(wall, (536 + game.x, 400 + game.y))
			screen.blit(wall, (472 + game.x, 464 + game.y))
			screen.blit(wall, (664 + game.x, 464 + game.y))
			screen.blit(wall, (472 + game.x, 528 + game.y))
			screen.blit(wall, (664 + game.x, 528 + game.y))
			# screen.blit(wall1, (3936 + game.x, 3906 + game.y))
			
		# for pixel in mass1.colony:
			# screen.set_at((pixel.x, pixel.y), (pixel.r, pixel.g, pixel.b))
			
		if game.level_type == "boss_level":
			screen.blit(alien_egg, (300 + game.x, 400 + game.y))
			screen.blit(alien_egg, (320 + game.x, 440 + game.y))
			screen.blit(alien_egg, (370 + game.x, 400 + game.y))
			screen.blit(alien_egg, (800 + game.x, 600 + game.y))
			screen.blit(alien_egg, (820 + game.x, 690 + game.y))
			screen.blit(alien_egg, (970 + game.x, 650 + game.y))

		if game.level_type == "arena":
			if game.bonus_loop == game.when_new_bonus and game.bonus_count < game.bonuses_per_level:
				game.bonus_loop = 0
				
				game.bonus_count += 1
				game.when_new_bonus = random.randint(game.new_bonus_min_time, game.new_bonus_max_time)
			
				#remember to increase this after adding new bonus to the game !!!
				which_one = random.randint(0, 8)

				random_x = random.randint(200, game.map_size_x - 200)
				random_y = random.randint(200, game.map_size_y - 200 - game.screen_bottom)
				
				while game.pixel_table[random_x][random_y] == 1:
					random_x = random.randint(200, game.map_size_x - 200)
					random_y = random.randint(200, game.map_size_y - 200 - game.screen_bottom)
			
				if which_one == 5: #vortex
					game.add_new_bonus(which_one, random_x, random_y, 100)
				elif which_one == 7: #yellow money
					game.add_new_bonus(which_one, random_x, random_y, 100)
				else: #all other bonuses
					game.add_new_bonus(which_one, random_x, random_y, 500)
			
			elif game.bonus_count < game.bonuses_per_level:
				game.bonus_loop += 1
				
			for bonus in game.bonuses:
				bonus.delay -= 1
				if bonus.delay <= 0:
					bonus.taken = True
				if bonus.taken == False: #should we remove taken bonuses from game.bonuses list?
					if bonus.which_one == 0:
						screen.blit(game.medkit_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 1:
						screen.blit(game.gasoline_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 2:
						screen.blit(game.refrigerant_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 3:
						screen.blit(game.laser_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 4:
						screen.blit(game.plasma_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 5:
						screen.blit(game.vortex_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 6:
						screen.blit(game.money_green_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 7:
						screen.blit(game.money_yellow_model, (bonus.x + game.x, bonus.y + game.y))
						
		elif game.level_type == "boss_level": #on boss level there will be no limit for bonuses number on the level
			if game.bonus_loop == game.when_new_bonus:
				game.bonus_loop = 0
				
				game.when_new_bonus = random.randint(game.new_bonus_min_time, game.new_bonus_max_time)
			
				#remember to increase this after adding new bonus to the game !!!
				which_one = random.randint(0, 8)

				random_x = random.randint(200, game.map_size_x - 200)
				random_y = random.randint(200, game.map_size_y - 200)
				
				while game.pixel_table[random_x][random_y] == 1:
					random_x = random.randint(200, game.map_size_x - 200)
					random_y = random.randint(200, game.map_size_y - 200)
			
				if which_one == 5: #vortex
					pass
				elif which_one == 7: #yellow money
					pass
				else: #all other bonuses
					game.add_new_bonus(which_one, random_x, random_y, 500)
			
			elif game.bonus_count < game.bonuses_per_level:
				game.bonus_loop += 1
				
			for bonus in game.bonuses:
				bonus.delay -= 1
				if bonus.delay <= 0:
					bonus.taken = True
				if bonus.taken == False: #should we remove taken bonuses from game.bonuses list?
					if bonus.which_one == 0:
						screen.blit(game.medkit_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 1:
						screen.blit(game.gasoline_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 2:
						screen.blit(game.refrigerant_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 3:
						screen.blit(game.laser_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 4:
						screen.blit(game.plasma_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 5:
						screen.blit(game.vortex_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 6:
						screen.blit(game.money_green_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 7:
						screen.blit(game.money_yellow_model, (bonus.x + game.x, bonus.y + game.y))
		
		elif game.level_type == "labirynth":
		
			for bonus in game.bonuses:
				if bonus.delay <= 0:
					bonus.taken = True
				if bonus.taken == False: #should we remove taken bonuses from game.bonuses list?
					if bonus.which_one == 0:
						screen.blit(game.medkit_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 1:
						screen.blit(game.gasoline_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 2:
						screen.blit(game.refrigerant_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 3:
						screen.blit(game.laser_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 4:
						screen.blit(game.plasma_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 5:
						screen.blit(game.vortex_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 6:
						screen.blit(game.money_green_model, (bonus.x + game.x, bonus.y + game.y))
					elif bonus.which_one == 7:
						screen.blit(game.money_yellow_model, (bonus.x + game.x, bonus.y + game.y))
						
			for key in game.keys:
				if key.taken == False:
					if key.which_one == 0:
						screen.blit(game.blue_key_model, (key.x + game.x, key.y + game.y))
					elif key.which_one == 1:
						screen.blit(game.red_key_model, (key.x + game.x, key.y + game.y))
					elif key.which_one == 2:
						screen.blit(game.green_key_model, (key.x + game.x, key.y + game.y))
					elif key.which_one == 3:
						screen.blit(game.yellow_key_model, (key.x + game.x, key.y + game.y))
			
		if game_loop == 3:
		
			who = 0 #one third of spiders will chase nash, 1/3 george and the rest will chase rxvt
		
			for spider in monster.monsters:
				if who == game.number_of_players:
					who = 0
				else:
					who += 1
					
				if who == 0:
				
					if spider.energy > 0:
						
						spider.offsetX = random.randint(0, game.spider_chaos)
						spider.offsetY = random.randint(0, game.spider_chaos)
						
						if nash.force_field_enabled == False:
							if nash.x - 20 > spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
							elif nash.x + 20 < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
								
							if nash.y - 20 > spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
							elif nash.y + 20 < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
						else:
							if nash.x - 50 > spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
							elif nash.x + 50 < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
							
							#throw spider away from force field
							elif nash.x >= spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
							elif nash.x < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
								
							if nash.y - 50 > spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
							elif nash.y + 50 < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
									
							#throw spider away from force field
							elif nash.y >= spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
							elif nash.y < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
				
							# print "spider.x = ", spider.x
							# print "spider.y = ", spider.y
				
				elif who == 1:
				
					if spider.energy > 0:
						
						spider.offsetX = random.randint(0, game.spider_chaos)
						spider.offsetY = random.randint(0, game.spider_chaos)
						
						if rxvt.force_field_enabled == False:
							if rxvt.x - 20 > spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
							elif rxvt.x + 20 < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
								
							if rxvt.y - 20 > spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
							elif rxvt.y + 20 < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
						else:
							if rxvt.x - 50 > spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
							elif rxvt.x + 50 < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
							
							#throw spider away from force field
							elif rxvt.x >= spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
							elif rxvt.x < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
								
							if rxvt.y - 50 > spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
							elif rxvt.y + 50 < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
									
							#throw spider away from force field
							elif rxvt.y >= spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
							elif rxvt.y < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed

				elif who == 2:
				
					if spider.energy > 0:
						
						spider.offsetX = random.randint(0, game.spider_chaos)
						spider.offsetY = random.randint(0, game.spider_chaos)
						
						if george.force_field_enabled == False:
							if george.x - 20 > spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
							elif george.x + 20 < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
								
							if george.y - 20 > spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
							elif george.y + 20 < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
						else:
							if george.x - 50 > spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
							elif george.x + 50 < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
							
							#throw spider away from force field
							elif george.x >= spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
							elif george.x < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
								
							if george.y - 50 > spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
							elif george.y + 50 < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
									
							#throw spider away from force field
							elif george.y >= spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
							elif george.y < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
					
				elif who == 3:
				
					if spider.energy > 0:
						
						spider.offsetX = random.randint(0, game.spider_chaos)
						spider.offsetY = random.randint(0, game.spider_chaos)
						
						if james.force_field_enabled == False:
							if james.x - 20 > spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
							elif james.x + 20 < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
								
							if james.y - 20 > spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
							elif james.y + 20 < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
						else:
							if james.x - 50 > spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
							elif james.x + 50 < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.x -= spider.speed
							
							#throw spider away from force field
							elif james.x >= spider.x:
								if (spider.x + spider.speed) > 28 and (spider.x + spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x - spider.speed)][int(spider.y)] == 0:
										spider.x -= spider.speed
							elif james.x < spider.x:
								if (spider.x - spider.speed) > 28 and (spider.x - spider.speed) < game.map_size_x - game.safety_border and spider.y > 65 and spider.y < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x + spider.speed)][int(spider.y)] == 0:
										spider.x += spider.speed
								
							if james.y - 50 > spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
							elif james.y + 50 < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
									
							#throw spider away from force field
							elif james.y >= spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y + spider.speed) > 65 and (spider.y + spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y - spider.speed)] == 0:
										spider.y -= spider.speed
							elif james.y < spider.y:
								if spider.x > 28 and spider.x < game.map_size_x - game.safety_border and (spider.y - spider.speed) > 65 and (spider.y - spider.speed) < game.map_size_y - game.screen_bottom - game.safety_border:
									if game.pixel_table[int(spider.x)][int(spider.y + spider.speed)] == 0:
										spider.y += spider.speed
				
			game_loop = 0
			
		# how to end level? / monsters movement
		if game.level_type == "arena":
			game.next_level = True
			for spider in monster.monsters:
				if spider.energy > 0:
					game.next_level = False
					
			for gigantula in monster.gigantulas:
				if gigantula.energy > 0:
					game.next_level = False
					
					if gigantula.breed_loop > gigantula.breed_loop_max:
						gigantula.breed_loop = 0
						
						monster.add_spider(game)
						monster.monsters[-1].x = gigantula.x
						monster.monsters[-1].y = gigantula.y
						
					else:
						gigantula.breed_loop += 1
					
					if gigantula.movement_loop >= 100:
						gigantula.movement_loop = 0
						
						if game.difficulty == 'easy':
							gigantula.offsetX = random.randint(-1, 2) * gigantula.speed
							gigantula.offsetY = random.randint(-1, 2) * gigantula.speed
						elif game.difficulty == 'medium':
							# gigantula.offsetX = random.randint(-1 - game.stage, 2 + game.stage) * gigantula.speed
							# gigantula.offsetY = random.randint(-1 - game.stage, 2 + game.stage) * gigantula.speed
							gigantula.offsetX = random.randint(-1, 2) * gigantula.speed
							gigantula.offsetY = random.randint(-1, 2) * gigantula.speed
						elif game.difficulty == 'hard':
							# gigantula.offsetX = random.randint(-1 - game.stage, 2 + game.stage) * gigantula.speed
							# gigantula.offsetY = random.randint(-1 - game.stage, 2 + game.stage) * gigantula.speed
							gigantula.offsetX = random.randint(-1, 2) * gigantula.speed
							gigantula.offsetY = random.randint(-1, 2) * gigantula.speed
					else:
						if game.difficulty == 'easy':
							gigantula.movement_loop += 1
						elif game.difficulty == 'medium':
							gigantula.movement_loop += 1
							if game.stage < 4:
								gigantula.movement_loop += game.stage
						elif game.difficulty == 'hard':
							gigantula.movement_loop += 2
							if game.stage < 4:
								gigantula.movement_loop += game.stage
						
			for robot in monster.robots:
				if robot.energy > 0:
					game.next_level = False
					if robot.movement_loop == 50:
						robot.movement_loop = 0
						
						if game.difficulty == 'easy':
							robot.offsetX = random.randint(-1, 2) * robot.speed
							robot.offsetY = random.randint(-1, 2) * robot.speed
						elif game.difficulty == 'medium':
							robot.offsetX = random.randint(-2, 3) * robot.speed
							robot.offsetY = random.randint(-2, 3) * robot.speed
						elif game.difficulty == 'hard':
							robot.offsetX = random.randint(-2, 3) * robot.speed
							robot.offsetY = random.randint(-2, 3) * robot.speed
					else:
						robot.movement_loop += 1
						
			for crane in monster.cranes:
				if crane.energy > 0:
					game.next_level = False
					if crane.movement_loop == 25:
						crane.movement_loop = 0
						
						if game.difficulty == 'easy':
							crane.offsetX = random.randint(-1, 2) * crane.speed
							crane.offsetY = random.randint(-1, 2) * crane.speed
						elif game.difficulty == 'medium':
							crane.offsetX = random.randint(-1, 2) * crane.speed
							crane.offsetY = random.randint(-1, 2) * crane.speed
						elif game.difficulty == 'hard':
							crane.offsetX = random.randint(-1 - game.stage, 2 + game.stage) * crane.speed
							crane.offsetY = random.randint(-1 - game.stage, 2 + game.stage) * crane.speed
					else:
						crane.movement_loop += 1
				
			for hunter in monster.hunters:
				if hunter.energy > 0:
					game.next_level = False
					if hunter.movement_loop == 5:
						hunter.movement_loop = 0
						
						if game.difficulty == 'easy':
							hunter.offsetX = random.randint(-1, 2) * hunter.speed
							hunter.offsetY = random.randint(-1, 2) * hunter.speed
						elif game.difficulty == 'medium':
							hunter.offsetX = random.randint(-1, 2) * hunter.speed
							hunter.offsetY = random.randint(-1, 2) * hunter.speed
						elif game.difficulty == 'hard':
							hunter.offsetX = random.randint(-1, 2) * hunter.speed
							hunter.offsetY = random.randint(-1, 2) * hunter.speed
					else:
						hunter.movement_loop += 1
						
		elif game.level_type == "boss_level":
			if game.boss.energy > 0:
				game.next_level = False
			else:
				# boss explosion sequence
				if game.wait_with_explosion_loop >= game.wait_with_explosion_loop_max:
					game.wait_with_explosion_loop = 0

					screen.blit(game.boss.model, (game.boss.x + game.x, game.boss.y + game.y))
					
					for j in range(0, 150):
						random_explosion_position_x = random.randint(-100, 100)
						random_explosion_position_y = random.randint(-100, 100)
						explosion_size = random.randint(3, 12)

						for i in range(0, explosion_size):
							for angl in range(0, 25):
								#draw explosions
								random_distortion = random.uniform(-0.2, 0.2)
								new_x = game.boss.x + 225 + int(math.sin(angl * 12 + random_distortion) * 4 * i) + random_explosion_position_x
								new_y = game.boss.y + 225 + int(math.cos(angl * 12 + random_distortion) * 4 * i) + random_explosion_position_y
								random_size = random.randint(2, 7)
								pygame.draw.circle(screen, (255 - i * 2, 30 + i * 2, 0), (new_x, new_y), random_size, 0)
									
							pygame.display.flip()
							time.sleep(0.003)
						
					game.next_level = True
				else:
					game.wait_with_explosion_loop += 1
				
			if game.boss.energy > 0:
				if game.boss.movement_loop == game.boss.movement_loop_max:
					game.boss.movement_loop = 0
					game.boss.offsetX = random.randint(-1, 2) * game.boss.speed
					game.boss.offsetY = random.randint(-1, 2) * game.boss.speed
				else:
					game.boss.movement_loop += 1
				
		
		elif game.level_type == "labirynth":
			game.next_level = False
					
			for gigantula in monster.gigantulas:
				if gigantula.energy > 0:
					game.next_level = False
					if gigantula.movement_loop >= 100:
						gigantula.movement_loop = 0
						
						if gigantula.breed_loop > gigantula.breed_loop_max:
							gigantula.breed_loop = 0
							
							monster.add_spider(game)
							monster.monsters[-1].x = gigantula.x
							monster.monsters[-1].y = gigantula.y
							
						else:
							gigantula.breed_loop += 1

						
						if game.difficulty == 'easy':
							gigantula.offsetX = random.randint(-1, 2) * gigantula.speed
							gigantula.offsetY = random.randint(-1, 2) * gigantula.speed
						elif game.difficulty == 'medium':
							# gigantula.offsetX = random.randint(-1 - game.stage, 2 + game.stage) * gigantula.speed
							# gigantula.offsetY = random.randint(-1 - game.stage, 2 + game.stage) * gigantula.speed
							gigantula.offsetX = random.randint(-1, 2) * gigantula.speed
							gigantula.offsetY = random.randint(-1, 2) * gigantula.speed
						elif game.difficulty == 'hard':
							# gigantula.offsetX = random.randint(-1 - game.stage, 2 + game.stage) * gigantula.speed
							# gigantula.offsetY = random.randint(-1 - game.stage, 2 + game.stage) * gigantula.speed
							gigantula.offsetX = random.randint(-1, 2) * gigantula.speed
							gigantula.offsetY = random.randint(-1, 2) * gigantula.speed
					else:
						if game.difficulty == 'easy':
							gigantula.movement_loop += 1
						elif game.difficulty == 'medium':
							gigantula.movement_loop += 1
							if game.stage < 4:
								gigantula.movement_loop += game.stage
						elif game.difficulty == 'hard':
							gigantula.movement_loop += 2
							if game.stage < 4:
								gigantula.movement_loop += game.stage
						
			for robot in monster.robots:
				if robot.energy > 0:
					if robot.movement_loop == 50:
						robot.movement_loop = 0
						
						if game.difficulty == 'easy':
							robot.offsetX = random.randint(-1, 2) * robot.speed
							robot.offsetY = random.randint(-1, 2) * robot.speed
						elif game.difficulty == 'medium':
							robot.offsetX = random.randint(-2, 3) * robot.speed
							robot.offsetY = random.randint(-2, 3) * robot.speed
						elif game.difficulty == 'hard':
							robot.offsetX = random.randint(-2 - game.stage, 3 + game.stage) * robot.speed
							robot.offsetY = random.randint(-2 - game.stage, 3 + game.stage) * robot.speed
					else:
						robot.movement_loop += 1
						
			for crane in monster.cranes:
				if crane.energy > 0:
					if crane.movement_loop == 25:
						crane.movement_loop = 0
						
						if game.difficulty == 'easy':
							crane.offsetX = random.randint(-1, 2) * crane.speed
							crane.offsetY = random.randint(-1, 2) * crane.speed
						elif game.difficulty == 'medium':
							crane.offsetX = random.randint(-1, 2) * crane.speed
							crane.offsetY = random.randint(-1, 2) * crane.speed
						elif game.difficulty == 'hard':
							crane.offsetX = random.randint(-1 - game.stage, 2 + game.stage) * crane.speed
							crane.offsetY = random.randint(-1 - game.stage, 2 + game.stage) * crane.speed
					else:
						crane.movement_loop += 1
						
			for hunter in monster.hunters:
				if hunter.energy > 0:
					if hunter.movement_loop == 5:
						hunter.movement_loop = 0
						
						if game.difficulty == 'easy':
							hunter.offsetX = random.randint(-1, 2) * hunter.speed
							hunter.offsetY = random.randint(-1, 2) * hunter.speed
						elif game.difficulty == 'medium':
							hunter.offsetX = random.randint(-1, 2) * hunter.speed
							hunter.offsetY = random.randint(-1, 2) * hunter.speed
						elif game.difficulty == 'hard':
							hunter.offsetX = random.randint(-1 - game.stage, 2 + game.stage) * hunter.speed
							hunter.offsetY = random.randint(-1 - game.stage, 2 + game.stage) * hunter.speed
					else:
						hunter.movement_loop += 1

			if game.exit_opened == True:
				if game.number_of_players == 1:
					if (math.fabs(nash.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(nash.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
						game.next_level = True
				elif game.number_of_players == 2:
					if nash.alive() and george.alive():
						if (math.fabs(nash.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(nash.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50) \
							and (math.fabs(george.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(george.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
							game.next_level = True
					elif not nash.alive():
						if (math.fabs(george.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(george.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
							game.next_level = True
					elif not george.alive():
						if (math.fabs(nash.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(nash.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
							game.next_level = True
				elif game.number_of_players == 3:
					if nash.alive() and george.alive() and james.alive():
						if (math.fabs(nash.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(nash.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50) \
							and (math.fabs(george.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(george.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50) \
							and (math.fabs(james.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(james.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
							game.next_level = True
					elif not nash.alive():
						if (math.fabs(george.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(george.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50) \
							and (math.fabs(james.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(james.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
							game.next_level = True
					elif not george.alive():
						if (math.fabs(nash.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(nash.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50) \
							and (math.fabs(james.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(james.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
							game.next_level = True
					elif not james.alive():
						if (math.fabs(nash.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(nash.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50) \
							and (math.fabs(george.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(george.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
							game.next_level = True
					elif not nash.alive() and not george.alive():
						if (math.fabs(james.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(james.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
							game.next_level = True
					elif not george.alive() and not james.alive():
						if (math.fabs(nash.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(nash.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
							game.next_level = True
					elif not nash.alive() and not james.alive():
						if (math.fabs(george.x + 32 - (320 * exit_place_x + 192 + game.x)) < 50) and (math.fabs(george.y + 32 - (320 * exit_place_y + 192 + game.y)) < 50):
							game.next_level = True
			
		for gigantula in monster.gigantulas:
			if gigantula.energy > 0:
				if (gigantula.x + gigantula.offsetX) >= 200 and (gigantula.x + gigantula.offsetX) < (game.map_size_x - 200):
					if game.pixel_table[int(gigantula.x + gigantula.offsetX)][int(gigantula.y + gigantula.offsetY)] == 0:
						# print "x"
						# print "gigantula.x + gigantula.offsetX = ", gigantula.x + gigantula.offsetX
						# print "gigantula.y + gigantula.offsetY = ", gigantula.y + gigantula.offsetY
						gigantula.x += gigantula.offsetX
				
				if (gigantula.y + gigantula.offsetY) >= 200 and (gigantula.y + gigantula.offsetY) < (game.map_size_y - 200 - game.screen_bottom):
					if game.pixel_table[int(gigantula.x + gigantula.offsetX)][int(gigantula.y + gigantula.offsetY)] == 0:
						# print "y"
						gigantula.y += gigantula.offsetY
						
		for robot in monster.robots:
			if robot.energy > 0:
				if (robot.x + robot.offsetX) >= 100 and (robot.x + robot.offsetX) < (game.map_size_x - 100):
					if game.pixel_table[int(robot.x + robot.offsetX)][int(robot.y + robot.offsetY)] == 0:
						# print "x"
						# print "robot.x + robot.offsetX = ", robot.x + robot.offsetX
						# print "robot.y + robot.offsetY = ", robot.y + robot.offsetY
						robot.x += robot.offsetX
				
				if (robot.y + robot.offsetY) >= 100 and (robot.y + robot.offsetY) < (game.map_size_y - 150 - game.screen_bottom):
					if game.pixel_table[int(robot.x + robot.offsetX)][int(robot.y + robot.offsetY)] == 0:
						# print "y"
						robot.y += robot.offsetY
						
		for crane in monster.cranes:
			if crane.energy > 0:
				if (crane.x + crane.offsetX) >= 200 and (crane.x + crane.offsetX) < (game.map_size_x - 200):
					if game.pixel_table[int(crane.x + 100 + crane.offsetX)][int(crane.y + 100 + crane.offsetY)] == 0:
						# print "x"
						# print "crane.x + crane.offsetX = ", crane.x + crane.offsetX
						# print "crane.y + crane.offsetY = ", crane.y + crane.offsetY
						crane.x += crane.offsetX
				
				if (crane.y + crane.offsetY) >= 200 and (crane.y + crane.offsetY) < (game.map_size_y - 250 - game.screen_bottom):
					if game.pixel_table[int(crane.x + 100 + crane.offsetX)][int(crane.y + 100 + crane.offsetY)] == 0:
						# print "y"
						crane.y += crane.offsetY
						
		for hunter in monster.hunters:
			if hunter.energy > 0:
				if (hunter.x + hunter.offsetX) >= 200 and (hunter.x + hunter.offsetX) < (game.map_size_x - 200):
					if game.pixel_table[int(hunter.x + 100 + hunter.offsetX)][int(hunter.y + 100 + hunter.offsetY)] == 0:
						# print "x"
						# print "hunter.x + hunter.offsetX = ", hunter.x + hunter.offsetX
						# print "hunter.y + hunter.offsetY = ", hunter.y + hunter.offsetY
						hunter.x += hunter.offsetX
				
				if (hunter.y + hunter.offsetY) >= 200 and (hunter.y + hunter.offsetY) < (game.map_size_y - 250 - game.screen_bottom):
					if game.pixel_table[int(hunter.x + 100 + hunter.offsetX)][int(hunter.y + 100 + hunter.offsetY)] == 0:
						# print "y"
						hunter.y += hunter.offsetY
						
		if game.boss.energy > 0:
			if (game.boss.x + game.boss.offsetX) >= 200 and (game.boss.x + game.boss.offsetX) < (game.map_size_x - 200):
				if game.pixel_table[int(game.boss.x + 100 + game.boss.offsetX)][int(game.boss.y + 100 + game.boss.offsetY)] == 0:
					# print "x"
					# print "game.boss.x + game.boss.offsetX = ", game.boss.x + game.boss.offsetX
					# print "game.boss.y + game.boss.offsetY = ", game.boss.y + game.boss.offsetY
					game.boss.x += game.boss.offsetX
			
			if (game.boss.y + game.boss.offsetY) >= 200 and (game.boss.y + game.boss.offsetY) < (game.map_size_y - 250 - game.screen_bottom):
				if game.pixel_table[int(game.boss.x + 100 + game.boss.offsetX)][int(game.boss.y + 100 + game.boss.offsetY)] == 0:
					# print "y"
					game.boss.y += game.boss.offsetY
		
		#monsters attacking?
		if nash.alive():
			for m in monster.monsters:
				if m.energy > 0:
					if (math.fabs(nash.x + 32 - (m.x + m.size/2 + game.x)) < 40) and (math.fabs(nash.y + 32 - (m.y + m.size/2 + game.y)) < 40):
						nash.energy -= game.spider_attack / nash.armor
						pain_sound.play()
						nash.being_attacked = True
						
			for g in monster.gigantulas:
				if g.energy > 0:
					if (math.fabs(nash.x + 32 - (g.x + g.size/2 + game.x)) < 40) and (math.fabs(nash.y + 32 - (g.y + g.size/2 + game.y)) < 40):
						nash.energy -= game.gigantula_attack / nash.armor
						pain_sound.play()
						nash.being_attacked = True
						
			for r in monster.robots:
				if r.energy > 0:
					if (math.fabs(nash.x + 32 - (r.x + r.size/2 + game.x)) < 40) and (math.fabs(nash.y + 32 - (r.y + r.size/2 + game.y)) < 40):
						nash.energy -= game.robot_attack / nash.armor
						pain_sound.play()
						nash.being_attacked = True
						
			for c in monster.cranes:
				if c.energy > 0:
					if (math.fabs(nash.x + 32 - (c.x + c.size/2 + game.x)) < c.size - 100) and (math.fabs(nash.y + 32 - (c.y + c.size/2 + game.y)) < c.size - 100):
						nash.energy -= game.crane_attack / nash.armor
						pain_sound.play()
						nash.being_attacked = True
						
			for hunter in monster.hunters:
				if hunter.energy > 0:
					if (math.fabs(nash.x + 32 - (hunter.x + hunter.size/2 + game.x)) < hunter.size) and (math.fabs(nash.y + 32 - (hunter.y + hunter.size/2 + game.y)) < hunter.size):
						nash.energy -= game.hunter_attack / nash.armor
						pain_sound.play()
						nash.being_attacked = True
						
			if game.level_type == "boss_level":
				if game.boss.energy > 0:
					if (math.fabs(nash.x + 32 - (game.boss.x + game.boss.size/2 + game.x)) < game.boss.size - 100) and (math.fabs(nash.y + 32 - (game.boss.y + game.boss.size/2 + game.y)) < game.boss.size - 100):
						nash.energy -= game.boss_attack / nash.armor
						pain_sound.play()
						nash.being_attacked = True
						
			if (math.fabs(nash.x + 32 - (mass1.x + mass1.size/2 + game.x)) < mass1.size / 2) and (math.fabs(nash.y + 32 - (mass1.y + mass1.size/2 + game.y)) < mass1.size / 2):
				if game.nash_character == 4: #doctor
					nash.in_mass = False
				else:
					nash.in_mass = True
					
			elif (math.fabs(nash.x + 32 - (mass2.x + mass2.size/2 + game.x)) < mass2.size / 2) and (math.fabs(nash.y + 32 - (mass2.y + mass2.size/2 + game.y)) < mass2.size / 2):
				if game.nash_character == 4:
					nash.in_mass = False
				else:
					nash.in_mass = True
			else:
				nash.in_mass = False
				
			if nash.in_mass == True:
				nash.energy -= 1.0 / nash.armor
				nash.player_speed = 1
			else:
				nash.player_speed = nash.base_speed
				
			if nash.energy <= 0:
				if game.lifes_pool > 0:
					game.lifes_pool -= 1
					nash.energy = nash.max_energy
					nash.force_field = nash.max_force_field
					pain_sound.play()
					
					#draw player's death/explosion
					for i in range(0, 25):
						for angl in range(0, 100):
							#draw bloody vortex
							random_distortion = random.uniform(-0.2, 0.2)
							new_x = nash.x + 32 + int(math.sin(angl * 3 + random_distortion) * 5 * i)
							new_y = nash.y + 32 + int(math.cos(angl * 3 + random_distortion) * 5 * i)
							
							random_size = random.randint(2, 7)
							pygame.draw.circle(screen, (100, 0, 0), (new_x, new_y), random_size, 0)
								
							#monster.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, 'nash')
							
							random_distortion = random.uniform(-0.2, 0.2)
							new_x = nash.x + 32 + int(math.sin(angl * 3 + random_distortion) * 5 * i)
							new_y = nash.y + 32 + int(math.cos(angl * 3 + random_distortion) * 5 * i)
							
							random_size = random.randint(1, 5)
							pygame.draw.circle(screen, (155 + i * 4, 0, 0), (new_x, new_y), random_size, 0)
									
							monster.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, 'nash')
							
						pygame.display.flip()
						time.sleep(game.player_death_time)
					
				else:
					nash.dead = True
					pain_sound.play()
		
		#monsters attacking?		
		if george.alive():
			for m in monster.monsters:
				if m.energy > 0:
					if (math.fabs(george.x + 32 - (m.x + m.size/2 + game.x)) < 40) and (math.fabs(george.y + 32 - (m.y + m.size/2 + game.y)) < 40):
						george.energy -= game.spider_attack / george.armor
						pain_sound.play()
						george.being_attacked = True
					
			for g in monster.gigantulas:
				if g.energy > 0:
					if (math.fabs(george.x + 32 - (g.x + g.size/2 + game.x)) < 40) and (math.fabs(george.y + 32 - (g.y + g.size/2 + game.y)) < 40):
						george.energy -= game.gigantula_attack / george.armor
						pain_sound.play()
						george.being_attacked = True
						
			for r in monster.robots:
				if r.energy > 0:
					if (math.fabs(george.x + 32 - (r.x + g.size/2 + game.x)) < 40) and (math.fabs(george.y + 32 - (r.y + g.size/2 + game.y)) < 40):
						george.energy -= game.robot_attack / george.armor
						pain_sound.play()
						george.being_attacked = True
						
			for c in monster.cranes:
				if c.energy > 0:
					if (math.fabs(george.x + 32 - (c.x + c.size/2 + game.x)) < c.size - 100) and (math.fabs(george.y + 32 - (c.y + c.size/2 + game.y)) < c.size - 100):
						george.energy -= game.crane_attack / george.armor
						pain_sound.play()
						george.being_attacked = True
						
			for hunter in monster.hunters:
				if hunter.energy > 0:
					if (math.fabs(george.x + 32 - (hunter.x + hunter.size/2 + game.x)) < hunter.size) and (math.fabs(george.y + 32 - (hunter.y + hunter.size/2 + game.y)) < hunter.size):
						george.energy -= game.hunter_attack / george.armor
						pain_sound.play()
						george.being_attacked = True
						
			if game.level_type == "boss_level":
				if game.boss.energy > 0:
					if (math.fabs(george.x + 32 - (game.boss.x + game.boss.size/2 + game.x)) < game.boss.size - 100) and (math.fabs(george.y + 32 - (game.boss.y + game.boss.size/2 + game.y)) < game.boss.size - 100):
						george.energy -= game.boss_attack / george.armor
						pain_sound.play()
						george.being_attacked = True
						
			if (math.fabs(george.x + 32 - (mass1.x + mass1.size/2 + game.x)) < mass1.size / 2) and (math.fabs(george.y + 32 - (mass1.y + mass1.size/2 + game.y)) < mass1.size / 2):
				if game.george_character == 4:
					george.in_mass = False
				else:
					george.in_mass = True
			elif (math.fabs(george.x + 32 - (mass2.x + mass2.size/2 + game.x)) < mass2.size / 2) and (math.fabs(george.y + 32 - (mass2.y + mass2.size/2 + game.y)) < mass2.size / 2):
				if game.george_character == 4:
					george.in_mass = False
				else:
					george.in_mass = True
			else:
				george.in_mass = False
				
			if george.in_mass == True:
				george.energy -= 1.0 / george.armor
				george.player_speed = 1
			else:
				george.player_speed = george.base_speed
				
			if george.energy <= 0:
				if game.lifes_pool > 0:
					game.lifes_pool -= 1
					george.energy = george.max_energy
					george.force_field = george.max_force_field
					pain_sound.play()
					
					#draw player's death/explosion
					for i in range(0, 25):
						for angl in range(0, 100):
							#draw bloody vortex
							random_distortion = random.uniform(-0.2, 0.2)
							new_x = george.x + 32 + int(math.sin(angl * 3 + random_distortion) * 5 * i)
							new_y = george.y + 32 + int(math.cos(angl * 3 + random_distortion) * 5 * i)
							
							random_size = random.randint(2, 7)
							pygame.draw.circle(screen, (100, 0, 0), (new_x, new_y), random_size, 0)
								
							#monster.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, 'george')
							
							random_distortion = random.uniform(-0.2, 0.2)
							new_x = george.x + 32 + int(math.sin(angl * 3 + random_distortion) * 5 * i)
							new_y = george.y + 32 + int(math.cos(angl * 3 + random_distortion) * 5 * i)
							
							random_size = random.randint(1, 5)
							pygame.draw.circle(screen, (155 + i * 4, 0, 0), (new_x, new_y), random_size, 0)
									
							monster.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, 'george')
							
						pygame.display.flip()
						time.sleep(game.player_death_time)
					
				else:
					george.dead = True
					pain_sound.play()
		
		#monsters attacking?
		if james.alive():
			for m in monster.monsters:
				if m.energy > 0:
					if (math.fabs(james.x + 32 - (m.x + m.size/2 + game.x)) < 40) and (math.fabs(james.y + 32 - (m.y + m.size/2 + game.y)) < 40):
						james.energy -= game.spider_attack / james.armor
						pain_sound.play()
					
			for g in monster.gigantulas:
				if g.energy > 0:
					if (math.fabs(james.x + 32 - (g.x + g.size/2 + game.x)) < 40) and (math.fabs(james.y + 32 - (g.y + g.size/2 + game.y)) < 40):
						james.energy -= game.gigantula_attack / james.armor
						pain_sound.play()
						
			for r in monster.robots:
				if r.energy > 0:
					if (math.fabs(james.x + 32 - (r.x + g.size/2 + game.x)) < 40) and (math.fabs(james.y + 32 - (r.y + g.size/2 + game.y)) < 40):
						james.energy -= game.robot_attack / james.armor
						pain_sound.play()
						
			for c in monster.cranes:
				if c.energy > 0:
					if (math.fabs(james.x + 32 - (c.x + c.size/2 + game.x)) < c.size - 100) and (math.fabs(james.y + 32 - (c.y + c.size/2 + game.y)) < c.size - 100):
						james.energy -= game.crane_attack / james.armor
						pain_sound.play()
						james.being_attacked = True
						
			for hunter in monster.hunters:
				if hunter.energy > 0:
					if (math.fabs(james.x + 32 - (hunter.x + hunter.size/2 + game.x)) < hunter.size) and (math.fabs(james.y + 32 - (hunter.y + hunter.size/2 + game.y)) < hunter.size):
						james.energy -= game.hunter_attack / james.armor
						pain_sound.play()
						james.being_attacked = True
						
			if game.level_type == "boss_level":
				if game.boss.energy > 0:
					if (math.fabs(james.x + 32 - (game.boss.x + game.boss.size/2 + game.x)) < game.boss.size - 100) and (math.fabs(james.y + 32 - (game.boss.y + game.boss.size/2 + game.y)) < game.boss.size - 100):
						james.energy -= game.boss_attack / james.armor
						pain_sound.play()
						james.being_attacked = True
						
			if (math.fabs(james.x + 32 - (mass1.x + mass1.size/2 + game.x)) < mass1.size / 2) and (math.fabs(james.y + 32 - (mass1.y + mass1.size/2 + game.y)) < mass1.size / 2):
				if game.james_character == 4:
					james.in_mass = False
				else:
					james.in_mass = True
			elif (math.fabs(james.x + 32 - (mass2.x + mass2.size/2 + game.x)) < mass2.size / 2) and (math.fabs(james.y + 32 - (mass2.y + mass2.size/2 + game.y)) < mass2.size / 2):
				if game.james_character == 4:
					james.in_mass = False
				else:
					james.in_mass = True
			else:
				james.in_mass = False
				
			if james.in_mass == True:
				james.energy -= 1.0 / james.armor
				james.player_speed = 1
			else:
				james.player_speed = james.base_speed
						
			if james.energy <= 0:
				if game.lifes_pool > 0:
					game.lifes_pool -= 1
					james.energy = james.max_energy
					james.force_field = james.max_force_field
					pain_sound.play()
					
					#draw player's death/explosion
					for i in range(0, 25):
						for angl in range(0, 100):
							#draw bloody vortex
							random_distortion = random.uniform(-0.2, 0.2)
							new_x = james.x + 32 + int(math.sin(angl * 3 + random_distortion) * 5 * i)
							new_y = james.y + 32 + int(math.cos(angl * 3 + random_distortion) * 5 * i)
							
							random_size = random.randint(2, 7)
							pygame.draw.circle(screen, (100, 0, 0), (new_x, new_y), random_size, 0)
								
							#monster.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, 'james')
							
							random_distortion = random.uniform(-0.2, 0.2)
							new_x = james.x + 32 + int(math.sin(angl * 3 + random_distortion) * 5 * i)
							new_y = james.y + 32 + int(math.cos(angl * 3 + random_distortion) * 5 * i)
							
							random_size = random.randint(1, 5)
							pygame.draw.circle(screen, (155 + i * 4, 0, 0), (new_x, new_y), random_size, 0)
									
							monster.kill_monster(game, new_x, new_y, 50, 'vortex', global_player, 'james')
							
						pygame.display.flip()
						time.sleep(game.player_death_time)
					
				else:
					james.dead = True
					pain_sound.play()
					
		if nash.alive() and george.alive():
			# compute the center of players
			if nash.x > george.x:
				center_x = george.x + (nash.x - george.x) / 2
			elif nash.x < george.x:
				center_x = nash.x + (george.x - nash.x) / 2
			else:
				center_x = nash.x
				
			#compute the center of players
			if nash.y > george.y:
				center_y = george.y + (nash.y - george.y) / 2
			elif nash.y < george.y:
				center_y = nash.y + (george.y - nash.y) / 2
			else:
				center_y = nash.y
			
		if nash.alive():
			if game.number_of_players == 1 or (game.number_of_players == 2 and not george.alive()) or (game.number_of_players == 3 and not george.alive() and not james.alive()):
				
				# move player if possible
				if (nash.x + nash.offsetX) >= 0 and (nash.x + nash.offsetX) < resolution[0] - 60:
					if nash.x + nash.offsetX - game.x > 0 \
						and nash.x + nash.offsetX - game.x < game.map_size_x \
						and nash.y + nash.offsetY - game.y >= 0 \
						and nash.y + nash.offsetY - game.y < game.map_size_y - game.screen_bottom_player:
						if game.pixel_table[int(nash.x + nash.offsetX - game.x)][int(nash.y + nash.offsetY - game.y)] == 0:
							if game.x - nash.offsetX <= 0 and game.x - nash.offsetX > (-game.map_size_x + resolution[0]) and nash.x >= resolution[0] / 2 - 10 and nash.x <= resolution[0] / 2 + 10:
								
								nash.x = resolution[0] / 2
								game.x -= nash.offsetX
								
							else:
								nash.x += nash.offsetX
						
						elif game.pixel_table[int(nash.x + nash.offsetX - game.x)][int(nash.y - game.y)] == 0:
							if game.x - nash.offsetX <= 0 and game.x - nash.offsetX > (-game.map_size_x + resolution[0]) and nash.x >= resolution[0] / 2 - 10 and nash.x <= resolution[0] / 2 + 10:
								
								nash.x = resolution[0] / 2
								game.x -= nash.offsetX
								
							else:
								nash.x += nash.offsetX
			
				if  (nash.y + nash.offsetY) >= 30 and (nash.y + nash.offsetY) < resolution[1] - game.screen_bottom_player:
					if nash.x + nash.offsetX - game.x >= 0 \
						and nash.x + nash.offsetX - game.x < game.map_size_x \
						and nash.y + nash.offsetY - game.y >= 0 \
						and nash.y + nash.offsetY - game.y < game.map_size_y - game.screen_bottom_player:
						if game.pixel_table[int(nash.x + nash.offsetX - game.x)][int(nash.y + nash.offsetY - game.y)] == 0:
							if game.y - nash.offsetY <= 0 and game.y - nash.offsetY > (-game.map_size_y + resolution[1]) and nash.y >= resolution[1] / 2 - 10 and nash.y <= resolution[1] / 2 + 10:
								
								nash.y = resolution[1] / 2
								game.y -= nash.offsetY
								
							else:
								nash.y += nash.offsetY

						elif game.pixel_table[int(nash.x - game.x)][int(nash.y + nash.offsetY - game.y)] == 0:
							if game.y - nash.offsetY <= 0 and game.y - nash.offsetY > (-game.map_size_y + resolution[1]) and nash.y >= resolution[1] / 2 - 10 and nash.y <= resolution[1] / 2 + 10:
								
								nash.y = resolution[1] / 2
								game.y -= nash.offsetY
								
							else:
								nash.y += nash.offsetY
				
			elif game.number_of_players == 2:
				#move player if possible
				
				#tracing labels
				
				# trc_label = font.render('center_x: ' + str(center_x), True, (0, 255, 100), (0, 0, 0))
				# screen.blit(trc_label, (0, 50))
				# trc_label = font.render('center_y: ' + str(center_y), True, (0, 255, 100), (0, 0, 0))
				# screen.blit(trc_label, (200, 50))
				
				# trc_label = font.render('game.x: ' + str(game.x), True, (0, 255, 100), (0, 0, 0))
				# screen.blit(trc_label, (400, 50))
				# trc_label = font.render('game.y: ' + str(game.y), True, (0, 255, 100), (0, 0, 0))
				# screen.blit(trc_label, (600, 50))
			
				if (nash.x + nash.offsetX) >= 60 and (nash.x + nash.offsetX) < resolution[0] - 90:
					if nash.x + nash.offsetX - game.x > 0 \
						and nash.x + nash.offsetX - game.x < game.map_size_x \
						and nash.y + nash.offsetY - game.y >= 0 \
						and nash.y + nash.offsetY - game.y < game.map_size_y - game.screen_bottom_player:
						if game.pixel_table[int(nash.x + nash.offsetX - game.x)][int(nash.y + nash.offsetY - game.y)] == 0:
							if game.x - nash.offsetX <= 0 and game.x - nash.offsetX > (-game.map_size_x + resolution[0]) \
							and ((nash.offsetX > 0 and center_x >= resolution[0] / 2 - 10) or (nash.offsetX < 0 and center_x <= resolution[0] / 2 + 10)):
								
								game.x -= nash.offsetX
								george.x -= nash.offsetX
									
							else:
								nash.x += nash.offsetX
						
						elif game.pixel_table[int(nash.x + nash.offsetX - game.x)][int(nash.y - game.y)] == 0:
							if game.x - nash.offsetX <= 0 and game.x - nash.offsetX > (-game.map_size_x + resolution[0]) \
							and ((nash.offsetX > 0 and center_x >= resolution[0] / 2 - 10) or (nash.offsetX < 0 and center_x <= resolution[0] / 2 + 10)):
								
								game.x -= nash.offsetX
								george.x -= nash.offsetX
									
							else:
								nash.x += nash.offsetX
				
				if  (nash.y + nash.offsetY) >= 60 and (nash.y + nash.offsetY) < resolution[1] - game.screen_bottom_player:
					if nash.x + nash.offsetX - game.x >= 0 \
						and nash.x + nash.offsetX - game.x < game.map_size_x \
						and nash.y + nash.offsetY - game.y >= 0 \
						and nash.y + nash.offsetY - game.y < game.map_size_y - game.screen_bottom_player:
						if game.pixel_table[int(nash.x + nash.offsetX - game.x)][int(nash.y + nash.offsetY - game.y)] == 0:
							if game.y - nash.offsetY <= 0 and game.y - nash.offsetY > (-game.map_size_y + resolution[1]) \
							and ((nash.offsetY > 0 and center_y >= resolution[1] / 2 - 10) or (nash.offsetY < 0 and center_y <= resolution[1] / 2 + 10)):
								
								game.y -= nash.offsetY
								george.y -= nash.offsetY
									
							else:
								nash.y += nash.offsetY

						elif game.pixel_table[int(nash.x - game.x)][int(nash.y + nash.offsetY - game.y)] == 0:
							if game.y - nash.offsetY <= 0 and game.y - nash.offsetY > (-game.map_size_y + resolution[1]) \
							and ((nash.offsetY > 0 and center_y >= resolution[1] / 2 - 10) or (nash.offsetY < 0 and center_y <= resolution[1] / 2 + 10)):
								
								game.y -= nash.offsetY
								george.y -= nash.offsetY
									
							else:
								nash.y += nash.offsetY

			elif game.number_of_players == 3:
				#move player if possible
				
				#compute the x center of players
				max_x = max(nash.x, george.x, james.x)
				min_x = min(nash.x, george.x, james.x)
				
				if min_x != max_x:
					center_x = min_x + (max_x - min_x) / 2
				else:
					center_x = min_x
					
				#compute the y center of players
				max_y = max(nash.y, george.y, james.y)
				min_y = min(nash.y, george.y, james.y)
				
				if min_y != max_y:
					center_y = min_y + (max_y - min_y) / 2
				else:
					center_y = min_y
				
				if (nash.x + nash.offsetX) >= 0 and (nash.x + nash.offsetX) < resolution[0] - 60:
					if nash.x + nash.offsetX - game.x > 0 \
						and nash.x + nash.offsetX - game.x < game.map_size_x \
						and nash.y + nash.offsetY - game.y >= 0 \
						and nash.y + nash.offsetY - game.y < game.map_size_y - game.screen_bottom_player:
						if game.pixel_table[int(nash.x + nash.offsetX - game.x)][int(nash.y + nash.offsetY - game.y)] == 0:
							if game.x - nash.offsetX < 0 and game.x - nash.offsetX > (-game.map_size_x + resolution[0]) and center_x >= resolution[0] / 2 - 10 and center_x <= resolution[0] / 2 + 10:
								
								game.x -= nash.offsetX
								george.x -= nash.offsetX
								james.x -= nash.offsetX
								
							else:
								nash.x += nash.offsetX
						
						elif game.pixel_table[int(nash.x + nash.offsetX - game.x)][int(nash.y - game.y)] == 0:
							if game.x - nash.offsetX < 0 and game.x - nash.offsetX > (-game.map_size_x + resolution[0]) and center_x >= resolution[0] / 2 - 10 and center_x <= resolution[0] / 2 + 10:
								
								game.x -= nash.offsetX
								george.x -= nash.offsetX
								james.x -= nash.offsetX
								
							else:
								nash.x += nash.offsetX
				
				if  (nash.y + nash.offsetY) >= 30 and (nash.y + nash.offsetY) < resolution[1] - game.screen_bottom_player:
					if nash.x + nash.offsetX - game.x >= 0 \
						and nash.x + nash.offsetX - game.x < game.map_size_x \
						and nash.y + nash.offsetY - game.y >= 0 \
						and nash.y + nash.offsetY - game.y < game.map_size_y - game.screen_bottom_player:
						if game.pixel_table[int(nash.x + nash.offsetX - game.x)][int(nash.y + nash.offsetY - game.y)] == 0:
							if game.y - nash.offsetY < 0 and game.y - nash.offsetY > (-game.map_size_y + resolution[1]) and center_y >= resolution[1] / 2 - 10 and center_y <= resolution[1] / 2 + 10:
								
								game.y -= nash.offsetY
								george.y -= nash.offsetY
								james.y -= nash.offsetY
								
							else:
								nash.y += nash.offsetY

						elif game.pixel_table[int(nash.x - game.x)][int(nash.y + nash.offsetY - game.y)] == 0:
							if game.y - nash.offsetY < 0 and game.y - nash.offsetY > (-game.map_size_y + resolution[1]) and center_y >= resolution[1] / 2 - 10 and center_y <= resolution[1] / 2 + 10:
								
								game.y -= nash.offsetY
								george.y -= nash.offsetY
								james.y -= nash.offsetY
								
							else:
								nash.y += 2 * nash.offsetY
							
			#RIGHT
			if nash.offsetX > 0:
				nash.model = pygame.image.load('data/images/players/nash/nash-90.png')
				nash.pain_model = pygame.image.load('data/images/players/nash/nash_pain-90.png')
				nash.angle = 90
			#LEFT
			if nash.offsetX < 0:
				nash.model = pygame.image.load('data/images/players/nash/nash-270.png')
				nash.pain_model = pygame.image.load('data/images/players/nash/nash_pain-270.png')
				nash.angle = 270
			#DOWN
			if nash.offsetY > 0:
				nash.model = pygame.image.load('data/images/players/nash/nash-180.png')
				nash.pain_model = pygame.image.load('data/images/players/nash/nash_pain-180.png')
				nash.angle = 180
			#UP
			if nash.offsetY < 0:
				nash.model = pygame.image.load('data/images/players/nash/nash-0.png')
				nash.pain_model = pygame.image.load('data/images/players/nash/nash_pain-0.png')
				nash.angle = 0
			
			#diagonal directions
			if nash.offsetX < 0 and nash.offsetY < 0:
				nash.model = pygame.image.load('data/images/players/nash/nash-315.png')
				nash.pain_model = pygame.image.load('data/images/players/nash/nash_pain-315.png')
				nash.angle = 315
			if nash.offsetX < 0 and nash.offsetY > 0:
				nash.model = pygame.image.load('data/images/players/nash/nash-225.png')
				nash.pain_model = pygame.image.load('data/images/players/nash/nash_pain-225.png')
				nash.angle = 225
			if nash.offsetX > 0 and nash.offsetY > 0:
				nash.model = pygame.image.load('data/images/players/nash/nash-135.png')
				nash.pain_model = pygame.image.load('data/images/players/nash/nash_pain-135.png')
				nash.angle = 135
			if nash.offsetX > 0 and nash.offsetY < 0:
				nash.model = pygame.image.load('data/images/players/nash/nash-45.png')
				nash.pain_model = pygame.image.load('data/images/players/nash/nash_pain-45.png')
				nash.angle = 45
				
			#found bonus?
			for bonus in game.bonuses:
				if bonus.taken == False:
					if (math.fabs(nash.x + 32 - (bonus.x + 16 + game.x)) < 50) and (math.fabs(nash.y + 32 - (bonus.y + 16 + game.y)) < 50):
						bonus.taken = True
						#medkit
						if bonus.which_one == 0:
							if nash.alive():
								nash.add_energy(game.medkit_ammount + nash.add_energy_booster)
							if george.alive():
								george.add_energy(game.medkit_ammount + george.add_energy_booster)
							if james.alive():
								james.add_energy(game.medkit_ammount + james.add_energy_booster)
				
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
				
						#gasoline
						elif bonus.which_one == 1:
							nash.add_ammo('flamethrower', game.bonus_flamethrower_ammo)
							george.add_ammo('flamethrower', game.bonus_flamethrower_ammo)
							james.add_ammo('flamethrower', game.bonus_flamethrower_ammo)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10

						#refrigerant
						elif bonus.which_one == 2:
							nash.add_ammo('freezer', game.bonus_freezer_ammo)
							george.add_ammo('freezer', game.bonus_freezer_ammo)
							james.add_ammo('freezer', game.bonus_freezer_ammo)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10

						#laser
						elif bonus.which_one == 3:
							game.laser_power += game.laser_power_boost
							# nash.laser_time_upgrade += 1
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10

						#plasma
						elif bonus.which_one == 4:
							nash.add_ammo('plasma', game.plasma_spheres)
							george.add_ammo('plasma', game.plasma_spheres)
							james.add_ammo('plasma', game.plasma_spheres)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10

						#vortex
						elif bonus.which_one == 5:
							if nash.ammo['vortex'] < 1:
								nash.add_ammo('vortex', 1)
							
							nash.money += 50
							game.points += 50
							if game.number_of_players > 1:
								george.money += 50
							elif game.number_of_players > 2:
								james.money += 50

						#green money
						elif bonus.which_one == 6:
							nash.money += game.green_money
							game.points += game.green_money
							if game.number_of_players > 1:
								george.money += game.green_money
							elif game.number_of_players > 2:
								james.money += game.green_money

						#gold money
						elif bonus.which_one == 7:
							nash.money += game.gold_money
							game.points += game.gold_money
							if game.number_of_players > 1:
								george.money += game.gold_money
							elif game.number_of_players > 2:
								james.money += game.gold_money
			
			#found key?
			for key in game.keys:
				if key.taken == False:
					if (math.fabs(nash.x + 32 - (key.x + 16 + game.x)) < 70) and (math.fabs(nash.y + 32 - (key.y + 16 + game.y)) < 70):
						key.taken = True
						#blue key
						if key.which_one == 0:
							game.keys_possesed.append("blue")
						elif key.which_one == 1:
							game.keys_possesed.append("red")
						elif key.which_one == 2:
							game.keys_possesed.append("green")
						elif key.which_one == 3:
							game.keys_possesed.append("yellow")
			
			
			
			if len(game.keys_possesed) == 4:
				game.exit_opened = True
			
			# game.exit_opened = True # for testing
			
			
			
			#auto-enable armor for nash?
			if nash.energy < nash.ff_auto_enable_level and nash.has_force_field:
				nash.force_field_enabled = True
						
			if nash.force_field_enabled:
				if nash.force_field > 0:
					nash.force_field -= 1
					nash.armor = 200
					pygame.draw.circle(screen, (0, 255, 0), (nash.x + 32, nash.y + 32), 55, 8)
				else:
					nash.force_field_enabled = False
					nash.armor = nash.base_armor
			else:
				nash.armor = nash.base_armor
			
			#fire weapon?
			if nash.fire == True and not nash.in_mass:
				if nash.current_weapon == "laser":
					try:
						_thread.start_new_thread(laser, ("Thread-laser", 0.001, screen, laser_sound, nash.x, nash.y, nash.angle, nash.ammo, monster, game, global_player, 'nash'))
					except:
						print("Error: unable to start laser thread")
				elif nash.current_weapon == "flamethrower":
					try:
						#thread.start_new_thread(flamethrower, ("Thread-flamethrower", 0.001, screen, flamethrower_sound, nash.x, nash.y, nash.angle, nash.ammo, monster, game, global_player, 'nash'))
						_thread.start_new_thread(flamethrower, ("Thread-flamethrower", 0.001, screen, flamethrower_sound, nash.x, nash.y, nash.angle, nash.ammo, monster, game, global_player, 'nash'))
					except:
						print("Error: unable to start flamethrower thread")
				elif nash.current_weapon == "freezer":
					try:
						if nash.slot1 == 0:
							_thread.start_new_thread(freezer, ("Thread-freezer", 0.001, screen, freezer_sound, nash.x, nash.y, nash.angle, nash.ammo, monster, game,  global_player, 'nash'))
						elif nash.slot1 == 1:
							_thread.start_new_thread(long_range_freezer, ("Thread-freezer", 0.001, screen, freezer_sound, nash.x, nash.y, nash.angle, nash.ammo, monster, game,  global_player, 'nash'))
					except:
						print("Error: unable to start freezer thread")
				elif nash.current_weapon == "plasma":
					try:
						_thread.start_new_thread(plasma, ("Thread-plasma", 0.001, screen, plasma_sound, nash.x, nash.y, nash.angle, nash.ammo, monster, game,  global_player, 'nash'))
					except:
						print("Error: unable to start plasma thread")
					
		if rxvt.alive():
			if game.bot_movement_loop == game.bot_movement_loop_max:
				game.bot_movement_loop = 0
				rxvt.offsetX = random.randint(-1, 2) * game.rxvt_speed
				rxvt.offsetY = random.randint(-1, 2) * game.rxvt_speed
		
		if rxvt.alive():

			if (rxvt.x + rxvt.offsetX) >= 150 and (rxvt.x + rxvt.offsetX) < game.map_size_x - 150:
				# print "x"
				rxvt.x += rxvt.offsetX
			
			if (rxvt.y + rxvt.offsetY) >= 150 and (rxvt.y + rxvt.offsetY) < game.map_size_y - 250:
				# print "y"
				rxvt.y += rxvt.offsetY

			#RIGHT
			if rxvt.offsetX > 0:
				rxvt.model = pygame.image.load('data/images/players/rxvt/rxvt-90.png')
				rxvt.angle = 90
			#LEFT
			if rxvt.offsetX < 0:
				rxvt.model = pygame.image.load('data/images/players/rxvt/rxvt-270.png')
				rxvt.angle = 270
			#DOWN
			if rxvt.offsetY > 0:
				rxvt.model = pygame.image.load('data/images/players/rxvt/rxvt-180.png')
				rxvt.angle = 180
			#UP
			if rxvt.offsetY < 0:
				rxvt.model = pygame.image.load('data/images/players/rxvt/rxvt-0.png')
				rxvt.angle = 0
			
			#diagonal directions
			if rxvt.offsetX < 0 and rxvt.offsetY < 0:
				rxvt.model = pygame.image.load('data/images/players/rxvt/rxvt-315.png')
				rxvt.angle = 315
			if rxvt.offsetX < 0 and rxvt.offsetY > 0:
				rxvt.model = pygame.image.load('data/images/players/rxvt/rxvt-225.png')
				rxvt.angle = 225
			if rxvt.offsetX > 0 and rxvt.offsetY > 0:
				rxvt.model = pygame.image.load('data/images/players/rxvt/rxvt-135.png')
				rxvt.angle = 135
			if rxvt.offsetX > 0 and rxvt.offsetY < 0:
				rxvt.model = pygame.image.load('data/images/players/rxvt/rxvt-45.png')
				rxvt.angle = 45
				
			#Nash last hope!
			if nash.energy < 15 and nash.force_field < 15 and rxvt.ammo['vortex'] > 0 and rxvt.vortex_launched == False:
				rxvt.vortex_launched = True
				vortex_sound.play()
				# for spider in monster.monsters:
					# spider.speed = 1
					# spider.armor = 1
					
				# for gigantula in monster.gigantulas:
					# gigantula.speed = 1
					# gigantula.armor = 1

				rxvt.ammo['vortex'] -= 1
				try:
					_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, rxvt.x, rxvt.y, rxvt.angle, rxvt.ammo, monster, game,  global_player, 'rxvt'))
				except:
					print("Error: unable to start rxvt vortex for nash thread")
			
			#George last hope!
			if george.energy < 15 and george.force_field < 15 and rxvt.ammo['vortex'] > 0 and rxvt.vortex_launched == False:
				rxvt.vortex_launched = True
				vortex_sound.play()
				# for spider in monster.monsters:
					# spider.speed = 1
					# spider.armor = 1
					
				# for gigantula in monster.gigantulas:
					# gigantula.speed = 1
					# gigantula.armor = 1

				rxvt.ammo['vortex'] -= 1
				try:
					_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, rxvt.x, rxvt.y, rxvt.angle, rxvt.ammo, monster, game,  global_player, 'rxvt'))
				except:
					print("Error: unable to start rxvt vortex for george thread")
					
			#James last hope!
			if james.energy < 15 and james.force_field < 15 and rxvt.ammo['vortex'] > 0 and rxvt.vortex_launched == False:
				rxvt.vortex_launched = True
				vortex_sound.play()
				# for spider in monster.monsters:
					# spider.speed = 1
					# spider.armor = 1
					
				# for gigantula in monster.gigantulas:
					# gigantula.speed = 1
					# gigantula.armor = 1

				rxvt.ammo['vortex'] -= 1
				try:
					_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, rxvt.x, rxvt.y, rxvt.angle, rxvt.ammo, monster, game,  global_player, 'rxvt'))
				except:
					print("Error: unable to start rxvt vortex for james thread")
				
			#fire weapon our brave rxvt!
			if rxvt.ammo['flamethrower'] > 0:
				rxvt.current_weapon = "flamethrower"
				try:
					_thread.start_new_thread(flamethrower, ("Thread-flamethrower", 0.001, screen, flamethrower_sound, rxvt.x + game.x, rxvt.y + game.y, rxvt.angle, rxvt.ammo, monster, game, global_player, 'rxvt'))
				except:
					print("Error: unable to start rxvt flamethrower thread")
			elif rxvt.ammo['plasma'] > 0:
				rxvt.current_weapon = "plasma"
				try:
					_thread.start_new_thread(plasma, ("Thread-plasma", 0.001, screen, plasma_sound, rxvt.x + game.x, rxvt.y + game.y, rxvt.angle, rxvt.ammo, monster, game, global_player, 'rxvt'))
				except:
					print("Error: unable to start rxvt plasma thread")
			elif rxvt.ammo['laser'] > 0:
				rxvt.current_weapon = "laser"
				try:
					_thread.start_new_thread(laser, ("Thread-laser", 0.001, screen, laser_sound, rxvt.x + game.x, rxvt.y + game.y, rxvt.angle, rxvt.ammo, monster, game, global_player, 'rxvt'))
				except:
					print("Error: unable to start rxvt laser thread")
			elif rxvt.ammo['freezer'] > 0:
				rxvt.current_weapon = "freezer"
				try:
					_thread.start_new_thread(freezer, ("Thread-freezer", 0.001, screen, freezer_sound, rxvt.x + game.x, rxvt.y + game.y, rxvt.angle, rxvt.ammo, monster, game, global_player, 'rxvt'))
				except:
					print("Error: unable to start rxvt freezer thread")
					
					
			#fire our bad monsters :(
			# if robot_fire_loop == 8:
			# if robot_fire_loop == 10:
			if robot_fire_loop == 15 - game.stage:			
				robot_fire_loop = 0
				for robot in monster.robots:
					if robot.energy > 0:
						try:
							_thread.start_new_thread(robot_weapon, ("Thread-robot_weapon", 0.01, screen, laser_sound, robot.x + game.x, robot.y + game.y, monster, game, global_player, pain_sound))
						except:
							print("Error: unable to start robot weapon thread")
			else:
				robot_fire_loop += 1
				
			if game.boss.energy > 0:
				if game.boss.fire_loop >= game.boss.fire_loop_max:
					game.boss.fire_loop = 0
					try:
						_thread.start_new_thread(boss_weapon, ("Thread-boss_weapon", 0.003, screen, laser_sound, game.boss.x + game.x, game.boss.y + game.y, monster, game, global_player, pain_sound))
					except:
						print("Error: unable to start boss weapon thread")
				else:
					game.boss.fire_loop += 1
					
			for hunter in monster.hunters:
				if hunter.energy > 0:
					if hunter.fire_loop >= 10:			
						hunter.fire_loop = 0
						try:
							_thread.start_new_thread(boss_weapon, ("Thread-boss_weapon", 0.01, screen, laser_sound, hunter.x + game.x, hunter.y + game.y, monster, game, global_player, pain_sound))
						except:
							print("Error: unable to start hunter weapon thread")
					else:
						hunter.fire_loop += 1
					
			# elif rxvt.ammo['plasma'] > 0:
				# rxvt.current_weapon = "plasma"
				# try:
					# thread.start_new_thread(plasma, ("Thread-plasma", 0.001, screen, plasma_sound, rxvt.x + game.x, rxvt.y + game.y, rxvt.angle, rxvt.ammo, monster, game, global_player, 'rxvt'))
				# except:
					# print "Error: unable to start rxvt plasma thread"
			# elif rxvt.ammo['laser'] > 0:
				# rxvt.current_weapon = "laser"
				# try:
					# thread.start_new_thread(laser, ("Thread-laser", 0.001, screen, laser_sound, rxvt.x + game.x, rxvt.y + game.y, rxvt.angle, rxvt.ammo, monster, game, global_player, 'rxvt'))
				# except:
					# print "Error: unable to start rxvt laser thread"
			# elif rxvt.ammo['freezer'] > 0:
				# rxvt.current_weapon = "freezer"
				# try:
					# thread.start_new_thread(freezer, ("Thread-freezer", 0.001, screen, freezer_sound, rxvt.x + game.x, rxvt.y + game.y, rxvt.angle, rxvt.ammo, monster, game, global_player, 'rxvt'))
				# except:
					# print "Error: unable to start rxvt freezer thread"
			
		if george.alive():
			if (game.number_of_players == 2 and not nash.alive()) or (game.number_of_players == 3 and not nash.alive() and not james.alive()):
				
				#fix this!!
				#fix this!!
				# fix this!!! to avoid errors in the future (if player step will be bigger than 8, 
				# or it will be upgraded (and it WILL be sometimes during the game)) - change "- 10" and "+ 10" to "-george.players_speed - 5" and "-george.players_speed - 5" or something like that
				# -5/+5 or some other values
				# otherwise the map won't scroll somethimes, because player won't hit the center of a screen (resolution / 2)
				
				# move player if possible
				if (george.x + george.offsetX) >= 0 and (george.x + george.offsetX) < resolution[0] - 60:
					if george.x + george.offsetX - game.x > 0 \
						and george.x + george.offsetX - game.x < game.map_size_x \
						and george.y + george.offsetY - game.y >= 0 \
						and george.y + george.offsetY - game.y < game.map_size_y:
						if game.pixel_table[int(george.x + george.offsetX - game.x)][int(george.y + george.offsetY - game.y)] == 0:
							if game.x - george.offsetX <= 0 and game.x - george.offsetX > (-game.map_size_x + resolution[0]) and george.x >= resolution[0] / 2 - 10 and george.x <= resolution[0] / 2 + 10:
								
								george.x = resolution[0] / 2
								game.x -= george.offsetX
								
							else:
								george.x += george.offsetX
						
						elif game.pixel_table[int(george.x + george.offsetX - game.x)][int(george.y - game.y)] == 0:
							if game.x - george.offsetX <= 0 and game.x - george.offsetX > (-game.map_size_x + resolution[0]) and george.x >= resolution[0] / 2 - 10 and george.x <= resolution[0] / 2 + 10:
								
								george.x = resolution[0] / 2
								game.x -= george.offsetX
								
							else:
								george.x += george.offsetX
			
				if  (george.y + george.offsetY) >= 30 and (george.y + george.offsetY) < resolution[1] - game.screen_bottom_player:
					if george.x + george.offsetX - game.x >= 0 \
						and george.x + george.offsetX - game.x < game.map_size_x \
						and george.y + george.offsetY - game.y >= 0 \
						and george.y + george.offsetY - game.y < game.map_size_y:
						if game.pixel_table[int(george.x + george.offsetX - game.x)][int(george.y + george.offsetY - game.y)] == 0:
							if game.y - george.offsetY <= 0 and game.y - george.offsetY > (-game.map_size_y + resolution[1]) and george.y >= resolution[1] / 2 - 10 and george.y <= resolution[1] / 2 + 10:
								
								george.y = resolution[1] / 2
								game.y -= george.offsetY
								
							else:
								george.y += george.offsetY

						elif game.pixel_table[int(george.x - game.x)][int(george.y + george.offsetY - game.y)] == 0:
							if game.y - george.offsetY <= 0 and game.y - george.offsetY > (-game.map_size_y + resolution[1]) and george.y >= resolution[1] / 2 - 10 and george.y <= resolution[1] / 2 + 10:
								
								george.y = resolution[1] / 2
								game.y -= george.offsetY
								
							else:
								george.y += george.offsetY
		
			if game.number_of_players == 2:
											
				#move player if possible
				if (george.x + george.offsetX) >= 60 and (george.x + george.offsetX) < resolution[0] - 90:
					if george.x + george.offsetX - game.x > 0 \
						and george.x + george.offsetX - game.x < game.map_size_x \
						and george.y + george.offsetY - game.y >= 0 \
						and george.y + george.offsetY - game.y < game.map_size_y:
						if game.pixel_table[int(george.x + george.offsetX - game.x)][int(george.y + george.offsetY - game.y)] == 0:
							if game.x - george.offsetX <= 0 and game.x - george.offsetX > (-game.map_size_x + resolution[0]) \
							and ((george.offsetX > 0 and center_x >= resolution[0] / 2 - 10) or (george.offsetX < 0 and center_x <= resolution[0] / 2 + 10)):
											
								game.x -= george.offsetX
								nash.x -= george.offsetX
									
							else:
								george.x += george.offsetX
						
						elif game.pixel_table[int(george.x + george.offsetX - game.x)][int(george.y - game.y)] == 0:
							if game.x - george.offsetX <= 0 and game.x - george.offsetX > (-game.map_size_x + resolution[0]) \
							and ((george.offsetX > 0 and center_x >= resolution[0] / 2 - 10) or (george.offsetX < 0 and center_x <= resolution[0] / 2 + 10)):
									
								game.x -= george.offsetX
								nash.x -= george.offsetX
									
							else:
								george.x += george.offsetX
				
				if  (george.y + george.offsetY) >= 60 and (george.y + george.offsetY) < resolution[1] - game.screen_bottom_player:
					if george.x + george.offsetX - game.x >= 0 \
						and george.x + george.offsetX - game.x < game.map_size_x \
						and george.y + george.offsetY - game.y >= 0 \
						and george.y + george.offsetY - game.y < game.map_size_y:
						if game.pixel_table[int(george.x + george.offsetX - game.x)][int(george.y + george.offsetY - game.y)] == 0:
							if game.y - george.offsetY <= 0 and game.y - george.offsetY > (-game.map_size_y + resolution[1]) \
							and ((george.offsetY > 0 and center_y >= resolution[1] / 2 - 10) or (george.offsetY < 0 and center_y <= resolution[1] / 2 + 10)):
							
								game.y -= george.offsetY
								nash.y -= george.offsetY
								
							else:
								george.y += george.offsetY

						elif game.pixel_table[int(george.x - game.x)][int(george.y + george.offsetY - game.y)] == 0:
							if game.y - george.offsetY <= 0 and game.y - george.offsetY > (-game.map_size_y + resolution[1]) \
							and ((george.offsetY > 0 and center_y >= resolution[1] / 2 - 10) or (george.offsetY < 0 and center_y <= resolution[1] / 2 + 10)):
							
								game.y -= george.offsetY
								nash.y -= george.offsetY
									
							else:
								george.y += george.offsetY

			elif game.number_of_players == 3:
				#compute the x center of players
				max_x = max(nash.x, george.x, james.x)
				min_x = min(nash.x, george.x, james.x)
				
				if min_x != max_x:
					center_x = min_x + (max_x - min_x) / 2
				else:
					center_x = min_x
					
				#compute the y center of players
				max_y = max(nash.y, george.y, james.y)
				min_y = min(nash.y, george.y, james.y)
				
				if min_y != max_y:
					center_y = min_y + (max_y - min_y) / 2
				else:
					center_y = min_y
				
				#move player if possible
				if (george.x + george.offsetX) >= 0 and (george.x + george.offsetX) < resolution[0] - 60:
					if george.x + george.offsetX - game.x > 0 \
						and george.x + george.offsetX - game.x < game.map_size_x \
						and george.y + george.offsetY - game.y >= 0 \
						and george.y + george.offsetY - game.y < game.map_size_y:
						if game.pixel_table[int(george.x + george.offsetX - game.x)][int(george.y + george.offsetY - game.y)] == 0:
							if game.x - george.offsetX < 0 and game.x - george.offsetX > (-game.map_size_x + resolution[0]) and center_x >= resolution[0] / 2 - 10 and center_x <= resolution[0] / 2 + 10:
							# if game.x - george.offsetX < 0 and game.x - george.offsetX > (-4000 + resolution[0]):
								
								game.x -= george.offsetX
								nash.x -= george.offsetX
								james.x -= george.offsetX
								
							else:
								george.x += george.offsetX
						
						elif game.pixel_table[int(george.x + george.offsetX - game.x)][int(george.y - game.y)] == 0:
							if game.x - george.offsetX < 0 and game.x - george.offsetX > (-game.map_size_x + resolution[0]) and center_x >= resolution[0] / 2 - 10 and center_x <= resolution[0] / 2 + 10:
							# if game.x - george.offsetX < 0 and game.x - george.offsetX > (-4000 + resolution[0]):
								
								game.x -= george.offsetX
								nash.x -= george.offsetX
								james.x -= george.offsetX
								
							else:
								george.x += george.offsetX
				
				if  (george.y + george.offsetY) >= 30 and (george.y + george.offsetY) < resolution[1] - game.screen_bottom_player:
					if george.x + george.offsetX - game.x >= 0 \
						and george.x + george.offsetX - game.x < game.map_size_x \
						and george.y + george.offsetY - game.y >= 0 \
						and george.y + george.offsetY - game.y < game.map_size_y:
						if game.pixel_table[int(george.x + george.offsetX - game.x)][int(george.y + george.offsetY - game.y)] == 0:
							if game.y - george.offsetY < 0 and game.y - george.offsetY > (-game.map_size_y + resolution[1]) and center_y >= resolution[1] / 2 - 10 and center_y <= resolution[1] / 2 + 10:
							# if game.y - george.offsetY < 0 and game.y - george.offsetY > (-4000 + resolution[1]):
								
								game.y -= george.offsetY
								nash.y -= george.offsetY
								james.y -= george.offsetY
								
							else:
								george.y += george.offsetY

						elif game.pixel_table[int(george.x - game.x)][int(george.y + george.offsetY - game.y)] == 0:
							if game.y - george.offsetY < 0 and game.y - george.offsetY > (-game.map_size_y + resolution[1]) and center_y >= resolution[1] / 2 - 10 and center_y <= resolution[1] / 2 + 10:
							# if game.y - george.offsetY < 0 and game.y - george.offsetY > (-4000 + resolution[1]):
								
								game.y -= george.offsetY
								nash.y -= george.offsetY
								james.y -= george.offsetY
								
							else:
								george.y += george.offsetY
			
			#RIGHT
			if george.offsetX > 0:
				george.model = pygame.image.load('data/images/players/george/george-90.png')
				george.pain_model = pygame.image.load('data/images/players/george/george_pain-90.png')
				george.angle = 90
			#LEFT
			if george.offsetX < 0:
				george.model = pygame.image.load('data/images/players/george/george-270.png')
				george.pain_model = pygame.image.load('data/images/players/george/george_pain-270.png')
				george.angle = 270
			#DOWN
			if george.offsetY > 0:
				george.model = pygame.image.load('data/images/players/george/george-180.png')
				george.pain_model = pygame.image.load('data/images/players/george/george_pain-180.png')
				george.angle = 180
			#UP
			if george.offsetY < 0:
				george.model = pygame.image.load('data/images/players/george/george-0.png')
				george.pain_model = pygame.image.load('data/images/players/george/george_pain-0.png')
				george.angle = 0
			
			#diagonal directions
			if george.offsetX < 0 and george.offsetY < 0:
				george.model = pygame.image.load('data/images/players/george/george-315.png')
				george.pain_model = pygame.image.load('data/images/players/george/george_pain-315.png')
				george.angle = 315
			if george.offsetX < 0 and george.offsetY > 0:
				george.model = pygame.image.load('data/images/players/george/george-225.png')
				george.pain_model = pygame.image.load('data/images/players/george/george_pain-225.png')
				george.angle = 225
			if george.offsetX > 0 and george.offsetY > 0:
				george.model = pygame.image.load('data/images/players/george/george-135.png')
				george.pain_model = pygame.image.load('data/images/players/george/george_pain-135.png')
				george.angle = 135
			if george.offsetX > 0 and george.offsetY < 0:
				george.model = pygame.image.load('data/images/players/george/george-45.png')
				george.pain_model = pygame.image.load('data/images/players/george/george_pain-45.png')
				george.angle = 45
			
			#found bonus?
			for bonus in game.bonuses:
				if bonus.taken == False:
					if (math.fabs(george.x + 32 - (bonus.x + 16 + game.x)) < 50) and (math.fabs(george.y + 32 - (bonus.y + 16 + game.y)) < 50):
						bonus.taken = True
						#medkit
						if bonus.which_one == 0:
							if nash.alive():
								nash.add_energy(game.medkit_ammount + nash.add_energy_booster)
							if george.alive():
								george.add_energy(game.medkit_ammount + george.add_energy_booster)
							if james.alive():
								james.add_energy(game.medkit_ammount + james.add_energy_booster)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
						#gasoline
						elif bonus.which_one == 1:
							nash.add_ammo('flamethrower', game.bonus_flamethrower_ammo)
							george.add_ammo('flamethrower', game.bonus_flamethrower_ammo)
							james.add_ammo('flamethrower', game.bonus_flamethrower_ammo)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
						#refrigerant
						elif bonus.which_one == 2:
							nash.add_ammo('freezer', game.bonus_freezer_ammo)
							george.add_ammo('freezer', game.bonus_freezer_ammo)
							james.add_ammo('freezer', game.bonus_freezer_ammo)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
						#laser
						elif bonus.which_one == 3:
							game.laser_power += game.laser_power_boost
							# george.laser_time_upgrade += 1
																				
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
						#plasma
						elif bonus.which_one == 4:
							nash.add_ammo('plasma', game.plasma_spheres)
							george.add_ammo('plasma', game.plasma_spheres)
							james.add_ammo('plasma', game.plasma_spheres)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
						#vortex
						elif bonus.which_one == 5:
							if nash.ammo['vortex'] < 1:
								nash.add_ammo('vortex', 1)
							
							nash.money += 50
							game.points += 50
							if game.number_of_players > 1:
								george.money += 50
							elif game.number_of_players > 2:
								james.money += 50
								
						#green money
						elif bonus.which_one == 6:
							nash.money += game.green_money
							game.points += game.green_money
							if game.number_of_players > 1:
								george.money += game.green_money
							elif game.number_of_players > 2:
								james.money += game.green_money
						#gold money
						elif bonus.which_one == 7:
							nash.money += game.gold_money
							game.points += game.gold_money
							if game.number_of_players > 1:
								george.money += game.gold_money
							elif game.number_of_players > 2:
								james.money += game.gold_money
							
			#found key?
			for key in game.keys:
				if key.taken == False:
					if (math.fabs(george.x + 32 - (key.x + 16 + game.x)) < 70) and (math.fabs(george.y + 32 - (key.y + 16 + game.y)) < 70):
						key.taken = True
						#blue key
						if key.which_one == 0:
							game.keys_possesed.append("blue")
						elif key.which_one == 1:
							game.keys_possesed.append("red")
						elif key.which_one == 2:
							game.keys_possesed.append("green")
						elif key.which_one == 3:
							game.keys_possesed.append("yellow")
							
			if len(game.keys_possesed) == 4:
				game.exit_opened = True
			
			#auto-enable armor for george?
			if george.energy < george.ff_auto_enable_level and george.has_force_field:
				george.force_field_enabled = True
			
			if george.force_field_enabled:
				if george.force_field > 0:
					george.force_field -= 1
					george.armor = 200
					pygame.draw.circle(screen, (0, 255, 0), (george.x + 32, george.y + 32), 55, 8)
				else:
					george.force_field_enabled = False
					george.armor = george.base_armor
			else:
				george.armor = george.base_armor
			
			#change weapon?
			if george.next_weapon == True:
				george.next_weapon = False
				if george.current_weapon == "flamethrower":
					george.current_weapon = "freezer"
				elif george.current_weapon == "freezer":
					george.current_weapon = "laser"
				elif george.current_weapon == "laser":
					george.current_weapon = "flamethrower"
			
			#fire weapon?
			if george.fire == True and not george.in_mass:
				if george.current_weapon == "laser":
					try:
						_thread.start_new_thread(laser, ("Thread-laser", 0.001, screen, laser_sound, george.x, george.y, george.angle, george.ammo, monster, game, global_player, 'george'))
					except:
						print("Error: unable to start flamethrower thread")
				elif george.current_weapon == "flamethrower":
					try:
						_thread.start_new_thread(flamethrower, ("Thread-flamethrower", 0.001, screen, flamethrower_sound, george.x, george.y, george.angle, george.ammo, monster, game, global_player, 'george'))
					except:
						print("Error: unable to start flamethrower thread")
				elif george.current_weapon == "freezer":
					try:
						_thread.start_new_thread(freezer, ("Thread-freezer", 0.001, screen, freezer_sound, george.x, george.y, george.angle, george.ammo, monster, game, global_player, 'george'))
					except:
						print("Error: unable to start freezer thread")
				elif george.current_weapon == "plasma":
					try:
						_thread.start_new_thread(plasma, ("Thread-plasma", 0.001, screen, plasma_sound, george.x, george.y, george.angle, george.ammo, monster, game, global_player, 'george'))
					except:
						print("Error: unable to start plasma thread")
						
		if james.alive():
			if not nash.alive() and not george.alive():
						
				# move player if possible
				if (james.x + james.offsetX) >= 0 and (james.x + james.offsetX) < resolution[0] - 60:
					if james.x + james.offsetX - game.x > 0 \
						and james.x + james.offsetX - game.x < game.map_size_x \
						and james.y + james.offsetY - game.y >= 0 \
						and james.y + james.offsetY - game.y < game.map_size_y:
						if game.pixel_table[int(james.x + james.offsetX - game.x)][int(james.y + james.offsetY - game.y)] == 0:
							if game.x - james.offsetX < 0 and game.x - james.offsetX > (-game.map_size_x + resolution[0]) and james.x >= resolution[0] / 2 - 10 and james.x <= resolution[0] / 2 + 10:
								
								james.x = resolution[0] / 2
								game.x -= james.offsetX
								
							else:
								james.x += james.offsetX
						
						elif game.pixel_table[int(james.x + james.offsetX - game.x)][int(james.y - game.y)] == 0:
							if game.x - james.offsetX < 0 and game.x - james.offsetX > (-game.map_size_x + resolution[0]) and james.x >= resolution[0] / 2 - 10 and james.x <= resolution[0] / 2 + 10:
								
								james.x = resolution[0] / 2
								game.x -= james.offsetX
								
							else:
								james.x += james.offsetX
			
				if  (james.y + james.offsetY) >= 30 and (james.y + james.offsetY) < resolution[1] - game.screen_bottom_player:
					if james.x + james.offsetX - game.x >= 0 \
						and james.x + james.offsetX - game.x < game.map_size_x \
						and james.y + james.offsetY - game.y >= 0 \
						and james.y + james.offsetY - game.y < game.map_size_y:
						if game.pixel_table[int(james.x + james.offsetX - game.x)][int(james.y + james.offsetY - game.y)] == 0:
							if game.y - james.offsetY < 0 and game.y - james.offsetY > (-game.map_size_y + resolution[1]) and james.y >= resolution[1] / 2 - 10 and james.y <= resolution[1] / 2 + 10:
								
								james.y = resolution[1] / 2
								game.y -= james.offsetY
								
							else:
								james.y += james.offsetY

						elif game.pixel_table[int(james.x - game.x)][int(james.y + james.offsetY - game.y)] == 0:
							if game.y - james.offsetY < 0 and game.y - james.offsetY > (-game.map_size_y + resolution[1]) and james.y >= resolution[1] / 2 - 10 and james.y <= resolution[1] / 2 + 10:
								
								james.y = resolution[1] / 2
								game.y -= james.offsetY
								
							else:
								james.y += james.offsetY
			else:
				#compute the x center of players
				max_x = max(nash.x, george.x, james.x)
				min_x = min(nash.x, george.x, james.x)
				
				if min_x != max_x:
					center_x = min_x + (max_x - min_x) / 2
				else:
					center_x = min_x
					
				#compute the y center of players
				max_y = max(nash.y, george.y, james.y)
				min_y = min(nash.y, george.y, james.y)
				
				if min_y != max_y:
					center_y = min_y + (max_y - min_y) / 2
				else:
					center_y = min_y
				
				#move player if possible
				if (james.x + james.offsetX) >= 0 and (james.x + james.offsetX) < resolution[0] - 60:
					if james.x + james.offsetX - game.x > 0 \
						and james.x + james.offsetX - game.x < game.map_size_x \
						and james.y + james.offsetY - game.y >= 0 \
						and james.y + james.offsetY - game.y < game.map_size_y:
						if game.pixel_table[int(james.x + james.offsetX - game.x)][int(james.y + james.offsetY - game.y)] == 0:
							if game.x - james.offsetX < 0 and game.x - james.offsetX > (-game.map_size_x + resolution[0]) and center_x >= resolution[0] / 2 - 10 and center_x <= resolution[0] / 2 + 10:
								
								game.x -= james.offsetX
								nash.x -= james.offsetX
								george.x -= james.offsetX
								
							else:
								james.x += james.offsetX
						
						elif game.pixel_table[int(james.x + james.offsetX - game.x)][int(james.y - game.y)] == 0:
							if game.x - james.offsetX < 0 and game.x - james.offsetX > (-game.map_size_x + resolution[0]) and center_x >= resolution[0] / 2 - 10 and center_x <= resolution[0] / 2 + 10:
								
								game.x -= james.offsetX
								nash.x -= james.offsetX
								george.x -= james.offsetX
								
							else:
								james.x += james.offsetX
				
				if  (james.y + james.offsetY) >= 30 and (james.y + james.offsetY) < resolution[1] - game.screen_bottom_player:
					if james.x + james.offsetX - game.x >= 0 \
						and james.x + james.offsetX - game.x < game.map_size_x \
						and james.y + james.offsetY - game.y >= 0 \
						and james.y + james.offsetY - game.y < game.map_size_y:
						if game.pixel_table[int(james.x + james.offsetX - game.x)][int(james.y + james.offsetY - game.y)] == 0:
							if game.y - james.offsetY < 0 and game.y - james.offsetY > (-game.map_size_y + resolution[1]) and center_y >= resolution[1] / 2 - 10 and center_y <= resolution[1] / 2 + 10:
								
								game.y -= james.offsetY
								nash.y -= james.offsetY
								george.y -= james.offsetY
								
							else:
								james.y += james.offsetY

						elif game.pixel_table[int(james.x - game.x)][int(james.y + james.offsetY - game.y)] == 0:
							# james.offsetX = 0
							if game.y - james.offsetY < 0 and game.y - james.offsetY > (-game.map_size_y + resolution[1]) and center_y >= resolution[1] / 2 - 10 and center_y <= resolution[1] / 2 + 10:
								
								game.y -= james.offsetY
								nash.y -= james.offsetY
								george.y -= james.offsetY
								
							else:
								james.y += james.offsetY					

			#RIGHT
			if james.offsetX > 0:
				james.model = pygame.image.load('data/images/players/james/james-90.png')
				james.pain_model = pygame.image.load('data/images/players/james/james_pain-90.png')
				james.angle = 90
			#LEFT
			if james.offsetX < 0:
				james.model = pygame.image.load('data/images/players/james/james-270.png')
				james.pain_model = pygame.image.load('data/images/players/james/james_pain-270.png')
				james.angle = 270
			#DOWN
			if james.offsetY > 0:
				james.model = pygame.image.load('data/images/players/james/james-180.png')
				james.pain_model = pygame.image.load('data/images/players/james/james_pain-180.png')
				james.angle = 180
			#UP
			if james.offsetY < 0:
				james.model = pygame.image.load('data/images/players/james/james-0.png')
				james.pain_model = pygame.image.load('data/images/players/james/james_pain-0.png')
				james.angle = 0
			
			#diagonal directions
			if james.offsetX < 0 and james.offsetY < 0:
				james.model = pygame.image.load('data/images/players/james/james-315.png')
				james.pain_model = pygame.image.load('data/images/players/james/james_pain-315.png')
				james.angle = 315
			if james.offsetX < 0 and james.offsetY > 0:
				james.model = pygame.image.load('data/images/players/james/james-225.png')
				james.pain_model = pygame.image.load('data/images/players/james/james_pain-225.png')
				james.angle = 225
			if james.offsetX > 0 and james.offsetY > 0:
				james.model = pygame.image.load('data/images/players/james/james-135.png')
				james.pain_model = pygame.image.load('data/images/players/james/james_pain-135.png')
				james.angle = 135
			if james.offsetX > 0 and james.offsetY < 0:
				james.model = pygame.image.load('data/images/players/james/james-45.png')
				james.pain_model = pygame.image.load('data/images/players/james/james_pain-45.png')
				james.angle = 45
			
			#found bonus?
			for bonus in game.bonuses:
				if bonus.taken == False:
					if (math.fabs(james.x + 32 - (bonus.x + 16 + game.x)) < 50) and (math.fabs(james.y + 32 - (bonus.y + 16 + game.y)) < 50):
						bonus.taken = True
						#medkit
						if bonus.which_one == 0:
							if nash.alive():
								nash.add_energy(game.medkit_ammount + nash.add_energy_booster)
							if george.alive():
								george.add_energy(game.medkit_ammount + george.add_energy_booster)
							if james.alive():
								james.add_energy(game.medkit_ammount + james.add_energy_booster)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
						#gasoline
						elif bonus.which_one == 1:
							nash.add_ammo('flamethrower', game.bonus_flamethrower_ammo)
							george.add_ammo('flamethrower', game.bonus_flamethrower_ammo)
							james.add_ammo('flamethrower', game.bonus_flamethrower_ammo)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
						#refrigerant
						elif bonus.which_one == 2:
							nash.add_ammo('freezer', game.bonus_freezer_ammo)
							george.add_ammo('freezer', game.bonus_freezer_ammo)
							james.add_ammo('freezer', game.bonus_freezer_ammo)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
						#laser
						elif bonus.which_one == 3:
							game.laser_power += game.laser_power_boost
							# james.laser_time_upgrade += 1
														
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
						#plasma
						elif bonus.which_one == 4:
							nash.add_ammo('plasma', game.plasma_spheres)
							george.add_ammo('plasma', game.plasma_spheres)
							james.add_ammo('plasma', game.plasma_spheres)
							
							nash.money += 10
							game.points += 10
							if game.number_of_players > 1:
								george.money += 10
							elif game.number_of_players > 2:
								james.money += 10
						#vortex
						elif bonus.which_one == 5:
							if nash.ammo['vortex'] < 1:
								nash.add_ammo('vortex', 1)
							
							nash.money += 50
							game.points += 50
							if game.number_of_players > 1:
								george.money += 50
							elif game.number_of_players > 2:
								james.money += 50
								
						#green money
						elif bonus.which_one == 6:
							nash.money += game.green_money
							game.points += game.green_money
							if game.number_of_players > 1:
								george.money += game.green_money
							elif game.number_of_players > 2:
								james.money += game.green_money
						#gold money
						elif bonus.which_one == 7:
							nash.money += game.gold_money
							game.points += game.gold_money
							if game.number_of_players > 1:
								george.money += game.gold_money
							elif game.number_of_players > 2:
								james.money += game.gold_money
							
			#found key?
			for key in game.keys:
				if key.taken == False:
					if (math.fabs(james.x + 32 - (key.x + 16 + game.x)) < 70) and (math.fabs(james.y + 32 - (key.y + 16 + game.y)) < 70):
						key.taken = True
						#blue key
						if key.which_one == 0:
							game.keys_possesed.append("blue")
						elif key.which_one == 1:
							game.keys_possesed.append("red")
						elif key.which_one == 2:
							game.keys_possesed.append("green")
						elif key.which_one == 3:
							game.keys_possesed.append("yellow")
							
			if len(game.keys_possesed) == 4:
				game.exit_opened = True
				
			#auto-enable armor for james?
			if james.energy < james.ff_auto_enable_level and james.has_force_field:
				james.force_field_enabled = True
			
			if james.force_field_enabled:
				if james.force_field > 0:
					james.force_field -= 1
					james.armor = 200
					pygame.draw.circle(screen, (0, 255, 0), (james.x + 32, james.y + 32), 55, 8)
				else:
					james.force_field_enabled = False
					james.armor = james.base_armor
			else:
				james.armor = james.base_armor
			
			#change weapon?
			if james.next_weapon == True:
				james.next_weapon = False
				if james.current_weapon == "flamethrower":
					james.current_weapon = "freezer"
				elif james.current_weapon == "freezer":
					james.current_weapon = "laser"
				elif james.current_weapon == "laser":
					james.current_weapon = "flamethrower"
			
			#fire weapon?
			if james.fire == True and not george.in_mass:
				if james.current_weapon == "laser":
					try:
						_thread.start_new_thread(laser, ("Thread-laser", 0.001, screen, laser_sound, james.x, james.y, james.angle, james.ammo, monster, game, global_player, 'james'))
					except:
						print("Error: unable to start flamethrower thread")
				elif james.current_weapon == "flamethrower":
					try:
						_thread.start_new_thread(flamethrower, ("Thread-flamethrower", 0.001, screen, flamethrower_sound, james.x, james.y, james.angle, james.ammo, monster, game, global_player, 'james'))
					except:
						print("Error: unable to start flamethrower thread")
				elif james.current_weapon == "freezer":
					try:
						_thread.start_new_thread(freezer, ("Thread-freezer", 0.001, screen, freezer_sound, james.x, james.y, james.angle, james.ammo, monster, game, global_player, 'james'))
					except:
						print("Error: unable to start freezer thread")
				elif james.current_weapon == "plasma":
					try:
						_thread.start_new_thread(plasma, ("Thread-plasma", 0.001, screen, plasma_sound, james.x, james.y, james.angle, james.ammo, monster, game, global_player, 'james'))
					except:
						print("Error: unable to start plasma thread")
				
		if nash.alive() or george.alive() or james.alive():
		
			#blit monsters images to the screen (dead ones first so they will be at the bottom and player can walk on their dead bodies, then player, then monsters, so they can make an illusion that they cover player all over
			for spider in monster.monsters:
				if spider.energy <= 0 and spider.decay > 0:
					spider.decay -= 1
					if spider.frozen == True:
						screen.blit(spider.frozen_model, (spider.x + game.x, spider.y + game.y))
						if spider.death_sound_played == False:
							spider.death_sound_played = True
							spider_death_sound.play()
					elif spider.killed == True:
						screen.blit(spider.dead_model, (spider.x + game.x, spider.y + game.y))
						if spider.death_sound_played == False:
							spider.death_sound_played = True
							spider_death_sound.play()
					elif spider.fried == True:
						screen.blit(spider.fried_model, (spider.x + game.x, spider.y + game.y))
						if spider.death_sound_played == False:
							spider.death_sound_played = True
							spider_death_sound.play()
	
			for gigantula in monster.gigantulas:
				if gigantula.energy <= 0 and gigantula.decay > 0:
					gigantula.decay -= 1
					if gigantula.frozen == True:
						screen.blit(gigantula.frozen_model, (gigantula.x + game.x, gigantula.y + game.y))
						if gigantula.death_sound_played == False:
							gigantula.death_sound_played = True
							gigantula_death_sound.play()
					elif gigantula.killed == True:
						screen.blit(gigantula.dead_model, (gigantula.x + game.x, gigantula.y + game.y))
						if gigantula.death_sound_played == False:
							gigantula.death_sound_played = True
							gigantula_death_sound.play()
					elif gigantula.fried == True:
						screen.blit(gigantula.fried_model, (gigantula.x + game.x, gigantula.y + game.y))
						if gigantula.death_sound_played == False:
							gigantula.death_sound_played = True
							gigantula_death_sound.play()
						
			for robot in monster.robots:
				if robot.energy <= 0 and robot.decay > 0:
					robot.decay -= 1
					if robot.frozen == True:
						screen.blit(robot.frozen_model, (robot.x + game.x, robot.y + game.y))
						if robot.death_sound_played == False:
							robot.death_sound_played = True
							robot_death_sound.play()
					elif robot.killed == True:
						screen.blit(robot.dead_model, (robot.x + game.x, robot.y + game.y))
						if robot.death_sound_played == False:
							robot.death_sound_played = True
							robot_death_sound.play()
					elif robot.fried == True:
						screen.blit(robot.fried_model, (robot.x + game.x, robot.y + game.y))
						if robot.death_sound_played == False:
							robot.death_sound_played = True
							robot_death_sound.play()
							
			for hunter in monster.hunters:
				if hunter.energy <= 0 and hunter.decay > 0:
					hunter.decay -= 1
					if hunter.frozen == True:
						screen.blit(hunter.frozen_model, (hunter.x + game.x, hunter.y + game.y))
						if hunter.death_sound_played == False:
							hunter.death_sound_played = True
							hunter_death_sound.play()
					elif hunter.killed == True:
						screen.blit(hunter.dead_model, (hunter.x + game.x, hunter.y + game.y))
						if hunter.death_sound_played == False:
							hunter.death_sound_played = True
							hunter_death_sound.play()
					elif hunter.fried == True:
						screen.blit(hunter.fried_model, (hunter.x + game.x, hunter.y + game.y))
						if hunter.death_sound_played == False:
							hunter.death_sound_played = True
							hunter_death_sound.play()
			
			if nash.alive():
				screen.blit(nash.model, (nash.x, nash.y))
				if nash.being_attacked == True:
					nash.being_attacked = False
					screen.blit(nash.pain_model, (nash.x, nash.y))
		
			if george.alive():
				screen.blit(george.model, (george.x, george.y))
				if george.being_attacked == True:
					george.being_attacked = False
					screen.blit(george.pain_model, (george.x, george.y))
				
			if james.alive():
				screen.blit(james.model, (james.x, james.y))
				if james.being_attacked == True:
					james.being_attacked = False
					screen.blit(james.pain_model, (james.x, james.y))
			
			if rxvt.alive():
				screen.blit(rxvt.model, (rxvt.x + game.x, rxvt.y + game.y))

			#blit alive monsters
			for spider in monster.monsters:
				if spider.energy > 0:
					screen.blit(spider.model, (spider.x + spider.offsetX + game.x, spider.y + spider.offsetY + game.y))
					
			for gigantula in monster.gigantulas:
				if gigantula.energy > 0:
					screen.blit(gigantula.model, (gigantula.x + game.x, gigantula.y + game.y))
					
			for robot in monster.robots:
				if robot.energy > 0:
					screen.blit(robot.model, (robot.x + game.x, robot.y + game.y))
					
			for crane in monster.cranes:
				if crane.energy > 0:
					screen.blit(crane.model, (crane.x + game.x, crane.y + game.y))
					
			for hunter in monster.hunters:
				if hunter.energy > 0:
					screen.blit(hunter.model, (hunter.x + game.x, hunter.y + game.y))
					
			#crane is very big, so even if he's "dead" draw him above the player
			for crane in monster.cranes:
				if crane.energy <= 0 and crane.decay > 0:
					crane.decay -= 1
					if crane.frozen == True:
						screen.blit(crane.frozen_model, (crane.x + game.x, crane.y + game.y))
						if crane.death_sound_played == False:
							crane.death_sound_played = True
							crane_death_sound.play()
					elif crane.killed == True:
						screen.blit(crane.dead_model, (crane.x + game.x, crane.y + game.y))
						if crane.death_sound_played == False:
							crane.death_sound_played = True
							crane_death_sound.play()
					elif crane.fried == True:
						screen.blit(crane.fried_model, (crane.x + game.x, crane.y + game.y))
						if crane.death_sound_played == False:
							crane.death_sound_played = True
							crane_death_sound.play()
							
			if game.boss.energy > 0:
				screen.blit(game.boss.model, (game.boss.x + game.x, game.boss.y + game.y))
		
			#menu upper belt
			pygame.draw.rect(screen, (0, 0, 0), (0, 0, resolution[0], 30), 0)
			
			#menu lower belt
			pygame.draw.rect(screen, (0, 0, 0), (0, resolution[1] - 152, resolution[0], resolution[1]), 0)
		
			# Render the text

			# nash_energy_label = font.render('Energy: ' + str(int(nash.energy)) + '/' + str(int(nash.max_energy)), True, (0, 255, 0), (0, 0, 0))
			
			# pygame.draw.line(screen, (255, 255, 255), (8, resolution[1] - 150), (8, resolution[1] - 135), 2)
			
			
			
			# pygame.draw.rect(screen, (255, 255, 255), (8, resolution[1] - 150, 110, 17), 2)
			
			if nash.energy > 0:
				for i in range(int(nash.energy * 2.5)):
					pygame.draw.line(screen, (255, 0, 0), (10 + i, resolution[1] - 148), (10 + i, resolution[1] - 117), 1)
			
			# horizontal lines arround energy bar
			pygame.draw.line(screen, (255, 255, 255), (8, resolution[1] - 150), (260, resolution[1] - 150), 2)
			pygame.draw.line(screen, (255, 255, 255), (8, resolution[1] - 116), (260, resolution[1] - 116), 2)
			
			# vertical lines arround energy bar
			pygame.draw.line(screen, (255, 255, 255), (8, resolution[1] - 150), (8, resolution[1] - 116), 2)
			pygame.draw.line(screen, (255, 255, 255), (260, resolution[1] - 150), (260, resolution[1] - 115), 2)
			
			
			# if nash.current_weapon == 'flamethrower':
				# nash_ammo_label = font.render(nash.current_weapon + ' ammo: ' + str(nash.ammo[nash.current_weapon] / 100), True, (0, 255, 0), (0, 0, 0))
			# elif nash.current_weapon == 'laser':
				# nash_ammo_label = font.render(nash.current_weapon + ' ammo: ' + str(nash.ammo[nash.current_weapon] / 10), True, (0, 255, 0), (0, 0, 0))
			# elif nash.current_weapon == 'freezer':
				# nash_ammo_label = font.render(nash.current_weapon + ' ammo: ' + str(nash.ammo[nash.current_weapon] / 10), True, (0, 255, 0), (0, 0, 0))
			# elif nash.current_weapon == 'plasma':
				# nash_ammo_label = font.render(nash.current_weapon + ' ammo: ' + str(nash.ammo[nash.current_weapon] / 10), True, (0, 255, 0), (0, 0, 0))
			
			level_label = font.render('level: ' + str(game.level), True, (0, 255, 0), (0, 0, 0))
			
#			george_energy_label = font.render('Energy: ' + str(int(george.energy)) + '/' + str(int(george.max_energy)), True, (0, 100, 255), (0, 0, 0))

			if game.number_of_players > 1:
				if george.energy > 0:
					for i in range(int(george.energy * 2.5)):
						pygame.draw.line(screen, (255, 0, 0), (310 + i, resolution[1] - 148), (310 + i, resolution[1] - 117), 1)
			
				# horizontal lines arround energy bar
				pygame.draw.line(screen, (255, 255, 255), (308, resolution[1] - 150), (560, resolution[1] - 150), 2)
				pygame.draw.line(screen, (255, 255, 255), (308, resolution[1] - 116), (560, resolution[1] - 116), 2)
			
				# vertical lines arround energy bar
				pygame.draw.line(screen, (255, 255, 255), (308, resolution[1] - 150), (308, resolution[1] - 116), 2)
				pygame.draw.line(screen, (255, 255, 255), (560, resolution[1] - 150), (560, resolution[1] - 115), 2)
			
			
#			if george.current_weapon == 'flamethrower':
#				george_ammo_label = font.render(george.current_weapon + ' ammo: ' + str(george.ammo[george.current_weapon] / 100), True, (0, 100, 255), (0, 0, 0))
#			elif george.current_weapon == 'laser':
#				george_ammo_label = font.render(george.current_weapon + ' ammo: ' + str(george.ammo[george.current_weapon] / 10), True, (0, 100, 255), (0, 0, 0))
#			elif george.current_weapon == 'freezer':
#				george_ammo_label = font.render(george.current_weapon + ' ammo: ' + str(george.ammo[george.current_weapon] / 10), True, (0, 100, 255), (0, 0, 0))
#			elif george.current_weapon == 'plasma':
#				george_ammo_label = font.render(george.current_weapon + ' ammo: ' + str(george.ammo[george.current_weapon] / 10), True, (0, 100, 255), (0, 0, 0))
				
			james_energy_label = font.render('Energy: ' + str(int(james.energy)) + '/' + str(int(james.max_energy)), True, (255, 255, 0), (0, 0, 0))
			
			if james.current_weapon == 'flamethrower':
				james_ammo_label = font.render(james.current_weapon + ' ammo: ' + str(james.ammo[james.current_weapon] / 100), True, (255, 255, 0), (0, 0, 0))
			elif james.current_weapon == 'laser':
				james_ammo_label = font.render(james.current_weapon + ' ammo: ' + str(james.ammo[james.current_weapon] / 10), True, (255, 255, 0), (0, 0, 0))
			elif james.current_weapon == 'freezer':
				james_ammo_label = font.render(james.current_weapon + ' ammo: ' + str(james.ammo[james.current_weapon] / 10), True, (255, 255, 0), (0, 0, 0))
			elif james.current_weapon == 'plasma':
				james_ammo_label = font.render(james.current_weapon + ' ammo: ' + str(james.ammo[james.current_weapon] / 10), True, (255, 255, 0), (0, 0, 0))
							
			money_label = font.render('money: ' + str(nash.money), True, (0, 255, 100), (0, 0, 0))
			if game.number_of_players > 1:
				money_label = font.render('money: ' + str(nash.money + george.money), True, (0, 255, 100), (0, 0, 0))
			if game.number_of_players > 2:
				money_label = font.render('money: ' + str(nash.money + george.money + james.money), True, (0, 255, 100), (0, 0, 0))	
			
			ammo_bars_y_offset = 1
			
			# nash ammo bars
			if nash.ammo['flamethrower'] > 0:
				for i in range(int(nash.ammo['flamethrower'] / 100)):
					pygame.draw.line(screen, (255, 70, 0), (10 + i, resolution[1] - 110 + ammo_bars_y_offset), (10 + i, resolution[1] - 104 + ammo_bars_y_offset), 1)
					
			if nash.ammo['plasma'] > 0:
				for i in range(int(nash.ammo['plasma'] / 2)):
					pygame.draw.line(screen, (0, 200, 0), (10 + i, resolution[1] - 100 + ammo_bars_y_offset), (10 + i, resolution[1] - 94 + ammo_bars_y_offset), 1)
					
			if nash.ammo['laser'] > 0:
				for i in range(int(nash.ammo['laser'] * 5)):
					pygame.draw.line(screen, (255, 0, 0), (10 + i, resolution[1] - 90 + ammo_bars_y_offset), (10 + i, resolution[1] - 84 + ammo_bars_y_offset), 1)
					
			if nash.ammo['freezer'] > 0:
				for i in range(int(nash.ammo['freezer'] / 8)):
					pygame.draw.line(screen, (0, 0, 255), (10 + i, resolution[1] - 80 + ammo_bars_y_offset), (10 + i, resolution[1] - 74 + ammo_bars_y_offset), 1)
					
					
			# george ammo bars
			if game.number_of_players > 1:
				if george.ammo['flamethrower'] > 0:
					for i in range(int(george.ammo['flamethrower'] / 100)):
						pygame.draw.line(screen, (255, 70, 0), (310 + i, resolution[1] - 110 + ammo_bars_y_offset), (310 + i, resolution[1] - 104 + ammo_bars_y_offset), 1)
					
				if george.ammo['plasma'] > 0:
					for i in range(int(george.ammo['plasma'] / 2)):
						pygame.draw.line(screen, (0, 200, 0), (310 + i, resolution[1] - 100 + ammo_bars_y_offset), (310 + i, resolution[1] - 94 + ammo_bars_y_offset), 1)
					
				if george.ammo['laser'] > 0:
					for i in range(int(george.ammo['laser'] * 5)):
						pygame.draw.line(screen, (255, 0, 0), (310 + i, resolution[1] - 90 + ammo_bars_y_offset), (310 + i, resolution[1] - 84 + ammo_bars_y_offset), 1)
					
				if george.ammo['freezer'] > 0:
					for i in range(int(george.ammo['freezer'] / 8)):
						pygame.draw.line(screen, (0, 0, 255), (310 + i, resolution[1] - 80 + ammo_bars_y_offset), (310 + i, resolution[1] - 74 + ammo_bars_y_offset), 1)
			
			screen.blit(level_label, (430, 0))
			screen.blit(money_label, (600, resolution[1] - 150))
			
			nash_experience_label = font.render('xp: ' + str(int(nash.experience)), True, (0, 255, 0), (0, 0, 0))
			screen.blit(nash_experience_label, (780, resolution[1] - 150))
			
			lifes_pool_label = font.render('lifes left: ' + str(game.lifes_pool), True, (0, 255, 100), (0, 0, 0))
			screen.blit(lifes_pool_label, (10, 0))
			
			points_label = font.render('points: ' + str(game.points), True, (0, 255, 100), (0, 0, 0))
			screen.blit(points_label, (150, 0))

#			if game.number_of_players > 1:
#				screen.blit(george_energy_label, (0, resolution[1] - 59))
#				screen.blit(george_ammo_label, (170, resolution[1] - 59))
				
			if game.number_of_players > 2:
				screen.blit(james_energy_label, (0, resolution[1] - 29))
				screen.blit(james_ammo_label, (170, resolution[1] - 29))
				
			if "blue" in game.keys_possesed:
				screen.blit(game.blue_key_model, (500, resolution[1] - 59))
			if "red" in game.keys_possesed:
				screen.blit(game.red_key_model, (532, resolution[1] - 59))
			if "green" in game.keys_possesed:
				screen.blit(game.green_key_model, (564, resolution[1] - 59))
			if "yellow" in game.keys_possesed:
				screen.blit(game.yellow_key_model, (596, resolution[1] - 59))

			#world 1
			if game.level < game.stage1_frontier:
				surface = background_earth
				level_name_text = font.render('IT STARTED ON EARTH...', True, (0, 255, 255), (0, 0, 0))
			elif game.level < game.stage2_frontier:
				# surface = background_earth
				level_name_text = font.render('NASA HQ INFECTED!', True, (0, 255, 255), (0, 0, 0))
			elif game.level < game.stage3_frontier:
				level_name_text = font.render('HERE COMES THE ALIENOG!', True, (0, 255, 255), (0, 0, 0))
				
				boss_energy_label = font.render('boss: ' + str(int(game.boss.energy)), True, (0, 255, 255), (0, 0, 0))
				screen.blit(boss_energy_label, (850, 0))
				
			#world 2
			elif game.level < game.stage4_frontier:
				surface = background_moon
				level_name_text = font.render('ARRIVAL TO THE MOON', True, (0, 150, 150), (0, 0, 0))
			elif game.level < game.stage5_frontier:
				# surface = background_moon
				level_name_text = font.render('INTERNATIONAL MOON BASE', True, (0, 150, 225), (0, 0, 0))
			elif game.level < game.stage6_frontier:
				level_name_text = font.render('HERE COMES THE HUNTER!', True, (0, 255, 255), (0, 0, 0))
				
				boss_energy_label = font.render('boss: ' + str(int(game.boss.energy)), True, (0, 255, 255), (0, 0, 0))
				screen.blit(boss_energy_label, (850, 0))
				
			#world 3
			elif game.level < game.stage7_frontier:
				surface = background_mars
				level_name_text = font.render('MARS DISTRESS SIGNAL', True, (255, 70, 0), (0, 0, 0))
			elif game.level < game.stage8_frontier:
				# surface = background_mars
				level_name_text = font.render('MARS COLONY', True, (255, 70, 0), (0, 0, 0))
			elif game.level < game.stage9_frontier:
				level_name_text = font.render('HERE COMES THE CRUSHER!', True, (0, 255, 255), (0, 0, 0))
				
				boss_energy_label = font.render('boss: ' + str(int(game.boss.energy)), True, (0, 255, 255), (0, 0, 0))
				screen.blit(boss_energy_label, (850, 0))
				
			#world 4
			elif game.level < game.stage10_frontier:
				surface = background_venus
				level_name_text = font.render('VENUS HEAT', True, (255, 0, 0), (0, 0, 0))
			elif game.level < game.stage11_frontier:
				# surface = background_venus
				level_name_text = font.render('VENUS ALPHA LABS', True, (135, 135, 120), (0, 0, 0))
			elif game.level < game.stage12_frontier:
				level_name_text = font.render('HERE COMES THE MASS LORD!', True, (0, 255, 255), (0, 0, 0))
				
				boss_energy_label = font.render('boss: ' + str(int(game.boss.energy)), True, (0, 255, 255), (0, 0, 0))
				screen.blit(boss_energy_label, (850, 0))

			#world 5
			elif game.level < game.stage13_frontier:
				surface = background_neptune
				level_name_text = font.render('NEPTUNES FRONTIER', True, (255, 0, 0), (0, 0, 0))
			elif game.level < game.stage14_frontier:
				level_name_text = font.render('NEPTUNES MYSTERIOUS CORRIDORS', True, (135, 135, 120), (0, 0, 0))
			elif game.level < game.stage15_frontier:
				level_name_text = font.render('HERE COMES THE LAST SOLAR SYSTEM BOSS', True, (0, 255, 255), (0, 0, 0))
				
				boss_energy_label = font.render('boss: ' + str(int(game.boss.energy)), True, (0, 255, 255), (0, 0, 0))
				screen.blit(boss_energy_label, (850, 0))
				
			else:
				time.sleep(1.0)
				screen.fill((0, 0, 0))
				pygame.display.flip()
				screen.blit(end_screen, ( -( (1920 - resolution[0]) / 2), -( (1080 - resolution[1]) / 2)))
				pygame.display.flip()
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/end_music.ogg')
				pygame.mixer.music.play()
				
				while(True):
					for event in pygame.event.get():
						if event.type == QUIT:
							sys.exit()
						elif event.type == KEYDOWN and event.key == K_ESCAPE:
							sys.exit()
			
			screen.blit(level_name_text, (530, 0))
			
			#show if Nash has super weapon ready
			if nash.ammo['vortex'] < 1:
				for i in range(int(nash.ammo['vortex'] * 250)):
					pygame.draw.line(screen, (80, 80, 80), (10 + i, resolution[1] - 70 + ammo_bars_y_offset), (10 + i, resolution[1] - 64 + ammo_bars_y_offset), 1)
			else:
				for i in range(int(nash.ammo['vortex'] * 250)):
					pygame.draw.line(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (10 + i, resolution[1] - 70 + ammo_bars_y_offset), (10 + i, resolution[1] - 64 + ammo_bars_y_offset), 1)
				#vortex_label = font.render('VORTEX: ' + str(nash.ammo['vortex']), True, (0, 255, 0), (0, 0, 0))
				#screen.blit(vortex_label, (resolution[0] - 310, resolution[1] - 150))
			#else:
				#vortex_label = font.render('VORTEX: ' + str(nash.ammo['vortex']), True, (0, 100, 0), (0, 0, 0))
				#screen.blit(vortex_label, (resolution[0] - 310, resolution[1] - 150))
				
			#show if George has super weapon ready
			if game.number_of_players > 1:
				if george.ammo['vortex'] < 1:
					for i in range(int(george.ammo['vortex'] * 250)):
						pygame.draw.line(screen, (80, 80, 80), (310 + i, resolution[1] - 70 + ammo_bars_y_offset), (310 + i, resolution[1] - 64 + ammo_bars_y_offset), 1)
				else:
					for i in range(int(george.ammo['vortex'] * 250)):
						pygame.draw.line(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (310 + i, resolution[1] - 70 + ammo_bars_y_offset), (310 + i, resolution[1] - 64 + ammo_bars_y_offset), 1)
					#vortex_label = font.render('VORTEX: ' + str(george.ammo['vortex']), True, (0, 100, 255), (0, 0, 0))
					#screen.blit(vortex_label, (resolution[0] - 310, resolution[1] - 59))
				#else:
					#vortex_label = font.render('VORTEX: ' + str(george.ammo['vortex']), True, (0, 40, 105), (0, 0, 0))
					#screen.blit(vortex_label, (resolution[0] - 310, resolution[1] - 59))
					
			#show if james has super weapon ready
			if game.number_of_players > 2:
				if james.ammo['vortex'] < 1:
					for i in range(int(james.ammo['vortex'] * 250)):
						pygame.draw.line(screen, (80, 80, 80), (600 + i, resolution[1] - 70 + ammo_bars_y_offset), (600 + i, resolution[1] - 54 + ammo_bars_y_offset), 1)
				else:
					for i in range(int(james.ammo['vortex'] * 250)):
						pygame.draw.line(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (600 + i, resolution[1] - 70 + ammo_bars_y_offset), (600 + i, resolution[1] - 54 + ammo_bars_y_offset), 1)
					#vortex_label = font.render('VORTEX: ' + str(james.ammo['vortex']), True, (255, 255, 0), (0, 0, 0))
					#screen.blit(vortex_label, (resolution[0] - 310, resolution[1] - 29))
				#else:
					#vortex_label = font.render('VORTEX: ' + str(james.ammo['vortex']), True, (255, 255, 0), (0, 0, 0))
					#screen.blit(vortex_label, (resolution[0] - 310, resolution[1] - 29))
				
			#show Nash force field status
			if nash.has_force_field:
				nash_ff_label = font.render('force field: ' + str(nash.force_field), True, (0, 255, 0), (0, 0, 0))
				screen.blit(nash_ff_label, (resolution[0] - 170, resolution[1] - 150))
			
			#show George force field status
			if game.number_of_players > 1:
				if george.has_force_field:
					george_ff_label = font.render('force field: ' + str(george.force_field), True, (0, 100, 255), (0, 0, 0))
					screen.blit(george_ff_label, (resolution[0] - 170, resolution[1] - 59))
				
			#show james force field status
			if game.number_of_players > 2:
				if james.has_force_field:
					james_ff_label = font.render('force field: ' + str(james.force_field), True, (255, 255, 0), (0, 0, 0))
					screen.blit(james_ff_label, (resolution[0] - 170, resolution[1] - 29))
			
			#show rxvt force field status
			#rxvt_ff_label = font.render('force field: ' + str(rxvt.force_field), True, (0, 100, 255), (0, 0, 0))
			#screen.blit(rxvt_ff_label, (975, resolution[1] - 89))
			
		if game.next_level == True:
			you_win_text = font.render('LOADING...', True, (0, 255, 0))
			screen.blit(you_win_text, (resolution[0] / 2 - 75, resolution[1] / 2))
			#if applause_sound_played == False:
				#applause_sound.play()
				#applause_sound_played = True
				
		if not nash.alive() and not george.alive() and not james.alive():
			time.sleep(1.0)
			screen.fill((0, 0, 0))
			pygame.display.flip()
			screen.blit(game_over_screen, ( -( (1920 - resolution[0]) / 2), -( (1080 - resolution[1]) / 2)))
			pygame.display.flip()
			pygame.mixer.music.stop()
			pygame.mixer.music.load('data/music/game_over.ogg')
			pygame.mixer.music.play()

			while(True):
				for event in pygame.event.get():
					if event.type == QUIT:
						sys.exit()
					elif event.type == KEYDOWN and event.key == K_ESCAPE:
						sys.exit()

		#draw everything before calling this function		
		#================================== END OF DRAWING !!! ====================================================
		pygame.display.flip()
		clock.tick(30)
			
		if nash.energy > 0:
			if nash.has_super_regeneration_upgrade == False:
				if nash_regeneration_loop == 40:
					nash.regenerate_energy(game.difficulty)
					nash_regeneration_loop = 0
			elif nash.has_super_regeneration_upgrade == True:
				if nash_regeneration_loop >= 20:
					nash.regenerate_energy(game.difficulty)
					nash_regeneration_loop = 0
			
			if nash.doctor_energy_regeneration == True:
				if nash_regeneration_loop >= 20:
					nash.regenerate_energy('easy')
					nash_regeneration_loop = 0
							
			if nash_ff_regeneration_loop == 40:
				nash.regenerate_force_field()
				nash_ff_regeneration_loop = 0

			#if nash.has_level2_force_field_upgrade == False:
			#	if nash_ff_regeneration_loop == 40:
			#		nash.regenerate_force_field()
			#		nash_ff_regeneration_loop = 0
			#elif nash.has_level2_force_field_upgrade == True:
			#	if nash_ff_regeneration_loop >= 20:
			#		nash.regenerate_force_field()
			#		nash_ff_regeneration_loop = 0

			nash_regeneration_loop += 1
			nash_ff_regeneration_loop += 1
			
		if george.energy > 0:
			if george.has_super_regeneration_upgrade == False:
				if george_regeneration_loop == 40:
					george.regenerate_energy(game.difficulty)
					george_regeneration_loop = 0
			elif george.has_super_regeneration_upgrade == True:
				if george_regeneration_loop >= 20:
					george.regenerate_energy(game.difficulty)
					george_regeneration_loop = 0
				
			if george.doctor_energy_regeneration == True:
				if george_regeneration_loop >= 20:
					george.regenerate_energy('easy')
					george_regeneration_loop = 0

			if george_ff_regeneration_loop == 40:
				george.regenerate_force_field()
				george_ff_regeneration_loop = 0

			#if george.has_level2_force_field_upgrade == False:
			#	if george_ff_regeneration_loop == 40:
			#		george.regenerate_force_field()
			#		george_ff_regeneration_loop = 0
			#elif george.has_level2_force_field_upgrade == True:
			#	if george_ff_regeneration_loop >= 20:
			#		george.regenerate_force_field()
			#		george_ff_regeneration_loop = 0
				
			george_regeneration_loop += 1
			george_ff_regeneration_loop += 1
			
		if james.energy > 0:
			if james.has_super_regeneration_upgrade == False:
				if james_regeneration_loop == 40:
					james.regenerate_energy(game.difficulty)
					james_regeneration_loop = 0
			elif james.has_super_regeneration_upgrade == True:
				if james_regeneration_loop >= 20:
					james.regenerate_energy(game.difficulty)
					james_regeneration_loop = 0
					
			if james.doctor_energy_regeneration == True:
				if james_regeneration_loop >= 20:
					james.regenerate_energy('easy')
					james_regeneration_loop = 0

			if james_ff_regeneration_loop == 40:
				james.regenerate_force_field()
				james_ff_regeneration_loop = 0

			#if james.has_level2_force_field_upgrade == False:
			#	if james_ff_regeneration_loop == 40:
			#		james.regenerate_force_field()
			#		james_ff_regeneration_loop = 0
			#elif james.has_level2_force_field_upgrade == True:
			#	if james_ff_regeneration_loop >= 20:
			#		james.regenerate_force_field()
			#		james_ff_regeneration_loop = 0
				
			james_regeneration_loop += 1
			james_ff_regeneration_loop += 1
		
		if nash.energy > 0 and nash.ammo['vortex'] < 1:
			if nash.vortex_loop >= nash.vortex_loop_max:
				nash.add_ammo('vortex', 0.01)
				nash.vortex_loop = 0
			else:
				nash.vortex_loop += 1
				
		if george.energy > 0 and george.ammo['vortex'] < 1:
			if george.vortex_loop >= george.vortex_loop_max:
				george.add_ammo('vortex', 0.01)
				george.vortex_loop = 0
			else:
				george.vortex_loop += 1
				
		if james.energy > 0 and james.ammo['vortex'] < 1:
			if james.vortex_loop >= james.vortex_loop_max:
				james.add_ammo('vortex', 0.01)
				james.vortex_loop = 0
			else:
				james.vortex_loop += 1
		
		if nash.energy > 0 and nash.fire == False:
			if nash.laser_loop >= nash.laser_loop_max - nash.ammo['laser'] / 3:
				nash.add_ammo('laser', 1)
				nash.laser_loop = 0
			else:
				nash.laser_loop += 1
				
			# if nash.laser_time_upgrade > 0:
				# if nash.laser_time_upgrade_loop < nash.laser_time_upgrade_loop_max:
					# nash.laser_time_upgrade_loop += 1
				# else:
					# nash.laser_time_upgrade_loop = 0
					# nash.laser_time_upgrade = 0
				
		if george.energy > 0 and george.fire == False:
			if george.laser_loop >= george.laser_loop_max - george.ammo['laser'] / 3:
				george.add_ammo('laser', 1)
				george.laser_loop = 0
			else:
				george.laser_loop += 1
				
			# if george.laser_time_upgrade > 0:
				# if george.laser_time_upgrade_loop < george.laser_time_upgrade_loop_max:
					# george.laser_time_upgrade_loop += 1
				# else:
					# george.laser_time_upgrade_loop = 0
					# george.laser_time_upgrade = 0
				
		if james.energy > 0 and james.fire == False:
			if james.laser_loop >= james.laser_loop_max - james.ammo['laser'] / 3:
				james.add_ammo('laser', 1)
				james.laser_loop = 0
			else:
				james.laser_loop += 1
				
			# if james.laser_time_upgrade > 0:
				# if james.laser_time_upgrade_loop < james.laser_time_upgrade_loop_max:
					# james.laser_time_upgrade_loop += 1
				# else:
					# james.laser_time_upgrade_loop = 0
					# james.laser_time_upgrade = 0
			
		if game.level_type == "arena":
			#spiders are getting faster during the play in a level, unless vortex is launched
			if nash.vortex_launched == False and george.vortex_launched == False and james.vortex_launched == False and rxvt.vortex_launched == False: 
				if chase_loop % 50 == 49:
					for spider in monster.monsters:
						pass
						# deprecated
						# spider.speed += 1
				
		time.sleep(0.001)
		
		game_loop += 1
		
		if game.level_type == "arena":
			chase_loop += 1
			
		game.bot_movement_loop += 1

		#=============================== START NEW LEVEL =================================================
		if game.next_level == True:
			game.level += 1
			game.next_level = False
			game.bonus_count = 0
			
			game.points += 200
			
			if game.number_of_players == 2:
				if not nash.alive() or not george.alive():
					energy_sum = nash.energy + george.energy
					
					if energy_sum >= 2:
						nash.dead = False
						nash.energy = energy_sum / 2.0

						george.dead = False
						george.energy = energy_sum / 2.0
					
			elif game.number_of_players == 3:
				if not nash.alive() or not george.alive() or not james.alive():
					energy_sum = nash.energy + george.energy + james.energy
					
					if energy_sum >= 3:
						nash.dead = False
						nash.energy = energy_sum / 3.0
						
						george.dead = False
						george.energy = energy_sum / 3.0
						
						james.dead = False
						james.energy = energy_sum / 3.0
		
			#change stage
			if game.level == game.stage1_frontier: 
				game.stage = 2
				
				game.number_of_new_robots = 1
								
				game.level_type = "labirynth"
				
				game.map_size_x = game.labirynth_dim_x * 320 + 64
				game.map_size_y = game.labirynth_dim_y * 320 + 64
						
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage2_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage2_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage2_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage2_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
				
			elif game.level == game.stage2_frontier: #boss level
				game.stage = 3
				
				game.level_type = "boss_level"
				
				del monster.monsters[:]
				del monster.gigantulas[:]
				del monster.robots[:]
				del monster.cranes[:]
				del monster.hunters[:]
				
				game.number_of_spiders = 0
				game.number_of_new_spiders = 0
				
				game.number_of_gigantulas = 0
				game.number_of_new_gigantulas = 0
				
				game.number_of_robots = 0
				game.number_of_new_robots = 0
				
				game.number_of_cranes = 0
				game.number_of_new_cranes = 0
				
				game.number_of_hunters = 0
				game.number_of_new_hunters = 0
				
				game.boss = Boss1(resolution[0] / 2, 300)
				game.boss.energy = 100
				
				game.map_size_x = resolution[0]
				game.map_size_y = resolution[1]
				
				nash.x = 100
				nash.y = 100
				
				rxvt.x = 200
				rxvt.y = 200
				
				if game.number_of_players > 1:
					george.x = 200
					george.y = 100
					
				if game.number_of_players > 2:
					james.x = 100
					james.y = 200
				
				game.x = 0
				game.y = 0

				clear_object_table(game)
				
				shop = Shop()
				shop.enter_shop(screen, game, global_player)
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world1.ogg')
				pygame.mixer.music.play()
				
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage3_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage3_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage3_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage3_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
				
				
			elif game.level == game.stage3_frontier: 
				game.stage = 4
				
				game.level_type = "arena"
				
				game.number_of_spiders = 4
				game.number_of_new_spiders = 2
				
				game.number_of_gigantulas = 2
				game.number_of_new_gigantulas = 1
				
				game.number_of_robots = 1
				game.number_of_new_robots = 1
				
				game.number_of_cranes = 1
				game.number_of_new_cranes = 1
				
				game.number_of_hunters = 0
				game.number_of_new_hunters = 0
				
				for i in range(0, game.number_of_spiders):
					monster.add_spider(game)
						
				for i in range(0, game.number_of_gigantulas):
					monster.add_gigantula(game)
					
				for i in range(0, game.number_of_robots):
					monster.add_robot(game)
					
				for i in range(0, game.number_of_cranes):
					monster.add_crane(game)
				
				for i in range(0, game.number_of_hunters):
					monster.add_hunter(game)

				game.map_size_x = resolution[0]
				game.map_size_y = resolution[1]
				
				nash.x = 100
				nash.y = 100
				
				rxvt.x = 200
				rxvt.y = 200
				
				if game.number_of_players > 1:
					george.x = 200
					george.y = 100
					
				if game.number_of_players > 2:
					james.x = 100
					james.y = 200
				
				game.x = 0
				game.y = 0

				clear_object_table(game)

				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world2.ogg')
				pygame.mixer.music.play()
							
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage4_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage4_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage4_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage4_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
				
			elif game.level == game.stage4_frontier:
				game.stage = 5
				
				game.number_of_new_cranes = 1
				
				game.level_type = "labirynth"
											
				game.labirynth_dim_x += 1
				game.labirynth_dim_y += 1

				game.map_size_x = game.labirynth_dim_x * 320 + 64
				game.map_size_y = game.labirynth_dim_y * 320 + 64
				
				shop = Shop()
				shop.enter_shop(screen, game, global_player)
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world2.ogg')
				pygame.mixer.music.play()
				
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage5_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage5_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage5_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage5_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
				
			elif game.level == game.stage5_frontier: #boss level
				game.stage = 6
				
				game.level_type = "boss_level"
				
				del monster.monsters[:]
				del monster.gigantulas[:]
				del monster.robots[:]
				del monster.cranes[:]
				del monster.hunters[:]
				
				game.number_of_spiders = 0
				game.number_of_new_spiders = 0
				
				game.number_of_gigantulas = 0
				game.number_of_new_gigantulas = 0
				
				game.number_of_robots = 0
				game.number_of_new_robots = 0
				
				game.number_of_cranes = 0
				game.number_of_new_cranes = 0
				
				game.number_of_hunters = 0
				game.number_of_new_hunters = 0
				
				game.boss = Boss2(resolution[0] / 2, 300)
				game.boss.energy = 100
				
				game.map_size_x = resolution[0]
				game.map_size_y = resolution[1]
				
				nash.x = 100
				nash.y = 100
				
				rxvt.x = 200
				rxvt.y = 200
				
				if game.number_of_players > 1:
					george.x = 200
					george.y = 100
					
				if game.number_of_players > 2:
					james.x = 100
					james.y = 200
				
				game.x = 0
				game.y = 0

				clear_object_table(game)
				
				shop = Shop()
				shop.enter_shop(screen, game, global_player)
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world2.ogg')
				pygame.mixer.music.play()
				
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage6_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage6_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage6_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage6_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
			
				
			elif game.level == game.stage6_frontier:
				game.stage = 7
				
				game.number_of_new_cranes = 0
				
				game.level_type = "arena"
				
				game.number_of_spiders = 10
				game.number_of_new_spiders = 2
				
				game.number_of_gigantulas = 10
				game.number_of_new_gigantulas = 1
				
				game.number_of_robots = 10
				game.number_of_new_robots = 1
				
				game.number_of_cranes = 4
				game.number_of_new_cranes = 1
				
				game.number_of_hunters = 1
				game.number_of_new_hunters = 1
				
				for i in range(0, game.number_of_spiders):
					monster.add_spider(game)
						
				for i in range(0, game.number_of_gigantulas):
					monster.add_gigantula(game)
					
				for i in range(0, game.number_of_robots):
					monster.add_robot(game)
					
				for i in range(0, game.number_of_cranes):
					monster.add_crane(game)
					
				for i in range(0, game.number_of_hunters):
					monster.add_hunter(game)
				
				game.map_size_x = resolution[0]
				game.map_size_y = resolution[1]
				
				nash.x = 100
				nash.y = 100
				
				rxvt.x = 200
				rxvt.y = 200
				
				if game.number_of_players > 1:
					george.x = 200
					george.y = 100
					
				if game.number_of_players > 2:
					james.x = 100
					james.y = 200
				
				game.x = 0
				game.y = 0

				clear_object_table(game)

				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world3.ogg')
				pygame.mixer.music.play()
								
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage7_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage7_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage7_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage7_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
				
			elif game.level == game.stage7_frontier:
				game.stage = 8
				
				game.number_of_new_cranes = 1
				
				game.level_type = "labirynth"
				
				game.labirynth_dim_x += 1
				game.labirynth_dim_y += 1

				game.map_size_x = game.labirynth_dim_x * 320 + 64
				game.map_size_y = game.labirynth_dim_y * 320 + 64
				
				shop = Shop()
				shop.enter_shop(screen, game, global_player)
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world3.ogg')
				pygame.mixer.music.play()
				
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage8_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage8_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage8_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage8_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
				
			elif game.level == game.stage8_frontier: #boss level
				game.stage = 9
				
				game.level_type = "boss_level"
				
				del monster.monsters[:]
				del monster.gigantulas[:]
				del monster.robots[:]
				del monster.cranes[:]
				del monster.hunters[:]
				
				game.number_of_spiders = 0
				game.number_of_new_spiders = 0
				
				game.number_of_gigantulas = 0
				game.number_of_new_gigantulas = 0
				
				game.number_of_robots = 0
				game.number_of_new_robots = 0
				
				game.number_of_cranes = 0
				game.number_of_new_cranes = 0
				
				game.number_of_hunters = 0
				game.number_of_new_hunters = 0
				
				game.boss = Boss3(resolution[0] / 2, 300)
				game.boss.energy = 100
				
				game.map_size_x = resolution[0]
				game.map_size_y = resolution[1]
				
				nash.x = 100
				nash.y = 100
				
				rxvt.x = 200
				rxvt.y = 200
				
				if game.number_of_players > 1:
					george.x = 200
					george.y = 100
					
				if game.number_of_players > 2:
					james.x = 100
					james.y = 200
				
				game.x = 0
				game.y = 0

				clear_object_table(game)
				
				shop = Shop()
				shop.enter_shop(screen, game, global_player)
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world3.ogg')
				pygame.mixer.music.play()
				
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage9_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage9_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage9_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage9_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
				
			elif game.level == game.stage9_frontier:
				game.stage = 10
				
				game.level_type = "arena"
				
				game.number_of_spiders = 20
				game.number_of_new_spiders = 2
				
				game.number_of_gigantulas = 10
				game.number_of_new_gigantulas = 1
				
				game.number_of_robots = 20
				game.number_of_new_robots = 2
				
				game.number_of_cranes = 10
				game.number_of_new_cranes = 1
				
				game.number_of_hunters = 7
				game.number_of_new_hunters = 2
				
				for i in range(0, game.number_of_spiders):
					monster.add_spider(game)
						
				for i in range(0, game.number_of_gigantulas):
					monster.add_gigantula(game)
					
				for i in range(0, game.number_of_robots):
					monster.add_robot(game)
					
				for i in range(0, game.number_of_cranes):
					monster.add_crane(game)
					
				for i in range(0, game.number_of_hunters):
					monster.add_hunter(game)
				
				game.map_size_x = resolution[0]
				game.map_size_y = resolution[1]
				
				nash.x = 100
				nash.y = 100
				
				rxvt.x = 200
				rxvt.y = 200
				
				if game.number_of_players > 1:
					george.x = 200
					george.y = 100
					
				if game.number_of_players > 2:
					james.x = 100
					james.y = 200
				
				game.x = 0
				game.y = 0

				clear_object_table(game)

				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world4.ogg')
				pygame.mixer.music.play()
				
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage10_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage10_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage10_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage10_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
				
			elif game.level == game.stage10_frontier:
				game.stage = 11
				
				game.level_type = "labirynth"
				
				game.labirynth_dim_x += 1
				game.labirynth_dim_y += 1

				game.map_size_x = game.labirynth_dim_x * 320 + 64
				game.map_size_y = game.labirynth_dim_y * 320 + 64
				
				shop = Shop()
				shop.enter_shop(screen, game, global_player)
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world4.ogg')
				pygame.mixer.music.play()
								
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage11_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 150))
				text_label = story_font.render(game.stage11_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 200))
				text_label = story_font.render(game.stage11_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 250))
				text_label = story_font.render(game.stage11_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage11_story_text5, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage11_story_text6, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage11_story_text7, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				text_label = story_font.render(game.stage11_story_text8, True, (0, 255, 100))
				screen.blit(text_label, (200, 500))
				text_label = story_font.render(game.stage11_story_text9, True, (0, 255, 100))
				screen.blit(text_label, (200, 550))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
			elif game.level == game.stage11_frontier: #boss level
				game.stage = 12
				
				game.level_type = "boss_level"
				
				del monster.monsters[:]
				del monster.gigantulas[:]
				del monster.robots[:]
				del monster.cranes[:]
				del monster.hunters[:]
				
				game.number_of_spiders = 0
				game.number_of_new_spiders = 0
				
				game.number_of_gigantulas = 0
				game.number_of_new_gigantulas = 0
				
				game.number_of_robots = 0
				game.number_of_new_robots = 0
				
				game.number_of_cranes = 0
				game.number_of_new_cranes = 0
				
				game.number_of_hunters = 0
				game.number_of_new_hunters = 0
				
				game.boss = Boss4(resolution[0] / 2, 300)
				game.boss.energy = 100
				
				game.map_size_x = resolution[0]
				game.map_size_y = resolution[1]
				
				nash.x = 100
				nash.y = 100
				
				rxvt.x = 200
				rxvt.y = 200
				
				if game.number_of_players > 1:
					george.x = 200
					george.y = 100
					
				if game.number_of_players > 2:
					james.x = 100
					james.y = 200
				
				game.x = 0
				game.y = 0

				clear_object_table(game)
				
				shop = Shop()
				shop.enter_shop(screen, game, global_player)
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world4.ogg')
				pygame.mixer.music.play()
				
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage12_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage12_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage12_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage12_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()

			elif game.level == game.stage12_frontier:
				game.stage = 13
				
				game.level_type = "arena"
				
				game.number_of_spiders = 20
				game.number_of_new_spiders = 2
				
				game.number_of_gigantulas = 10
				game.number_of_new_gigantulas = 1
				
				game.number_of_robots = 20
				game.number_of_new_robots = 2
				
				game.number_of_cranes = 10
				game.number_of_new_cranes = 1
				
				game.number_of_hunters = 7
				game.number_of_new_hunters = 2
				
				for i in range(0, game.number_of_spiders):
					monster.add_spider(game)
						
				for i in range(0, game.number_of_gigantulas):
					monster.add_gigantula(game)
					
				for i in range(0, game.number_of_robots):
					monster.add_robot(game)
					
				for i in range(0, game.number_of_cranes):
					monster.add_crane(game)
					
				for i in range(0, game.number_of_hunters):
					monster.add_hunter(game)
				
				game.map_size_x = resolution[0]
				game.map_size_y = resolution[1]
				
				nash.x = 100
				nash.y = 100
				
				rxvt.x = 200
				rxvt.y = 200
				
				if game.number_of_players > 1:
					george.x = 200
					george.y = 100
					
				if game.number_of_players > 2:
					james.x = 100
					james.y = 200
				
				game.x = 0
				game.y = 0

				clear_object_table(game)

				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world5.ogg')
				pygame.mixer.music.play()
				
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage13_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage13_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage13_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage13_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
				
			elif game.level == game.stage13_frontier:
				game.stage = 14
				
				game.level_type = "labirynth"
				
				game.labirynth_dim_x += 1
				game.labirynth_dim_y += 1

				game.map_size_x = game.labirynth_dim_x * 320 + 64
				game.map_size_y = game.labirynth_dim_y * 320 + 64
				
				shop = Shop()
				shop.enter_shop(screen, game, global_player)
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world5.ogg')
				pygame.mixer.music.play()
								
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage14_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 150))
				text_label = story_font.render(game.stage14_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 200))
				text_label = story_font.render(game.stage14_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 250))
				text_label = story_font.render(game.stage14_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
			elif game.level == game.stage14_frontier: #boss level
				game.stage = 15
				
				game.level_type = "boss_level"
				
				del monster.monsters[:]
				del monster.gigantulas[:]
				del monster.robots[:]
				del monster.cranes[:]
				del monster.hunters[:]
				
				game.number_of_spiders = 0
				game.number_of_new_spiders = 0
				
				game.number_of_gigantulas = 0
				game.number_of_new_gigantulas = 0
				
				game.number_of_robots = 0
				game.number_of_new_robots = 0
				
				game.number_of_cranes = 0
				game.number_of_new_cranes = 0
				
				game.number_of_hunters = 0
				game.number_of_new_hunters = 0
				
				game.boss = Boss5(resolution[0] / 2, 300)
				game.boss.energy = 100
				
				game.map_size_x = resolution[0]
				game.map_size_y = resolution[1]
				
				nash.x = 100
				nash.y = 100
				
				rxvt.x = 200
				rxvt.y = 200
				
				if game.number_of_players > 1:
					george.x = 200
					george.y = 100
					
				if game.number_of_players > 2:
					james.x = 100
					james.y = 200
				
				game.x = 0
				game.y = 0

				clear_object_table(game)
				
				shop = Shop()
				shop.enter_shop(screen, game, global_player)
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world5.ogg')
				pygame.mixer.music.play()
				
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage15_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage15_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage15_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage15_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				screen.fill((0, 0, 0))
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
			
			if game.level_type == "labirynth":
				nash.x = 100
				nash.y = 100
				
				rxvt.x = 200
				rxvt.y = 200
				
				if game.number_of_players > 1:
					george.x = 200
					george.y = 100
					
				if game.number_of_players > 2:
					james.x = 100
					james.y = 200
				
				game.x = 0
				game.y = 0

				exit_place_x = random.randint(0, game.labirynth_dim_x)
				exit_place_y = random.randint(0, game.labirynth_dim_y)
				
				while exit_place_x == 0 and exit_place_y == 0:
					exit_place_x = random.randint(0, game.labirynth_dim_x)
					exit_place_y = random.randint(0, game.labirynth_dim_y)
				
				clear_object_table(game)

				labirynth = TableMazeModel(rowsNum = game.labirynth_dim_x, colsNum = game.labirynth_dim_y)
				labirynth.genMaze()
				set_labirynth(game, labirynth, game.labirynth_dim_x, game.labirynth_dim_y)
				
				# f = open('d:/prg/AlienThreat/logs/labirynth', 'w')
				# # f = open('f:/prg/at/AlienThreat/logs/labirynth', 'w')
				# # print f
				# f.write(str(labirynth))
				# f.close()
				
			elif game.level_type == "arena":
				time.sleep(2.0)
				
				# add eggs to object table again
				add_object(game, 300, 400, 48, 48)	
				add_object(game, 320, 440, 48, 48)	
				add_object(game, 370, 400, 48, 48)	
				add_object(game, 800, 600, 48, 48)	
				add_object(game, 820, 690, 48, 48)	
				add_object(game, 970, 650, 48, 48)	
				
				w1 = (600, 400)
				w2 = (664, 400)
				w3 = (472, 400)
				w4 = (536, 400)
				w5 = (472, 464)
				w6 = (664, 464)
				w7 = (472, 528)
				w8 = (664, 528)

				#walls
				add_object(game, w1[0], w1[1], 64, 64)
				add_object(game, w2[0], w2[1], 64, 64)	
				add_object(game, w3[0], w3[1], 64, 64)
				add_object(game, w4[0], w4[1], 64, 64)
				add_object(game, w5[0], w5[1], 64, 64)
				add_object(game, w6[0], w6[1], 64, 64)
				add_object(game, w7[0], w7[1], 64, 64)
				add_object(game, w8[0], w8[1], 64, 64)
				
			elif game.level_type == "boss_level":
				time.sleep(2.0)
				
				# add eggs to object table again
				add_object(game, 300, 400, 48, 48)	
				add_object(game, 320, 440, 48, 48)	
				add_object(game, 370, 400, 48, 48)	
				add_object(game, 800, 600, 48, 48)	
				add_object(game, 820, 690, 48, 48)	
				add_object(game, 970, 650, 48, 48)
				
			game.bonuses = []
			game.bonus_count = 0
			
			if game.level_type == "labirynth":
				for game.bonus_count in range(0, game.bonuses_per_level):
					#remember to increase this after adding new bonus to the game !!!
					which_one = random.randint(0, 8)
					
					if which_one == 5: #vortex
						pass #no vortex bonus in a labirynth
						#game.add_new_bonus(which_one, random.randint(150, game.map_size_x - 150), random.randint(150, game.map_size_y - 150), 100)
					elif which_one == 7: #yellow money
						game.add_new_bonus(which_one, random.randint(150, game.map_size_x - 150), random.randint(150, game.map_size_y - 150 - game.screen_bottom), 100)
					else: #all other bonuses
						game.add_new_bonus(which_one, random.randint(150, game.map_size_x - 150), random.randint(150, game.map_size_y - 150 - game.screen_bottom), 500)
						
			if game.level_type == "labirynth":
				game.exit_opened = False
				del game.keys[:]
				del game.keys_possesed[:]
				game.bonus_count = 0
				for game.keys_count in range(0, game.keys_per_level + 1):
					game.add_new_key(game.keys_count, random.randint(150, game.map_size_x - 150), random.randint(150, game.map_size_y - 150), 100)
			elif game.level_type == "arena":
				game.exit_opened = False
				del game.keys[:]
				del game.keys_possesed[:]
				game.bonus_count = 0
			
			nash.vortex_launched = False
			george.vortex_launched = False
			james.vortex_launched = False
			rxvt.vortex_launched = False
			
			if game.level_type == "arena" or game.level_type == "labirynth":
				game.number_of_spiders += game.number_of_new_spiders
				game.number_of_gigantulas += game.number_of_new_gigantulas
				game.number_of_robots += game.number_of_new_robots
				game.number_of_cranes += game.number_of_new_cranes
					
				for i in range(0, game.number_of_new_spiders):
					monster.add_spider(game)
					
				for i in range(0, game.number_of_new_gigantulas):
					monster.add_gigantula(game)
					
				for i in range(0, game.number_of_new_robots):
					monster.add_robot(game)
					
				for i in range(0, game.number_of_new_cranes):
					monster.add_crane(game)
	
			rxvt.add_ammo('laser', 300)
			rxvt.add_ammo('freezer', 250)
			rxvt.add_ammo('plasma', 15)
			rxvt.force_field += (20 + 2 * game.level)
				
			chase_loop = 0
			
			rxvt.ammo['flamethrower'] = 3000
			
			# if game.level % game.number_of_levels_in_stage == 1 and game.level != 1:
				# if game.difficulty == 'easy':
					# nash.max_energy += 20
					# george.max_energy += 20
					# james.max_energy += 20
					
					# nash.player_speed += 1
					# george.player_speed += 1
					# james.player_speed += 1
					# rxvt.player_speed += 1
					
				# elif game.difficulty == 'medium':
					# nash.max_energy += 10
					# george.max_energy += 10
					# james.max_energy += 10
					
					# nash.player_speed += 1
					# george.player_speed += 1
					# james.player_speed += 1
					# rxvt.player_speed += 1
						
				# game.spider_chaos += 10
				
				# game.gigantulas_speed += game.gigantulas_new_speed
			
			if game.level_type == "arena" or game.level_type == "labirynth":
				for spider in monster.monsters:
					spider.energy = 100
					# spider.speed = game.spiders_speed
					spider.x = random.randint(200, game.map_size_x - 200)
					spider.y = random.randint(200, game.map_size_y - 200 - game.screen_bottom)
					spider.frozen = False
					spider.killed = False
					spider.fried = False
					spider.death_sound_played = False
					spider.decay = spider.base_decay
					
					# if game.level % game.number_of_levels_in_stage == 1 & game.level != 1:
						# spider.armor += 20
					
				for gigantula in monster.gigantulas:
					gigantula.energy = 100
					gigantula.x = random.randint(200, game.map_size_x - 200)
					gigantula.y = random.randint(200, game.map_size_y - 200 - game.screen_bottom)
					gigantula.frozen = False
					gigantula.killed = False
					gigantula.fried = False
					gigantula.death_sound_played = False
					gigantula.decay = gigantula.base_decay
					
					# if game.level % game.number_of_levels_in_stage == 1 & game.level != 1:
						# if game.difficulty == 'easy':
							# gigantula.armor += 10
						# elif game.difficulty == 'medium':
							# gigantula.armor += 25
						# elif game.difficulty == 'hard':
							# gigantula.armor += 50
							
				for robot in monster.robots:
					robot.energy = 100
					robot.x = random.randint(200, game.map_size_x - 200)
					robot.y = random.randint(200, game.map_size_y - 200 - game.screen_bottom)
					robot.frozen = False
					robot.killed = False
					robot.fried = False
					robot.death_sound_played = False
					robot.decay = robot.base_decay
					
				for crane in monster.cranes:
					crane.energy = 100
					crane.x = random.randint(200, game.map_size_x - 200)
					crane.y = random.randint(200, game.map_size_y - 200 - game.screen_bottom)
					crane.frozen = False
					crane.killed = False
					crane.fried = False
					crane.death_sound_played = False
					crane.decay = crane.base_decay
					
				for hunter in monster.hunters:
					hunter.energy = 100
					hunter.x = random.randint(200, game.map_size_x - 200)
					hunter.y = random.randint(200, game.map_size_y - 200 - game.screen_bottom)
					hunter.frozen = False
					hunter.killed = False
					hunter.fried = False
					hunter.death_sound_played = False
					hunter.decay = hunter.base_decay
					
				mass1 = Mass(random.randint(200, game.map_size_x - 200), random.randint(200, game.map_size_y - 200 - game.screen_bottom))
				mass2 = Mass(random.randint(200, game.map_size_x - 200), random.randint(200, game.map_size_y - 200 - game.screen_bottom))
					
	#================================ KEYBOARD EVENTS ==========================================================================
	for event in pygame.event.get():
		
		if event.type == QUIT:
			sys.exit()
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			menu(screen, game)

		elif event.type == KEYDOWN and event.key == K_r:
			#reset players:
			nash = Player(100, 100, 'data/images/players/nash/nash-0.png', 'data/images/players/nash/nash_pain-0.png', game)
			
			if game.number_of_players > 1:
				george = Player(200, 100, 'data/images/players/george/george-0.png', 'data/images/players/george/george_pain-0.png', game)
			
			if game.number_of_players > 2:
				james = Player(100, 200, 'data/images/players/james/james-0.png', 'data/images/players/james/james-0.png', game)
			
			rxvt = Player(200, 200, 'data/images/players/rxvt/rxvt-0.png', 'data/images/players/rxvt/rxvt-0.png', game)
			
			define_character()
			
			game.x = 0
			game.y = 0
		elif event.type == KEYDOWN and event.key == K_p:
			pause = True
			pygame.mixer.music.stop()
			pause_text = font.render('GAME PAUSED', True, (0, 255, 0), (0, 0, 0))
			screen.blit(pause_text, (resolution[0] / 2 - 100, resolution[1] / 2 - 50))
			pygame.display.flip()
						
			while pause == True:
				for event in pygame.event.get():
					if event.type == KEYDOWN and event.key == K_p:
						pause = False
						pygame.mixer.music.play()
					
		elif event.type == KEYUP and event.key == K_RETURN:
			if game.started == False:
				menu(screen, game)
				game.started = True
				
				nash = Player(100, 100, 'data/images/players/nash/nash-0.png', 'data/images/players/nash/nash_pain-0.png', game)
				george = Player(200, 100, 'data/images/players/george/george-0.png', 'data/images/players/george/george_pain-0.png', game)
				james = Player(100, 200, 'data/images/players/james/james-0.png', 'data/images/players/james/james_pain-0.png', game)
				rxvt = Player(200, 200, 'data/images/players/rxvt/rxvt-0.png', 'data/images/players/rxvt/rxvt-0.png', game)

				define_character()
				
				nash.name = 'nash'
				george.name = 'george'
				james.name = 'james'
				rxvt.name = 'rxvt'

				global_player = Players()
				global_player.add_player('nash', nash)
				global_player.add_player('george', george)
				global_player.add_player('james', james)
				global_player.add_player('rxvt', james)

				if game.number_of_players == 1:
					george.energy = 0
					george.dead = True
					james.energy = 0
					james.dead = True
				elif game.number_of_players == 2:
					james.energy = 0
					james.dead = True

				rxvt.offsetX = random.randint(-1, 2)
				rxvt.offsetY = random.randint(-1, 2)

				rxvt.ammo['flamethrower'] = 50000

				
				pygame.mixer.music.stop()
				pygame.mixer.music.load('data/music/world1.ogg')
				pygame.mixer.music.play()
				
				#story
				time.sleep(2.0)
				screen.fill((0, 0, 0))
				text_label = story_font.render(game.stage1_story_text1, True, (0, 255, 100))
				screen.blit(text_label, (200, 300))
				text_label = story_font.render(game.stage1_story_text2, True, (0, 255, 100))
				screen.blit(text_label, (200, 350))
				text_label = story_font.render(game.stage1_story_text3, True, (0, 255, 100))
				screen.blit(text_label, (200, 400))
				text_label = story_font.render(game.stage1_story_text4, True, (0, 255, 100))
				screen.blit(text_label, (200, 450))
				pygame.display.flip()
				
				skip = False
				while(skip == False):
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							skip = True
							
				loading_label = loading_font.render('Loading...', True, (0, 255, 100))
				screen.blit(loading_label, (400, 300))
				pygame.display.flip()
					
		if game.nash_pad == True:
			#PAD / JOYSTICK
			#RIGHT
			if joy1.get_axis(0) > 0.5:
				nash.offsetX = +nash.player_speed
			elif joy1.get_axis(0) >= 0 and joy1.get_axis(0) <= 0.5:
				nash.offsetX = 0
			
			#LEFT
			if joy1.get_axis(0) < -0.5:
				nash.offsetX = -nash.player_speed
			elif joy1.get_axis(0) <= 0 and joy1.get_axis(0) >= -0.5:
				nash.offsetX = 0
			
			#DOWN
			if joy1.get_axis(1) > 0.5:
				nash.offsetY = +nash.player_speed
			elif joy1.get_axis(1) >= 0 and joy1.get_axis(1) <= 0.5:
				nash.offsetY = 0
			
			#UP
			if joy1.get_axis(1) < -0.5:
				nash.offsetY = -nash.player_speed
			elif joy1.get_axis(1) <= 0 and joy1.get_axis(1) >= -0.5:
				nash.offsetY = 0
			
			#fire with right trigger
			# if joy1.get_axis(2) < -0.3:
				# nash.fire = True
			# elif joy1.get_axis(2) <= 0 and joy1.get_axis(1) >= -0.3:
				# nash.fire = False

			if joy1.get_name() == 'Controller (Xbox 360 Wireless Receiver for Windows)':
				if joy1.get_button(3) != 0:
					nash.current_weapon = "flamethrower"
					nash.fire = True
				elif joy1.get_button(1) != 0:
					nash.current_weapon = "laser"
					nash.fire = True
				elif joy1.get_button(2) != 0:
					nash.current_weapon = "freezer"
					nash.fire = True
				elif joy1.get_button(0) != 0: #green button starts the game
					if game.started == False:
						menu(screen, game)
						game.started = True
						
						nash = Player(100, 100, 'data/images/players/nash/nash-0.png', 'data/images/players/nash/nash_pain-0.png', game)
						george = Player(200, 100, 'data/images/players/george/george-0.png', 'data/images/players/george/george_pain-0.png', game)
						james = Player(100, 200, 'data/images/players/james/james-0.png', 'data/images/players/james/james_pain-0.png', game)
						rxvt = Player(200, 200, 'data/images/players/rxvt/rxvt-0.png', 'data/images/players/rxvt/rxvt-0.png', game)

						define_character()
						
						nash.name = 'nash'
						george.name = 'george'
						james.name = 'james'
						rxvt.name = 'rxvt'

						global_player = Players()
						global_player.add_player('nash', nash)
						global_player.add_player('george', george)
						global_player.add_player('james', james)
						global_player.add_player('rxvt', james)

						if game.number_of_players == 1:
							george.energy = 0
							george.dead = True
							james.energy = 0
							james.dead = True
						elif game.number_of_players == 2:
							james.energy = 0
							james.dead = True

						rxvt.offsetX = random.randint(-1, 2)
						rxvt.offsetY = random.randint(-1, 2)

						# is this used or overwritten in other place??
						rxvt.ammo['flamethrower'] = 50000

						
						pygame.mixer.music.stop()
						pygame.mixer.music.load('data/music/world1.ogg')
						pygame.mixer.music.play()
						
						#story
						time.sleep(2.0)
						screen.fill((0, 0, 0))
						text_label = story_font.render(game.stage1_story_text1, True, (0, 255, 100))
						screen.blit(text_label, (200, 300))
						text_label = story_font.render(game.stage1_story_text2, True, (0, 255, 100))
						screen.blit(text_label, (200, 350))
						text_label = story_font.render(game.stage1_story_text3, True, (0, 255, 100))
						screen.blit(text_label, (200, 400))
						text_label = story_font.render(game.stage1_story_text4, True, (0, 255, 100))
						screen.blit(text_label, (200, 450))
						pygame.display.flip()
						
						skip = False
						while(skip == False):
							for event in pygame.event.get():
								if event.type == KEYDOWN:
									skip = True
									
						loading_label = loading_font.render('Loading...', True, (0, 255, 100))
						screen.blit(loading_label, (400, 300))
						pygame.display.flip()
					else:
						nash.current_weapon = "plasma"
						nash.fire = True
				else:
					nash.fire = False
				
				if joy1.get_button(8) != 0:
					if nash.force_field_enabled == False and nash.has_force_field:
						nash.force_field_enabled = True
					else:
						if nash.energy >= nash.ff_auto_enable_level:
							nash.force_field_enabled = False
				
				if joy1.get_button(9) != 0:
					if nash.ammo['vortex'] == 1:
						nash.vortex_launched = True
						vortex_sound.play()
						# for spider in monster.monsters:
							# spider.speed = 1
							# spider.armor = 1

						nash.ammo['vortex'] -= 1
						try:
							_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, nash.x, nash.y, nash.angle, nash.ammo, monster, game, global_player, 'james'))
						except:
							print("Error: unable to start vortex thread")

			else: # 'PC TWIN SHOCK'
				if joy1.get_button(1) != 0:
					nash.current_weapon = "flamethrower"
					nash.fire = True
				elif joy1.get_button(3) != 0:
					nash.current_weapon = "laser"
					nash.fire = True
				elif joy1.get_button(0) != 0:
					nash.current_weapon = "freezer"
					nash.fire = True
				elif joy1.get_button(2) != 0: #green button starts the game
					if game.started == False:
						menu(screen, game)
						game.started = True
						
						nash = Player(100, 100, 'data/images/players/nash/nash-0.png', 'data/images/players/nash/nash_pain-0.png', game)
						george = Player(200, 100, 'data/images/players/george/george-0.png', 'data/images/players/george/george_pain-0.png', game)
						james = Player(100, 200, 'data/images/players/james/james-0.png', 'data/images/players/james/james_pain-0.png', game)
						rxvt = Player(200, 200, 'data/images/players/rxvt/rxvt-0.png', 'data/images/players/rxvt/rxvt-0.png', game)

						define_character()

						nash.name = 'nash'
						george.name = 'george'
						james.name = 'james'
						rxvt.name = 'rxvt'

						global_player = Players()
						global_player.add_player('nash', nash)
						global_player.add_player('george', george)
						global_player.add_player('james', james)
						global_player.add_player('rxvt', james)

						if game.number_of_players == 1:
							george.energy = 0
							george.dead = True
							james.energy = 0
							james.dead = True
						elif game.number_of_players == 2:
							james.energy = 0
							james.dead = True

						rxvt.offsetX = random.randint(-1, 2)
						rxvt.offsetY = random.randint(-1, 2)

						rxvt.ammo['flamethrower'] = 50000

						pygame.mixer.music.stop()
						pygame.mixer.music.load('data/music/world1.ogg')
						pygame.mixer.music.play()
						
						#story
						time.sleep(2.0)
						screen.fill((0, 0, 0))
						text_label = story_font.render(game.stage1_story_text1, True, (0, 255, 100))
						screen.blit(text_label, (200, 300))
						text_label = story_font.render(game.stage1_story_text2, True, (0, 255, 100))
						screen.blit(text_label, (200, 350))
						text_label = story_font.render(game.stage1_story_text3, True, (0, 255, 100))
						screen.blit(text_label, (200, 400))
						text_label = story_font.render(game.stage1_story_text4, True, (0, 255, 100))
						screen.blit(text_label, (200, 450))
						pygame.display.flip()
						
						skip = False
						while(skip == False):
							for event in pygame.event.get():
								if event.type == KEYDOWN:
									skip = True
									
						loading_label = loading_font.render('Loading...', True, (0, 255, 100))
						screen.blit(loading_label, (400, 300))
						pygame.display.flip()
					else:
						nash.current_weapon = "plasma"
						nash.fire = True
				else:
					nash.fire = False
				
				if joy1.get_button(10) != 0:
					if nash.force_field_enabled == False and nash.has_force_field:
						nash.force_field_enabled = True
					else:
						if nash.energy >= nash.ff_auto_enable_level:
							nash.force_field_enabled = False
				
				if joy1.get_button(11) != 0:
					if nash.ammo['vortex'] == 1:
						nash.vortex_launched = True
						vortex_sound.play()
						# for spider in monster.monsters:
							# spider.speed = 1
							# spider.armor = 1

						nash.ammo['vortex'] -= 1
						try:
							_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, nash.x, nash.y, nash.angle, nash.ammo, monster, game, global_player, 'nash'))
						except:
							print("Error: unable to start vortex thread")
				
				# if joy1.get_button(6) != 0 or joy1.get_button(7) != 0:
					# sys.exit()
		elif (game.nash_pad == False and game.george_pad == True) or (game.nash_pad == False and game.number_of_players == 1):
			#UP
			if event.type == KEYDOWN and event.key == K_UP:
				nash.offsetY = -nash.player_speed
			elif event.type == KEYUP and event.key == K_UP:
				if nash.offsetY <= 0:
					nash.offsetY = 0
			
			#DOWN
			elif event.type == KEYDOWN and event.key == K_DOWN:
				nash.offsetY = +nash.player_speed
			elif event.type == KEYUP and event.key == K_DOWN:
				if nash.offsetY >= 0:
					nash.offsetY = 0
			
			#RIGHT
			elif event.type == KEYDOWN and event.key == K_RIGHT:
				nash.offsetX = +nash.player_speed
			elif event.type == KEYUP and event.key == K_RIGHT:
				if nash.offsetX >= 0:
					nash.offsetX = 0
			
			#LEFT
			elif event.type == KEYDOWN and event.key == K_LEFT:
				nash.offsetX = -nash.player_speed
			elif event.type == KEYUP and event.key == K_LEFT:
				if nash.offsetX <= 0:
					nash.offsetX = 0

			if event.type == KEYDOWN and event.key == K_f:
				nash.current_weapon = "flamethrower"
				nash.fire = True
			elif event.type == KEYDOWN and event.key == K_s:
				nash.current_weapon = "laser"
				nash.fire = True
			elif event.type == KEYDOWN and event.key == K_a:
				nash.current_weapon = "freezer"
				nash.fire = True
			elif event.type == KEYDOWN and event.key == K_d:
				nash.current_weapon = "plasma"
				nash.fire = True
			
			if event.type == KEYUP and event.key == K_f:
				if nash.current_weapon == "flamethrower":
					nash.fire = False
			elif event.type == KEYUP and event.key == K_s:
				if nash.current_weapon == "laser":
					nash.fire = False
			elif event.type == KEYUP and event.key == K_a:
				if nash.current_weapon == "freezer":
					nash.fire = False
			elif event.type == KEYUP and event.key == K_d:
				if nash.current_weapon == "plasma":
					nash.fire = False
					
			elif event.type == KEYDOWN and event.key == K_e:
				if nash.force_field_enabled == False and nash.has_force_field:
					nash.force_field_enabled = True
				else:
					if nash.energy >= nash.ff_auto_enable_level:
						nash.force_field_enabled = False
					
			if event.type == KEYDOWN and event.key == K_v:
				#if nash.ammo['vortex'] >= 1:
				if nash.ammo['vortex'] == 1:
					nash.vortex_launched = True
					vortex_sound.play()
					# for spider in monster.monsters:
						# spider.speed = 1
						# spider.armor = 1

					nash.ammo['vortex'] -= 1
					try:
						_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, nash.x, nash.y, nash.angle, nash.ammo, monster, game, global_player, 'nash'))
					except:
						print("Error: unable to start nash vortex thread")
		elif game.nash_pad == False and game.george_pad == False and game.number_of_players == 2:
			#UP
			if event.type == KEYDOWN and event.key == K_t:
				nash.offsetY = -nash.player_speed
			elif event.type == KEYUP and event.key == K_t:
				if nash.offsetY <= 0:
					nash.offsetY = 0
			
			#DOWN
			elif event.type == KEYDOWN and event.key == K_g:
				nash.offsetY = +nash.player_speed
			elif event.type == KEYUP and event.key == K_g:
				if nash.offsetY >= 0:
					nash.offsetY = 0
			
			#RIGHT
			elif event.type == KEYDOWN and event.key == K_h:
				nash.offsetX = +nash.player_speed
			elif event.type == KEYUP and event.key == K_h:
				if nash.offsetX >= 0:
					nash.offsetX = 0
			
			#LEFT
			elif event.type == KEYDOWN and event.key == K_f:
				nash.offsetX = -nash.player_speed
			elif event.type == KEYUP and event.key == K_f:
				if nash.offsetX <= 0:
					nash.offsetX = 0

			if event.type == KEYDOWN and event.key == K_q:
				nash.current_weapon = "flamethrower"
				nash.fire = True
			elif event.type == KEYDOWN and event.key == K_w:
				nash.current_weapon = "laser"
				nash.fire = True
			elif event.type == KEYDOWN and event.key == K_a:
				nash.current_weapon = "freezer"
				nash.fire = True
			elif event.type == KEYDOWN and event.key == K_s:
				nash.current_weapon = "plasma"
				nash.fire = True
			
			if event.type == KEYUP and event.key == K_q:
				if nash.current_weapon == "flamethrower":
					nash.fire = False
			elif event.type == KEYUP and event.key == K_w:
				if nash.current_weapon == "laser":
					nash.fire = False
			elif event.type == KEYUP and event.key == K_a:
				if nash.current_weapon == "freezer":
					nash.fire = False
			elif event.type == KEYUP and event.key == K_s:
				if nash.current_weapon == "plasma":
					nash.fire = False
					
			elif event.type == KEYDOWN and event.key == K_e:
				if nash.force_field_enabled == False and nash.has_force_field:
					nash.force_field_enabled = True
				else:
					if nash.energy >= nash.ff_auto_enable_level:
						nash.force_field_enabled = False
					
			if event.type == KEYDOWN and event.key == K_v:
				if nash.ammo['vortex'] == 1:
					nash.vortex_launched = True
					vortex_sound.play()
					# for spider in monster.monsters:
						# spider.speed = 1
						# spider.armor = 1

					nash.ammo['vortex'] -= 1
					try:
						_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, nash.x, nash.y, nash.angle, nash.ammo, monster, game, global_player, 'nash'))
					except:
						print("Error: unable to start nash vortex thread")
						
		#George player directions:
		if game.number_of_players > 1 and game.george_pad == True:
			#PAD / JOYSTICK
			#RIGHT
			if joy2.get_axis(0) > 0.5:
				george.offsetX = +george.player_speed
			elif joy2.get_axis(0) >= 0 and joy2.get_axis(0) <= 0.5:
				george.offsetX = 0
			
			#LEFT
			if joy2.get_axis(0) < -0.5:
				george.offsetX = -george.player_speed
			elif joy2.get_axis(0) <= 0 and joy2.get_axis(0) >= -0.5:
				george.offsetX = 0
			
			#DOWN
			if joy2.get_axis(1) > 0.5:
				george.offsetY = +george.player_speed
			elif joy2.get_axis(1) >= 0 and joy2.get_axis(1) <= 0.5:
				george.offsetY = 0
			
			#UP
			if joy2.get_axis(1) < -0.5:
				george.offsetY = -george.player_speed
			elif joy2.get_axis(1) <= 0 and joy2.get_axis(1) >= -0.5:
				george.offsetY = 0
			
			#fire with right trigger
			# if joy2.get_axis(2) < -0.3:
				# george.fire = True
			# elif joy2.get_axis(2) <= 0 and joy2.get_axis(1) >= -0.3:
				# george.fire = False
			
			if joy2.get_name() == 'Controller (Xbox 360 Wireless Receiver for Windows)':
				if joy2.get_button(3) != 0:
					george.current_weapon = "flamethrower"
					george.fire = True
				elif joy2.get_button(1) != 0:
					george.current_weapon = "laser"
					george.fire = True
				elif joy2.get_button(2) != 0:
					george.current_weapon = "freezer"
					george.fire = True
				elif joy2.get_button(0) != 0: #green button starts the game
					if game.started == False:
						menu(screen, game)
						game.started = True
						
						nash = Player(100, 100, 'data/images/players/nash/nash-0.png', 'data/images/players/nash/nash_pain-0.png', game)
						george = Player(200, 100, 'data/images/players/george/george-0.png', 'data/images/players/george/george_pain-0.png', game)
						james = Player(100, 200, 'data/images/players/james/james-0.png', 'data/images/players/james/james_pain-0.png', game)
						rxvt = Player(200, 200, 'data/images/players/rxvt/rxvt-0.png', 'data/images/players/rxvt/rxvt-0.png', game)

						define_character()
						
						nash.name = 'nash'
						george.name = 'george'
						james.name = 'james'
						rxvt.name = 'rxvt'

						global_player = Players()
						global_player.add_player('nash', nash)
						global_player.add_player('george', george)
						global_player.add_player('james', james)
						global_player.add_player('rxvt', james)

						if game.number_of_players == 1:
							george.energy = 0
							george.dead = True
							james.energy = 0
							james.dead = True
						elif game.number_of_players == 2:
							james.energy = 0
							james.dead = True

						rxvt.offsetX = random.randint(-1, 2)
						rxvt.offsetY = random.randint(-1, 2)

						rxvt.ammo['flamethrower'] = 50000
						
						pygame.mixer.music.stop()
						pygame.mixer.music.load('data/music/world1.ogg')
						pygame.mixer.music.play()
						
						#story
						time.sleep(2.0)
						screen.fill((0, 0, 0))
						text_label = story_font.render(game.stage1_story_text1, True, (0, 255, 100))
						screen.blit(text_label, (200, 300))
						text_label = story_font.render(game.stage1_story_text2, True, (0, 255, 100))
						screen.blit(text_label, (200, 350))
						text_label = story_font.render(game.stage1_story_text3, True, (0, 255, 100))
						screen.blit(text_label, (200, 400))
						text_label = story_font.render(game.stage1_story_text4, True, (0, 255, 100))
						screen.blit(text_label, (200, 450))
						pygame.display.flip()
						
						skip = False
						while(skip == False):
							for event in pygame.event.get():
								if event.type == KEYDOWN:
									skip = True
									
						loading_label = loading_font.render('Loading...', True, (0, 255, 100))
						screen.blit(loading_label, (400, 300))
						pygame.display.flip()
					else:
						george.current_weapon = "plasma"
						george.fire = True
				else:
					george.fire = False
				
				if joy2.get_button(8) != 0:
					if george.force_field_enabled == False and george.has_force_field:
						george.force_field_enabled = True
					else:
						if george.energy >= george.ff_auto_enable_level:
							george.force_field_enabled = False
				
				if joy2.get_button(9) != 0:
					if george.ammo['vortex'] == 1:
						george.vortex_launched = True
						vortex_sound.play()
						# for spider in monster.monsters:
							# spider.speed = 1
							# spider.armor = 1

						george.ammo['vortex'] -= 1
						try:
							_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, george.x, george.y, george.angle, george.ammo, monster, game, global_player, 'george'))
						except:
							print("Error: unable to start vortex thread")
				
				# if joy2.get_button(6) != 0 or joy2.get_button(7) != 0:
					# sys.exit()
					
			else: # 'PC TWIN SHOCK'
				if joy2.get_button(1) != 0:
					george.current_weapon = "flamethrower"
					george.fire = True
				elif joy2.get_button(3) != 0:
					george.current_weapon = "laser"
					george.fire = True
				elif joy2.get_button(0) != 0:
					george.current_weapon = "freezer"
					george.fire = True
				elif joy2.get_button(2) != 0: #green button starts the game
					if game.started == False:
						menu(screen, game)
						game.started = True
						
						nash = Player(100, 100, 'data/images/players/nash/nash-0.png', 'data/images/players/nash/nash_pain-0.png', game)
						george = Player(200, 100, 'data/images/players/george/george-0.png', 'data/images/players/george/george_pain-0.png', game)
						james = Player(100, 200, 'data/images/players/james/james-0.png', 'data/images/players/james/james_pain-0.png', game)
						rxvt = Player(200, 200, 'data/images/players/rxvt/rxvt-0.png', 'data/images/players/rxvt/rxvt-0.png', game)

						define_character()
						
						nash.name = 'nash'
						george.name = 'george'
						james.name = 'james'
						rxvt.name = 'rxvt'

						global_player = Players()
						global_player.add_player('nash', nash)
						global_player.add_player('george', george)
						global_player.add_player('james', james)
						global_player.add_player('rxvt', james)

						if game.number_of_players == 1:
							george.energy = 0
							george.dead = True
							james.energy = 0
							james.dead = True
						elif game.number_of_players == 2:
							james.energy = 0
							james.dead = True

						rxvt.offsetX = random.randint(-1, 2)
						rxvt.offsetY = random.randint(-1, 2)

						rxvt.ammo['flamethrower'] = 50000

						pygame.mixer.music.stop()
						pygame.mixer.music.load('data/music/world1.ogg')
						pygame.mixer.music.play()
						
						#story
						time.sleep(2.0)
						screen.fill((0, 0, 0))
						text_label = story_font.render(game.stage1_story_text1, True, (0, 255, 100))
						screen.blit(text_label, (200, 300))
						text_label = story_font.render(game.stage1_story_text2, True, (0, 255, 100))
						screen.blit(text_label, (200, 350))
						text_label = story_font.render(game.stage1_story_text3, True, (0, 255, 100))
						screen.blit(text_label, (200, 400))
						text_label = story_font.render(game.stage1_story_text4, True, (0, 255, 100))
						screen.blit(text_label, (200, 450))
						pygame.display.flip()
						
						skip = False
						while(skip == False):
							for event in pygame.event.get():
								if event.type == KEYDOWN:
									skip = True
									
						loading_label = loading_font.render('Loading...', True, (0, 255, 100))
						screen.blit(loading_label, (400, 300))
						pygame.display.flip()
					else:
						george.current_weapon = "plasma"
						george.fire = True
				else:
					george.fire = False
				
				if joy2.get_button(10) != 0:
					if george.force_field_enabled == False and george.has_force_field:
						george.force_field_enabled = True
					else:
						if george.energy >= george.ff_auto_enable_level:
							george.force_field_enabled = False
				
				if joy2.get_button(11) != 0:
					if george.ammo['vortex'] == 1:
						george.vortex_launched = True
						vortex_sound.play()
						# for spider in monster.monsters:
							# spider.speed = 1
							# spider.armor = 1

						george.ammo['vortex'] -= 1
						try:
							_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, george.x, george.y, george.angle, george.ammo, monster, game, global_player, 'george'))
						except:
							print("Error: unable to start vortex thread")
				
		elif game.number_of_players > 1 and game.george_pad == False and game.nash_pad == True:
			#UP
			if event.type == KEYDOWN and event.key == K_UP:
				george.offsetY = -george.player_speed
			elif event.type == KEYUP and event.key == K_UP:
				if george.offsetY <= 0:
					george.offsetY = 0
			
			#DOWN
			elif event.type == KEYDOWN and event.key == K_DOWN:
				george.offsetY = +george.player_speed
			elif event.type == KEYUP and event.key == K_DOWN:
				if george.offsetY >= 0:
					george.offsetY = 0
			
			#RIGHT
			elif event.type == KEYDOWN and event.key == K_RIGHT:
				george.offsetX = +george.player_speed
			elif event.type == KEYUP and event.key == K_RIGHT:
				if george.offsetX >= 0:
					george.offsetX = 0
			
			#LEFT
			elif event.type == KEYDOWN and event.key == K_LEFT:
				george.offsetX = -george.player_speed
			elif event.type == KEYUP and event.key == K_LEFT:
				if george.offsetX <= 0:
					george.offsetX = 0

			if event.type == KEYDOWN and event.key == K_f:
				george.current_weapon = "flamethrower"
				george.fire = True
			elif event.type == KEYDOWN and event.key == K_s:
				george.current_weapon = "laser"
				george.fire = True
			elif event.type == KEYDOWN and event.key == K_a:
				george.current_weapon = "freezer"
				george.fire = True
			elif event.type == KEYDOWN and event.key == K_d:
				george.current_weapon = "plasma"
				george.fire = True
			
			if event.type == KEYUP and event.key == K_f:
				if george.current_weapon == "flamethrower":
					george.fire = False
			elif event.type == KEYUP and event.key == K_s:
				if george.current_weapon == "laser":
					george.fire = False
			elif event.type == KEYUP and event.key == K_a:
				if george.current_weapon == "freezer":
					george.fire = False
			elif event.type == KEYUP and event.key == K_d:
				if george.current_weapon == "plasma":
					george.fire = False
					
			elif event.type == KEYDOWN and event.key == K_e:
				if george.force_field_enabled == False and george.has_force_field:
					george.force_field_enabled = True
				else:
					if george.energy >= george.ff_auto_enable_level:
						george.force_field_enabled = False
					
			if event.type == KEYDOWN and event.key == K_v:
				if george.ammo['vortex'] == 1:
					george.vortex_launched = True
					vortex_sound.play()
					# for spider in monster.monsters:
						# spider.speed = 1
						# spider.armor = 1

					george.ammo['vortex'] -= 1
					try:
						_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, george.x, george.y, george.angle, george.ammo, monster, game, global_player, 'george'))
					except:
						print("Error: unable to start George vortex thread")
		
		elif game.number_of_players == 2 and game.george_pad == False and game.nash_pad == False:
			#UP
			if event.type == KEYDOWN and event.key == K_KP8:
				george.offsetY = -george.player_speed
			elif event.type == KEYUP and event.key == K_KP8:
				if george.offsetY <= 0:
					george.offsetY = 0
			
			#DOWN
			elif event.type == KEYDOWN and event.key == K_KP5:
				george.offsetY = +george.player_speed
			elif event.type == KEYUP and event.key == K_KP5:
				if george.offsetY >= 0:
					george.offsetY = 0
			
			#RIGHT
			elif event.type == KEYDOWN and event.key == K_KP6:
				george.offsetX = +george.player_speed
			elif event.type == KEYUP and event.key == K_KP6:
				if george.offsetX >= 0:
					george.offsetX = 0
			
			#LEFT
			elif event.type == KEYDOWN and event.key == K_KP4:
				george.offsetX = -george.player_speed
			elif event.type == KEYUP and event.key == K_KP4:
				if george.offsetX <= 0:
					george.offsetX = 0

			if event.type == KEYDOWN and event.key == K_UP:
				george.current_weapon = "flamethrower"
				george.fire = True
			elif event.type == KEYDOWN and event.key == K_RIGHT:
				george.current_weapon = "laser"
				george.fire = True
			elif event.type == KEYDOWN and event.key == K_LEFT:
				george.current_weapon = "freezer"
				george.fire = True
			elif event.type == KEYDOWN and event.key == K_DOWN:
				george.current_weapon = "plasma"
				george.fire = True
			
			if event.type == KEYUP and event.key == K_UP:
				if george.current_weapon == "flamethrower":
					george.fire = False
			elif event.type == KEYUP and event.key == K_RIGHT:
				if george.current_weapon == "laser":
					george.fire = False
			elif event.type == KEYUP and event.key == K_LEFT:
				if george.current_weapon == "freezer":
					george.fire = False
			elif event.type == KEYUP and event.key == K_DOWN:
				if george.current_weapon == "plasma":
					george.fire = False
					
			elif event.type == KEYDOWN and event.key == K_RCTRL:
				if george.force_field_enabled == False and george.has_force_field:
					george.force_field_enabled = True
				else:
					if george.energy >= george.ff_auto_enable_level:
						george.force_field_enabled = False
					
			if event.type == KEYDOWN and event.key == K_RSHIFT:
				if george.ammo['vortex'] == 1:
					george.vortex_launched = True
					vortex_sound.play()
					# for spider in monster.monsters:
						# spider.speed = 1
						# spider.armor = 1

					george.ammo['vortex'] -= 1
					try:
						_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, george.x, george.y, george.angle, george.ammo, monster, game, global_player, 'george'))
					except:
						print("Error: unable to start George vortex thread")
		
		
		if game.number_of_players > 2:
			#james
			#UP
			if event.type == KEYDOWN and event.key == K_UP:
				james.offsetY = -james.player_speed
			elif event.type == KEYUP and event.key == K_UP:
				if james.offsetY <= 0:
					james.offsetY = 0
			
			#DOWN
			elif event.type == KEYDOWN and event.key == K_DOWN:
				james.offsetY = +james.player_speed
			elif event.type == KEYUP and event.key == K_DOWN:
				if james.offsetY >= 0:
					james.offsetY = 0
			
			#RIGHT
			elif event.type == KEYDOWN and event.key == K_RIGHT:
				james.offsetX = +james.player_speed
			elif event.type == KEYUP and event.key == K_RIGHT:
				if james.offsetX >= 0:
					james.offsetX = 0
			
			#LEFT
			elif event.type == KEYDOWN and event.key == K_LEFT:
				james.offsetX = -james.player_speed
			elif event.type == KEYUP and event.key == K_LEFT:
				if james.offsetX <= 0:
					james.offsetX = 0

			if event.type == KEYDOWN and event.key == K_f:
				james.current_weapon = "flamethrower"
				james.fire = True
			elif event.type == KEYDOWN and event.key == K_s:
				james.current_weapon = "laser"
				james.fire = True
			elif event.type == KEYDOWN and event.key == K_a:
				james.current_weapon = "freezer"
				james.fire = True
			elif event.type == KEYDOWN and event.key == K_d:
				james.current_weapon = "plasma"
				james.fire = True
			
			if event.type == KEYUP and event.key == K_f:
				if james.current_weapon == "flamethrower":
					james.fire = False
			elif event.type == KEYUP and event.key == K_s:
				if james.current_weapon == "laser":
					james.fire = False
			elif event.type == KEYUP and event.key == K_a:
				if james.current_weapon == "freezer":
					james.fire = False
			elif event.type == KEYUP and event.key == K_d:
				if james.current_weapon == "plasma":
					james.fire = False
					
			elif event.type == KEYDOWN and event.key == K_e:
				if james.force_field_enabled == False and james.has_force_field:
					james.force_field_enabled = True
				else:
					if james.energy >= james.ff_auto_enable_level:
						james.force_field_enabled = False
					
			if event.type == KEYDOWN and event.key == K_v:
				if james.ammo['vortex'] == 1:
					james.vortex_launched = True
					vortex_sound.play()
					# for spider in monster.monsters:
						# spider.speed = 1
						# spider.armor = 1

					james.ammo['vortex'] -= 1
					try:
						_thread.start_new_thread(vortex, ("Thread-vortex", 0.001, screen, james.x, james.y, james.angle, james.ammo, monster, game, global_player, 'james'))
					except:
						print("Error: unable to start james vortex thread")
			
