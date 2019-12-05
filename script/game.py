import pygame, random
from functions import text,colors,exit
from math import sqrt
from pygame.locals import *

pygame.init()

def game():
	class elements():

		color = colors['white']
		width = 25
		height = 100
		posx = 100
		posy = 250
		speedy = 3

		def colide(self,object):

			if self.posx + self.width >= object.posx and self.posx < object.posx and object.posy >= self.posy and object.posy <= self.posy + self.height:
				object.speedx = -object.speedx

			#elif self.posx + self.width >= object.posx  object.posy >= self.posy

		def draw(self):
			pygame.draw.rect(screen, self.color,(self.posx,self.posy,self.width,self.height))

	class ball(elements):

		speedx = 0

		def limit(self):
			if self.posy <= 0 or self.posy + self.height >= screenHeight:
				self.speedy = -self.speedy

		def speed(self):

			#falta variar o negativo positivo pro y

			self.speedx = random.uniform(-0.8,0.8)

			if self.speedx <= 0.25 and self.speedx >= -0.25:
				self.speedx = random.choice([0.8,-0.8])

			self.speedy = sqrt(1-self.speedx**2)*3

			self.speedx = self.speedx*3

		def move(self):
			self.speedx += 1
			self.speedy += 1
			self.posx += self.speedx
			self.posy += self.speedy

	class player(elements):

		score = 0

		def limit(self):

			if self.posy <= 0:
				self.posy = 0

			elif self.posy + self.height >= screenHeight:
				self.posy = screenHeight - self.height

		def move(self,up,down,key):
			if key[up]:
				self.posy -= self.speedy

			if key[down]:
				self.posy += self.speedy

	clock = pygame.time.Clock()
	clock.tick(120)

	screenSize = screenWidth, screenHeight = 1000, 600
	screen = pygame.display.set_mode(screenSize)

	player1 = player()

	player2 = player()
	player2.posx = 875

	ball = ball()
	ball.height = 25
	ball.posx = 480
	ball.posy = 288
	ball.speed()

	while True:
		clock = pygame.time.Clock()
		clock.tick(120)
		exit()

		key = pygame.key.get_pressed()

		player1.move(K_w,K_s,key)
		player1.limit()

		player2.move(K_UP,K_DOWN,key)
		player2.limit()

		ball.limit()
		ball.move()

		player1.colide(ball)
		player2.colide(ball)

		### mudar o speed da bola
		### ajeitar as funcoes de colissao

		if ball.posx <= 0:
			ball.speed()
			ball.posx = 488
			ball.posy = 288
			#pygame.time.delay(1000) ###ajeitar isso pq ta travado ate pra fechar o jogo
			player2.score += 1

		elif ball.posx + ball.width >= screenWidth:
			ball.speed()
			ball.posx = 488
			ball.posy = 288
			#pygame.time.delay(1000)
			player1.score += 1

		if player1.score == 5 or player2.score == 5:
			break

		screen.fill(colors['black'])
		player1.draw()
		player2.draw()
		ball.draw()
		text('%d x %d' %(player1.score,player2.score), screen, 45, 480, 60)

		pygame.display.update()

pygame.quit()
