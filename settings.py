#!/usr/bin/env python3

class Settings():
	"""Class for saving all settings of Human Invasion game."""

	def __init__(self):
		"""Initializes game settings."""
		# Screen parameters
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		
		# ship speed adjusting
		self.ship_limit = 2
		
		# bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 160, 60)
		self.bullets_allowed = 5

		# invaders settings
		self.fleet_drop_speed = 10

		# factor of increasing tempo of the game
		self.speedup_scale = 1.2

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Initializes settings changing during the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 3
		self.invader_speed = 1.0

		# fleet_direction = 1 if moving to the right; -1 - to the left
		self.fleet_direction = 1

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.invader_speed *= self.speedup_scale
