import pygame
import sys
import random
import time

width = 1200
height = 300


white = (255,255,255)
black = (0,0,0)
green = (0,255,0)

screen = pygame.display.set_mode((width, height))

polygon_position = [0, 260]


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
	pygame.draw.polygon(screen,green, [(polygon_position[0], polygon_position[1] ), (polygon_position[0] + 35, polygon_position[1] - 60), (polygon_position[0] +70, polygon_position[1]),(polygon_position[0] + 100, polygon_position[1] - 80 ), (polygon_position[0] + 135, polygon_position[1] ),(polygon_position[0]+ 170, polygon_position[1] - 110 ), (polygon_position[0]+200, polygon_position[1] ), (polygon_position[0] + 230, polygon_position[1] - 60), (polygon_position[0]+260, polygon_position[1]),(polygon_position[0]+295, polygon_position[1] - 90), (polygon_position[0] + 330, polygon_position[1] ),(polygon_position[0] + 380, polygon_position[1] - 130 ),(polygon_position[0]+430, polygon_position[1] ),(polygon_position[0]+470, polygon_position[1] -120),(polygon_position[0] + 510, polygon_position[1]),(polygon_position[0]+530, polygon_position[1]-40),(polygon_position[0]+550, polygon_position[1]), (polygon_position[0]+570, polygon_position[1]-50),(polygon_position[0]+590, polygon_position[1]), (polygon_position[0]+640, polygon_position[1]-100), (polygon_position[0]+690,polygon_position[1]),(polygon_position[0]+730,polygon_position[1]-80),(polygon_position[0]+770,polygon_position[1]), (polygon_position[0]+820,polygon_position[1]-130),(polygon_position[0]+870,polygon_position[1]),(polygon_position[0]+900,polygon_position[1]-100),(polygon_position[0]+930,polygon_position[1]),(polygon_position[0]+960,polygon_position[1]-60),(polygon_position[0]+990,polygon_position[1]),(polygon_position[0]+1020,polygon_position[1]-120),(polygon_position[0]+1050,polygon_position[1]),(polygon_position[0]+1100,polygon_position[1]-120),(polygon_position[0]+1150,polygon_position[1]),(polygon_position[0]+1175,polygon_position[1]-40),(polygon_position[0]+1200,polygon_position[1])],  0)
	
	pygame.draw.polygon(screen,green, [(polygon_position[0]+1200, polygon_position[1] ), (polygon_position[0] + 35+1200, polygon_position[1] - 60), (polygon_position[0] +70+1200, polygon_position[1]),(polygon_position[0] + 100+1200, polygon_position[1] - 80 ), (polygon_position[0] + 135+1200, polygon_position[1] ),(polygon_position[0]+ 170+1200, polygon_position[1] - 110 ), (polygon_position[0]+200+1200, polygon_position[1] ), (polygon_position[0] +1200+ 230, polygon_position[1] - 60), (polygon_position[0]+260+1200, polygon_position[1]),(polygon_position[0]+295+1200, polygon_position[1] - 90), (polygon_position[0]+1200 + 330, polygon_position[1] ),(polygon_position[0] + 380+1200, polygon_position[1] - 130 ),(polygon_position[0]+1200+430, polygon_position[1] ),(polygon_position[0]+1200+470, polygon_position[1] -120),(polygon_position[0] +1200+ 510, polygon_position[1]),(polygon_position[0]+1200+530, polygon_position[1]-40),(polygon_position[0]+550+1200, polygon_position[1]), (polygon_position[0]+570+1200, polygon_position[1]-50),(polygon_position[0]+590+1200, polygon_position[1]), (polygon_position[0]+1200+640, polygon_position[1]-100), (polygon_position[0]+1200+690,polygon_position[1]),(polygon_position[0]+1200+730,polygon_position[1]-80),(polygon_position[0]+770+1200,polygon_position[1]), (polygon_position[0]+1200+820,polygon_position[1]-130),(polygon_position[0]+870+1200,polygon_position[1]),(polygon_position[0]+900+1200,polygon_position[1]-100),(polygon_position[0]+930+1200,polygon_position[1]),(polygon_position[0]+1200+960,polygon_position[1]-60),(polygon_position[0]+1200+990,polygon_position[1]),(polygon_position[0]+1200+1020,polygon_position[1]-120),(polygon_position[0]+1200+1050,polygon_position[1]),(polygon_position[0]+1200+1100,polygon_position[1]-120),(polygon_position[0]+1150+1200,polygon_position[1]),(polygon_position[0]+1175+1200,polygon_position[1]-40),(polygon_position[0]+1200+1200,polygon_position[1])],  0)

	#pygame.draw.polygon(screen, white,[(polygon_position[0], polygon_position[1]), (polygon_position[0] , polygon_position[1] + 50), (polygon_position[0] + 50, polygon_position[1])], 1 )
	#pygame.draw.polygon(screen, white, [()])
	pygame.draw.rect(screen,white, (0, 260, 1200, 10))
	time.sleep(.01)	
	pygame.display.update()
pygame.quit()