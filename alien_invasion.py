#!/usr/bin/env python3

import sys

import pygame

class AlienInvasion:
	"""Class for resources and game behaviour handling."""
	def __init__(self):
		"""Initializes the game and creates game resources."""
		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")
		# Setting background color.
		self.bg_color = (230, 230, 230)

	def run_game(self):
		"""Launch main cycle of the game."""
		while True:
			# Monitoring events of keyboard and mouse.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# filling the color to background in every iteration
			self.screen.fill(self.bg_color)

			# Displaying last drawn screen.
			pygame.display.flip()

if __name__ == '__main__':
	# create instance and launch the game
	ai = AlienInvasion()
	ai.run_game()
