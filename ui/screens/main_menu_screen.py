from ui.screens.screen import Screen
import ui.ui_builder as ui_builder
from graphics.data.graphics_data import GraphicsData

class MainMenuScreen(Screen):


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

		button_pixel_size = title_pixel_size[0] / 2, title_pixel_size[1] / 2
		first_button_pixel_position = title_pixel_position[0], title_pixel_position[1] + title_pixel_size[1] + 10
		second_button_pixel_position = first_button_pixel_position[0], first_button_pixel_position[1] + button_pixel_size[1]

		ui_builder.draw_title(
			window_label="Title",
			text="My Game", 
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
			text="Quit",
			font_size=2.0,
			size=button_pixel_size,
			position=second_button_pixel_position,
			font_key="base_font"
		):
			exit()