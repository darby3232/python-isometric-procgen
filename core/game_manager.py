from core.event_bus import event_bus
from core.event_types import EventType, no_data_event_instance
from graphics.game_window import GameWindow
from graphics.data.graphics_data import GraphicsData

class GameManager:
	
	window: GameWindow 
	graphics_data: GraphicsData

	def __init__(self) -> None:
		pass

	def start(self) -> None:
		# Startup sequence:
		
		# initial load: graphics data, ui_images, sound
		self.initial_load()

		# start the graphics and sound for loading screen
		self.__graphics_start()

		# do full load


		# start the game itself
		self.__game_start()

	def initial_load(self) -> None:
		print("Loading...")
		# create the graphics data
		self.graphics_data = GraphicsData()
		self.graphics_data.load()

		self.window = GameWindow(self.graphics_data)

	def full_load(self) -> None:
		# main images
		pass

	def __graphics_start(self) -> None:
		self.window.start()
		# show the load menu


	def __game_start(self) -> None:
		# show menu, etc
		pass