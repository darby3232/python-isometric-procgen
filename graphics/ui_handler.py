from __future__ import absolute_import
from typing import Union

import pyglet
from pyglet import gl

import imgui
from imgui.integrations.pyglet import create_renderer, PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer


class UIHandler:

	impl: Union[PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer]

	def __init__(self, window: pyglet.window.Window):
		gl.glClearColor(1, 1, 1, 1)

		imgui.create_context()
		self.impl = create_renderer(window)

	def draw(self) -> None:

		imgui.new_frame()

		if imgui.begin_main_menu_bar():
			if imgui.begin_menu("File", True):

				clicked_quit, selected_quit = imgui.menu_item(
					"Quit", 'Cmd+Q', False, True
				)

				if clicked_quit:
					exit(1)

				imgui.end_menu()
			imgui.end_main_menu_bar()

		imgui.render()
		self.impl.render(imgui.get_draw_data())