from graphics.data.graphics_data import GraphicsData
from graphics.data.image_names import UIImageNames, GameImageNames

class ImageLoader:

	graphics_data: GraphicsData

	ui_images: dict[UIImageNames, any] = dict()
	game_images: dict[GameImageNames, any] = dict()

	def init(self, graphics_data: GraphicsData) -> None:
		self.graphics_data = graphics_data

	def load_ui_images(self) -> None:
		pass

	def load_game_images(self) -> None:
		pass

image_loader = ImageLoader()