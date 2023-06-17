import pygame

class SettingsButton:
	def __init__(self, hi_game):
		self.screen = hi_game.screen
		self.settings = hi_game.settings
		self.screen_rect = hi_game.screen.get_rect()

		self.image = pygame.image.load('images/settings_button.png').convert_alpha()

		# rescale the image of the button
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * 0.1, h * 0.1))
		self.rect = self.image.get_rect()
		self.rect.right = self.screen_rect.right - 10
		self.rect.top = self.screen_rect.top + 10


	def draw_button(self):
		self.screen.blit(self.image, self.rect)