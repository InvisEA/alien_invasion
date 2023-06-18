#!/usr/bin/env python3

import pygame
from button import Button

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
		# cost per invader scale factor
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

		# if settings menu is active
		self.settings_active = False


	def initialize_dynamic_settings(self):
		"""Initializes settings changing during the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 3
		self.invader_speed = 1.0

		# fleet_direction = 1 if moving to the right; -1 - to the left
		self.fleet_direction = 1
		# Point counting
		self.per_invader_points = 50


	def initialize_easy_settings(self):
		pass


	def initialize_medium_settings(self):
		self.ship_speed = 1.5
		self.bullet_speed = 3
		self.invader_speed = 2.0


	def initialize_hard_settings(self):
		self.ship_speed = 2
		self.bullet_speed = 4
		self.invader_speed = 5.0


	def increase_speed(self):
		"""Increases speed settings and cost per invader."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.invader_speed *= self.speedup_scale

		self.per_invader_points = int(self.per_invader_points * self.score_scale)


