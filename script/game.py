import pygame, random
from gameClasses import rect,player,ball
from functions import colors,exit,text
from math import sqrt
from pygame.locals import *

pygame.init()

def game():

	screenSize = screenWidth, screenHeight = 1000, 600
	screen = pygame.display.set_mode(screenSize)

	player1 = player()

	player2 = player()
	player2.posx = 875

	mainBall = ball()
	mainBall.height = 25
	mainBall.posx = 480
	mainBall.posy = 288

	mainBall.speed()

	while True:

		exit()

		clock = pygame.time.Clock()
		clock.tick(120)

		key = pygame.key.get_pressed()

		player1.move(K_w,K_s,key)
		player1.limit(screenSize)

		player2.move(K_UP,K_DOWN,key)
		player2.limit(screenSize)

		mainBall.limit(screenSize)
		mainBall.move()

		player1.collide(mainBall)
		player2.collide(mainBall)

		### ajeitar as funcoes de colissao

		if mainBall.posx <= 0:

			mainBall.reset()
			#pygame.time.delay(1000) ###ajeitar isso pq ta travado ate pra fechar o jogo
			player2.score += 1

		elif mainBall.posx + mainBall.width >= screenWidth:

			mainBall.reset()
			#pygame.time.delay(1000)
			player1.score += 1

		if player1.score == 5 or player2.score == 5:
			break

		screen.fill(colors['black'])
		player1.draw(screen)
		player2.draw(screen)
		mainBall.draw(screen)
		text('%d x %d' %(player1.score,player2.score), screen, 45, 480, 60)

		pygame.display.update()

pygame.quit()
