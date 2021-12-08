
from graphics.data.graphics_data import GraphicsData
from graphics.game_draw_data_container import GameDrawDataContainer
from graphics.ui_handler import UIHandler


class Screen:

	ui_handler: UIHandler
	draw_handler: GameDrawDataContainer
	graphics_data: GraphicsData

	def initialize(self, ui_handler: UIHandler, draw_handler: GameDrawDataContainer, graphics_data: GraphicsData) -> None:
		self.ui_handler = ui_handler
		self.draw_handler = draw_handler
		self.graphics_data = graphics_data

	# when drawn
	def on_activate(self) -> None:
		pass

	# on leaving the page
	def on_leave(self) -> None:
		pass