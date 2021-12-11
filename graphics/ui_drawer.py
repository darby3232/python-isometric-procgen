from __future__ import absolute_import
from typing import Union
import pyglet
from pyglet import gl

from graphics.data.graphics_data import GraphicsData
from imgui.integrations.pyglet import PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer
from ui.screens.screen_state import ScreenStateMachine  
import ui.ui_immediate_functions as ui_int


class UIDrawer:

	graphics_data: GraphicsData
	screen_state_machine: ScreenStateMachine

	impl: Union[PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer]

	def __init__(self, window: pyglet.window.Window, screen_state_machine: ScreenStateMachine, graphics_data: GraphicsData):
		self.graphics_data = graphics_data
		self.screen_state_machine = screen_state_machine

		self.impl = ui_int.create_ui_renderer(window)

		# load fonts after creating renderer impl
		for key, value in self.graphics_data.font_paths.items():
			ui_int.font_manager.load_font(key, value, self.graphics_data.font_pixel_size)


	def draw(self) -> None:
		ui_int.new_frame()

		if self.screen_state_machine.current_screen:
			self.screen_state_machine.current_screen.draw()

		ui_int.render()
		self.impl.render(ui_int.get_draw_data())