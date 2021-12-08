from __future__ import annotations
from typing import List

from core.event_bus import EventListener, ListenerContext, event_bus
from core.event_types import EventType, OnChangeScreenStateEvent, no_data_event_instance, OnDrawEvent
from ui.screens.screen_state import ScreenStateMachine
from ui.screens.screen_state_enum import ScreenState
from graphics.data.graphics_data import GraphicsData
from graphics.game_draw_data_container import GameDrawDataContainer
from graphics.game_window import GameWindow
from graphics.image_loader import ImageLoader
from graphics.ui_handler import UIHandler
from ui.ui_test import UITestObject
from ui.ui_immediate_functions import font_manager
import graphics.graphics_helper_functions as graphics_helpers


class GameManager(ListenerContext):
	
	# graphics
	window: GameWindow 
	graphics_data: GraphicsData
	image_loader: ImageLoader
	draw_data_container: GameDrawDataContainer	
	ui_handler: UIHandler
	screen_state_machine: ScreenStateMachine

	# loading
	first_frame_event_listener: EventListener

	def __init__(self) -> None:
		# on first frame, do this
		# self.first_frame_event_listener = EventListener(self.full_load, self)
		event_bus.add_listener(EventType.ON_DRAW_FRAME, self.full_load)

	def start(self) -> None:
		# Startup sequence:
		
		# IO initial load: graphics data, ui_images, imgui startup, sound
		self.initial_load()

		# object creation
		self.window = GameWindow(self.graphics_data)
		self.ui_handler = UIHandler(self.window, self.graphics_data)
		self.draw_data_container = GameDrawDataContainer(self.graphics_data)
		self.window.register_ui_handler(self.ui_handler)
		self.screen_state_machine = ScreenStateMachine(self.ui_handler, self.draw_data_container, self.graphics_data)

		# start the graphics and sound for loading screen
		self.__graphics_start()

	def initial_load(self) -> None:
		print("Loading...")
		# create the graphics data
		self.graphics_data = GraphicsData()
		self.graphics_data.load()

		# load ui images
		self.image_loader = ImageLoader(self.graphics_data)
		self.image_loader.set_resource_paths(self.graphics_data.asset_base_paths)
		self.image_loader.load_ui_images()


	def full_load(self, on_draw_frame: OnDrawEvent) -> None:

		print(self)

		# remove this, since we only do this on the first frame
		event_bus.remove_listener(EventType.ON_DRAW_FRAME, self.full_load)

		# show the loading screen
		change_screen_event: OnChangeScreenStateEvent = OnChangeScreenStateEvent(ScreenState.LOADING)
		event_bus.emit(EventType.ON_SCREEN_STATE_CHANGE, change_screen_event)

		# main images

		self.__game_start()


	def __graphics_start(self) -> None:
		# once i do this, everything is an event
		graphics_helpers.start_pyglet()

	def __game_start(self) -> None:
		# show menu, etc
		print("game starting!")
