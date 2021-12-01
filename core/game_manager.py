from __future__ import annotations

from core.event_bus import event_bus
from core.event_types import EventType, no_data_event_instance
from graphics.data.graphics_data import GraphicsData
from graphics.game_draw_data_container import GameDrawDataContainer
from graphics.game_window import GameWindow
from graphics.image_loader import ImageLoader
from graphics.ui_handler import UIHandler
from graphics.ui.ui_test import UITestObject
import graphics.graphics_helper_functions as graphics_helpers


class GameManager:
	
	# graphics
	window: GameWindow 
	graphics_data: GraphicsData
	image_loader: ImageLoader
	draw_data_container: GameDrawDataContainer	
	ui_handler: UIHandler

	def __init__(self) -> None:
		# on first frame, do this
		event_bus.add_listener(EventType.ON_DRAW_FRAME, self.full_load)

	def start(self) -> None:
		# Startup sequence:
		
		# initial load: graphics data, ui_images, imgui startup, sound
		self.initial_load()
		self.window = GameWindow(self.graphics_data)
		self.ui_handler = UIHandler(self.window, self.graphics_data)
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
		self.image_loader = ImageLoader(self.graphics_data, self)
		self.image_loader.set_resource_paths(self.graphics_data.asset_base_paths)
		self.image_loader.load_ui_images()

	def full_load(game_manager: GameManager) -> None:
		# remove this, since we only do this on the first frame
		event_bus.remove_listener(EventType.ON_DRAW_FRAME, game_manager.full_load)
		
		# main images
		game_manager.draw_data_container.load_game_images()

		# load other things

		# show the main menu
		game_manager.__game_start()	


	def __graphics_start(self) -> None:
		# place the ui  
		test_object: UITestObject = UITestObject()
		self.ui_handler.add_ui_object("tester", test_object)
		
		# once i do this, everything is an event
		graphics_helpers.start_pyglet()

	def __game_start(self) -> None:
		# show menu, etc
		print("game starting!")