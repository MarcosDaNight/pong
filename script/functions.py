import pygame,sys
from pygame import *

pygame.init()

colors = {
    'black': (0,0,0),
    'white': (255,255,255),
    'red': (255,0,0),
    'green': (0,255,0),
    'blue': (0,0,255),
    'yellow': (255,255,0),
    'orange': (255,140,0),
    'pink': (255,20,147),
    'purple': (128,0,128)
}

def exit():
    #condicoes de saida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = pygame.key.get_pressed()
    if key[K_w] and key[K_LCTRL]:
        sys.exit()

### func click ta atrapalhando no desempenho da func exit


def text(text,screen,size,px,py,font = pygame.font.get_default_font(),color = colors['white']):

    font = pygame.font.SysFont(font, size)
    text = font.render(text, 1, color) # essa funcao tem como parametros texto, suavidade, cor, background=None
    screen.blit(text,(px,py)) # pra printar na tela
    return text.get_width(),text.get_height() # pra ter as dimensoes pro botao

pygame.quit()
