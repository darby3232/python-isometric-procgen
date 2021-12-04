from __future__ import annotations
from typing import Optional

from core.event_bus import EventListener, event_bus
from core.event_types import EventType, OnChangeScreenStateEvent
from graphics.game_draw_data_container import GameDrawDataContainer 
from graphics.screens.screen import Screen
from graphics.screens.loading_screen import LoadingScreen
from graphics.ui_handler import UIHandler
from game.screen_state_enum import ScreenState

class ScreenStateMachine(EventListener):

	ui_handler: UIHandler
	draw_data_container: GameDrawDataContainer

	current_screen: Screen = None

	screen_states: dict[ScreenState, Screen] = {
		ScreenState.LOADING: LoadingScreen(),
	}

	def on_screen_state_change(self, event_data: OnChangeScreenStateEvent) -> None:
		print("screen state change :O")

		if self.current_screen != None:
			self.current_screen.on_leave()

		self.current_screen = self.screen_states[event_data.new_state]
		self.current_screen.on_activate()

	def __init__(self, ui_handler: UIHandler, draw_data_container: GameDrawDataContainer):
		self.ui_handler = ui_handler
		self.draw_data_container = draw_data_container

		for screen in self.screen_states.values():
			screen.initialize(self.ui_handler, self.draw_data_container)

		event_bus.add_listener(EventType.ON_SCREEN_STATE_CHANGE, self.on_screen_state_change)

	 
