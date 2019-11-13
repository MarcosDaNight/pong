import pygame, functions
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

		if pygame.mouse.get_pressed()[0]:
			mouse.append(True)
		else:
			mouse.append(False)

		functions.text('play', 45, self.posx, self.posy)

		if self.posx<mouse[0] and mouse[0]<self.width+self.posx and self.posy<mouse[1] and mouse[1]<self.height+self.posy and mouse[2] == True:
			function()

def printe():
	print('k')

def main():
	screen.fill(black)
	play = button()
	options = button()

	while True:
		functions.exit()
		screen.fill(black)
		play.button('play',printe())

		pygame.display.update()

main()
pygame.quit()
