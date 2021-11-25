from __future__ import absolute_import
from typing import Union

import pyglet
from pyglet import gl

import imgui
from imgui.integrations.pyglet import create_renderer, PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer

def initialize_ui(window: pyglet.window.Window) -> Union[PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer]:
	gl.glClearColor(1, 1, 1, 1)

	imgui.create_context()

	return create_renderer(window)

def ui_new_frame() -> None:
	imgui.new_frame()

"""
Returns true if main menu bar is opened
"""
def ui_begin_main_menu_bar() -> bool:
	return imgui.begin_main_menu_bar()

def ui_end_main_menu_bar() -> None:
	imgui.end_main_menu_bar()

"""
Returns true if menu is displayed
"""
def begin_menu(name: str, enabled: bool) -> bool:
	return imgui.begin_menu(name, enabled)

def end_menu() -> None:
	return imgui.end_menu()

# TODO check what state is here??
def menu_item(label: str, shortcut: str, selected: bool, enabled: bool) -> tuple[bool, any]:
	clicked, state = imgui.menu_item(label, shortcut, selected, enabled)
	print(state)
	return clicked, state
