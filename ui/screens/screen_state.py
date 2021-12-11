from __future__ import annotations
from typing import Optional

from core.event_bus import EventListener, event_bus
from core.event_types import EventType, OnChangeScreenStateEvent
from graphics.data.graphics_data import GraphicsData
from ui.screens.main_menu_screen import MainMenuScreen
from ui.screens.screen import Screen
from ui.screens.loading_screen import LoadingScreen
from ui.screens.screen_state_enum import ScreenState

class ScreenStateMachine(EventListener):

	graphics_data: GraphicsData

	current_screen: Screen = None

	screen_states: dict[ScreenState, Screen] = {
		ScreenState.LOADING: LoadingScreen(),
		ScreenState.MAIN_MENU: MainMenuScreen(),
	}

	def on_screen_state_change(self, event_data: OnChangeScreenStateEvent) -> None:
		print("screen state change :O")

		if self.current_screen != None:
			self.current_screen.on_leave()

		self.current_screen = self.screen_states[event_data.new_state]
		self.current_screen.on_activate()

	def __init__(self, graphics_data: GraphicsData):
		self.graphics_data = graphics_data

		for screen in self.screen_states.values():
			screen.initialize(self.graphics_data)

		event_bus.add_listener(EventType.ON_SCREEN_STATE_CHANGE, self.on_screen_state_change)

	 
