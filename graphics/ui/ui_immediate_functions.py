from __future__ import absolute_import
from typing import Optional, Union
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

class UIConditionFlags(Enum):
	ALWAYS = imgui.ALWAYS
	ONCE = imgui.ONCE
	FIRST_USE_EVER = imgui.FIRST_USE_EVER
	APPEARING = imgui.APPEARING

class UIStyleVars(Enum):
	ALPHA = imgui.STYLE_ALPHA
	BUTTON_TEXT_ALIGN = imgui.STYLE_BUTTON_TEXT_ALIGN
	CHILD_BORDERSIZE = imgui.STYLE_CHILD_BORDERSIZE
	CHILD_ROUNDING = imgui.STYLE_CHILD_ROUNDING
	FRAME_BORDERSIZE = imgui.STYLE_FRAME_BORDERSIZE
	FRAME_PADDING = imgui.STYLE_FRAME_PADDING
	FRAME_ROUNDING = imgui.STYLE_FRAME_ROUNDING
	GRAB_MIN_SIZE = imgui.STYLE_GRAB_MIN_SIZE
	GRAB_ROUNDING = imgui.STYLE_GRAB_ROUNDING
	INDENT_SPACING = imgui.STYLE_INDENT_SPACING
	ITEM_INNER_SPACING = imgui.STYLE_ITEM_INNER_SPACING
	POPUP_BORDERSIZE = imgui.STYLE_POPUP_BORDERSIZE
	POPUP_ROUNDING = imgui.STYLE_POPUP_ROUNDING
	SCROLLBAR_ROUNDING = imgui.STYLE_SCROLLBAR_ROUNDING
	SCROLLBAR_SIZE = imgui.STYLE_SCROLLBAR_SIZE
	WINDOW_BORDERSIZE = imgui.STYLE_WINDOW_BORDERSIZE
	WINDOW_MIN_SIZE = imgui.STYL

class FontManager:

	fonts: dict[str, any] = dict()
	io: any
	impl: Union[PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer]

	def __init__(self):
		self.io = imgui.get_io()

	def register_impl(self, impl: Union[PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer]) -> None:
		self.impl = impl

	def load_font(self, key: str, file_path: str, pixel_size: int) -> None:
		font = self.io.fonts.add_font_from_file_ttf(file_path, pixel_size)
		self.impl.refresh_font_texture()
		self.fonts[key] = font


gl.glClearColor(1, 1, 1, 1)
imgui.create_context()
font_manager: FontManager = FontManager()

def create_ui_renderer(window: pyglet.window.Window) -> Union[PygletFixedPipelineRenderer, PygletProgrammablePipelineRenderer]:
	impl = create_renderer(window)
	font_manager.register_impl(impl)	
	return impl

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
Set next window alpha.
"""
def set_next_window_bg_alpha(alpha: float) -> None:
	imgui.set_next_window_bg_alpha(alpha)

"""
Set next window position.
"""
def set_next_window_position(x: float, y: float, pivot_x: float, pivot_y: float, condition: UIConditionFlags = UIConditionFlags.ALWAYS) -> None:
	imgui.set_next_window_position(x, y, condition.value, pivot_x, pivot_y)


"""
Set next window size.
"""
def set_next_window_size(width: float, height: float, condition: UIConditionFlags = UIConditionFlags.ALWAYS) -> None:
	imgui.set_next_window_size(width, height, condition.value)

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
def text(text: str, font_key: str = "base_font") -> None:
	font = font_manager.fonts[font_key]
	with imgui.font(font):
		imgui.text(text)

"""
set window text scale	
"""
def set_window_font_scale(size: float) -> None:
	imgui.set_window_font_scale(size)

"""
good for large text block??
"""
def text_unformatted(text: str) -> None:
	imgui.text_unformatted(text)

def text_colored(text: str, r: float, g: float, b: float, a: float) -> None:
	imgui.text_colored(text, r, g, b, a)
