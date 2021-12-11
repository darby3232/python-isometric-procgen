from ui.screens.screen import Screen
from ui.ui_immediate_functions import button
import ui.ui_builder as ui_builder
from graphics.data.graphics_data import GraphicsData

class LoadingScreen(Screen):
	"""
	ui_handler: UIHandler
	draw_handler: GameDrawDataContainer
	graphics_data: GraphicsData
	"""

	def initialize(self, graphics_data: GraphicsData) -> None:
		super().initialize(graphics_data)

	def draw(self) -> None:
		
		# use graphics data to find the middle and such
		percent_size_x = 40 / 100
		percent_size_y = 20 / 100
		title_pixel_size = self.graphics_data.window_x_size * percent_size_x, self.graphics_data.window_y_size * percent_size_y

		percent_position_x = (1 - percent_size_x) / 2
		percent_position_y = (1 - percent_size_y) / 2
		title_pixel_position = self.graphics_data.window_x_size * percent_position_x, self.graphics_data.window_y_size * percent_position_y


		ui_builder.draw_title(
			window_label="Title",
			text="Loading", 
			font_size=1.0, 
			size=title_pixel_size,
			position=title_pixel_position,
			font_key="base_font"
		)

		

	def on_activate(self) -> None:
		pass

	def on_leave(self) -> None:
		pass