from graphics.data.graphics_data import GraphicsData
from graphics.data.image_names import UIImageNames, GameImageNames
from graphics.graphics_helper_functions import set_pyglet_resource_paths

from pyglet.resource import image

class ImageLoader:

	ui_images: dict[UIImageNames, any] = dict()
	game_images: dict[GameImageNames, any] = dict()

	graphics_data: GraphicsData

	def __init__(self, graphics_data: GraphicsData):
		self.graphics_data = graphics_data

	def set_resource_paths(self, resource_paths: list[str]) -> None:
		# set the pyglet asset paths
		set_pyglet_resource_paths(resource_paths)

	def load_ui_images(self) -> None:
		# for key in image name list
		for ui_member, key_value in UIImageNames.list():
			file_name: str = self.graphics_data.image_filenames[key_value]
			self.ui_images[ui_member] = image(file_name)

	def load_game_images(self) -> None:
		# for key in image name list
		for game_member, key_value in GameImageNames.list():
			file_name: str = self.graphics_data.image_filenames[key_value]
			self.game_images[game_member] = image(file_name)
