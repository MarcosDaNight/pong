import pygame, functions, random
from pygame.locals import *

pygame.init()

def game():

	screenSize = screenWidth, screenHeight = 1000, 600
	screen = pygame.display.set_mode(screenSize)

	# esqueleto dos remos e da bola

	class player:

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
	ball.speedy = random.choice([0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35])

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

		if ball.posy <= 0:
			ball.speedy = -ball.speedy

		elif ball.posy + ball.height >= screenHeight:
			ball.speedy = -ball.speedy

		if ball.posx <= 0:

			ball.speedx = random.choice([-1,1])
			ball.speedy = random.choice([0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35])
			ball.posx = 488
			ball.posy = 288
			#pygame.time.wait(10000) ###ajeitar isso pq ta travado ate pra fechar o jogo
			player2.score += 1

		elif ball.posx + ball.width >= screenWidth:

			ball.speedx = random.choice([-1,1])
			ball.speedy = random.choice([0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35])
			ball.posx = 488
			ball.posy = 288
			#pygame.time.wait(10000)
			player1.score += 1

		#condicao de parada
		if player1.score == 3 or player2.score == 3:
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
		functions.text('%s %d x %d %s' %(player1.nickname,player1.score,player2.score,player2.nickname), screen, 45, 350, 60)

		pygame.display.update()
pygame.quit()
