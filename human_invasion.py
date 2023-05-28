#!/usr/bin/env python3

import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from invader import Invader
from background import Star
from random import randint

class HumanInvasion:
	"""Class for resources and game behaviour handling."""
	def __init__(self):
		"""Initializes the game and creates game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Human Invasion")

		self.ship = Ship(self)
		self.stars = pygame.sprite.Group()
		self._create_stars_bg()
		self.bullets = pygame.sprite.Group()
		self.invaders = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		"""Launch main cycle of the game."""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()
	
	def _create_stars_bg(self):
		star = Star(self)
		star_width, star_height = star.rect.size
		num_stars_x = self.settings.screen_width // star_width
		num_stars_y = self.settings.screen_height // star_height

		for row_num in range(num_stars_y):
			for col_num in range(num_stars_x):
				star = Star(self)
				star.x = 0.5 * star_width + 2 * star_width * col_num
				star.y = 0.5 * star_height + 2 * star_height * row_num
				star.rect.x = star.x
				star.rect.y = star.y
				self.stars.add(star)


	def _check_events(self):
		"""Monitoring events of keyboard and mouse."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Reacts on pressing buttons."""
		if event.key == pygame.K_RIGHT:
			# Setting a flag for moving the ship to the right.
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# Setting a flag for moving the ship to the left.
			self.ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_ESCAPE:
			sys.exit()

	def _check_keyup_events(self, event):
		"""Reacts on releasing buttons."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Creates a new bullet and adds it to the bullets group."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Updates positions of bullets and delete old bullets."""
		# will cause every bullet in the sprite update its position
		self.bullets.update()

		# deleting bullets came out from the screen
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _create_fleet(self):
		"""Creates invaders fleet."""
		# creates single invader.
		invader = Invader(self)
		invader_width, invader_height = invader.rect.size
		# defines number of invaders accross columns
		available_space_x = self.settings.screen_width - 2 * invader_width
		number_invaders_x = available_space_x // (2 * invader_width)
		# defines number of invaders accross rows
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - 3 * invader_height 
			- ship_height)
		number_rows = available_space_y // (2 * invader_height)

		# creation of the first row of the human invaders
		for row_number in range(number_rows):
			for invader_number in range(number_invaders_x):
				self._create_invader(invader_number, row_number)

	def _create_invader(self, invader_number, row_number):
		"""Creation of one invader in the row."""
		invader = Invader(self)
		invader_width, invader_height = invader.rect.size
		invader.x = invader_width + 2 * invader_width * invader_number
		invader.rect.x = invader.x
		invader.y = invader_height + 2 * invader_height * row_number
		invader.rect.y = invader.y
		self.invaders.add(invader)

	def _update_screen(self):
		# filling the color to background in every iteration
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)
		# drawing the alien starship
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.invaders.draw(self.screen)
		# Displaying last drawn screen.
		pygame.display.flip()


if __name__ == '__main__':
	# create instance and launch the game
	hi = HumanInvasion()
	hi.run_game()
