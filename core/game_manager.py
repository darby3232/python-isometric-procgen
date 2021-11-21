from core.event_bus import event_bus
from core.event_types import EventType, no_data_event_instance
from graphics.data.graphics_data import GraphicsData
from graphics.draw_data_container import DrawDataContainer
from graphics.game_window import GameWindow

class GameManager:
	
	window: GameWindow 
	graphics_data: GraphicsData
	draw_data_container: DrawDataContainer	

	def __init__(self) -> None:
		pass

	def start(self) -> None:
		# Startup sequence:
		
		# initial load: graphics data, ui_images, sound
		self.initial_load()
		self.window = GameWindow(self.graphics_data)

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

		self.draw_data_container = DrawDataContainer()

		# load ui images
		self.draw_data_container.set_resource_paths(self.graphics_data.asset_base_paths)
		self.draw_data_container.load_ui_images(self.graphics_data)

	def full_load(self) -> None:
		# main images
		self.draw_data_container.load_game_images(self.graphics_data)

	def __graphics_start(self) -> None:
		self.window.start()
		# show the load menu


	def __game_start(self) -> None:
		# show menu, etc
		pass