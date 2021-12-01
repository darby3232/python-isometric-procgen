from __future__ import absolute_import
from typing import Union
from enum import Enum, auto

import pyglet
from pyglet import gl

import imgui
from imgui.integrations.pyglet import create_renderer, PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer

class UIWindowFlags(Enum):
	NO_TITLE_BAR = imgui.WINDOW_NO_TITLE_BAR # auto()
	NO_RESIZE = imgui.WINDOW_NO_RESIZE # auto()
	NO_MOVE = imgui.WINDOW_NO_MOVE # auto()
	NO_SCROLLBAR = imgui.WINDOW_NO_SCROLLBAR # auto()
	NO_SCROLL_WITH_MOUSE = imgui.WINDOW_NO_SCROLL_WITH_MOUSE # auto()
	NO_COLLAPSE = imgui.WINDOW_NO_COLLAPSE # auto()
	ALWAYS_AUTO_RESIZE = imgui.WINDOW_ALWAYS_AUTO_RESIZE # auto() 
	NO_SAVED_SETTINGS = imgui.WINDOW_NO_SAVED_SETTINGS # auto()
	NO_INPUTS = imgui.WINDOW_NO_INPUTS # auto()
	MENU_BAR = imgui.WINDOW_MENU_BAR # auto()
	HORIZONTAL_SCROLLING_BAR = imgui.WINDOW_HORIZONTAL_SCROLLING_BAR # auto()
	NO_FOCUS_ON_APPEARING = imgui.WINDOW_NO_FOCUS_ON_APPEARING # auto()
	NO_BRING_TO_FRONT_ON_FOCUS = imgui.WINDOW_NO_BRING_TO_FRONT_ON_FOCUS # auto()
	ALWAYS_VERTICAL_SCROLLBAR = imgui.WINDOW_ALWAYS_VERTICAL_SCROLLBAR # auto()
	ALWAYS_HORIZONTAL_SCROLLBAR = imgui.WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR # auto()
	ALWAYS_USE_WINDOW_PADDING = imgui.WINDOW_ALWAYS_USE_WINDOW_PADDING # auto()


def initialize_ui(window: pyglet.window.Window) -> Union[PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer]:
	gl.glClearColor(1, 1, 1, 1)

	imgui.create_context()

	return create_renderer(window)

def new_frame() -> None:
	imgui.new_frame()


def render() -> None:
	imgui.render()

def get_draw_data() -> any:
	return imgui.get_draw_data()

"""
Returns true if main menu bar is opened
"""
def begin_main_menu_bar() -> bool:
	return imgui.begin_main_menu_bar()

def end_main_menu_bar() -> None:
	imgui.end_main_menu_bar()

"""
Returns true if menu is displayed
"""
def begin_menu(label: str, enabled: bool) -> bool:
	return imgui.begin_menu(label, enabled)

def end_menu() -> None:
	return imgui.end_menu()

# TODO check what state is here??
def menu_item(label: str, shortcut: str, selected: bool, enabled: bool) -> tuple[bool, any]:
	clicked, state = imgui.menu_item(label, shortcut, selected, enabled)
	print(state)
	return clicked, state

"""
Returns expanded, opened of bools. 
"""
def begin(label: str, closable: bool, flags: list[UIWindowFlags]) -> tuple[bool, bool]:
	# ui_flags = False 
	ui_flags = True 
	#for flag in flags:
	#	ui_flags = ui_flags | flag

	expanded, opened = imgui.begin(label, closable, ui_flags)

	return expanded, opened

"""
Ends window instruction
"""
def end() -> None:
	imgui.end()

"""
begin scrolling region. returns is_visible
"""
def begin_child(label: str, width: float, height: float, border: bool, flags: list[UIWindowFlags]) -> bool:
	ui_flags = False
	for flag in flags:
		ui_flags = ui_flags | flag

	is_visible = imgui.being_child(label, width, height, border, ui_flags)

	return is_visible

def end_child() -> None:
	imgui.end_child()

"""
add text to widget stack.
"""
def text(text: str) -> None:
	imgui.text(text)

"""
good for large text block??
"""
def text_unformatted(text: str) -> None:
	imgui.text_unformatted(text)

def text_colored(text: str, r: float, g: float, b: float, a: float) -> None:
	imgui.text_colored(text, r, g, b, a)
