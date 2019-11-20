import pygame, functions, game

def options():
    screenSize = screenWidth, screenHeight = 1000, 600
    screen = pygame.display.set_mode(screenSize)

    while True:
        functions.exit()

		#background
        screen.fill(functions.colors['black'])

        functions.button('sair', screen, game.game, 50,50,60,30)

        pygame.display.update()
