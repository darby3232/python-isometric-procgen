from typing import Optional
from graphics.ui.ui_object import UIObject
import graphics.ui.ui_immediate_functions as ui_int
from graphics.ui.ui_immediate_functions import UIWindowFlags, UIConditionFlags

class UITitle(UIObject):

	text: str
	font_size: float
	size: float
	position: tuple[int, int]
	font_key: Optional[str]

	def __init__(self, text: str, font_size: float, size: tuple[float, float], position: tuple[float, float], font_key: Optional[str]) -> None:

		self.text = text
		self.font_size = font_size
		self.size = size
		self.position = position
		self.font_key = font_key


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

		ui_int.begin("title",
			False,
			[
				UIWindowFlags.NO_MOVE,
				UIWindowFlags.NO_INPUTS,
				UIWindowFlags.NO_TITLE_BAR,
				UIWindowFlags.NO_SCROLL_WITH_MOUSE
			],
		)

		ui_int.set_window_font_scale(self.font_size)

		ui_int.text("LOADING...", self.font_key)

		ui_int.end()