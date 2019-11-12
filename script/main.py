import sys, pygame
from pygame.locals import *

screenSize = screenWidth, screenHeight = 1000, 600

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
		text = fonteDefault.render(title, 1, self.color)
		screen.blit(text,(self.posx,self.posy))

		if self.posx<mouse[0] and mouse[0]<self.width+self.posx and self.posy<mouse[1] and mouse[1]<self.height+self.posy and mouse[2] == True:
			function()

def main():
	screen.fill(black)
	play = button()
	options = button()

	while True:
		screen.fill(black)

    	#condicoes de saida
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		key = pygame.key.get_pressed()
		if key[K_w] and key[K_LCTRL]:
			sys.exit()

		pygame.display.update()


pygame.init()

# backtrack
#pygame.mixer.music.load('backtrack.mp3')
#pygame.mixer.music.play()

# aqui fica definida a font usada no jogo
fonteMain = pygame.font.get_default_font()
titulo = pygame.font.SysFont(fonteMain,60)
fonteDefault = pygame.font.SysFont(fonteMain, 45)

screen = pygame.display.set_mode(screenSize) #aqui a gente cria a tela

pygame.display.set_caption("") #aqui a gente pode colocar aqle nome de roda teto

pygame.quit()
