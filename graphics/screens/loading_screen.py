from graphics.screens.screen import Screen
from graphics.ui.ui_title import UITitle
from graphics.ui_handler import UIHandler
from graphics.game_draw_data_container import GameDrawDataContainer
from graphics.ui.ui_test import UITestObject
from graphics.data.graphics_data import GraphicsData

class LoadingScreen(Screen):
	"""
	ui_handler: UIHandler
	draw_handler: GameDrawDataContainer
	graphics_data: GraphicsData
	"""

	def initialize(self, ui_handler: UIHandler, draw_handler: GameDrawDataContainer, graphics_data: GraphicsData) -> None:
		super().initialize(ui_handler, draw_handler, graphics_data)

		self.ui_handler = ui_handler
		self.draw_handler = draw_handler
		self.graphics_data = graphics_data

		# add things to the ui_handler

		# START HERE
		loading_title: UITitle("Loading", )

		self.ui_handler.add_ui_object("loading_screen", UITestObject())

	def on_activate(self) -> None:
		# show things on ui handler
		self.ui_handler.show_ui_object("loading_screen")

	def on_leave(self) -> None:
		# hide things on ui handler
		self.ui_handler.hide_ui_object("loading_screen")