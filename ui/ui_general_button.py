from typing import Optional, Callable
from ui.get_random_ui_id import get_random_id
from ui.ui_object import UIObject
import ui.ui_immediate_functions as ui_int
from ui.ui_immediate_functions import UIStyleVars, UIWindowFlags, UIConditionFlags

class UIGeneralButton(UIObject):

	text: str
	font_size: float
	size: float
	position: tuple[int, int]
	font_key: Optional[str]
	on_click: Callable
	window_label: str

	def __init__(self, text: str, font_size: float, size: tuple[float, float], position: tuple[float, float], on_click: Callable, font_key: Optional[str]) -> None:
		self.text = text
		self.font_size = font_size
		self.size = size
		self.position = position
		self.font_key = font_key
		self.on_click = on_click
		self.window_label = f"GenericButton###{get_random_id()}"

	def draw(self) -> None:

		ui_int.set_next_window_position(
			x=self.position[0], 
			y=self.position[1], 
			pivot_x=0, 
			pivot_y=0,
		)
		
		ui_int.set_next_window_size(
			width=self.size[0],
			height=self.size[1]
		)

		ui_int.set_next_window_bg_alpha(0)

		ui_int.push_style_var(UIStyleVars.WINDOW_BORDERSIZE, 0)

		ui_int.begin(self.window_label,
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


		ui_int.set_window_font_scale(self.font_size)

		if ui_int.button(self.text, self.size[0], self.size[1]):
			print("button clicked")
			self.on_click()

		ui_int.end()

		ui_int.pop_style_var(1)