import pygame
from random import uniform as decimalValueGenerator # 0 < x < 1
from random import choice
from functions import text,colors
from math import sqrt
from pygame.locals import *

pygame.init()

class rect():

	color = colors['white']
	width = 25
	height = 100
	posx = 100
	posy = 250
	speedy = 4

	def collide(self,object):
		rect1 = Rect(self.posx, self.posy, self.width, self.height)
		rect2 = Rect(object.posx, object.posy, object.width, object.height)

		if rect1.colliderect(rect2):
			object.speedx = -object.speedx

	def draw(self,screen):
		pygame.draw.rect(screen, self.color,(self.posx,self.posy,self.width,self.height))

class ball(rect):

	speedx = 1

	def limit(self,screenSize):
		if self.posy <= 0 or self.posy + self.height >= screenSize[1]:
			self.speedy = -self.speedy

	def speed(self):

		def speedXGenerator():

			self.speedx = decimalValueGenerator(-0.8,0.8)
			if self.speedx <= 0.25 and self.speedx >= -0.25:
				speedXGenerator()

		speedXGenerator()

		self.speedy = sqrt(1-self.speedx**2)*choice([1,-1])

	def move(self):

		self.speedx *= 1.001
		self.speedy *= 1.001

		self.posx += self.speedx
		self.posy += self.speedy

	def reset(self):
		self.posx = 488
		self.posy = 288
		self.speedx = 0
		self.speedy = 0
		self.speed()

class player(rect):

	score = 0

	def limit(self,screenSize):

		if self.posy <= 0:
			self.posy = 0

		elif self.posy + self.height >= screenSize[1]:
			self.posy = screenSize[1] - self.height

	def move(self,up,down,key):
		if key[up]:
			self.posy -= self.speedy

		if key[down]:
			self.posy += self.speedy
pygame.quit()
