from __future__ import annotations
from typing import List
import time

from core.event_bus import EventListener, ListenerContext, event_bus
from core.event_types import EventType, OnChangeScreenStateEvent, no_data_event_instance, OnDrawEvent
from ui.screens.screen_state import ScreenStateMachine
from ui.screens.screen_state_enum import ScreenState
from graphics.data.graphics_data import GraphicsData
from graphics.game_draw_data_container import GameDrawDataContainer
from graphics.game_window import GameWindow
from graphics.image_loader import ImageLoader
from graphics.ui_drawer import UIDrawer
from ui.ui_immediate_functions import font_manager
import graphics.graphics_helper_functions as graphics_helpers


class GameManager(ListenerContext):
	
	# graphics
	window: GameWindow 
	graphics_data: GraphicsData
	image_loader: ImageLoader
	draw_data_container: GameDrawDataContainer	
	ui_drawer: UIDrawer
	screen_state_machine: ScreenStateMachine

	# loading
	first_frame_event_listener: EventListener

	def __init__(self) -> None:
		# on first frame, do this
		# self.first_frame_event_listener = EventListener(self.full_load, self)
		event_bus.add_listener(EventType.ON_DRAW_FRAME, self.full_load)

	def start(self) -> None:
		# IO initial load: graphics data, ui_images, imgui startup, sound
		# create the graphics data
		self.graphics_data = GraphicsData()
		self.graphics_data.load()

		# load ui images
		self.image_loader = ImageLoader(self.graphics_data)
		self.image_loader.set_resource_paths(self.graphics_data.asset_base_paths)
		self.image_loader.load_ui_images()

		# object creation
		self.window = GameWindow(self.graphics_data)
		self.screen_state_machine = ScreenStateMachine(self.graphics_data)
		self.ui_drawer = UIDrawer(self.window, self.screen_state_machine, self.graphics_data)
		self.draw_data_container = GameDrawDataContainer(self.graphics_data)
		self.window.register_ui_drawer(self.ui_drawer)

		# start the graphics and sound for loading screen
		change_screen_event: OnChangeScreenStateEvent = OnChangeScreenStateEvent(ScreenState.LOADING)
		event_bus.emit(EventType.ON_SCREEN_STATE_CHANGE, change_screen_event)
		
		graphics_helpers.start_pyglet()
		
	def full_load(self, on_draw_frame: OnDrawEvent) -> None:

		print(self)

		# remove this, since we only do this on the first frame
		event_bus.remove_listener(EventType.ON_DRAW_FRAME, self.full_load)

		# show the loading screen

		# load images, etc.

		# main images
		change_screen_event: OnChangeScreenStateEvent = OnChangeScreenStateEvent(ScreenState.MAIN_MENU)
		event_bus.emit(EventType.ON_SCREEN_STATE_CHANGE, change_screen_event)


