#!/usr/bin/env python3

import pygame

class Ship():
	"""Class for controlling the ship."""
	def __init__(self, hi_game):
		self.screen = hi_game.screen
		self.screen_rect = hi_game.screen.get_rect()

		# Loads image of the ship and gets rectangle.
		self.image = pygame.image.load('images/spaceship.png').convert_alpha()
		
		# rescale the image of the ship
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * 0.15, h * 0.15))
		self.rect = self.image.get_rect()

		# New spaceship appears on the bottom border of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		# flag that tracks moving
		self.moving_right = False
		self.moving_left = False


	def blitme(self):
		"""Paints ship in the current position."""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Updates the position of the ship with respect to certain flag."""
		if self.moving_right:
			self.rect.x += 1
		if self.moving_left:
			self.rect.x -= 1
