from typing import Optional
from ui.ui_object import UIObject
import graphics.ui.ui_immediate_functions as ui_int
from graphics.ui.ui_immediate_functions import UIWindowFlags

class UITitle(UIObject):

	def __init__(self, text: str, font_size: float, size: float, position: tuple[int, int], font_key: Optional[str]) -> None:
		pass

	def draw(self) -> None:

		ui_int.begin("title",
			False,
			[
				UIWindowFlags.NO_MOVE,
				UIWindowFlags.NO_INPUTS,
				UIWindowFlags.NO_TITLE_BAR,
				UIWindowFlags.NO_SCROLL_WITH_MOUSE
			],
		)

		ui_int.set_window_font_scale(2.0)

		ui_int.text("LOADING...")

		ui_int.end()