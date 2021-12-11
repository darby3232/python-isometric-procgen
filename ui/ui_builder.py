from typing import Optional
import ui.ui_immediate_functions as ui_int
from ui.ui_immediate_functions import UIStyleVars, UIWindowFlags, UIConditionFlags


def draw_title(window_label: str, text: str, font_size: float, size: tuple[float, float], position: tuple[float, float], font_key: Optional[str]) -> None:
		
	ui_int.set_next_window_position(
		x=position[0], 
		y=position[1], 
		pivot_x=0, 
		pivot_y=0,
	)
	
	ui_int.set_next_window_size(
		width=size[0],
		height=size[1]
	)

	ui_int.set_next_window_bg_alpha(0)

	ui_int.push_style_var(UIStyleVars.WINDOW_BORDERSIZE, 0)

	ui_int.begin(window_label,
		False,
		[
			UIWindowFlags.NO_MOVE,
			UIWindowFlags.NO_INPUTS,
			UIWindowFlags.NO_TITLE_BAR,
			UIWindowFlags.NO_SCROLL_WITH_MOUSE,
			UIWindowFlags.NO_SCROLLBAR,
			UIWindowFlags.NO_RESIZE
		],
	)

	ui_int.set_window_font_scale(font_size)

	ui_int.text(text, font_key)

	ui_int.end()

	ui_int.pop_style_var(1)

def draw_single_button(window_label:str, text: str, font_size: float, size: tuple[float, float], position: tuple[float, float], font_key: Optional[str]) -> bool:

	ui_int.set_next_window_position(
		x=position[0], 
		y=position[1], 
		pivot_x=0, 
		pivot_y=0,
	)
	
	ui_int.set_next_window_size(
		width=size[0],
		height=size[1]
	)

	ui_int.set_next_window_bg_alpha(0)

	ui_int.push_style_var(UIStyleVars.WINDOW_BORDERSIZE, 0)

	ui_int.begin(window_label,
		False,
		[
			UIWindowFlags.NO_MOVE,
			# UIWindowFlags.NO_INPUTS,
			UIWindowFlags.NO_TITLE_BAR,
			UIWindowFlags.NO_SCROLL_WITH_MOUSE,
			UIWindowFlags.NO_SCROLLBAR,
			UIWindowFlags.NO_RESIZE
		],
	)


	ui_int.set_window_font_scale(font_size)

	button_pressed: bool = ui_int.button(text, size[0], size[1])

	ui_int.end()

	ui_int.pop_style_var(1)

	return button_pressed