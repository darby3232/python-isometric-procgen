from graphics.screens.screen import Screen
from graphics.ui_handler import UIHandler
from graphics.game_draw_data_container import GameDrawDataContainer
from graphics.ui.ui_test import UITestObject

class LoadingScreen(Screen):

	ui_handler: UIHandler
	draw_handler: GameDrawDataContainer

	def initialize(self, ui_handler: UIHandler, draw_handler: GameDrawDataContainer) -> None:
		super().initialize(ui_handler, draw_handler)

		self.ui_handler = ui_handler
		self.draw_handler = draw_handler

		# add things to the ui_handler
		self.ui_handler.add_ui_object("tester", UITestObject())


	def on_activate(self) -> None:
		# show things on ui handler
		self.ui_handler.show_ui_object("tester")

	def on_leave(self) -> None:
		# hide things on ui handler
		self.ui_handler.hide_ui_object("tester")