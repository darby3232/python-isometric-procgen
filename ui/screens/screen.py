from graphics.data.graphics_data import GraphicsData


class Screen:

	graphics_data: GraphicsData

	def initialize(self, graphics_data: GraphicsData) -> None:
		self.graphics_data = graphics_data

	def draw(self) -> None:
		pass 

	# when drawn
	def on_activate(self) -> None:
		pass

	# on leaving the page
	def on_leave(self) -> None:
		pass