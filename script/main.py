import pygame, functions, game
from pygame.locals import *

pygame.init()

screenSize = screenWidth, screenHeight = 1000, 600
screen = pygame.display.set_mode(screenSize) #aqui a gente cria a tela
pygame.display.set_caption("") #aqui a gente pode colocar aqle nome de roda teto

black = 0,0,0
white = 255,255,255

class button:
	width = 50
	height = 50
	posx = 0
	posy = 0
	color = white

	def button(self,title,function):
		mouse = list(pygame.mouse.get_pos())

		functions.text('play', 45, self.posx, self.posy,screen)

		if pygame.mouse.get_pressed()[0] and self.posx<mouse[0] and mouse[0]<self.width+self.posx and self.posy<mouse[1] and mouse[1]<self.height+self.posy:
			function()

def main():
	screen.fill(black)
	play = button()
	options = button()

	while True:
		functions.exit()
		screen.fill(black)
		play.button('play', game.game)

		pygame.display.update()

main()
pygame.quit()
