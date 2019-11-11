import main

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
