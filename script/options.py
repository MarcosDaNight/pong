import functions, pygame

def options():
    screenSize = screenWidth, screenHeight = 1000, 600
    screen = pygame.display.set_mode(screenSize)

    while True:
        functions.exit()

		#background
        screen.fill(functions.colors['black'])

        functions.radio(screen,100,100)

        pygame.display.update()
