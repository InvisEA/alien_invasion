import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
	"""Class for showing game records."""

	def __init__(self, hi_game):
		"""Initializes attributes of scores counting."""
		self.hi_game = hi_game
		self.screen = hi_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = hi_game.settings
		self.stats = hi_game.stats

		# font settings for printing the score.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		# Preparation of current and highest scores, current level and
		# number of ships left.
		self.prepare_images()


	def prepare_images(self):
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()


	def prep_score(self):
		"""Transforms current score to graphical image."""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True,
			self.text_color, self.settings.bg_color)

		# Printing score in the right upper part of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20


	def prep_high_score(self):
		"""Transforms record  to graphical image."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
			self.text_color, self.settings.bg_color)

		# Record is aligned by center of the top side of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top


	def prep_level(self):
		"""Transforms level number to graphical image."""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True,
			self.text_color, self.settings.bg_color)

		# Places level under current score
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10


	def prep_ships(self):
		"""Tells the quantity of ships left."""
		self.ships = Group()
		#ship = Ship(self.hi_game)

		for ship_number in range(self.stats.ships_left + 1):
			ship = Ship(self.hi_game)
			rect = ship.rect
			new_rect = rect.scale_by(0.5)
			ship.image = pygame.transform.scale(ship.image, (new_rect.width, new_rect.height))
			ship.rect.x = 10 + ship_number * new_rect.width
			ship.rect.y = 10
			self.ships.add(ship)


	def show_score(self):
		"""Prints a score, a record, a level and amount lives left
		to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)


	def check_high_score(self):
		"""Checks if new record is made."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()

