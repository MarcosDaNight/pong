import pygame, functions, random
from math import sqrt
from pygame.locals import *

pygame.init()

def game():
	class elements():

		color = functions.colors['white']
		width = 25
		height = 100
		posx = 100
		posy = 250
		speedy = 1

		def colide(self,object):

			if self.posx + self.width >= object.posx and self.posx < object.posx and object.posy >= self.posy and object.posy <= self.posy + self.height:
				object.speedx = -object.speedx

			#elif self.posx + self.width >= object.posx  object.posy >= self.posy

		def draw(self):
			pygame.draw.rect(screen, self.color,(self.posx,self.posy,self.width,self.height))

	class bal(elements):

		speedx = 0

		def limit(self):
			if self.posy <= 0 or self.posy + self.height >= screenHeight:
				self.speedy = -self.speedy

		def speed(self):

			self.speedx = random.uniform(-1,1)

			if self.speedx <= -0.8 or self.speedx == 0 or self.speedx >= 0.8:
				self.speedx = 0.8

			self.speedy = sqrt(1-self.speedx**2)*5

			self.speedx = self.speedx*5

	class player(elements):

		nickname = 'player'
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

	# definindo player1

	player1 = player()
	player1.nickname = 'Raisson'

	# definindo player2

	player2 = player()
	player2.nickname = 'Marcos'
	player2.posx = 875

	# definindo ball

	ball = bal()
	ball.height = 25
	ball.posx = 480
	ball.posy = 288
	ball.speed()

	# loop q mantem o jogo

	while True:
		functions.exit()

		# captura os clicks no teclado
		key = pygame.key.get_pressed()

		# Movimentacao Player 1
		player1.move(K_w,K_s,key)

		player1.limit()

		# Movimentacao Player 2
		player2.move(K_UP,K_DOWN,key)

		player2.limit()

		ball.posx += ball.speedx
		ball.posy += ball.speedy

		# colissao

		player1.colide(ball)
		player2.colide(ball)

		ball.limit()

		### tirar o choice e fazer um pitagoras no lugar
		### mudar o speed da bola
		### ajeitar as funcoes de colissao

		if ball.posx <= 0:
			ball.speed()
			ball.posx = 488
			ball.posy = 288
			#pygame.time.wait(10000) ###ajeitar isso pq ta travado ate pra fechar o jogo
			player2.score += 1

		elif ball.posx + ball.width >= screenWidth:
			ball.speed()
			ball.posx = 488
			ball.posy = 288
			#pygame.time.wait(10000)
			player1.score += 1

		#condicao de parada
		if player1.score == 5 or player2.score == 5:
			break

		# parte q faz as coisas aparecerem na tela

		screen.fill(functions.colors['black'])
		player1.draw()
		player2.draw()
		ball.draw()
		functions.text('%d x %d' %(player1.score,player2.score), screen, 45, 480, 60)

		pygame.display.update()

pygame.quit()
