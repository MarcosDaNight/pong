import pygame, functions
from pygame.locals import *
pygame.init()

def game():
	screenSize = screenWidth, screenHeight = 1000, 600

	fonteMain = pygame.font.get_default_font()
	titulo = pygame.font.SysFont(fonteMain,60)
	fonteDefault = pygame.font.SysFont(fonteMain, 45)

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
		speed = 1
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
	ball.speedx = 1
	ball.speedy = 1

	# loop q mantem o jogo

	while True:
		functions.exit()

		# captura os clicks no teclado
		key = pygame.key.get_pressed()

		# Movimentacao Player 1

		if key[K_w]:
			player1.posy -= player1.speed

		if key[K_s]:
			player1.posy += player1.speed

		if player1.posy <= 0:
			player1.posy = 0

		elif player1.posy + player1.height >= screenHeight:
			player1.posy = screenHeight - player1.height

		# Movimentacao Player 2

		if key[K_UP]:
			player2.posy -= player2.speed

		if key[K_DOWN]:
			player2.posy += player2.speed

		# limite de movimentacao pros players

		if player2.posy <= 0:
			player2.posy = 0

		elif player2.posy + player2.height >= screenHeight:
			player2.posy = screenHeight - player2.height

		ball.posx += ball.speedx
		ball.posy += ball.speedy

		### o jogo esta sem efeito de colissao. existem duas solucoes para as colissoes,
		### troque o dicionario por um objeto e use o metodo coliderect() do pygame ou implemente
		### o propio sistema de colissoes

		if ball.posy <= 0:
			ball.speedy = -ball.speedy

		elif ball.posy + ball.height >= 600:
			ball.speedy = -ball.speedy

		if ball.posx <= 0:
			ballposx = 488
			ballposy = 288
			player2.score += 1

		elif ball.posx + ball.width >= 1000:
			ball.posx = 488
			ball.posy = 288
			player1.score += 1

		#condicao de parada
		if player1.score == 3 or player2.score == 3:
			break

		#background
		screen.fill(functions.colors['black'])

		#player 1
		pygame.draw.rect(screen,player1.color,(player1.posx,player1.posy,player1.width,player1.height))

		#player 2
		pygame.draw.rect(screen,player2.color,(player2.posx,player2.posy,player2.width,player2.height))

		#ball
		pygame.draw.rect(screen,ball.color,(ball.posx,ball.posy,ball.width,ball.height))

		#score
		functions.text('%d x %d' %(player1.score,player2.score), screen, 45, 450, 100)

		pygame.display.update()
pygame.quit()
