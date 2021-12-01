from __future__ import absolute_import
from typing import Union

from graphics.data.graphics_data import GraphicsData

import pyglet
from pyglet import gl

import imgui
from imgui.integrations.pyglet import create_renderer, PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer
from graphics.ui.ui_object import UIObject

import graphics.ui.ui_immediate_functions as ui_int

class UIHandler:

	impl: Union[PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer]

	ui_objects: dict[str, UIObject] = dict()
	objects_to_draw: list[str] = list()

	def __init__(self, window: pyglet.window.Window, graphics_data: GraphicsData):
		gl.glClearColor(1, 1, 1, 1)

		imgui.create_context()
		self.impl = ui_int.initialize_ui(window)

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