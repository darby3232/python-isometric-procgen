from ui.ui_object import UIObject
import graphics.ui.ui_immediate_functions as ui_int
from graphics.ui.ui_immediate_functions import UIWindowFlags

class UITitle(UIObject):


	def draw(self) -> None:

		ui_int.begin("title",
			False,
			[
				UIWindowFlags.NO_MOVE,
				UIWindowFlags.NO_INPUTS,
			]
		)

		ui_int.text("LOADING...")

		ui_int.end()
