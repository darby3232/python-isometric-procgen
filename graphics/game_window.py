import pyglet

from core.event_bus import event_bus
from core.event_types import EventType, OnMouseMoveEvent, OnDrawEvent, no_data_event_instance
from graphics.data.graphics_data import GraphicsData
from graphics.ui_drawer import UIDrawer
from graphics.game_draw_data_container import GameDrawDataContainer

key = pyglet.window.key

class GameWindow(pyglet.window.Window):
	
	draw_debug: bool = True
	graphics_data: GraphicsData

	ui_drawer: UIDrawer = None
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

	def register_ui_drawer(self, ui_drawer: UIDrawer) -> None:
		self.ui_drawer = ui_drawer
	
	def register_game_drawer(self, game_drawer: GameDrawDataContainer) -> None:
		self.game_drawer = game_drawer 

	def render(self) -> None:
		self.clear()
		
		if self.game_drawer is not None:
			self.game_drawer.draw()

		if self.ui_drawer is not None:
			self.ui_drawer.draw()

		# inform people that care the frame was drawn
		event_bus.emit(EventType.ON_DRAW_FRAME, no_data_event_instance)

	def on_draw(self):
		self.render()

	def on_close(self):
		self.alive = False

	def on_key_press(self, symbol, modkey):
		self.keys_down[symbol] = time()

	def on_key_release(self, symbol, modkey):
		if symbol in self.keys_down:
			del(self.keys_down[symbol])

	def on_mouse_release(self, x, y, button, modifiers):
		pass

	def on_mouse_press(self, x, y, button, modifiers):
		print(button,'pressed',(x,y))
	
	def on_mouse_motion(self, x, y, dx, dy):
		mouse_move_event = OnMouseMoveEvent(x, y, dx, dy)
		event_bus.emit(EventType.ON_MOUSE_MOVE, mouse_move_event)

	def run(self):
		while self.alive:
			event = self.dispatch_events()

			for symbol in self.keys_down:
				if symbol == key.ESCAPE:
					self.alive = None
					break
				elif symbol == key.LEFT:
					pass #Arrowkey Left
				elif symbol == key.RIGHT:
					pass #Arrowkey Right
				elif symbol == key.UP:
					pass #Arrowkey Up
				elif symbol == key.DOWN:
					pass #Arrowkey Down
				elif symbol == 65515:
					pass # Win key
				else:
					print(symbol)
			self.render()


		# pyglet's own clear function

