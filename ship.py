#!/usr/bin/env python3

import pygame

class Ship():
	"""Class for controlling the ship."""
	def __init__(self, hi_game):
		self.screen = hi_game.screen
		self.screen_rect = hi_game.screen.get_rect()

		# Loads image of the ship and gets rectangle.
		self.image = pygame.image.load('images/spaceship.png').convert_alpha()
		self.rect = self.image.get_rect()
		# New spaceship appears on the bottom border of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""Paints ship in the current position."""
		self.screen.blit(self.image, self.rect)