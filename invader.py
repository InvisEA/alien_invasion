import pygame
from pygame.sprite import Sprite

class Invader(Sprite):
	"""Class that represents one human ship (invader)."""

	def __init__(self, hi_game):
		"""Initializes single invader and sets his initial position."""
		super().__init__()
		self.screen = hi_game.screen

		# loads the image of invader and sets his rect attribute."""
		self.image = pygame.image.load('images/humship.png')
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * 0.1, h * 0.1))
		# rotate the image so it look at the bottom of the screen
		self.image = pygame.transform.rotate(self.image, 180)
		self.rect = self.image.get_rect()

		# every new invader appears in the top left side of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# saves precise horizontal position of the invader
		self.x = float(self.rect.x)

