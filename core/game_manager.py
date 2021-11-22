from core.event_bus import event_bus
from core.event_types import EventType, no_data_event_instance
from graphics.data.graphics_data import GraphicsData
from graphics.game_draw_data_container import DrawDataContainer
from graphics.game_window import GameWindow
from graphics.image_loader import ImageLoader
from graphics.ui_handler import UIHandler

class GameManager:
	
	# graphics
	window: GameWindow 
	graphics_data: GraphicsData
	image_loader: ImageLoader
	draw_data_container: DrawDataContainer	
	ui_handler: UIHandler


	def __init__(self) -> None:
		pass

	def start(self) -> None:
		# Startup sequence:
		
		# initial load: graphics data, ui_images, imgui startup, sound
		self.initial_load()
		self.window = GameWindow(self.graphics_data)
		self.ui_handler = UIHandler(self.window)
		self.window.register_ui_handler(self.ui_handler)

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
		self.image_loader = ImageLoader(self.graphics_data)
		self.image_loader.set_resource_paths(self.graphics_data.asset_base_paths)
		self.image_loader.load_ui_images()


	def full_load(self) -> None:
		# main images
		self.draw_data_container.load_game_images()

	def __graphics_start(self) -> None:
		self.window.start()
		# show the load menu


	def __game_start(self) -> None:
		# show menu, etc
		pass