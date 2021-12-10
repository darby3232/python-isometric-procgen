from ui.screens.screen import Screen
from graphics.ui_handler import UIHandler

class MainMenuScreen(Screen):


	def initialize(self, ui_handler: UIHandler, draw_handler: GameDrawDataContainer, graphics_data: GraphicsData) -> None:
		super().initialize(ui_handler, draw_handler, graphics_data)
