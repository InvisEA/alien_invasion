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
		self.ship_speed = 1.5
		
		# bullet settings
		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 160, 60)
		self.bullets_allowed = 5
