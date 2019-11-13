import pygame,sys
from pygame import *

pygame.init()

def exit():
    #condicoes de saida
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    key = pygame.key.get_pressed()
    if key[K_w] and key[K_LCTRL]:
        sys.exit()

def text(text,size,px,py,font = pygame.font.get_default_font(),color = (255,255,255)):

    font = pygame.font.SysFont(font,size)
    text = font.render(text, 100, color) # essa funcao tem como parametros texto, suavidade, cor, background=None
    screen.blit(text,(px,py))

pygame.quit()
