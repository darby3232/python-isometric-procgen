from pyglet.resource import image
from graphics.data import graphics_data
from graphics.data.graphics_data import GraphicsData
from graphics.data.image_names import UIImageNames, GameImageNames
from graphics.graphics_helper_functions import set_pyglet_resource_paths

import pyglet

class GameDrawDataContainer:

	graphics_data: GraphicsData

	def __init__(self, graphics_data: GraphicsData):
		self.graphics_data = graphics_data

	def draw(self):
		pass
