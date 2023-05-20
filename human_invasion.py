#!/usr/bin/env python3

import sys

import pygame
from settings import Settings
from ship import Ship

class HumanInvasion:
	"""Class for resources and game behaviour handling."""
	def __init__(self):
		"""Initializes the game and creates game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Human Invasion")

		self.ship = Ship(self)

	def run_game(self):
		"""Launch main cycle of the game."""
		while True:
			# Monitoring events of keyboard and mouse.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# filling the color to background in every iteration
			self.screen.fill(self.settings.bg_color)
			# drawing the alien starship
			self.ship.blitme()

			# Displaying last drawn screen.
			pygame.display.flip()

if __name__ == '__main__':
	# create instance and launch the game
	ai = HumanInvasion()
	ai.run_game()
