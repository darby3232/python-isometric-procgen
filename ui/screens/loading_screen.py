from ui.screens.screen import Screen
from ui.ui_general_button import UIGeneralButton
from ui.ui_immediate_functions import button
from ui.ui_title import UITitle
from graphics.ui_handler import UIHandler
from graphics.game_draw_data_container import GameDrawDataContainer
from ui.ui_test import UITestObject
from graphics.data.graphics_data import GraphicsData

class LoadingScreen(Screen):
	"""
	ui_handler: UIHandler
	draw_handler: GameDrawDataContainer
	graphics_data: GraphicsData
	"""

	def initialize(self, ui_handler: UIHandler, draw_handler: GameDrawDataContainer, graphics_data: GraphicsData) -> None:
		super().initialize(ui_handler, draw_handler, graphics_data)

		"""
		self.ui_handler = ui_handler
		self.draw_handler = draw_handler
		self.graphics_data = graphics_data
		"""

		# add things to the ui_handler

		# with ui, just always assume we are pivoting in the top left corner?

		# use graphics data to find the middle and such
		percent_size_x = 40 / 100
		percent_size_y = 20 / 100
		window_pixel_size = graphics_data.window_x_size * percent_size_x, graphics_data.window_y_size * percent_size_y

		percent_position_x = (1 - percent_size_x) / 2
		percent_position_y = (1 - percent_size_y) / 2
		window_pixel_position = graphics_data.window_x_size * percent_position_x, graphics_data.window_y_size * percent_position_y

		loading_title = UITitle(
			text="Loading", 
			font_size=1.0, 
			size=window_pixel_size,
			position=window_pixel_position,
			font_key="base_font"
		)

		self.ui_handler.add_ui_object("loading_screen", loading_title)

		button_pixel_size = window_pixel_size[0] / 2, window_pixel_size[1] / 2

		general_button = UIGeneralButton(
			text="label",
			font_size=2.0,
			size=button_pixel_size,
			position=(0, 0),#(window_pixel_position[0], window_pixel_position[1]),
			on_click=self.on_click,
			font_key="base_font"
		)

		self.ui_handler.add_ui_object("test_button", general_button)

		general_button_2 = UIGeneralButton(
			text="label",
			font_size=2.0,
			size=button_pixel_size,
			position=(window_pixel_position[0], window_pixel_position[1] + button_pixel_size[1] + 10),
			on_click=self.on_click,
			font_key="base_font"
		)

		self.ui_handler.add_ui_object("test_button_two", general_button_2)

	def on_activate(self) -> None:
		# show things on ui handler
		self.ui_handler.show_ui_object("loading_screen")
		self.ui_handler.show_ui_object("test_button")
		self.ui_handler.show_ui_object("test_button_two")

	def on_leave(self) -> None:
		# hide things on ui handler
		self.ui_handler.hide_ui_object("loading_screen")
		self.ui_handler.hide_ui_object("test_button")

	def on_click(self) -> None:
		print("so this happened")
		print(self)