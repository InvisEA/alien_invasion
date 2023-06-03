import pygame
from pygame.sprite import Sprite

class Invader(Sprite):
	"""Class that represents one human ship (invader)."""

	def __init__(self, hi_game):
		"""Initializes single invader and sets his initial position."""
		super().__init__()
		self.screen = hi_game.screen
		self.settings = hi_game.settings
		self.screen_rect = hi_game.screen.get_rect()

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

	def check_edges(self):
		"""Returns True, if invader reached a border of the screen."""
		if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""Moves invader ship to the right."""
		self.x += self.settings.invader_speed * self.settings.fleet_direction
		self.rect.x = self.x

