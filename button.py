import pygame.font

class Button():

	def __init__(self, hi_game, msg):
		"""Initializes atributes of the button."""
		self.screen = hi_game.screen
		self.screen_rect = self.screen.get_rect()

		# Sets size and properties of buttons.
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Creates rect object of the button and aligns it to the 
		# center of the screen
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# Messages on the button is created
		self._prep_msg(msg)


	def _prep_msg(self, msg):
		"""Transforms msg to rectangle and aligns text to the center."""
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self):
		# shows empty button and print message on it
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

