import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Class for controlling the bullets shot by the ship."""

	def __init__(self, hi_game):
		"""Creates bullet object in the current position of the ship."""
		super().__init__()
		self.screen = hi_game.screen
		self.settings = hi_game.settings
		self.color = self.settings.bullet_color

		# Creates bullet in (0, 0) and then assigning right position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = hi_game.ship.rect.midtop

		# y position in float-point format
		self.y = float(self.rect.y)

	def update(self):
		"""Moves the bullet vertically to the top side of the screen."""
		# updating of bullet position in floating point
		self.y -= self.settings.bullet_speed
		# updating of the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		"""Drawing the bullet on the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)

