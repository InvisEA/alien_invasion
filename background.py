import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	def __init__(self, hi_game):
		super().__init__()
		self.screen = hi_game.screen

		self.image = pygame.image.load('images/star.png')
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * 0.07, h * 0.07))
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
