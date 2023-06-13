#!/usr/bin/env python3

import sys
from time import sleep
import argparse
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from invader import Invader
from background import Star
from random import random, uniform, randint

class HumanInvasion:
	"""Class for resources and game behaviour handling."""

	def __init__(self):
		"""Initializes the game and creates game resources."""
		pygame.init()
		self.settings = Settings()
		if args.test:
			self.settings.bullet_width = 500
			self.settings.bullet_speed = 5
			self.settings.ship_speed = 3
			self.settings.invader_speed = 20
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Human Invasion")

		# creates instance for storing game statistics.
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.stars = pygame.sprite.Group()
		self._create_stars_bg()
		self.bullets = pygame.sprite.Group()
		self.invaders = pygame.sprite.Group()

		self._create_fleet()

		# Creates Play button
		self.play_button = Button(self, "Play")


	def run_game(self):
		"""Launch main cycle of the game."""
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_invaders()
			self._update_screen()

	
	def _create_stars_bg(self):
		star = Star(self)
		star_width, star_height = star.rect.size
		num_stars_x = self.settings.screen_width // star_width
		num_stars_y = self.settings.screen_height // star_height

		for row_num in range(num_stars_y):
			for col_num in range(num_stars_x):
				star = Star(self)
				pertubation_x = randint(-15, 15)
				star.x = 0.5 * star_width + 2 * star_width * col_num + pertubation_x
				pertubation_y = randint(-15, 15)
				star.y = 0.5 * star_height + 2 * star_height * row_num + pertubation_y
				star.rect.x = star.x
				star.rect.y = star.y
				factor = uniform(0.1, 0.9)
				star.image = pygame.transform.scale(star.image, 
						(star.W * factor, star.H * factor))
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
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)


	def _check_play_button(self, mouse_pos):
		"""Launches a new game after pressing Play button."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self._start_game()

			# mouse pointer is hidden
			pygame.mouse.set_visible(False)


	def _start_game(self):
		# Resets the whole game to initial state
		self.stats.reset_stats()
		self.stats.game_active = True

		# Clears invaders and bullets
		self.invaders.empty()
		self.bullets.empty()

		# Creates new fleet and places the ship on the center of the screen
		self._create_fleet()
		self.ship.center_ship()


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
		elif event.key == pygame.K_RETURN:
			if not self.stats.game_active:
				self._start_game()
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

		self._check_bullet_invader_collisions()


	def _check_bullet_invader_collisions(self):
		"""checks hits of invaders."""
		# if hit is registered, delete the bullet and the invader.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.invaders, True, True)

		if not self.invaders:
			# delete existing bullets and create a new fleet.
			self.bullets.empty()
			self._create_fleet()


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


	def _check_fleet_edges(self):
		"""Reacts on reaching a border of the screen of any invader."""
		for invader in self.invaders.sprites():
			if invader.check_edges():
				self._change_fleet_direction()
				break


	def _change_fleet_direction(self):
		"""Drops the fleet and changes its direction."""
		for invader in self.invaders.sprites():
			invader.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1


	def _update_invaders(self):
		"""Updates positions of all invaders on the screen."""
		self._check_fleet_edges()
		self.invaders.update()
		# check alien-invaders collision
		if pygame.sprite.spritecollideany(self.ship, self.invaders):
			self._ship_hit()

		# checks if any of invaders reaches the bottom of the screen
		self._check_invaders_bottom()


	def _ship_hit(self):
		"""Handles collision between alien and invader."""
		# decrease amount of avaiable ships (lives)
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1

			# Deletes all bullets and invaders from the screen
			self.invaders.empty()
			self.bullets.empty()

			# creates new fleet and place the alien ship to the center
			self._create_fleet()
			self.ship.center_ship()

			# creates a little pause before a new round
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _check_invaders_bottom(self):
		"""Check if invaders reached bottom part of the screen."""
		for invader in self.invaders:
			if invader.rect.bottom >= self.settings.screen_height:
				self._ship_hit()
				break


	def _update_screen(self):
		# filling the color to background in every iteration
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)
		# drawing the alien starship
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.invaders.draw(self.screen)

		# Play button is shown only if game is inactive
		if not self.stats.game_active:
			self.play_button.draw_button()

		# Displaying last drawn screen.
		pygame.display.flip()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--test", help="if specified game is launched in\
						the test mode",
						action="store_true")
	args = parser.parse_args()
	# create instance and launch the game
	hi = HumanInvasion()
	hi.run_game()
