from __future__ import absolute_import
from typing import Union

from graphics.data.graphics_data import GraphicsData

import pyglet
from pyglet import gl

from imgui.integrations.pyglet import PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer
from ui.ui_object import UIObject

import ui.ui_immediate_functions as ui_int

class UIHandler:

	graphics_data: GraphicsData
	impl: Union[PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer]

	ui_objects: dict[str, UIObject] = dict()
	objects_to_draw: list[str] = list()

	def __init__(self, window: pyglet.window.Window, graphics_data: GraphicsData):
		self.graphics_data = graphics_data

		self.impl = ui_int.create_ui_renderer(window)

		# load fonts after creating renderer impl
		for key, value in self.graphics_data.font_paths.items():
			ui_int.font_manager.load_font(key, value, self.graphics_data.font_pixel_size)


	def add_ui_object(self, object_key: str, ui_object: UIObject) -> None:
		self.ui_objects[object_key] = ui_object 
	
	def remove_ui_object(self, object_key: str) -> None:
		del self.ui_objects[object_key]
		self.objects_to_draw.remove(object_key)		

	def show_ui_object(self, object_key: str) -> None:
		self.objects_to_draw.append(object_key)

	def hide_ui_object(self, object_key: str) -> None:
		self.objects_to_draw.remove(object_key)

	def draw(self) -> None:
		ui_int.new_frame()

		for key in self.objects_to_draw:
			self.ui_objects[key].draw()

		ui_int.render()
		self.impl.render(ui_int.get_draw_data())