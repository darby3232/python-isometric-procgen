from ui.screens.screen import Screen
from ui.ui_immediate_functions import button
import ui.ui_builder as ui_builder
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


	def draw(self) -> None:
		
		# use graphics data to find the middle and such
		percent_size_x = 40 / 100
		percent_size_y = 20 / 100
		title_pixel_size = self.graphics_data.window_x_size * percent_size_x, self.graphics_data.window_y_size * percent_size_y

		percent_position_x = (1 - percent_size_x) / 2
		percent_position_y = (1 - percent_size_y) / 2
		title_pixel_position = self.graphics_data.window_x_size * percent_position_x, self.graphics_data.window_y_size * percent_position_y

		button_pixel_size = title_pixel_size[0] / 2, title_pixel_size[1] / 2
		first_button_pixel_position = title_pixel_position[0], title_pixel_position[1] + title_pixel_size[1] + 10
		second_button_pixel_position = first_button_pixel_position[0], first_button_pixel_position[1] + button_pixel_size

		ui_builder.draw_title(
			window_label="Title",
			text="Loading", 
			font_size=1.0, 
			size=title_pixel_size,
			position=title_pixel_position,
			font_key="base_font"
		)

		if ui_builder.draw_single_button(
			window_label="start_button",
			text="Start",
			font_size=2.0,
			size=button_pixel_size,
			position=first_button_pixel_position,
			font_key="base_font"
		):
			print("start pressed")

		if ui_builder.draw_single_button(
			window_label="exit_button",
			text="label",
			font_size=2.0,
			size=button_pixel_size,
			position=(window_pixel_position[0], window_pixel_position[1] + button_pixel_size[1] + 10),
			font_key="base_font"
		):
			exit()

	def on_activate(self) -> None:
		# show things on ui handler
		pass

	def on_leave(self) -> None:
		# hide things on ui handler
		pass