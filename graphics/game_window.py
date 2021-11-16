import pyglet

from core.event_bus import event_bus
from core.event_types import EventType, OnMouseMoveEvent, no_data_event_instance 
from graphics.data.graphics_data import GraphicsData

class GameWindow(pyglet.window.Window):
	
	draw_debug: bool = True
	graphics_data: GraphicsData

	def __init__(self, graphics_data: GraphicsData):
		super().__init__()
		
		self.graphics_data = graphics_data
		# create all the pyglet objects
		
		self.world_origin_x_s = (self.width // 2) 
		self.world_origin_y_s = (self.height // 2)

	def start(self):
		# we probably don't want this here 
		pyglet.app.run()

	def render(self):
		pass

	def on_draw(self):
		# pyglet's own clear function
		self.clear()

		#our render function	
		self.render()

		# inform people that care the frame was drawn
		event_bus.emit(EventType.ON_DRAW_FRAME, no_data_event_instance)

	def on_mouse_motion(self, x, y, dx, dy):
		mouse_move_event = OnMouseMoveEvent(x, y, dx, dy)
		event_bus.emit(EventType.ON_MOUSE_MOVE, mouse_move_event)