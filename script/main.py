import sys, random, pygame
from pygame.locals import *

### falta a implementacao de botoes

screenSize = screenWidth, screenHeight = 1000, 600

backgroundcolor = 0,0,0
white = 255,255,255

def click():
	click = list(pygame.mouse.get_pos())

	if pygame.mouse.get_pressed()[0]:
		click.append(True)
	else:
		click.append(False)
	return click

class button:
	width = 0
	height = 0
	posx = 0
	posy = 0
	color = white
	title = ''
	def title(self):
		text = fonteDefault.render(self.title, 1, self.color)
		screen.blit(text,(self.posx,self.posy))

	def range(self,function):
		if self.posx<click()[0]<self.width+self.posx and self.posy<click()[1]<self.height+self.posy and click()[2] == True:
			function()
			

def telaInicial():
    screen.fill(backgroundcolor)
    play = fonteDefault.render('play', 1, white)
    options = fonteDefault.render('options', 30, white)
    credits = fonteDefault.render('credits', 1, white)
    screen.blit(play,(300,200))
    screen.blit(options,(300,250))
    screen.blit(credits,(300,300))

def credits():
	pygame.display.update()
	screen.fill(backgroundcolor)
    ### colocar algo definitivo
	msg = fonteDefault.render('Obrigado Galerinha por Jogar este meu joguinho muito bom, porque eu tenho que ter a autoestima alta', 1, white)
	screen.blit(msg,(300,300))

def options():
    ###fazer algo que realmente faca sentido
    print('ok')

def game():

	#tirar isso daq

	pygame.mixer.music.pause()

	player1 = {
    'nickname': 'player 1',
    'score': 0,
    'width': 25,
    'height': 100,
    'posx': 100,
    'posy': 250,
    'speed': 1
    }

	player2 = {
    'nickname': 'player 2',
    'score': 0,
    'width': 25,
    'height': 100,
    'posx': 875,
    'posy': 250,
    'speed': 1
	}

	ball = {
    'width': 25,
    'height': 25,
    'posx': 480,
    'posy': 288,
    'speedx': 1,
    'speedy': 1
	}

	while True:

		pygame.mouse.set_visible(False)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		key = pygame.key.get_pressed()

		# Movimentacao Player 1

		if key[K_w]:
			player1['posy'] -= player1['speed']

		if key[K_s]:
			player1['posy'] += player1['speed']

		if player1['posy'] <= 0:
			player1['posy'] = 0

		elif player1['posy'] + player1['height'] >= screenHeight:
			player1['posy'] = screenHeight - player1['height']

		# Movimentacao Player 2

		if key[K_UP]:
			player2['posy'] -= player2['speed']

		if key[K_DOWN]:
			player2['posy'] += player2['speed']

		if player2['posy'] <= 0:
			player2['posy'] = 0

		elif player2['posy'] + player2['height'] >= screenHeight:
			player2['posy'] = screenHeight - player2['height']

		ball['posx'] += ball['speedx']
		ball['posy'] += ball['speedy']

		### o jogo esta sem efeito de colissao. existem duas solucoes para as colissoes, troque o dicionario por um objeto e use o metodo coliderect() do pygame ou implemente o propio sistema de colissoes

		if ball['posy'] <= 0:
			ball['speedy'] = -ball['speedy']

		elif ball['posy']+ball['height'] >= 600:
			ball['speedy'] = -ball['speedy']

		if ball['posx'] <= 0:
			ball['posx'] = 488
			ball['posy'] = 288
			player2['score'] += 1

		elif ball['posx']+ball['width'] >= 1000:
			ball['posx'] = 488
			ball['posy'] = 288
			player1['score'] += 1


		#condicao de parada
		if player1['score'] == 10 or player2['score'] == 10:
			break

		#background
		screen.fill(backgroundcolor)

		#player 1
		pygame.draw.rect(screen,white,(player1['posx'],player1['posy'],player1['width'],player1['height']))

		#player 2
		pygame.draw.rect(screen,white,(player2['posx'],player2['posy'],player2['width'],player2['height']))

		#ball
		pygame.draw.rect(screen,white,(ball['posx'],ball['posy'],ball['width'],ball['height']))

		#score
		score = fonteDefault.render('%d x %d' %(player1['score'],player2['score']), 1, white)
		screen.blit(score,(450,100))

		pygame.display.update()

pygame.init()

# backtrack
pygame.mixer.music.load('backtrack.mp3')
pygame.mixer.music.play()

# aqui fica definida a font usada no jogo
fonteMain = pygame.font.get_default_font()
titulo = pygame.font.SysFont(fonteMain,60)
fonteDefault = pygame.font.SysFont(fonteMain, 45)

screen = pygame.display.set_mode(screenSize) #aqui a gente cria a tela

pygame.display.set_caption("") #aqui a gente pode colocar aqle nome de roda teto

while True:

	click()
    #condicoes de saida
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	key = pygame.key.get_pressed()
	if key[K_w] and key[K_LCTRL]:
		sys.exit()

	#entrando no jogo propiamente dito

	if key[K_g] or (click()[2] == True and click()[0]<365 and click()[0]>300 and click()[1]>200 and click()[1]<235):
		game()
		pygame.mouse.set_visible(True)

	elif key[K_c] or (click()[2] == True and click()[0]<365 and click()[0]>300 and click()[1]>400 and click()[1]<435):
		credits()

	telaInicial()

	pygame.display.update()

pygame.quit()
