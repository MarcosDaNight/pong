import pygame, functions, game, options
from pygame.locals import *

pygame.init()

screenSize = screenWidth, screenHeight = 1000, 600
screen = pygame.display.set_mode(screenSize) #aqui a gente cria a tela
pygame.display.set_caption("") #aqui a gente pode colocar aqle nome de roda teto

def main():
	while True:
		functions.exit() #condicao de saida

		screen.fill(functions.colors['black'])
		functions.button('play', screen, game.game, 50,50,60,30)
		functions.button('options', screen, options.options,50,100,110,30)

		pygame.display.update()

main()
pygame.quit()

# bugs ou melhorias:
# - criar a aba options
# - resolver o problema de mexer na tela durante o jogo (congela)
# - fazer o jogo em si
# - descobrir como coloca logo no pygame
