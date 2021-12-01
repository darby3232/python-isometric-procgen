
from graphics.game_draw_data_container import GameDrawDataContainer
from graphics.ui_handler import UIHandler


class Screen:

	ui_handler: UIHandler
	draw_handler: GameDrawDataContainer

	def initialize(self, ui_handler: UIHandler, draw_handler: GameDrawDataContainer) -> None:
		self.ui_handler = ui_handler
		self.draw_handler = draw_handler

	# when drawn
	def on_enter(self) -> None:
		pass

	# on leaving the page
	def on_leave(self) -> None:
		pass