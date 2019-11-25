import pygame,sys
from pygame import *

pygame.init()

def passleft():
    print('left')

def passright():
    print('right')

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
        if event.type == pygame.QUIT: sys.exit()

    key = pygame.key.get_pressed()
    if key[K_w] and key[K_LCTRL]:
        sys.exit()

### preciso fazer uma func click e a hold pra separar os eventos

def radio(screen,posx,posy):
    button('<',screen,passleft,posx,posy)
    button('>',screen,passright,posx+30,posy)
    text('blabla',screen,45,posx,posy)

def text(text,screen,size,px,py,font = pygame.font.get_default_font(),color = colors['white']):

    font = pygame.font.SysFont(font, size)
    text = font.render(text, 1, color) # essa funcao tem como parametros texto, suavidade, cor, background=None
<<<<<<< HEAD
    screen.blit(text,(px,py)) # pra printar na tela

    return text.get_width(),text.get_height() # pra ter as dimensoes pro botao
=======
    screen.blit(text,(px,py))
    return text
>>>>>>> e306bd9d652c81a44d520e0155a0a5d9d5242085

def button(title, screen, function, posx = 0, posy = 0, color = colors['white']):

<<<<<<< HEAD
    size = text(title,screen, 45, posx, posy) # recebe o tamanho do botao e printa o nome dele na tela
=======
    pygame.draw.rect(screen,colors['green'],(posx,posy,width,height))
    
    text(title,screen, 45, posx, posy)
>>>>>>> e306bd9d652c81a44d520e0155a0a5d9d5242085

    mouse = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0] and posx<mouse[0] and mouse[0]<size[0]+posx and posy<mouse[1] and mouse[1]<size[1]+posy:
        function() # verifica se o botao foi clicado, caso ss, ativa essa func

pygame.quit()
