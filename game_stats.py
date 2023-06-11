class GameStats():
	"""Tracks some statistics about the game."""

	def __init__(self, hi_game):
		"""Initializes statistics."""
		self.settings = hi_game.settings
		self.reset_stats()

	def reset_stats(self):
		"""Initializes statistic changing during the game."""
		self.ships_left = self.settings.ship_limit

