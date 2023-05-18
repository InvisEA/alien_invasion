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

	def run_game(self):
		"""Launch main cycle of the game."""
		while True:
			# Monitoring events of keyboard and mouse.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# Displaying last drawn screen.
			pygame.display.flip()

if __name__ == '__main__':
	# create instance and launch the game
	ai = AlienInvasion()
	ai.run_game()
