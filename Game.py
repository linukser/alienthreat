from Bonus import *
from Key import *

class Game:
	version = "0.71"

	# map x, y
	x = 0
	y = 0
	
	# labirynth_dim_x = 3 # for testing
	# labirynth_dim_y = 3 # for testing
	
	labirynth_dim_x = 7
	labirynth_dim_y = 7
	
	#stages
	stage = 1
	
	# rxvt
	bot_movement_loop = 0
	bot_movement_loop_max = 50
	rxvt_speed = 2
	
	# characters speed
	commando_speed = 8
	#commando_speed = 25 #for testing
	robot_speed = 3
	doctor_speed = 5
	scientist_speed = 10
	
	# characters armor
	commando_armor = 25
	robot_armor = 50
	doctor_armor = 15
	scientist_armor = 25
	# commando_armor = 100
	# robot_armor = 200
	# doctor_armor = 40
	# scientist_armor = 70
	
	# bonus ammo
	bonus_flamethrower_ammo = 15 # 15 litres
	bonus_freezer_ammo = 100

	# number_of_levels_in_arena_stage = 5
	# number_of_levels_in_arena_stage = 3
	number_of_levels_in_arena_stage = 1 # for testing
	number_of_levels_in_labirynth_stage = 1
	
	# number_of_levels_in_stage = 1 # deprecated

	
	# labirynth_dim_x = 3 # for testing
	# labirynth_dim_y = 3 # for testing

	wait_with_explosion_loop = 0
	wait_with_explosion_loop_max = 20
	
	points = 0
	lifes_pool = 7
	#player_death_time = 0.06
	player_death_time = 0.03
	
	#technical stuff
	started = False
	next_level = False
	level = 1
	safety_border = None
	level_type = "labirynth"
	
	screen_bottom = 152 # interface height from bottom of the screen
	screen_bottom_player = 212 # interface height from bottom of the screen
	
	mute = False
	# mute = True
	
	# characters: 1 - commando, 2 - robot, 3 - doctor, 4 - scientist
	nash_character = 1
	george_character = 1
	james_character = 1
	
	#gameplay options
	number_of_players = 1
	
	# nash_pad = True
	nash_pad = False
	
	# george_pad = True
	george_pad = False
	
	# difficulty = 'easy'
	# difficulty = 'medium'
	difficulty = 'hard'

	spider_attack = 10.0
	gigantula_attack = 100.0
	robot_attack = 20.0
	crane_attack = 15.0
	hunter_attack = 15.0
	boss_attack = 20.0

	boss_fire_range = 1000
	
	#monsters
	number_of_spiders = 10
	# number_of_spiders = 40
	number_of_new_spiders = 6
	
	number_of_gigantulas = 4
	number_of_new_gigantulas = 2
	
	number_of_robots = 0
	number_of_new_robots = 0
	
	number_of_cranes = 0
	number_of_new_cranes = 0
	
	number_of_hunters = 0
	number_of_new_hunters = 0
	
	gigantulas_speed = 2
	gigantulas_new_speed = 1
	
	robots_speed = 1
	robots_new_speed = 1
	
	spider_chaos = 10
	
	#bosses
	boss1 = None
	boss2 = None
	boss3 = None
	boss4 = None
	final_boss = None
	
	#weapons
	vortex_power = 500.0

	flamethrower_power_for_crane = 40.0
	flamethrower_power_for_robot = flamethrower_power_for_crane
	
	laser_power = 10.0
	laser_power_boost = 8.0 #power boost for each taken laser bonus
	laser_additional_power_boost = 4.0 #additional boost to normal boost - increases for every player, everytime only one player buys it
	
	plasma_power = 100.0
	
	freezer_power = 180.0
	freezer_power_for_spider = freezer_power
	freezer_power_for_gigantula = freezer_power
	freezer_power_for_robot = freezer_power
	freezer_power_for_crane = freezer_power
	freezer_power_for_hunter = freezer_power
	freezer_power_for_boss = freezer_power
	
	
	laser_power_for_spider = 15.0
	laser_power_for_gigantula = 20.0
	laser_power_for_robot = 70.0
	laser_power_for_crane = 50.0
	laser_power_for_hunter = 80.0
	laser_power_for_boss = 50.0
	
	laser_power_for_spider_upgrade1 = 30.0
	laser_power_for_gigantula_upgrade1 = 40.0
	laser_power_for_robot_upgrade1 = 140.0
	laser_power_for_crane_upgrade1 = 100.0
	laser_power_for_hunter_upgrade1 = 160.0
	laser_power_for_boss_upgrade1 = 80.0
	
	
	laser_power_for_spider_time_upgrade = 45.0
	laser_power_for_gigantula_time_upgrade = 60.0
	laser_power_for_robot_time_upgrade = 210.0
	laser_power_for_crane_time_upgrade = 150.0
	laser_power_for_hunter_time_upgrade = 240.0
	laser_power_for_boss_time_upgrade = 120.0
	
	
	laser_power_for_spider_time_upgrade1 = 120.0
	laser_power_for_gigantula_time_upgrade1 = 120.0
	laser_power_for_robot_time_upgrade1 = 420.0
	laser_power_for_crane_time_upgrade1 = 300.0
	laser_power_for_hunter_time_upgrade1 = 480.0
	laser_power_for_boss_time_upgrade1 = 240.0
	
	
	# laser_power_for_spider = 20.0
	# laser_power_for_gigantula = 20.0
	# laser_power_for_robot = 70.0
	# laser_power_for_crane = 50.0
	# laser_power_for_hunter = 80.0
	# laser_power_for_boss = 50.0
		
	# laser_power_for_spider_upgrade1 = 40.0
	# laser_power_for_gigantula_upgrade1 = 40.0
	# laser_power_for_robot_upgrade1 = 140.0
	# laser_power_for_crane_upgrade1 = 100.0
	# laser_power_for_hunter_upgrade1 = 160.0
	# laser_power_for_boss_upgrade1 = 80.0
	
	
	# laser_power_for_spider_time_upgrade = 60.0
	# laser_power_for_gigantula_time_upgrade = 60.0
	# laser_power_for_robot_time_upgrade = 210.0
	# laser_power_for_crane_time_upgrade = 150.0
	# laser_power_for_hunter_time_upgrade = 240.0
	# laser_power_for_boss_time_upgrade = 120.0
	
	
	# laser_power_for_spider_time_upgrade1 = 120.0
	# laser_power_for_gigantula_time_upgrade1 = 120.0
	# laser_power_for_robot_time_upgrade1 = 420.0
	# laser_power_for_crane_time_upgrade1 = 300.0
	# laser_power_for_hunter_time_upgrade1 = 480.0
	# laser_power_for_boss_time_upgrade1 = 240.0
	
	
	#from which level starts next stage
	stage1_frontier = number_of_levels_in_arena_stage + 1 #4
	stage2_frontier = stage1_frontier + number_of_levels_in_labirynth_stage #7
	stage3_frontier = stage2_frontier + 1 #8
	
	stage4_frontier = stage3_frontier + number_of_levels_in_arena_stage #11
	stage5_frontier = stage4_frontier + number_of_levels_in_labirynth_stage #14	
	stage6_frontier = stage5_frontier + 1 #15
	
	stage7_frontier = stage6_frontier + number_of_levels_in_arena_stage #18
	stage8_frontier = stage7_frontier + number_of_levels_in_labirynth_stage #21
	stage9_frontier = stage8_frontier + 1 #22
	
	stage10_frontier = stage9_frontier + number_of_levels_in_arena_stage #25
	stage11_frontier = stage10_frontier + number_of_levels_in_labirynth_stage #28
	stage12_frontier = stage11_frontier + 1 #29
	
	stage13_frontier = stage12_frontier + number_of_levels_in_arena_stage #25
	stage14_frontier = stage13_frontier + number_of_levels_in_labirynth_stage #28
	stage15_frontier = stage14_frontier + 1 #29
	
	#world 1
	stage1_story_text1 = 'It is year 2211... planet Earth'
	stage1_story_text2 = 'You\'re part of NASA special rescue forces.'
	stage1_story_text3 = 'You received an emergency call from headquarters.'
	stage1_story_text4 = 'Head to NASA facility to find out what happened!'
	
	stage2_story_text1 = 'In the NASA headquarters there is an alien invasion!'
	stage2_story_text2 = 'Kill the aliens and help scientists restore control to the facility.'
	stage2_story_text3 = 'Find dr Leo who sent you the distress call.'
	stage2_story_text4 = 'If you\'re lucky he may still be alive.'
	
	stage3_story_text1 = 'Unfortunately dr Leo is dead.'
	stage3_story_text2 = 'However you found out that the aliens came from the moon base.'
	stage3_story_text3 = ''
	stage3_story_text4 = 'But... what\'s this?? A gigantic alien blocks your way to the star port!'
	
	#world 2 - MOON
	stage4_story_text1 = 'That wasn\'t easy...'
	stage4_story_text2 = ''
	stage4_story_text3 = 'You take your Big City Destroyer type "solar cruiser II" to the spin!'
	stage4_story_text4 = 'Your journey to the stars begin!'
	
	stage5_story_text1 = 'Moon base was emergency sealed off.'
	stage5_story_text2 = 'After breaking inside you found a real mess!'
	stage5_story_text3 = 'Aliens all over, facility robots gone mad and shoting at everything.'
	stage5_story_text4 = 'Try to get more info, and first of all... try to stay alive.'
	
	stage6_story_text1 = 'What the...'
	stage6_story_text2 = 'Looks like someone is still alive...'
	stage6_story_text3 = 'But hey...'
	stage6_story_text4 = 'Why is he shooting at us???'
	
	#world 3 - MARS
	stage7_story_text1 = 'In the mean time you get a distress signal from the colony on Mars.'
	stage7_story_text2 = 'There is nothing here you can do to help these people.'
	stage7_story_text3 = 'You rush to Mars to save alive people from the threat.'
	stage7_story_text4 = 'Maybe their distress call has something to do with those aliens?'
	
	stage8_story_text1 = 'What you saw on Mars was horrible.'
	stage8_story_text2 = 'Thousands of colonists were murdered, consumed by alien life form.'
	stage8_story_text3 = 'You need to save the ones that are still alive.'
	stage8_story_text4 = 'You need to know what the heck is going on!'

	stage9_story_text1 = 'This automated rock crushing mashine probably won\'t give you any answers...'
	stage9_story_text2 = 'But you can\'t give up!'
	stage9_story_text3 = 'Answers are coming Neo...'
	stage9_story_text4 = 'Hmmmm...'
	
	#world 4 - VENUS
	stage10_story_text1 = 'You\'re exhausted after your most difficult life experience.'
	stage10_story_text2 = 'You will never forget about it and it will haunt you in your dreams.'
	stage10_story_text3 = 'But you know where to go now and what to do...'
	stage10_story_text4 = 'You must visit the real hell... it\'s called Venus'
	
	stage11_story_text1 = 'Here you are - Alpha Labs, hope of mankind in finding new home.'
	stage11_story_text2 = 'Billions of Credits, many years of work.'
	stage11_story_text3 = 'Looks like terraforming wasn\'t everything they were doing here.'
	stage11_story_text4 = 'It seems they tried to learn the nature of this mysterious alien life form.'
	stage11_story_text5 = 'For pure science? In defence? Or maybe for pure... profit?'
	stage11_story_text6 = 'Military industry was always interested in inventing new weapons.'
	stage11_story_text7 = 'So... did they created it or just studied them?'
	stage11_story_text8 = 'IF you survive then maybe you\'ll know the answer'
	stage11_story_text9 = 'IF...'
	
	stage12_story_text1 = 'Mass Lord Approaches!'
	stage12_story_text2 = '"Duck!... and cover!..."'
	stage12_story_text3 = ''
	stage12_story_text4 = ''

	#world 5 - NEPTUNE
	stage13_story_text1 = 'After defeating the Mass Lord you gained access to incredible alien technology.'
	stage13_story_text2 = 'You modify your Big City Destroyer, and now it becomes the first ever Galactic Cruiser!'
	stage13_story_text3 = 'You want to search all the stars in the galaxy and find out more about the aliens.'
	stage13_story_text4 = 'However something tells you that you have to make one last stop in the Solar System - the Neptune!'
	
	stage14_story_text1 = 'You find mysterious corridors on Neptune.'
	stage14_story_text2 = 'And of course... they\'re full of aliens!'
	stage14_story_text3 = ''
	stage14_story_text4 = ''
	
	stage15_story_text1 = 'What\'s this?? A gigant gigantula?'
	stage15_story_text2 = 'A Gigantulax!!'
	stage15_story_text3 = ''
	stage15_story_text4 = ''

	
	#bonuses
	bonuses = []
	bonus_loop = 0
	bonus_count = 0
	bonuses_per_level = 15
	# bonuses_per_level = 100 #for testing
	when_new_bonus = 0
	new_bonus_min_time = 30 # minimum time after new bonus will appear
	new_bonus_max_time = 70 # maximum time after new bonus will appear
	
	# ammunition ammount
	plasma_spheres = 15
	
	green_money = 3000
	gold_money = 12000
	
	medkit_ammount = 15
	
	medkit_model = None
	gasoline_model = None
	refrigerant_model = None
	laser_model = None
	plasma_model = None
	vortex_model = None
	money_green_model = None
	money_yellow_model = None
	
	keys = []
	keys_count = 0
	keys_per_level = 4
	keys_possesed = []
	blue_key_model = None
	red_key_model = None
	green_key_model = None
	yellow_key_model = None
	
	exit_opened = False

	def __init__(self, resolution):
		self.pixel_table = None
		self.map_size_x = resolution[0]
		self.map_size_y = resolution[1]
	
	#add new bonus ( delay - how long the bonus will stay on a map if it's not grabbed)
	def add_new_bonus(self, which_one, x, y, delay):
		self.bonuses.append(Bonus(which_one, x, y, delay))
		
	def add_new_key(self, which_one, x, y, delay):
		self.keys.append(Key(which_one, x, y, delay))

	#deprecated, player adds his own money
	# def add_money(self, new_money):
		# self.points += new_money
		# self.money += new_money
