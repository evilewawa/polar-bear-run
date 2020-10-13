#final
import pygame
import sys
import random
import time

pygame.init()
width = 1200
height = 300


white = (255,255,255)
black = (0,0,0)
green = (0,200,0)
dark_green = (0,100,0)
brown = (150,75,0)
orange = (240, 75, 0)
light_orange = (255, 100, 0)
red = (255, 0,0)
screen = pygame.display.set_mode((width, height))
counter2= 0
counter6 =0
polygon_position = [0, 260]
actual_score = 0
trunk_position = [0,260]
high_score = 0
#def trunk(pos_x,size_one, size_two):
#	pygame.draw.rect(screen,brown, (polygon_position[0] + pos_x,260, size_one,size_two))

clock = pygame.time.Clock()

fake_score = 0

fire_position = [0, 300]

fire_twitch = 0

font = pygame.font.Font('freesansbold.ttf', 32) 
font2 = pygame.font.Font('freesansbold.ttf', 12) 
bluk = 0

#def trunk(pos_x,size_one, size_two):
#	pygame.draw.rect(screen,brown, (polygon_position[0] + pos_x,260, size_one,size_two))
move_down = 0

avatar_position = [0,260]
time = 0

move_up = 0

numOfEnemies = 1

player_size = 10
colliding_rect = [avatar_position[0] + 140, avatar_position[1]-26]

counter = 0
counter3 = 0
enemy_size = 10
enemy_pos = [ 1200,random.randint(0,height-enemy_size)]
enemy_list = [enemy_pos]
score = 0

moving_down = 0

x = 0
y = 260
counter10 = 0
def initialize():
	counter10 =0
	avatar_position = [0,260]
	p_x = 0
	p_y = 0

	e_x = 0
	e_y = 0

	counter2= 0

	polygon_position = [0, 260]
	actual_score = 0
	trunk_position = [0,260]

	#def trunk(pos_x,size_one, size_two):
	#	pygame.draw.rect(screen,brown, (polygon_position[0] + pos_x,260, size_one,size_two))

	clock = pygame.time.Clock()

	fake_score = 0

	fire_position = [0, 300]

	fire_twitch = 0
	counter5= 0

	font = pygame.font.Font('freesansbold.ttf', 32) 
	font2 = pygame.font.Font('freesansbold.ttf', 12) 
	bluk = 0

	#def trunk(pos_x,size_one, size_two):
	#	pygame.draw.rect(screen,brown, (polygon_position[0] + pos_x,260, size_one,size_two))
	move_down = 0

	avatar_position = [0,260]
	time = 0

	move_up = 0

	numOfEnemies = 1
	counter6=0
	player_size = 10
	colliding_rect = [avatar_position[0] + 140, avatar_position[1]-26]
	counter20 = 0
	counter = 0
	counter3 = 0
	enemy_size = 10
	enemy_pos = [ 1200,random.randint(0,height-enemy_size)]
	enemy_list = [enemy_pos]
	score = 0

	moving_down = 0

	x = 0
	y = 260
	counter4 = 0
	randomNum = 0
	randomNum2 = 0
	if enemy_pos[0] == 1:
		randomNum2 = random.randint(0,50)
	randomNum3 = 0
	speed = 1
	avatar_position = [x,y]
	colliding_rect = [x,y]
	enemy_pos = [ 1200,random.randint(0,height-enemy_size)]	
	enemy_list = [enemy_pos]

def drop_enemies(enemy_list):
	delay = random.randint(0,100)

	if len(enemy_list) < numOfEnemies and delay < 95:
		x_pos = 1200
		y_pos = enemy_position(random.randint(1,5))
		enemy_list.append([x_pos, y_pos])

def enemy_position(number):
	if number == 1:
		return 220
	elif number == 2:
		return 250
	elif number ==3:
		return 230
	elif number ==4:
		return 250
	elif number == 5:
		return 210

randomNum = 0
randomNum2 = 0
if enemy_pos[0] == 1:
	randomNum2 = random.randint(0,50)
randomNum3 = 0

def randomNum12():
	return random.randint(0, width)
def randomNum21():
	return random.randint(0, height)

stars_pos = [randomNum12(), randomNum21()]
star_list = [stars_pos]

def draw_stars(star_list):
	for stars_pos in star_list:
		pygame.draw.rect(screen, white, (stars_pos[0], stars_pos[1], 2,2))

def drop_stars(star_list):
	delay = random.random()
	if len(star_list) < 5 and delay < .1:
		star_pos_x = random.randint(0,width)
		star_pos_y = random.randint(10,100)
		star_list.append([star_pos_x, star_pos_y])
def update_star_positions(star_list):
	for idx, stars_pos in enumerate(star_list):
		if len(star_list) < 5:
			draw_stars(star_list)
		else:
			star_list.pop(idx)

counter4 = 0

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		if actual_score < 10:
			enemy_pos[0] = 1200
		if enemy_pos[1] < 250:
			if randomNum2 < 30:
				if randomNum  == 0:
					pygame.draw.polygon(screen, white, [(enemy_pos[0], enemy_pos[1]), (enemy_pos[0] + 5,enemy_pos[1]), (enemy_pos[0] + 10, enemy_pos[1] - 3), (enemy_pos[0] + 15, enemy_pos[1]), (enemy_pos[0]+ 20, enemy_pos[1]), (enemy_pos[0] + 10, enemy_pos[1] - 5)])
				elif randomNum ==1:
					pygame.draw.polygon(screen, white, [(enemy_pos[0], enemy_pos[1] - 3), (enemy_pos[0] + 5,enemy_pos[1]), (enemy_pos[0] + 10, enemy_pos[1] - 3), (enemy_pos[0] + 15, enemy_pos[1]), (enemy_pos[0]+ 20, enemy_pos[1]-3), (enemy_pos[0] + 10, enemy_pos[1] - 5)])
			else:
				enemy_pos[1] == 250
				pygame.draw.rect(screen, white, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
		else:
			pygame.draw.rect(screen, white, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[0] <= 1200 and enemy_pos[0] >= 0:
			enemy_pos[0] -= speed

		else:
			enemy_list.pop(idx)

def collision_check(enemy_list, colliding_rect):
	for enemy_pos in enemy_list:
		if detect_collision1(enemy_pos, colliding_rect):
			return True
		if detect_collision2(enemy_pos, colliding_rect2):
			return True
		if detect_collision2(enemy_pos, colliding_rect3):
			return True
		if detect_collision2(enemy_pos, colliding_rect4):
			return True
	return False

def detect_collision1(colliding_rect, enemy_pos):
	p_x = colliding_rect[0]
	p_y = colliding_rect[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	#if x overlap
	if (e_x >= p_x and e_x < (p_x + 5)) or (p_x >= e_x and p_x < (e_x + 5)):
	#if y overlap
		if (e_y >= p_y and e_y < (p_y + 5)) or (p_y >= e_y and p_y < (e_y + 5)):
			return True
	return False
def detect_collision2(colliding_rect2, enemy_pos):
	p_x = colliding_rect2[0]
	p_y = colliding_rect2[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	#if x overlap
	if (e_x >= p_x and e_x < (p_x + 10)) or (p_x >= e_x and p_x < (e_x + 5)):
	#if y overlap
		if (e_y >= p_y and e_y < (p_y + 20)) or (p_y >= e_y and p_y < (e_y + 2)):
			return True
	return False
def detect_collision3(colliding_rect3, enemy_pos):
	p_x = colliding_rect3[0]
	p_y = colliding_rect3[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	#if x overlap
	if (e_x >= p_x and e_x < (p_x + 5)) or (p_x >= e_x and p_x < (e_x +5)):
	#if y overlap
		if (e_y >= p_y and e_y < (p_y -5 )) or (p_y >= e_y and p_y < (e_y -5)):
			return True
	return False
def detect_collision4(colliding_rect4, enemy_pos):
	p_x = colliding_rect4[0]
	p_y = colliding_rect4[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	#if x overlap
	if (e_x >= p_x and e_x < (p_x + 5)) or (p_x >= e_x and p_x < (e_x + 5)):
	#if y overlap
		if (e_y >= p_y and e_y < (p_y + 5)) or (p_y >= e_y and p_y < (e_y + 2)):
			return True
	return False

screen_over = False
game_over = True

counter5 = 0

speed = 1

while not screen_over:
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if actual_score == 1:
					x = 0
					y  = 260
				else:
					x = avatar_position[0]
					y = avatar_position[1]
				if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
					if y ==260:
						move_up += 1
				if event.key == pygame.K_DOWN:
					if y == 260:
						moving_down +=1
				

		if actual_score == 1:
			x = 0
			y  = 260
			move_up = 0
			moving_down = 0
			white = (255,255,255)
			black = (0,0,0)
		if move_up >= 1:
			y -=1
			if y <= 220:
				move_up = -1
		if move_up == -1:
			if counter < 75:
				counter +=1
			else:
				move_up = -2
		if move_up == -2:
			y += 1
			if y == 260:
				counter = 0
				move_up = 0

		if y < 220:
			y  =260
		if y != 260:
			counter5+=1
		else: 
			counter5 = 0
		if counter5 > 200:
			y = 260
			move_up = 0
			moving_down = 0



		if moving_down >= 1:
			y +=1
			if y >= 280:
				moving_down = -1
		if moving_down == -1:
			if counter10 < 75:
				counter10 +=1
			else:
				moving_down = -2
		if moving_down == -2:
			y -= 1
			if y == 260:
				counter10 = 0
				moving_down = 0

		if actual_score == 1:
			avatar_position = [0,260]
		avatar_position = [x,y]
		colliding_rect = [x,y]	
		screen.fill(black)
		a = polygon_position[0]
		b = polygon_position[1]
		if a > -1200:
			a -= 1
		else:
			a= 0
		polygon_position = [a,b]
		c = trunk_position[0]
		d= trunk_position[1]
		if c > -1200:
			c-=1
		else:
			c = 0
		trunk_position = [c,d]

		if counter3 == 75:
			randomNum = random.randint(0,1)
			counter3 = 0
		else:
			counter3+=1
		if counter10 == 0:
			numOfEnemies = 1

		randomNum4 = random.randint(0, width)
		randomNum5 = random.randint(0, height)

		point_a = [avatar_position[0]+100, avatar_position[1]]
		point_b = [avatar_position[0]+100, avatar_position[1]-30]
		point_c = [avatar_position[0]+140, avatar_position[1]-30]
		point_d = [avatar_position[0]+140, avatar_position[1]-26]
		point_e = [avatar_position[0]+150, avatar_position[1]-26]
		point_f = [avatar_position[0]+150, avatar_position[1]-16]
		point_g = [avatar_position[0]+140, avatar_position[1]-16]
		point_h = [avatar_position[0]+140, avatar_position[1]-12]
		point_i = [avatar_position[0]+130, avatar_position[1]-12]
		point_j = [avatar_position[0]+130, avatar_position[1]]	
		point_k = [avatar_position[0]+120, avatar_position[1]]
		point_l = [avatar_position[0]+120, avatar_position[1]-12]
		point_m = [avatar_position[0]+110, avatar_position[1]-12]	
		point_n = [avatar_position[0]+110, avatar_position[1]]
		eye = [avatar_position[0]+135,avatar_position[1]-27]
		colliding_rect = [avatar_position[0] + 140, avatar_position[1]-25]
		colliding_rect2 = [avatar_position[0] + 100, avatar_position[1] - 25]
		colliding_rect3 = [avatar_position[0] + 135, avatar_position[1] - 30]
		colliding_rect4 = [avatar_position[0] + 130, avatar_position[1] - 5]


		screen.fill(black)
		if actual_score == 1:
			numOfEnemies = 1
		
		
		fire_x = fire_position[0]
		fire_y = fire_position[1] 

		randomInt = random.randint(25, 75)
		if move_down == 0:
			if fire_y > 0:
				fire_y -= 1
		if fire_y == 0:
			move_down = 1
		if move_down == 1:
			if fire_y < randomInt:
				fire_y += 1
				if fire_y == randomInt:
					move_down = 0
		if fire_twitch == 1000:
			bluk = random.randint(-15,15)
			fire_twitch = 900
		else:
			fire_twitch += 1
		fire_position = [fire_x, fire_y]


		draw_stars(star_list)
		drop_stars(star_list)
		update_star_positions(star_list)
	##
		pygame.draw.rect(screen, white,(colliding_rect[0], colliding_rect[1], player_size, player_size))
		pygame.draw.rect(screen, white, (colliding_rect2[0], colliding_rect2[1], 10,20))
		pygame.draw.rect(screen, white, (colliding_rect3[0], colliding_rect3[1], 5,5))
		pygame.draw.rect(screen, white, (colliding_rect4[0], colliding_rect4[1], 5,5))

		pygame.draw.polygon(screen, light_orange, [(fire_position[0]+80, 300+fire_position[1]),(fire_position[0]+90, 180+fire_position[1]),(fire_position[0]+123, 130+fire_position[1]),(fire_position[0]+140 + bluk, 30+fire_position[1]),(fire_position[0]+220, 130+fire_position[1]),(fire_position[0]+210 + bluk, 60+fire_position[1]),(fire_position[0]+310, 110+fire_position[1]),(fire_position[0]+360 + bluk, 20+fire_position[1]),(fire_position[0]+380, 70+fire_position[1]),(fire_position[0]+440, 135+fire_position[1]),(fire_position[0]+450, 60+fire_position[1]),(fire_position[0]+505 + bluk, 27+fire_position[1]), (fire_position[0]+544, 90+fire_position[1]), (fire_position[0]+605, 15+fire_position[1]), (fire_position[0]+670 + bluk, 0+fire_position[1]), (fire_position[0]+715 +bluk , bluk + 15+fire_position[1]), (fire_position[0]+660, 30+fire_position[1]), (fire_position[0]+680, 60+fire_position[1]), (fire_position[0]+650, 150+fire_position[1]), (fire_position[0]+680, 140+fire_position[1]),(fire_position[0]+760, 100+fire_position[1]), (fire_position[0]+795 + bluk, 40+fire_position[1]),  (fire_position[0]+860, 130+fire_position[1]), (fire_position[0]+920 + bluk, 90+fire_position[1]), (fire_position[0]+965, 180+fire_position[1]), (fire_position[0]+1015, 125+fire_position[1]), (fire_position[0]+990 + bluk, 30+fire_position[1]), (fire_position[0]+1060, 70+fire_position[1]), (fire_position[0]+1080, 120+fire_position[1]), (fire_position[0]+1120, 200+fire_position[1]), (fire_position[0]+1140, 230+fire_position[1]), (fire_position[0]+1140, 300+fire_position[1])])
		pygame.draw.polygon(screen, red, [(fire_position[0] +100, 300+fire_position[1]), (fire_position[0] +116, 165+fire_position[1]), (fire_position[0] +140, 145+fire_position[1]), (fire_position[0] +153,83+fire_position[1]), (fire_position[0] +230, 180+fire_position[1]), (fire_position[0] +250, 140+fire_position[1]), (fire_position[0] +250, 100+fire_position[1]), (fire_position[0] +280, 130+fire_position[1]), (fire_position[0] +320, 130+fire_position[1]),(fire_position[0] +365, 60+fire_position[1]), (fire_position[0] +370, 90+fire_position[1]), (fire_position[0] +400, 140+fire_position[1]), (fire_position[0] +430, 170+fire_position[1]), (fire_position[0] +490,160+fire_position[1]), (fire_position[0] +470, 121+fire_position[1]), (fire_position[0] +500, 50+fire_position[1]), (fire_position[0] +526, 111+fire_position[1]), (fire_position[0] +550, 115+fire_position[1]), (fire_position[0] +600, 40+fire_position[1]), (fire_position[0] +630, 60+fire_position[1]), (fire_position[0] +650, 60+fire_position[1]), (fire_position[0] +630, 90+fire_position[1]), (fire_position[0] +630, 150+fire_position[1]), (fire_position[0] +640, 180+fire_position[1]), (fire_position[0] +720, 150+fire_position[1]), (fire_position[0] +760, 130+fire_position[1]), (fire_position[0] +795, 80+fire_position[1]), (fire_position[0] +820, 110+fire_position[1]), (fire_position[0] +840, 150+fire_position[1]), (fire_position[0] +880, 145+fire_position[1]), (fire_position[0] +905, 120+fire_position[1]), (fire_position[0] +960, 195+fire_position[1]), (fire_position[0] +1010, 160+fire_position[1]), (fire_position[0] +1030, 120+fire_position[1]), (fire_position[0] +1020, 70+fire_position[1]), (fire_position[0] +1060, 120+fire_position[1]), (fire_position[0] +1070, 170+fire_position[1]), (fire_position[0] +1100, 200+fire_position[1]), (fire_position[0] +1120, 300+fire_position[1])])


		pygame.draw.polygon(screen, dark_green, [(40, 260), (70,210),(100,260), (130,190), (160,260),(200,180),(240,260),(260,190), (280,260), (320,180), (360,260),(390,190),(420,260), (450,180),(480,260),(530,200),(580,260), (590,200),(600,260),(600+40, 260), (600+70,210),(600+100,260), (600+130,190), (600+160,260),(600+200,180),(600+240,260),(600+260,190), (600+280,260), (600+320,180), (600+360,260),(600+390,190),(600+420,260), (600+450,180),(600+480,260),(600+530,200),(600+580,260), (600+590,200),(600+600,260)])

		pygame.draw.polygon(screen,green, [(polygon_position[0], polygon_position[1] ), (polygon_position[0] + 35, polygon_position[1] - 60), (polygon_position[0] +70, polygon_position[1]),(polygon_position[0] + 100, polygon_position[1] - 80 ), (polygon_position[0] + 135, polygon_position[1] ),(polygon_position[0]+ 170, polygon_position[1] - 110 ), (polygon_position[0]+200, polygon_position[1] ), (polygon_position[0] + 230, polygon_position[1] - 60), (polygon_position[0]+260, polygon_position[1]),(polygon_position[0]+295, polygon_position[1] - 90), (polygon_position[0] + 330, polygon_position[1] ),(polygon_position[0] + 380, polygon_position[1] - 130 ),(polygon_position[0]+430, polygon_position[1] ),(polygon_position[0]+470, polygon_position[1] -120),(polygon_position[0] + 510, polygon_position[1]),(polygon_position[0]+530, polygon_position[1]-40),(polygon_position[0]+550, polygon_position[1]), (polygon_position[0]+570, polygon_position[1]-50),(polygon_position[0]+590, polygon_position[1]), (polygon_position[0]+640, polygon_position[1]-100), (polygon_position[0]+690,polygon_position[1]),(polygon_position[0]+730,polygon_position[1]-80),(polygon_position[0]+770,polygon_position[1]), (polygon_position[0]+820,polygon_position[1]-130),(polygon_position[0]+870,polygon_position[1]),(polygon_position[0]+900,polygon_position[1]-100),(polygon_position[0]+930,polygon_position[1]),(polygon_position[0]+960,polygon_position[1]-60),(polygon_position[0]+990,polygon_position[1]),(polygon_position[0]+1020,polygon_position[1]-120),(polygon_position[0]+1050,polygon_position[1]),(polygon_position[0]+1100,polygon_position[1]-120),(polygon_position[0]+1150,polygon_position[1]),(polygon_position[0]+1175,polygon_position[1]-40),(polygon_position[0]+1200,polygon_position[1])],  0)
		
		pygame.draw.polygon(screen,green, [(polygon_position[0]+1200, polygon_position[1] ), (polygon_position[0] + 35+1200, polygon_position[1] - 60), (polygon_position[0] +70+1200, polygon_position[1]),(polygon_position[0] + 100+1200, polygon_position[1] - 80 ), (polygon_position[0] + 135+1200, polygon_position[1] ),(polygon_position[0]+ 170+1200, polygon_position[1] - 110 ), (polygon_position[0]+200+1200, polygon_position[1] ), (polygon_position[0] +1200+ 230, polygon_position[1] - 60), (polygon_position[0]+260+1200, polygon_position[1]),(polygon_position[0]+295+1200, polygon_position[1] - 90), (polygon_position[0]+1200 + 330, polygon_position[1] ),(polygon_position[0] + 380+1200, polygon_position[1] - 130 ),(polygon_position[0]+1200+430, polygon_position[1] ),(polygon_position[0]+1200+470, polygon_position[1] -120),(polygon_position[0] +1200+ 510, polygon_position[1]),(polygon_position[0]+1200+530, polygon_position[1]-40),(polygon_position[0]+550+1200, polygon_position[1]), (polygon_position[0]+570+1200, polygon_position[1]-50),(polygon_position[0]+590+1200, polygon_position[1]), (polygon_position[0]+1200+640, polygon_position[1]-100), (polygon_position[0]+1200+690,polygon_position[1]),(polygon_position[0]+1200+730,polygon_position[1]-80),(polygon_position[0]+770+1200,polygon_position[1]), (polygon_position[0]+1200+820,polygon_position[1]-130),(polygon_position[0]+870+1200,polygon_position[1]),(polygon_position[0]+900+1200,polygon_position[1]-100),(polygon_position[0]+930+1200,polygon_position[1]),(polygon_position[0]+1200+960,polygon_position[1]-60),(polygon_position[0]+1200+990,polygon_position[1]),(polygon_position[0]+1200+1020,polygon_position[1]-120),(polygon_position[0]+1200+1050,polygon_position[1]),(polygon_position[0]+1200+1100,polygon_position[1]-120),(polygon_position[0]+1150+1200,polygon_position[1]),(polygon_position[0]+1175+1200,polygon_position[1]-40),(polygon_position[0]+1200+1200,polygon_position[1])],  0)

		pygame.draw.polygon(screen, brown,[(polygon_position[0]+30, polygon_position[1]),(polygon_position[0]+30, polygon_position[1] -20 ), (polygon_position[0]+38,polygon_position[1]-20),(polygon_position[0]+38, polygon_position[1]), (polygon_position[0]+95,polygon_position[1]), (polygon_position[0]+95, polygon_position[1]- 25),(polygon_position[0]+105,polygon_position[1]-25),(polygon_position[0]+105,polygon_position[1]),(polygon_position[0]+163,polygon_position[1]), (polygon_position[0]+163, polygon_position[1]- 30),(polygon_position[0]+170,polygon_position[1]-30),(polygon_position[0]+170,polygon_position[1]),(polygon_position[0]+227,polygon_position[1]), (polygon_position[0]+227, polygon_position[1]- 25),(polygon_position[0]+232,polygon_position[1]-25),(polygon_position[0]+232,polygon_position[1]),(polygon_position[0]+290,polygon_position[1]), (polygon_position[0]+290, polygon_position[1]- 25),(polygon_position[0]+300,polygon_position[1]-25),(polygon_position[0]+300,polygon_position[1]),(polygon_position[0]+375,polygon_position[1]), (polygon_position[0]+375, polygon_position[1]- 35),(polygon_position[0]+382,polygon_position[1]-35),(polygon_position[0]+382,polygon_position[1]),(polygon_position[0]+465,polygon_position[1]), (polygon_position[0]+465, polygon_position[1]- 30),(polygon_position[0]+472,polygon_position[1]-30),(polygon_position[0]+472,polygon_position[1]),(polygon_position[0]+527,polygon_position[1]), (polygon_position[0]+527, polygon_position[1]- 15),(polygon_position[0]+532,polygon_position[1]-15),(polygon_position[0]+532,polygon_position[1]),(polygon_position[0]+568,polygon_position[1]), (polygon_position[0]+568, polygon_position[1]- 15),(polygon_position[0]+572,polygon_position[1]-15),(polygon_position[0]+572,polygon_position[1]),(polygon_position[0]+635,polygon_position[1]), (polygon_position[0]+635, polygon_position[1]- 28),(polygon_position[0]+643,polygon_position[1]-28),(polygon_position[0]+643,polygon_position[1]),(polygon_position[0]+726,polygon_position[1]), (polygon_position[0]+726, polygon_position[1]- 28),(polygon_position[0]+733,polygon_position[1]-28),(polygon_position[0]+733,polygon_position[1]),(polygon_position[0]+810,polygon_position[1]), (polygon_position[0]+810, polygon_position[1]- 28),(polygon_position[0]+820,polygon_position[1]-28),(polygon_position[0]+820,polygon_position[1]),(polygon_position[0]+897,polygon_position[1]), (polygon_position[0]+897, polygon_position[1]- 28),(polygon_position[0]+902,polygon_position[1]-28),(polygon_position[0]+902,polygon_position[1]),(polygon_position[0]+957,polygon_position[1]), (polygon_position[0]+957, polygon_position[1]- 15),(polygon_position[0]+962,polygon_position[1]-15),(polygon_position[0]+962,polygon_position[1]),(polygon_position[0]+1017,polygon_position[1]), (polygon_position[0]+1017, polygon_position[1]- 29),(polygon_position[0]+1023,polygon_position[1]-29),(polygon_position[0]+1023,polygon_position[1]),(polygon_position[0]+1095,polygon_position[1]), (polygon_position[0]+1095, polygon_position[1]- 35),(polygon_position[0]+1105,polygon_position[1]-35),(polygon_position[0]+1105,polygon_position[1]),(polygon_position[0]+1172,polygon_position[1]), (polygon_position[0]+1172, polygon_position[1]- 15),(polygon_position[0]+1177,polygon_position[1]-15),(polygon_position[0]+1177,polygon_position[1]), (polygon_position[0],polygon_position[1])])

		pygame.draw.polygon(screen, brown,[(polygon_position[0]+30+1200, polygon_position[1]),(polygon_position[0]+30+1200, polygon_position[1] -20 ), (polygon_position[0]+38+1200,polygon_position[1]-20),(polygon_position[0]+38+1200, polygon_position[1]), (polygon_position[0]+95+1200,polygon_position[1]), (polygon_position[0]+95+1200, polygon_position[1]- 25),(polygon_position[0]+105+1200,polygon_position[1]-25),(polygon_position[0]+105+1200,polygon_position[1]),(polygon_position[0]+163+1200,polygon_position[1]), (polygon_position[0]+163+1200, polygon_position[1]- 30),(polygon_position[0]+170+1200,polygon_position[1]-30),(polygon_position[0]+170+1200,polygon_position[1]),(polygon_position[0]+227+1200,polygon_position[1]), (polygon_position[0]+227+1200, polygon_position[1]- 25),(polygon_position[0]+232+1200,polygon_position[1]-25),(polygon_position[0]+232+1200,polygon_position[1]),(polygon_position[0]+290+1200,polygon_position[1]), (polygon_position[0]+290+1200, polygon_position[1]- 25),(polygon_position[0]+300+1200,polygon_position[1]-25),(polygon_position[0]+300+1200,polygon_position[1]),(polygon_position[0]+375+1200,polygon_position[1]), (polygon_position[0]+375+1200, polygon_position[1]- 35),(polygon_position[0]+382+1200,polygon_position[1]-35),(polygon_position[0]+382+1200,polygon_position[1]),(polygon_position[0]+465+1200,polygon_position[1]), (polygon_position[0]+465+1200, polygon_position[1]- 30),(polygon_position[0]+472+1200,polygon_position[1]-30),(polygon_position[0]+472+1200,polygon_position[1]),(polygon_position[0]+527+1200,polygon_position[1]), (polygon_position[0]+527+1200, polygon_position[1]- 15),(polygon_position[0]+532+1200,polygon_position[1]-15),(polygon_position[0]+532+1200,polygon_position[1]),(polygon_position[0]+568+1200,polygon_position[1]), (polygon_position[0]+568+1200, polygon_position[1]- 15),(polygon_position[0]+572+1200,polygon_position[1]-15),(polygon_position[0]+572+1200,polygon_position[1]),(polygon_position[0]+635+1200,polygon_position[1]), (polygon_position[0]+635+1200, polygon_position[1]- 28),(polygon_position[0]+643+1200,polygon_position[1]-28),(polygon_position[0]+643+1200,polygon_position[1]),(polygon_position[0]+726+1200,polygon_position[1]), (polygon_position[0]+726+1200, polygon_position[1]- 28),(polygon_position[0]+733+1200,polygon_position[1]-28),(polygon_position[0]+733+1200,polygon_position[1]),(polygon_position[0]+810+1200,polygon_position[1]), (polygon_position[0]+810+1200, polygon_position[1]- 28),(polygon_position[0]+820+1200,polygon_position[1]-28),(polygon_position[0]+820+1200,polygon_position[1]),(polygon_position[0]+897+1200,polygon_position[1]), (polygon_position[0]+897+1200, polygon_position[1]- 28),(polygon_position[0]+902+1200,polygon_position[1]-28),(polygon_position[0]+902+1200,polygon_position[1]),(polygon_position[0]+957+1200,polygon_position[1]), (polygon_position[0]+957+1200, polygon_position[1]- 15),(polygon_position[0]+962+1200,polygon_position[1]-15),(polygon_position[0]+962+1200,polygon_position[1]),(polygon_position[0]+1017+1200,polygon_position[1]), (polygon_position[0]+1017+1200, polygon_position[1]- 29),(polygon_position[0]+1023+1200,polygon_position[1]-29),(polygon_position[0]+1023+1200,polygon_position[1]),(polygon_position[0]+1095+1200,polygon_position[1]), (polygon_position[0]+1095+1200, polygon_position[1]- 35),(polygon_position[0]+1105+1200,polygon_position[1]-35),(polygon_position[0]+1105+1200,polygon_position[1]),(polygon_position[0]+1172+1200,polygon_position[1]), (polygon_position[0]+1172+1200, polygon_position[1]- 15),(polygon_position[0]+1177+1200,polygon_position[1]-15),(polygon_position[0]+1177+1200,polygon_position[1]), (polygon_position[0]+1200,polygon_position[1])])

		pygame.draw.polygon(screen, white, [(point_a[0], point_a[1]), (point_b[0], point_b[1]), (point_c[0], point_c[1]),(point_d[0], point_d[1]), (point_e[0], point_e[1]),(point_f[0], point_f[1]), (point_g[0], point_g[1]), (point_h[0], point_h[1]),(point_i[0], point_i[1]), (point_j[0], point_j[1]), (point_k[0], point_k[1]),(point_l[0], point_l[1]),(point_m[0], point_m[1]),(point_n[0], point_n[1])])
		pygame.draw.rect(screen,black,(eye[0],eye[1], 5,5))

		if detect_collision1(colliding_rect, enemy_pos):
			game_over = True
			screen.fill(black)
		if detect_collision2(colliding_rect2, enemy_pos):
			game_over = True
			screen.fill(black)
		if detect_collision4(colliding_rect3, enemy_pos):
			game_over = True
			screen.fill(black)
		if detect_collision4(colliding_rect4, enemy_pos):
			game_over = True
			screen.fill(black)

		drop_enemies(enemy_list)
		update_enemy_positions(enemy_list)

		if collision_check(enemy_list,colliding_rect):
			game_over = True
			screen.fill(black)
			break
		draw_enemies(enemy_list)


		randomNum3 = random.randint(0, 1000)


		pygame.draw.rect(screen,white, (0, 260, 1200, 10))
		pygame.draw.rect(screen, black, (0, 270, 1200, 30))
		score += 1
		if score == 100:
			score = 0
			actual_score += 1
		text = "Score: " + str(actual_score)
		label = font.render(text, 1, white)
		screen.blit(label, (width-175, height-260))

		if actual_score > 0:
			if actual_score% 10 == 0:
				fake_score += 0.01

		if fake_score < 3:
			speed = fake_score
		if speed > 2:
			if counter2 == 1000:
				numOfEnemies = 1
			else:
				counter2+=1
		if actual_score > 75 and actual_score < 100:
			white = (0,0,0)
			black = (255,255,255)
		else: 
			white = (255,255,255)
			black = (0,0,0)
		text4 = "Instructions"
		label4 = font2.render(text4,1,white)
		screen.blit(label4, (20, 20))	
		text5 = "Space to Jump"
		label5 = font2.render(text5,1,white)
		screen.blit(label5, (20, 30))
		text6 = "Down arrow to duck"
		label6 = font2.render(text6,1,white)
		screen.blit(label6, (20, 40))
		text7 = "Avoid birds and bumps"
		label7 = font2.render(text7,1,white)
		screen.blit(label7, (20, 50))
		if high_score < actual_score:
			high_score = actual_score

		clock.tick(500)	
		pygame.display.update()
		if game_over:
			black = (0,0,0)
			white = (255,255,255)
	while game_over:
		score = 0
		actual_score = 0
		fake_score = 0
		numOfEnemies = 1
		counter2= 0
		initialize()

		pygame.draw.rect(screen,white, (width/2-50,height/2 - 50,100,100))
		white = (255,255,255)
		black = (0,0,0)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					game_over = False
		text2 = "Start"
		label2 = font.render(text2,1,black)
		screen.blit(label2, (width/2-45, height/2-25))
		text3 = "or left click"
		label3 = font2.render(text3,1,black)
		screen.blit(label3, (width/2-45, height/2+20))
		text4 = "Spam S key"
		label4 = font2.render(text4,1,black)
		screen.blit(label4, (width/2-45, height/2+5))
		mouse = pygame.mouse.get_pos()
		mouse2 =0
		if pygame.mouse.get_pressed()[0]:
			mouse2 = 1
		counter6+=1
		if counter6 > 500 and counter6<5000:
			if counter6 %5==0:
				pygame.draw.rect(screen, white, (random.randint(0, width), random.randint(0,height), 2,2))
			counter6 +=1
		text8 = "Highscore: "  +str(high_score)
		label8 = font.render(text8,1,white)
		screen.blit(label8, (500, 200))
		if 650 > mouse[0] > 550 and 200> mouse[1] > 100 and mouse2 == 1:
			game_over = False
		else:
			pygame.draw.rect(screen, white, (mouse[0],mouse[1], 2,2))

		pygame.display.update()
print(actual_score)
pygame.quit()
