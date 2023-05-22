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
			self._check_events()
			self.ship.update()
			self._update_screen()
			
	def _check_events(self):
		# Monitoring events of keyboard and mouse.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					# Setting a flag for moving the ship to the right.
					self.ship.moving_right = True
				elif event.key == pygame.K_LEFT:
					# Setting a flag for moving the ship to the left.
					self.ship.moving_left = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = False		


	def _update_screen(self):
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
