from core.event_bus import event_bus
from core.event_types import EventType, no_data_event_instance
from graphics.game_window import GameWindow
from graphics.data.graphics_data import GraphicsData
from graphics.image_loader import image_loader, ImageLoader

class GameManager:
	
	window: GameWindow 
	graphics_data: GraphicsData

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

		# load ui images
		image_loader.set_resource_paths(self.graphics_data.asset_base_paths)
		image_loader.load_ui_images(self.graphics_data)

	def full_load(self) -> None:
		# main images
		image_loader.load_game_images(self.graphics_data)

	def __graphics_start(self) -> None:
		self.window.start()
		# show the load menu


	def __game_start(self) -> None:
		# show menu, etc
		pass