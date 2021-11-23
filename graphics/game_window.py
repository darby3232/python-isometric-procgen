import pyglet

from core.event_bus import event_bus
from core.event_types import EventType, OnMouseMoveEvent, no_data_event_instance 
from graphics.data.graphics_data import GraphicsData
from graphics.ui_handler import UIHandler
from graphics.game_draw_data_container import GameDrawDataContainer


class GameWindow(pyglet.window.Window):
	
	draw_debug: bool = True
	graphics_data: GraphicsData

	ui_handler: UIHandler = None
	game_drawer: GameDrawDataContainer = None

	def __init__(self, graphics_data: GraphicsData):
		super().__init__()
		
		self.graphics_data = graphics_data
		# create all the pyglet objects
		
		self.world_origin_x_s = (self.width // 2) 
		self.world_origin_y_s = (self.height // 2)

	def start(self):
		# we probably don't want this here 
		pyglet.app.run()

	def register_ui_handler(self, ui_handler: UIHandler) -> None:
		self.ui_handler = ui_handler
	
	def register_game_drawer(self, game_drawer: GameDrawDataContainer) -> None:
		self.game_drawer = game_drawer 

	def render(self):
		if self.game_drawer is not None:
			self.game_drawer.draw()

		if self.ui_handler is not None:
			self.ui_handler.draw()

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