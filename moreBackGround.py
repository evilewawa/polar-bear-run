import pygame
import sys
import random
import time

width = 1200
height = 300


white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
dark_green = (0,150,0)
brown = (150,75,0)
orange = (240, 75, 0)
light_orange = (255, 100, 0)
red = (255, 0,0)
screen = pygame.display.set_mode((width, height))

polygon_position = [0, 260]

trunk_position = [0,260]

fire_position = [0, 300]

fire_twitch = 0

bluk = 0

#def trunk(pos_x,size_one, size_two):
#	pygame.draw.rect(screen,brown, (polygon_position[0] + pos_x,260, size_one,size_two))
move_down = 0
clock = pygame.time.Clock()

game_over = False
while not game_over:
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()
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

	fire_x = fire_position[0]
#0
	fire_y = fire_position[1] 
#600
	randomInt = random.randint(25, 75)
	if move_down ==0:
		if fire_y > 0:
			fire_y -= 1
	if fire_y == 0:
		move_down = 1
	if move_down == 1:
		if fire_y < a:
			fire_y += 1
			if fire_y == a:
				move_down = 0
	if fire_twitch == 1000:
		bluk = random.randint(- 10,10)
		fire_twitch = 900
	else:
		fire_twitch += 1
	fire_position = [fire_x, fire_y]
##
	pygame.draw.polygon(screen, light_orange, [(fire_position[0]+80, 300+fire_position[1]),(fire_position[0]+90, 180+fire_position[1]),(fire_position[0]+123, 130+fire_position[1]),(fire_position[0]+140 + bluk, 30+fire_position[1]),(fire_position[0]+220, 130+fire_position[1]),(fire_position[0]+210, 60+fire_position[1]),(fire_position[0]+310, 110+fire_position[1]),(fire_position[0]+360, 20+fire_position[1]),(fire_position[0]+380, 70+fire_position[1]),(fire_position[0]+440, 135+fire_position[1]),(fire_position[0]+450, 60+fire_position[1]),(fire_position[0]+505, 27+fire_position[1]), (fire_position[0]+544, 90+fire_position[1]), (fire_position[0]+605, 15+fire_position[1]), (fire_position[0]+670, 0+fire_position[1]), (fire_position[0]+715, 15+fire_position[1]), (fire_position[0]+660, 30+fire_position[1]), (fire_position[0]+680, 60+fire_position[1]), (fire_position[0]+650, 150+fire_position[1]), (fire_position[0]+680, 140+fire_position[1]),(fire_position[0]+760, 100+fire_position[1]), (fire_position[0]+795, 40+fire_position[1]),  (fire_position[0]+860, 130+fire_position[1]), (fire_position[0]+920, 90+fire_position[1]), (fire_position[0]+965, 180+fire_position[1]), (fire_position[0]+1015, 125+fire_position[1]), (fire_position[0]+990, 30+fire_position[1]), (fire_position[0]+1060, 70+fire_position[1]), (fire_position[0]+1080, 120+fire_position[1]), (fire_position[0]+1120, 200+fire_position[1]), (fire_position[0]+1140, 230+fire_position[1]), (fire_position[0]+1140, 300+fire_position[1])])
	pygame.draw.polygon(screen, red, [(fire_position[0] +100, 300+fire_position[1]), (fire_position[0] +116, 165+fire_position[1]), (fire_position[0] +140, 145+fire_position[1]), (fire_position[0] +153,83+fire_position[1]), (fire_position[0] +230, 180+fire_position[1]), (fire_position[0] +250, 140+fire_position[1]), (fire_position[0] +250, 100+fire_position[1]), (fire_position[0] +280, 130+fire_position[1]), (fire_position[0] +320, 130+fire_position[1]),(fire_position[0] +365, 60+fire_position[1]), (fire_position[0] +370, 90+fire_position[1]), (fire_position[0] +400, 140+fire_position[1]), (fire_position[0] +430, 170+fire_position[1]), (fire_position[0] +490,160+fire_position[1]), (fire_position[0] +470, 121+fire_position[1]), (fire_position[0] +500, 50+fire_position[1]), (fire_position[0] +526, 111+fire_position[1]), (fire_position[0] +550, 115+fire_position[1]), (fire_position[0] +600, 40+fire_position[1]), (fire_position[0] +630, 60+fire_position[1]), (fire_position[0] +650, 60+fire_position[1]), (fire_position[0] +630, 90+fire_position[1]), (fire_position[0] +630, 150+fire_position[1]), (fire_position[0] +640, 180+fire_position[1]), (fire_position[0] +720, 150+fire_position[1]), (fire_position[0] +760, 130+fire_position[1]), (fire_position[0] +795, 80+fire_position[1]), (fire_position[0] +820, 110+fire_position[1]), (fire_position[0] +840, 150+fire_position[1]), (fire_position[0] +880, 145+fire_position[1]), (fire_position[0] +905, 120+fire_position[1]), (fire_position[0] +960, 195+fire_position[1]), (fire_position[0] +1010, 160+fire_position[1]), (fire_position[0] +1030, 120+fire_position[1]), (fire_position[0] +1020, 70+fire_position[1]), (fire_position[0] +1060, 120+fire_position[1]), (fire_position[0] +1070, 170+fire_position[1]), (fire_position[0] +1100, 200+fire_position[1]), (fire_position[0] +1120, 300+fire_position[1])])

#	pygame.draw.line(screen, orange, (220, 130), (150, 300), 1)



#	pygame.draw.line(screen, orange, (440, 135), (600, 300), 1)

	pygame.draw.polygon(screen, dark_green, [(40, 260), (70,210),(100,260), (130,190), (160,260),(200,180),(240,260),(260,190), (280,260), (320,180), (360,260),(390,190),(420,260), (450,180),(480,260),(530,200),(580,260), (590,200),(600,260),(600+40, 260), (600+70,210),(600+100,260), (600+130,190), (600+160,260),(600+200,180),(600+240,260),(600+260,190), (600+280,260), (600+320,180), (600+360,260),(600+390,190),(600+420,260), (600+450,180),(600+480,260),(600+530,200),(600+580,260), (600+590,200),(600+600,260)])

	pygame.draw.polygon(screen,green, [(polygon_position[0], polygon_position[1] ), (polygon_position[0] + 35, polygon_position[1] - 60), (polygon_position[0] +70, polygon_position[1]),(polygon_position[0] + 100, polygon_position[1] - 80 ), (polygon_position[0] + 135, polygon_position[1] ),(polygon_position[0]+ 170, polygon_position[1] - 110 ), (polygon_position[0]+200, polygon_position[1] ), (polygon_position[0] + 230, polygon_position[1] - 60), (polygon_position[0]+260, polygon_position[1]),(polygon_position[0]+295, polygon_position[1] - 90), (polygon_position[0] + 330, polygon_position[1] ),(polygon_position[0] + 380, polygon_position[1] - 130 ),(polygon_position[0]+430, polygon_position[1] ),(polygon_position[0]+470, polygon_position[1] -120),(polygon_position[0] + 510, polygon_position[1]),(polygon_position[0]+530, polygon_position[1]-40),(polygon_position[0]+550, polygon_position[1]), (polygon_position[0]+570, polygon_position[1]-50),(polygon_position[0]+590, polygon_position[1]), (polygon_position[0]+640, polygon_position[1]-100), (polygon_position[0]+690,polygon_position[1]),(polygon_position[0]+730,polygon_position[1]-80),(polygon_position[0]+770,polygon_position[1]), (polygon_position[0]+820,polygon_position[1]-130),(polygon_position[0]+870,polygon_position[1]),(polygon_position[0]+900,polygon_position[1]-100),(polygon_position[0]+930,polygon_position[1]),(polygon_position[0]+960,polygon_position[1]-60),(polygon_position[0]+990,polygon_position[1]),(polygon_position[0]+1020,polygon_position[1]-120),(polygon_position[0]+1050,polygon_position[1]),(polygon_position[0]+1100,polygon_position[1]-120),(polygon_position[0]+1150,polygon_position[1]),(polygon_position[0]+1175,polygon_position[1]-40),(polygon_position[0]+1200,polygon_position[1])],  0)
	
	pygame.draw.polygon(screen,green, [(polygon_position[0]+1200, polygon_position[1] ), (polygon_position[0] + 35+1200, polygon_position[1] - 60), (polygon_position[0] +70+1200, polygon_position[1]),(polygon_position[0] + 100+1200, polygon_position[1] - 80 ), (polygon_position[0] + 135+1200, polygon_position[1] ),(polygon_position[0]+ 170+1200, polygon_position[1] - 110 ), (polygon_position[0]+200+1200, polygon_position[1] ), (polygon_position[0] +1200+ 230, polygon_position[1] - 60), (polygon_position[0]+260+1200, polygon_position[1]),(polygon_position[0]+295+1200, polygon_position[1] - 90), (polygon_position[0]+1200 + 330, polygon_position[1] ),(polygon_position[0] + 380+1200, polygon_position[1] - 130 ),(polygon_position[0]+1200+430, polygon_position[1] ),(polygon_position[0]+1200+470, polygon_position[1] -120),(polygon_position[0] +1200+ 510, polygon_position[1]),(polygon_position[0]+1200+530, polygon_position[1]-40),(polygon_position[0]+550+1200, polygon_position[1]), (polygon_position[0]+570+1200, polygon_position[1]-50),(polygon_position[0]+590+1200, polygon_position[1]), (polygon_position[0]+1200+640, polygon_position[1]-100), (polygon_position[0]+1200+690,polygon_position[1]),(polygon_position[0]+1200+730,polygon_position[1]-80),(polygon_position[0]+770+1200,polygon_position[1]), (polygon_position[0]+1200+820,polygon_position[1]-130),(polygon_position[0]+870+1200,polygon_position[1]),(polygon_position[0]+900+1200,polygon_position[1]-100),(polygon_position[0]+930+1200,polygon_position[1]),(polygon_position[0]+1200+960,polygon_position[1]-60),(polygon_position[0]+1200+990,polygon_position[1]),(polygon_position[0]+1200+1020,polygon_position[1]-120),(polygon_position[0]+1200+1050,polygon_position[1]),(polygon_position[0]+1200+1100,polygon_position[1]-120),(polygon_position[0]+1150+1200,polygon_position[1]),(polygon_position[0]+1175+1200,polygon_position[1]-40),(polygon_position[0]+1200+1200,polygon_position[1])],  0)

	pygame.draw.polygon(screen, brown,[(polygon_position[0]+30, polygon_position[1]),(polygon_position[0]+30, polygon_position[1] -20 ), (polygon_position[0]+38,polygon_position[1]-20),(polygon_position[0]+38, polygon_position[1]), (polygon_position[0]+95,polygon_position[1]), (polygon_position[0]+95, polygon_position[1]- 25),(polygon_position[0]+105,polygon_position[1]-25),(polygon_position[0]+105,polygon_position[1]),(polygon_position[0]+163,polygon_position[1]), (polygon_position[0]+163, polygon_position[1]- 30),(polygon_position[0]+170,polygon_position[1]-30),(polygon_position[0]+170,polygon_position[1]),(polygon_position[0]+227,polygon_position[1]), (polygon_position[0]+227, polygon_position[1]- 25),(polygon_position[0]+232,polygon_position[1]-25),(polygon_position[0]+232,polygon_position[1]),(polygon_position[0]+290,polygon_position[1]), (polygon_position[0]+290, polygon_position[1]- 25),(polygon_position[0]+300,polygon_position[1]-25),(polygon_position[0]+300,polygon_position[1]),(polygon_position[0]+375,polygon_position[1]), (polygon_position[0]+375, polygon_position[1]- 35),(polygon_position[0]+382,polygon_position[1]-35),(polygon_position[0]+382,polygon_position[1]),(polygon_position[0]+465,polygon_position[1]), (polygon_position[0]+465, polygon_position[1]- 30),(polygon_position[0]+472,polygon_position[1]-30),(polygon_position[0]+472,polygon_position[1]),(polygon_position[0]+527,polygon_position[1]), (polygon_position[0]+527, polygon_position[1]- 15),(polygon_position[0]+532,polygon_position[1]-15),(polygon_position[0]+532,polygon_position[1]),(polygon_position[0]+568,polygon_position[1]), (polygon_position[0]+568, polygon_position[1]- 15),(polygon_position[0]+572,polygon_position[1]-15),(polygon_position[0]+572,polygon_position[1]),(polygon_position[0]+635,polygon_position[1]), (polygon_position[0]+635, polygon_position[1]- 28),(polygon_position[0]+643,polygon_position[1]-28),(polygon_position[0]+643,polygon_position[1]),(polygon_position[0]+726,polygon_position[1]), (polygon_position[0]+726, polygon_position[1]- 28),(polygon_position[0]+733,polygon_position[1]-28),(polygon_position[0]+733,polygon_position[1]),(polygon_position[0]+810,polygon_position[1]), (polygon_position[0]+810, polygon_position[1]- 28),(polygon_position[0]+820,polygon_position[1]-28),(polygon_position[0]+820,polygon_position[1]),(polygon_position[0]+897,polygon_position[1]), (polygon_position[0]+897, polygon_position[1]- 28),(polygon_position[0]+902,polygon_position[1]-28),(polygon_position[0]+902,polygon_position[1]),(polygon_position[0]+957,polygon_position[1]), (polygon_position[0]+957, polygon_position[1]- 15),(polygon_position[0]+962,polygon_position[1]-15),(polygon_position[0]+962,polygon_position[1]),(polygon_position[0]+1017,polygon_position[1]), (polygon_position[0]+1017, polygon_position[1]- 29),(polygon_position[0]+1023,polygon_position[1]-29),(polygon_position[0]+1023,polygon_position[1]),(polygon_position[0]+1095,polygon_position[1]), (polygon_position[0]+1095, polygon_position[1]- 35),(polygon_position[0]+1105,polygon_position[1]-35),(polygon_position[0]+1105,polygon_position[1]),(polygon_position[0]+1172,polygon_position[1]), (polygon_position[0]+1172, polygon_position[1]- 15),(polygon_position[0]+1177,polygon_position[1]-15),(polygon_position[0]+1177,polygon_position[1]), (polygon_position[0],polygon_position[1])])

	pygame.draw.polygon(screen, brown,[(polygon_position[0]+30+1200, polygon_position[1]),(polygon_position[0]+30+1200, polygon_position[1] -20 ), (polygon_position[0]+38+1200,polygon_position[1]-20),(polygon_position[0]+38+1200, polygon_position[1]), (polygon_position[0]+95+1200,polygon_position[1]), (polygon_position[0]+95+1200, polygon_position[1]- 25),(polygon_position[0]+105+1200,polygon_position[1]-25),(polygon_position[0]+105+1200,polygon_position[1]),(polygon_position[0]+163+1200,polygon_position[1]), (polygon_position[0]+163+1200, polygon_position[1]- 30),(polygon_position[0]+170+1200,polygon_position[1]-30),(polygon_position[0]+170+1200,polygon_position[1]),(polygon_position[0]+227+1200,polygon_position[1]), (polygon_position[0]+227+1200, polygon_position[1]- 25),(polygon_position[0]+232+1200,polygon_position[1]-25),(polygon_position[0]+232+1200,polygon_position[1]),(polygon_position[0]+290+1200,polygon_position[1]), (polygon_position[0]+290+1200, polygon_position[1]- 25),(polygon_position[0]+300+1200,polygon_position[1]-25),(polygon_position[0]+300+1200,polygon_position[1]),(polygon_position[0]+375+1200,polygon_position[1]), (polygon_position[0]+375+1200, polygon_position[1]- 35),(polygon_position[0]+382+1200,polygon_position[1]-35),(polygon_position[0]+382+1200,polygon_position[1]),(polygon_position[0]+465+1200,polygon_position[1]), (polygon_position[0]+465+1200, polygon_position[1]- 30),(polygon_position[0]+472+1200,polygon_position[1]-30),(polygon_position[0]+472+1200,polygon_position[1]),(polygon_position[0]+527+1200,polygon_position[1]), (polygon_position[0]+527+1200, polygon_position[1]- 15),(polygon_position[0]+532+1200,polygon_position[1]-15),(polygon_position[0]+532+1200,polygon_position[1]),(polygon_position[0]+568+1200,polygon_position[1]), (polygon_position[0]+568+1200, polygon_position[1]- 15),(polygon_position[0]+572+1200,polygon_position[1]-15),(polygon_position[0]+572+1200,polygon_position[1]),(polygon_position[0]+635+1200,polygon_position[1]), (polygon_position[0]+635+1200, polygon_position[1]- 28),(polygon_position[0]+643+1200,polygon_position[1]-28),(polygon_position[0]+643+1200,polygon_position[1]),(polygon_position[0]+726+1200,polygon_position[1]), (polygon_position[0]+726+1200, polygon_position[1]- 28),(polygon_position[0]+733+1200,polygon_position[1]-28),(polygon_position[0]+733+1200,polygon_position[1]),(polygon_position[0]+810+1200,polygon_position[1]), (polygon_position[0]+810+1200, polygon_position[1]- 28),(polygon_position[0]+820+1200,polygon_position[1]-28),(polygon_position[0]+820+1200,polygon_position[1]),(polygon_position[0]+897+1200,polygon_position[1]), (polygon_position[0]+897+1200, polygon_position[1]- 28),(polygon_position[0]+902+1200,polygon_position[1]-28),(polygon_position[0]+902+1200,polygon_position[1]),(polygon_position[0]+957+1200,polygon_position[1]), (polygon_position[0]+957+1200, polygon_position[1]- 15),(polygon_position[0]+962+1200,polygon_position[1]-15),(polygon_position[0]+962+1200,polygon_position[1]),(polygon_position[0]+1017+1200,polygon_position[1]), (polygon_position[0]+1017+1200, polygon_position[1]- 29),(polygon_position[0]+1023+1200,polygon_position[1]-29),(polygon_position[0]+1023+1200,polygon_position[1]),(polygon_position[0]+1095+1200,polygon_position[1]), (polygon_position[0]+1095+1200, polygon_position[1]- 35),(polygon_position[0]+1105+1200,polygon_position[1]-35),(polygon_position[0]+1105+1200,polygon_position[1]),(polygon_position[0]+1172+1200,polygon_position[1]), (polygon_position[0]+1172+1200, polygon_position[1]- 15),(polygon_position[0]+1177+1200,polygon_position[1]-15),(polygon_position[0]+1177+1200,polygon_position[1]), (polygon_position[0]+1200,polygon_position[1])])

	pygame.draw.rect(screen, black, (0, 270, 1200, 30))

	#pygame.draw.rect(screen, white, (fire_position[0] + 600, fire_position[1], 10,10))


	#pygame.draw.rect(screen, white, (player_position[0], player_position[1], 50,50))
	#trunk(35, 10, -30)

	#pygame.draw.polygon(screen, dark_green)

	#pygame.draw.polygon(screen, white,[(polygon_position[0], polygon_position[1]), (polygon_position[0] , polygon_position[1] + 50), (polygon_position[0] + 50, polygon_position[1])], 1 )
	#pygame.draw.polygon(screen, white, ()])
	pygame.draw.rect(screen,white, (0, 260, 1200, 10))
	clock.tick(250)	
	pygame.display.update()
pygame.quit()