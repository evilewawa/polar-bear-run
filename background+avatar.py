import pygame
import sys
import random
import time

width = 1200
height = 300


white = (255,255,255)
black = (0,0,0)
green = (0,200,0)
dark_green = (0,100,0)
brown = (150,75,0)
screen = pygame.display.set_mode((width, height))

polygon_position = [0, 260]

trunk_position = [0,260]

#def trunk(pos_x,size_one, size_two):
#	pygame.draw.rect(screen,brown, (polygon_position[0] + pos_x,260, size_one,size_two))

clock = pygame.time.Clock()

avatar_position = [0,260]
time = 0

move_up = 0

player_size = 10
colliding_rect = [avatar_position[0] + 140, avatar_position[1]-26]

counter = 0

enemy_size = 20
enemy_pos = [ 1200,random.randint(0,height-enemy_size)]
enemy_list = [enemy_pos]

x = 0
y = 260

def drop_enemies(enemy_list):
	delay = random.random()

	if len(enemy_list) < 1 and delay < 0.1:
		x_pos = 1200
		y_pos = enemy_position(random.randint(1,3))
		enemy_list.append([x_pos, y_pos])

def enemy_position(number):
	if number == 1:
		return 220
	elif number == 2:
		return 250
	elif number ==3:
		return 230


def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, white, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[0] <= 1200 and enemy_pos[0] >= 0:
			enemy_pos[0] -= speed
		else:
			enemy_list.pop(idx)

def collision_check(enemy_list, colliding_rect):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, colliding_rect):
			return True
	return False

def detect_collision(colliding_rect, enemy_pos):
	p_x = colliding_rect[0]
	p_y = colliding_rect[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	#if x overlap: 1200 bigger than or equal to 140, and 1200 is less than 150 or 140 bigger than or equal to 1200 and 140 is less tha
	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x - enemy_size)):
	#if y overlap
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y - enemy_size)):
			print(enemy_pos, point_f, e_x, p_x, p_y,e_y)
			return True

	return False

game_over = False

speed = 2

while not game_over:
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			x = avatar_position[0]
			y = avatar_position[1]
			if event.key == pygame.K_UP:
				move_up += 1


			if event.key == pygame.K_DOWN:
				y +=40
				if y > 260:
					y -=40				
			
	if move_up >= 1:
		y -=1
		if y <= 220:
			move_up = -1
	if move_up == -1:
		if counter < 150:
			counter +=1
		else:
			move_up = -2
	if move_up == -2:
		y += 1
		if y == 260:
			counter = 0
			move_up = 0


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
	colliding_rect = [avatar_position[0] + 140, avatar_position[1]-26]




	screen.fill(black)
	
	
	

	pygame.draw.polygon(screen, dark_green, [(40, 260), (70,210),(100,260), (130,190), (160,260),(200,180),(240,260),(260,190), (280,260), (320,180), (360,260),(390,190),(420,260), (450,180),(480,260),(530,200),(580,260), (590,200),(600,260),(600+40, 260), (600+70,210),(600+100,260), (600+130,190), (600+160,260),(600+200,180),(600+240,260),(600+260,190), (600+280,260), (600+320,180), (600+360,260),(600+390,190),(600+420,260), (600+450,180),(600+480,260),(600+530,200),(600+580,260), (600+590,200),(600+600,260)])

	pygame.draw.polygon(screen,green, [(polygon_position[0], polygon_position[1] ), (polygon_position[0] + 35, polygon_position[1] - 60), (polygon_position[0] +70, polygon_position[1]),(polygon_position[0] + 100, polygon_position[1] - 80 ), (polygon_position[0] + 135, polygon_position[1] ),(polygon_position[0]+ 170, polygon_position[1] - 110 ), (polygon_position[0]+200, polygon_position[1] ), (polygon_position[0] + 230, polygon_position[1] - 60), (polygon_position[0]+260, polygon_position[1]),(polygon_position[0]+295, polygon_position[1] - 90), (polygon_position[0] + 330, polygon_position[1] ),(polygon_position[0] + 380, polygon_position[1] - 130 ),(polygon_position[0]+430, polygon_position[1] ),(polygon_position[0]+470, polygon_position[1] -120),(polygon_position[0] + 510, polygon_position[1]),(polygon_position[0]+530, polygon_position[1]-40),(polygon_position[0]+550, polygon_position[1]), (polygon_position[0]+570, polygon_position[1]-50),(polygon_position[0]+590, polygon_position[1]), (polygon_position[0]+640, polygon_position[1]-100), (polygon_position[0]+690,polygon_position[1]),(polygon_position[0]+730,polygon_position[1]-80),(polygon_position[0]+770,polygon_position[1]), (polygon_position[0]+820,polygon_position[1]-130),(polygon_position[0]+870,polygon_position[1]),(polygon_position[0]+900,polygon_position[1]-100),(polygon_position[0]+930,polygon_position[1]),(polygon_position[0]+960,polygon_position[1]-60),(polygon_position[0]+990,polygon_position[1]),(polygon_position[0]+1020,polygon_position[1]-120),(polygon_position[0]+1050,polygon_position[1]),(polygon_position[0]+1100,polygon_position[1]-120),(polygon_position[0]+1150,polygon_position[1]),(polygon_position[0]+1175,polygon_position[1]-40),(polygon_position[0]+1200,polygon_position[1])],  0)
	
	pygame.draw.polygon(screen,green, [(polygon_position[0]+1200, polygon_position[1] ), (polygon_position[0] + 35+1200, polygon_position[1] - 60), (polygon_position[0] +70+1200, polygon_position[1]),(polygon_position[0] + 100+1200, polygon_position[1] - 80 ), (polygon_position[0] + 135+1200, polygon_position[1] ),(polygon_position[0]+ 170+1200, polygon_position[1] - 110 ), (polygon_position[0]+200+1200, polygon_position[1] ), (polygon_position[0] +1200+ 230, polygon_position[1] - 60), (polygon_position[0]+260+1200, polygon_position[1]),(polygon_position[0]+295+1200, polygon_position[1] - 90), (polygon_position[0]+1200 + 330, polygon_position[1] ),(polygon_position[0] + 380+1200, polygon_position[1] - 130 ),(polygon_position[0]+1200+430, polygon_position[1] ),(polygon_position[0]+1200+470, polygon_position[1] -120),(polygon_position[0] +1200+ 510, polygon_position[1]),(polygon_position[0]+1200+530, polygon_position[1]-40),(polygon_position[0]+550+1200, polygon_position[1]), (polygon_position[0]+570+1200, polygon_position[1]-50),(polygon_position[0]+590+1200, polygon_position[1]), (polygon_position[0]+1200+640, polygon_position[1]-100), (polygon_position[0]+1200+690,polygon_position[1]),(polygon_position[0]+1200+730,polygon_position[1]-80),(polygon_position[0]+770+1200,polygon_position[1]), (polygon_position[0]+1200+820,polygon_position[1]-130),(polygon_position[0]+870+1200,polygon_position[1]),(polygon_position[0]+900+1200,polygon_position[1]-100),(polygon_position[0]+930+1200,polygon_position[1]),(polygon_position[0]+1200+960,polygon_position[1]-60),(polygon_position[0]+1200+990,polygon_position[1]),(polygon_position[0]+1200+1020,polygon_position[1]-120),(polygon_position[0]+1200+1050,polygon_position[1]),(polygon_position[0]+1200+1100,polygon_position[1]-120),(polygon_position[0]+1150+1200,polygon_position[1]),(polygon_position[0]+1175+1200,polygon_position[1]-40),(polygon_position[0]+1200+1200,polygon_position[1])],  0)

	pygame.draw.polygon(screen, brown,[(polygon_position[0]+30, polygon_position[1]),(polygon_position[0]+30, polygon_position[1] -20 ), (polygon_position[0]+38,polygon_position[1]-20),(polygon_position[0]+38, polygon_position[1]), (polygon_position[0]+95,polygon_position[1]), (polygon_position[0]+95, polygon_position[1]- 25),(polygon_position[0]+105,polygon_position[1]-25),(polygon_position[0]+105,polygon_position[1]),(polygon_position[0]+163,polygon_position[1]), (polygon_position[0]+163, polygon_position[1]- 30),(polygon_position[0]+170,polygon_position[1]-30),(polygon_position[0]+170,polygon_position[1]),(polygon_position[0]+227,polygon_position[1]), (polygon_position[0]+227, polygon_position[1]- 25),(polygon_position[0]+232,polygon_position[1]-25),(polygon_position[0]+232,polygon_position[1]),(polygon_position[0]+290,polygon_position[1]), (polygon_position[0]+290, polygon_position[1]- 25),(polygon_position[0]+300,polygon_position[1]-25),(polygon_position[0]+300,polygon_position[1]),(polygon_position[0]+375,polygon_position[1]), (polygon_position[0]+375, polygon_position[1]- 35),(polygon_position[0]+382,polygon_position[1]-35),(polygon_position[0]+382,polygon_position[1]),(polygon_position[0]+465,polygon_position[1]), (polygon_position[0]+465, polygon_position[1]- 30),(polygon_position[0]+472,polygon_position[1]-30),(polygon_position[0]+472,polygon_position[1]),(polygon_position[0]+527,polygon_position[1]), (polygon_position[0]+527, polygon_position[1]- 15),(polygon_position[0]+532,polygon_position[1]-15),(polygon_position[0]+532,polygon_position[1]),(polygon_position[0]+568,polygon_position[1]), (polygon_position[0]+568, polygon_position[1]- 15),(polygon_position[0]+572,polygon_position[1]-15),(polygon_position[0]+572,polygon_position[1]),(polygon_position[0]+635,polygon_position[1]), (polygon_position[0]+635, polygon_position[1]- 28),(polygon_position[0]+643,polygon_position[1]-28),(polygon_position[0]+643,polygon_position[1]),(polygon_position[0]+726,polygon_position[1]), (polygon_position[0]+726, polygon_position[1]- 28),(polygon_position[0]+733,polygon_position[1]-28),(polygon_position[0]+733,polygon_position[1]),(polygon_position[0]+810,polygon_position[1]), (polygon_position[0]+810, polygon_position[1]- 28),(polygon_position[0]+820,polygon_position[1]-28),(polygon_position[0]+820,polygon_position[1]),(polygon_position[0]+897,polygon_position[1]), (polygon_position[0]+897, polygon_position[1]- 28),(polygon_position[0]+902,polygon_position[1]-28),(polygon_position[0]+902,polygon_position[1]),(polygon_position[0]+957,polygon_position[1]), (polygon_position[0]+957, polygon_position[1]- 15),(polygon_position[0]+962,polygon_position[1]-15),(polygon_position[0]+962,polygon_position[1]),(polygon_position[0]+1017,polygon_position[1]), (polygon_position[0]+1017, polygon_position[1]- 29),(polygon_position[0]+1023,polygon_position[1]-29),(polygon_position[0]+1023,polygon_position[1]),(polygon_position[0]+1095,polygon_position[1]), (polygon_position[0]+1095, polygon_position[1]- 35),(polygon_position[0]+1105,polygon_position[1]-35),(polygon_position[0]+1105,polygon_position[1]),(polygon_position[0]+1172,polygon_position[1]), (polygon_position[0]+1172, polygon_position[1]- 15),(polygon_position[0]+1177,polygon_position[1]-15),(polygon_position[0]+1177,polygon_position[1]), (polygon_position[0],polygon_position[1])])

	pygame.draw.polygon(screen, brown,[(polygon_position[0]+30+1200, polygon_position[1]),(polygon_position[0]+30+1200, polygon_position[1] -20 ), (polygon_position[0]+38+1200,polygon_position[1]-20),(polygon_position[0]+38+1200, polygon_position[1]), (polygon_position[0]+95+1200,polygon_position[1]), (polygon_position[0]+95+1200, polygon_position[1]- 25),(polygon_position[0]+105+1200,polygon_position[1]-25),(polygon_position[0]+105+1200,polygon_position[1]),(polygon_position[0]+163+1200,polygon_position[1]), (polygon_position[0]+163+1200, polygon_position[1]- 30),(polygon_position[0]+170+1200,polygon_position[1]-30),(polygon_position[0]+170+1200,polygon_position[1]),(polygon_position[0]+227+1200,polygon_position[1]), (polygon_position[0]+227+1200, polygon_position[1]- 25),(polygon_position[0]+232+1200,polygon_position[1]-25),(polygon_position[0]+232+1200,polygon_position[1]),(polygon_position[0]+290+1200,polygon_position[1]), (polygon_position[0]+290+1200, polygon_position[1]- 25),(polygon_position[0]+300+1200,polygon_position[1]-25),(polygon_position[0]+300+1200,polygon_position[1]),(polygon_position[0]+375+1200,polygon_position[1]), (polygon_position[0]+375+1200, polygon_position[1]- 35),(polygon_position[0]+382+1200,polygon_position[1]-35),(polygon_position[0]+382+1200,polygon_position[1]),(polygon_position[0]+465+1200,polygon_position[1]), (polygon_position[0]+465+1200, polygon_position[1]- 30),(polygon_position[0]+472+1200,polygon_position[1]-30),(polygon_position[0]+472+1200,polygon_position[1]),(polygon_position[0]+527+1200,polygon_position[1]), (polygon_position[0]+527+1200, polygon_position[1]- 15),(polygon_position[0]+532+1200,polygon_position[1]-15),(polygon_position[0]+532+1200,polygon_position[1]),(polygon_position[0]+568+1200,polygon_position[1]), (polygon_position[0]+568+1200, polygon_position[1]- 15),(polygon_position[0]+572+1200,polygon_position[1]-15),(polygon_position[0]+572+1200,polygon_position[1]),(polygon_position[0]+635+1200,polygon_position[1]), (polygon_position[0]+635+1200, polygon_position[1]- 28),(polygon_position[0]+643+1200,polygon_position[1]-28),(polygon_position[0]+643+1200,polygon_position[1]),(polygon_position[0]+726+1200,polygon_position[1]), (polygon_position[0]+726+1200, polygon_position[1]- 28),(polygon_position[0]+733+1200,polygon_position[1]-28),(polygon_position[0]+733+1200,polygon_position[1]),(polygon_position[0]+810+1200,polygon_position[1]), (polygon_position[0]+810+1200, polygon_position[1]- 28),(polygon_position[0]+820+1200,polygon_position[1]-28),(polygon_position[0]+820+1200,polygon_position[1]),(polygon_position[0]+897+1200,polygon_position[1]), (polygon_position[0]+897+1200, polygon_position[1]- 28),(polygon_position[0]+902+1200,polygon_position[1]-28),(polygon_position[0]+902+1200,polygon_position[1]),(polygon_position[0]+957+1200,polygon_position[1]), (polygon_position[0]+957+1200, polygon_position[1]- 15),(polygon_position[0]+962+1200,polygon_position[1]-15),(polygon_position[0]+962+1200,polygon_position[1]),(polygon_position[0]+1017+1200,polygon_position[1]), (polygon_position[0]+1017+1200, polygon_position[1]- 29),(polygon_position[0]+1023+1200,polygon_position[1]-29),(polygon_position[0]+1023+1200,polygon_position[1]),(polygon_position[0]+1095+1200,polygon_position[1]), (polygon_position[0]+1095+1200, polygon_position[1]- 35),(polygon_position[0]+1105+1200,polygon_position[1]-35),(polygon_position[0]+1105+1200,polygon_position[1]),(polygon_position[0]+1172+1200,polygon_position[1]), (polygon_position[0]+1172+1200, polygon_position[1]- 15),(polygon_position[0]+1177+1200,polygon_position[1]-15),(polygon_position[0]+1177+1200,polygon_position[1]), (polygon_position[0]+1200,polygon_position[1])])

	pygame.draw.polygon(screen, white, [(point_a[0], point_a[1]), (point_b[0], point_b[1]), (point_c[0], point_c[1]),(point_d[0], point_d[1]), (point_e[0], point_e[1]),(point_f[0], point_f[1]), (point_g[0], point_g[1]), (point_h[0], point_h[1]),(point_i[0], point_i[1]), (point_j[0], point_j[1]), (point_k[0], point_k[1]),(point_l[0], point_l[1]),(point_m[0], point_m[1]),(point_n[0], point_n[1])])
	pygame.draw.rect(screen,black,(eye[0],eye[1], 5,5))
	pygame.draw.rect(screen, brown,(colliding_rect[0], colliding_rect[1], player_size, player_size))

	#pygame.draw.polygon(screen, white, [(avatar_position[0]+100, avatar_position[1]), (avatar_position[0]+100, avatar_position[1]-30), (avatar_position[0]+140, avatar_position[1]-30),(avatar_position[0]+140, avatar_position[1]-26), (avatar_position[0]+150, avatar_position[1]-26),(avatar_position[0]+150, avatar_position[1]-16), (avatar_position[0]+140, avatar_position[1]-16), (avatar_position[0]+140, avatar_position[1]-12),(avatar_position[0]+130, avatar_position[1]-12), (avatar_position[0]+130, avatar_position[1]), (avatar_position[0]+120, avatar_position[1]),(avatar_position[0]+120, avatar_position[1]-12),(avatar_position[0]+110, avatar_position[1]-12),(avatar_position[0]+110, avatar_position[1])])
#	pygame.draw.rect(screen,black,(avatar_position[0]+135,avatar_position[1]-27, 5,5))

	if detect_collision(colliding_rect, enemy_pos):
		game_over = True

	drop_enemies(enemy_list)
	update_enemy_positions(enemy_list)
	if collision_check(enemy_list,colliding_rect):
		game_over = True
		break
	draw_enemies(enemy_list)

	#pygame.draw.rect(screen, white, (player_position[0], player_position[1], 50,50))

	#trunk(35, 10, -30)

	#pygame.draw.polygon(screen, dark_green)

	#pygame.draw.polygon(screen, white,[(polygon_position[0], polygon_position[1]), (polygon_position[0] , polygon_position[1] + 50), (polygon_position[0] + 50, polygon_position[1])], 1 )
	#pygame.draw.polygon(screen, white, ()])
	pygame.draw.rect(screen,white, (0, 260, 1200, 10))
	clock.tick(500)	
	pygame.display.update()
pygame.quit()