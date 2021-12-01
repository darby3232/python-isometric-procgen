from graphics.screens.screen import Screen
from graphics.ui_handler import UIHandler
from game_draw_data_container import GameDrawDataContainer

class LoadingScreen(Screen):

	def __init__(self) -> None:
		pass

	def initialize(self, ui_handler: UIHandler, draw_handler: GameDrawDataContainer) -> None:
		super().initialize(ui_handler, draw_handler)

		# add things to the ui_handler

	def on_activate(self) -> None:
		# show things on ui handler
		pass

	def on_leave(self) -> None:
		# hide things on ui handler
		pass