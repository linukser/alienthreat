from numpy import *

def add_object(game, obj_pos_x, obj_pos_y, obj_size_x, obj_size_y):
	new_pos_x = obj_pos_x - obj_size_x + int(obj_size_x / 4.0) # - 1 1/4
	new_pos_y = obj_pos_y - obj_size_y + int(obj_size_y / 4.0) # - 1 1/4
	
	for x in range(new_pos_x, new_pos_x + obj_size_x + int(obj_size_x / 2.0) + int(obj_size_x / 4.0)): # + 3/4
		for y in range(new_pos_y, new_pos_y + obj_size_y + int(obj_size_y / 2.0) + int(obj_size_y / 4.0)): # + 3/4
			game.pixel_table[x][y] = 1
			
def clear_object_table(game):
	game.pixel_table = zeros( (4000, 4000) )

def set_labirynth(game, labirynth, dim_x, dim_y):
	# print labirynth
	# print labirynth.getCell( (0, 0) )
	
	#horizontal
	i = 0
	while i < 64 * 5 * dim_x:
		add_object(game, i + game.x, 0 + game.y, 64, 64)
		add_object(game, i + game.x, 64 * 5 * dim_x + game.y, 64, 64)
		i += 64
		
	#vertical
	i = 0
	while i < 64 * 5 * dim_y:
		add_object(game, 0 + game.x, i + game.y, 64, 64)
		add_object(game, 64 * 5 * dim_x + game.x, i + game.y, 64, 64)
		i += 64
	
	for x in range(0, dim_x):
		for y in range(0, dim_y):
			cell = labirynth.getCell( (y, x) )
			if cell == 0:
				dirs = [0, 0, 0, 0]
			elif cell == 1:
				dirs = [0, 0, 0, 1]
			elif cell == 2:
				dirs = [0, 0, 1, 0]
			elif cell == 3:
				dirs = [0, 0, 1, 1]
			elif cell == 4:
				dirs = [0, 1, 0, 0]
			elif cell == 5:
				dirs = [0, 1, 0, 1]
			elif cell == 6:
				dirs = [0, 1, 1, 0]
			elif cell == 7:
				dirs = [0, 1, 1, 1]
			elif cell == 8:
				dirs = [1, 0, 0, 0]
			elif cell == 9:
				dirs = [1, 0, 0, 1]
			elif cell == 10:
				dirs = [1, 0, 1, 0]
			elif cell == 11:
				dirs = [1, 0, 1, 1]
			elif cell == 12:
				dirs = [1, 1, 0, 0]
			elif cell == 13:
				dirs = [1, 1, 0, 1]
			elif cell == 14:
				dirs = [1, 1, 1, 0]
			elif cell == 15:
				dirs = [1, 1, 1, 1]
			
			if dirs[3] == 0:
				for i in range (1, 6):
					add_object(game, 320 * y + 64 * i + game.x, 320 * x + game.y, 64, 64)
			if dirs[2] == 0:
				for i in range (1, 6):
					add_object(game, 320 * y + game.x + 320, 320 * x + i * 64 + game.y, 64, 64)
			if dirs[1] == 0:
				for i in range (1, 6):
					add_object(game, 320 * y + 64 * i + game.x, 320 * x + game.y + 320, 64, 64)
			if dirs[0] == 0:
				for i in range (1, 6):
					add_object(game, 320 * y + game.x, 320 * x + i * 64 + game.y, 64, 64)
			
def draw_labirynth(screen, game, labirynth, wall1, dim_x, dim_y):
	# f = open('d:/prg/AlienThreat/logs/matrix', 'w')
	# f = open('f:/prg/at/AlienThreat/logs/labirynth', 'w')
	
	#horizontal
	i = 0
	while i < 64 * 5 * dim_x:
		screen.blit(wall1, (i + game.x, 0 + game.y))
		screen.blit(wall1, (i + game.x, 64 * 5 * dim_x + game.y))
		i += 64
		
	#vertical
	i = 0
	while i < 64 * 5 * dim_y:
		screen.blit(wall1, (0 + game.x, i + game.y))
		screen.blit(wall1, (64 * 5 * dim_x + game.x, i + game.y))
		i += 64
	
	for x in range(0, dim_x):
		for y in range(0, dim_y):		
			cell = labirynth.getCell( (y, x) )
			if cell == 0:
				dirs = [0, 0, 0, 0]
			elif cell == 1:
				dirs = [0, 0, 0, 1]
			elif cell == 2:
				dirs = [0, 0, 1, 0]
			elif cell == 3:
				dirs = [0, 0, 1, 1]
			elif cell == 4:
				dirs = [0, 1, 0, 0]
			elif cell == 5:
				dirs = [0, 1, 0, 1]
			elif cell == 6:
				dirs = [0, 1, 1, 0]
			elif cell == 7:
				dirs = [0, 1, 1, 1]
			elif cell == 8:
				dirs = [1, 0, 0, 0]
			elif cell == 9:
				dirs = [1, 0, 0, 1]
			elif cell == 10:
				dirs = [1, 0, 1, 0]
			elif cell == 11:
				dirs = [1, 0, 1, 1]
			elif cell == 12:
				dirs = [1, 1, 0, 0]
			elif cell == 13:
				dirs = [1, 1, 0, 1]
			elif cell == 14:
				dirs = [1, 1, 1, 0]
			elif cell == 15:
				dirs = [1, 1, 1, 1]
				
			# f.write(str(cell))
			# f.write("\t")
			
			if dirs[3] == 0:
				for i in range (1, 6):
					screen.blit(wall1, (320 * y + 64 * i + game.x, 320 * x + game.y))
			if dirs[2] == 0:
				for i in range (1, 6):
					screen.blit(wall1, (320 * y + game.x + 320, 320 * x + i * 64 + game.y))
			if dirs[1] == 0:
				for i in range (1, 6):
					screen.blit(wall1, (320 * y + 64 * i + game.x, 320 * x + game.y + 320))
			if dirs[0] == 0:
				for i in range (1, 6):
					screen.blit(wall1, (320 * y + game.x, 320 * x + i * 64 + game.y))
			
		# f.write("\n")
					
	# f.close()
