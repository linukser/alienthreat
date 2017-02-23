import pygame

class Player:
	
	def __init__(self, x, y, model, pain_model, game):
		self.name = None
	
		self.money = 0
		# self.money = 5000000
	
		self.x = x
		self.y = y
		self.model = pygame.image.load(model)
		self.pain_model = pygame.image.load(pain_model)
		
		self.dead = False
		self.being_attacked = False
		self.in_mass = False
		
		#movement
		self.offsetX = 0
		self.offsetY = 0
		
		#upgrades
		self.has_super_regeneration_upgrade = False
		self.has_body_armor_upgrade = False
		self.has_enhanced_vortex_upgrade = False
		self.has_level2_force_field_upgrade = False
		self.has_light_armor_upgrade = False
		self.has_force_field = False
		
		self.has_flamethrower_upgrade1 = False
		self.has_flamethrower_upgrade2 = False
		
		self.has_laser_upgrade1 = False
		self.has_laser_upgrade2 = False
		
		self.has_plasma_upgrade1 = False
		self.has_plasma_upgrade2 = False
		
		self.has_freezer_upgrade1 = False
		self.has_freezer_upgrade2 = False

		self.flamethrower_range_upgrade = 1 #must NOT be zero! otherwise not upgraded flamethrower won't work (fireball diameter is mutliplied by this variable)
		self.plasma_range_upgrade = 1 #must NOT be zero! otherwise not upgraded plasma won't work (plasma fireball diameter is mutliplied by this variable)
		self.freezer_range_upgrade = 0
		self.laser_diameter_upgrade = 0
		
		self.laser_time_upgrade = 0
		self.laser_time_upgrade_loop = 0
		self.laser_time_upgrade_loop_max = 400
		
		#game stuff
		self.max_energy = 100
		self.energy = 100
		
		self.experience = 0
		
		# if game.difficulty == 'hard':
			# self.base_armor = 2
			# self.armor = 2
		# elif game.difficulty == 'medium':
			# self.base_armor = 5
			# self.armor = 5
		# elif game.difficulty == 'easy':
			# self.base_armor = 10
			# self.armor = 10
			
		# self.base_armor = 10
		# self.armor = 10
		
		# armor is overwritten anyway when chosing character
		self.base_armor = self.armor = 200
		
		
		# self.base_armor = 999999
		# self.armor = 999999

		self.force_field = 100 #emergency force field, turns on automatically if player energy drops below ff_auto_enable_level (usually 25)
		self.max_force_field = 100
		#self.force_field = 500 #for testing
		self.force_field_enabled = False
		self.ff_auto_enable_level = 25
		
		self.slot1 = 0
		self.slot2 = 0
		self.slot3 = 0
		self.slot4 = 0
		
		self.laser_ammo = 70
		self.flamethrower_ammo = 35 # 25 litres of gasoline
		self.freezer_ammo = 100
		self.plasma_ammo = 20
		
		# for testing
		# self.laser_ammo = 5
		# self.flamethrower_ammo = 250
		# self.freezer_ammo = 200
		# self.plasma_ammo = 50
		
		self.vortex_ammo = 0
		#self.vortex_ammo = 3
		
		self.ammo = {'laser': self.laser_ammo, 'flamethrower': self.flamethrower_ammo * 1000, 'freezer': self.freezer_ammo * 10, 'plasma': self.plasma_ammo * 10, 'vortex': self.vortex_ammo}
		
		self.laser_max_ammo = 70
		self.flamethrower_max_ammo = 35 # 25 litres of gasoline
		self.freezer_max_ammo = 300
		self.plasma_max_ammo = 50
		self.vortex_max_ammo = 1
		
		self.max_ammo = {'laser': self.laser_max_ammo, 'flamethrower': self.flamethrower_max_ammo * 1000, 'freezer': self.freezer_max_ammo * 10, 'plasma': self.plasma_max_ammo * 10, 'vortex': self.vortex_max_ammo}
		
		self.laser_loop = 0
		self.laser_loop_max = 6 #the bigger value, the slower regeneration
		
		self.vortex_loop = 0
		self.vortex_loop_max = 25 # if this number is lower then vortex regenerates faster
		
		#weapons
		self.fire = False
		self.current_weapon = "flamethrower"
		self.next_weapon = False
		self.vortex_launched = False
		
		#speed is overwritten anyway when chosing character
		self.base_speed = self.player_speed = 3 #the bigger number, the faster player goes
		self.angle = 0
		
	#check if player is still alive
	def alive(self):
		if self.dead == False and self.energy > 0:
			return True
		else:
			return False
		
	def add_ammo(self, weapon, new_ammo):
	
		if weapon == 'flamethrower':
			new_ammo *= 1000
			
		if weapon == 'freezer' or weapon == 'plasma':
			new_ammo *= 10
	
		if self.ammo[weapon] < self.max_ammo[weapon]:
			self.ammo[weapon] += new_ammo
		
		if self.ammo[weapon] > self.max_ammo[weapon]:
			self.ammo[weapon] = self.max_ammo[weapon]
			
	def add_energy(self, new_energy):
		if self.energy < self.max_energy:
			self.energy += new_energy
			
		if self.energy > self.max_energy:
			self.energy = self.max_energy
		
	doctor_energy_regeneration = False
		
	def regenerate_energy(self, difficulty):
		if self.has_super_regeneration_upgrade == False:
			if difficulty == 'easy':
				if self.energy < self.max_energy:
					self.energy += 1
			elif difficulty == 'medium':
				if self.energy < (self.max_energy / 2.0) + 5:
					self.energy += 1
			elif difficulty == 'hard':
				if self.energy < (self.max_energy / 4.0) + 5:
					self.energy += 1
		elif self.has_super_regeneration_upgrade == True:
			if difficulty == 'easy':
				if self.energy < self.max_energy:
					self.energy += 1
			elif difficulty == 'medium':
				if self.energy < self.max_energy:
					self.energy += 1
			elif difficulty == 'hard':
				if self.energy < self.max_energy:
					self.energy += 1
			
	def regenerate_force_field(self):
		if self.force_field < self.max_force_field:
			self.force_field += 1
				
	def get_ammo(self, weapon):
		if weapon == 'flamethrower':
			return self.ammo['flamethrower'] / 100
		elif weapon == 'laser':
			return self.ammo['laser'] / 10
		elif weapon == 'plasma':
			return self.ammo['plasma'] / 10
		elif weapon == 'freezer':
			return self.ammo['freezer'] / 10
				
	def get_max_ammo(self, weapon):
		if weapon == 'flamethrower':
			return self.flamethrower_max_ammo
		elif weapon == 'laser':
			return self.laser_max_ammo
		elif weapon == 'plasma':
			return self.plasma_max_ammo
		elif weapon == 'freezer':
			return self.freezer_max_ammo
