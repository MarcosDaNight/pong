import pygame, functions, random
from pygame.locals import *

pygame.init()

def game():

	screenSize = screenWidth, screenHeight = 1000, 600
	screen = pygame.display.set_mode(screenSize)
	choice = [1.2,1.15,1.1,1.05,1,0.95,0.9,0.85,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,-1.2,-1.15,-1.1,-1.05,-1,-0.95,-0.9,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35]

	# esqueleto dos remos e da bola

	class player:

		clock = pygame.time.Clock()
		clock.tick(30)

		### tirar o choice e fazer um pitagoras no lugar
		### mudar o spped da bola
		### ajeitar as funcoes de colissao

		nickname = 'player'
		color = functions.colors['white']
		score = 0
		width = 25
		height = 100
		posx = 100
		posy = 250
		speedx = 0
		speedy = 1

		def wall(self):

			if self.posy <= 0:
				self.posy = 0

			elif self.posy + self.height >= screenHeight:
				self.posy = screenHeight - self.height

		def colide(self,object):

			if self.posx + self.width >= object.posx and self.posx < object.posx and object.posy >= self.posy and object.posy <= self.posy + self.height:
				object.speedx = -object.speedx

			#elif self.posx + self.width >= object.posx  object.posy >= self.posy

		def draw(self):
			pygame.draw.rect(screen, self.color,(self.posx,self.posy,self.width,self.height))

	# definindo player1

	player1 = player()
	player1.nickname = 'Raisson'

	# definindo player2

	player2 = player()
	player2.nickname = 'Marcos'
	player2.posx = 875

	# definindo ball

	ball = player()
	ball.height = 25
	ball.posx = 480
	ball.posy = 288
	ball.speedx = random.choice([-2,2])
	ball.speedy = random.choice(choice)

	# loop q mantem o jogo

	while True:
		functions.exit()

		# captura os clicks no teclado
		key = pygame.key.get_pressed()

		# Movimentacao Player 1
		if key[K_w]:
			player1.posy -= player1.speedy

		if key[K_s]:
			player1.posy += player1.speedy

		player1.wall()

		# Movimentacao Player 2
		if key[K_UP]:
			player2.posy -= player2.speedy

		if key[K_DOWN]:
			player2.posy += player2.speedy

		player2.wall()

		ball.posx += ball.speedx
		ball.posy += ball.speedy

		# colissao

		player1.colide(ball)
		player2.colide(ball)

		if ball.posy <= 0:
			ball.speedy = -ball.speedy

		elif ball.posy + ball.height >= screenHeight:
			ball.speedy = -ball.speedy

		if ball.posx <= 0:

			ball.speedx = random.choice([-1,1])
			ball.speedy = random.choice(choice)
			ball.posx = 488
			ball.posy = 288
			#pygame.time.wait(10000) ###ajeitar isso pq ta travado ate pra fechar o jogo
			player2.score += 1

		elif ball.posx + ball.width >= screenWidth:

			ball.speedx = random.choice([-1,1])
			ball.speedy = random.choice(choice)
			ball.posx = 488
			ball.posy = 288
			#pygame.time.wait(10000)
			player1.score += 1

		#condicao de parada
		if player1.score == 5 or player2.score == 5:
			break

		#background
		screen.fill(functions.colors['black'])

		#player 1
		player1.draw()

		#player 2
		player2.draw()

		#ball
		ball.draw()

		#score
		functions.text('%d x %d' %(player1.score,player2.score), screen, 45, 480, 60)

		pygame.display.update()

pygame.quit()
