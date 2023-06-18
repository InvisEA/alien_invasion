class GameStats():
	"""Tracks some statistics about the game."""

	def __init__(self, hi_game):
		"""Initializes statistics."""
		self.settings = hi_game.settings
		self.reset_stats()

		# flag if game is in active state
		self.game_active = False

		# record should not been reset
		self.high_score = 0


	def reset_stats(self):
		"""Initializes statistic changing during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

