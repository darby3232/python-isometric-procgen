from __future__ import annotations
from enum import Enum, auto
from typing import Optional

from core.event_bus import EventListener, event_bus
from core.event_types import EventType, OnChangeScreenState
from graphics.game_draw_data_container import GameDrawDataContainer 
from graphics.screens.screen import Screen
from graphics.screens.loading_screen import LoadingScreen
from graphics.ui_handler import UIHandler


class ScreenState(Enum):
	LOADING = auto()
	MAIN_MENU = auto()


class ScreenStateMachine(EventListener):

	ui_handler: UIHandler
	draw_data_container: GameDrawDataContainer

	current_screen: Screen = None

	screen_states: dict[ScreenState, Screen] = {
		ScreenState.LOADING: LoadingScreen(),
	}

	def on_screen_state_change(event_data: OnChangeScreenState, context: Optional[ScreenStateMachine]) -> None:
		if context.current_screen != None:
			context.current_screen.on_leave()

		context.current_screen = context.screen_states[event_data.new_state]
		context.current_screen.on_enter()

	def __init__(self, ui_handler: UIHandler, draw_data_container: GameDrawDataContainer):
		self.ui_handler = ui_handler
		self.draw_data_container = draw_data_container

		for screen in self.screen_states.values():
			screen.initialize(self.ui_handler, self.draw_data_container)

		event_bus.add_listener(EventType.ON_SCREEN_STATE_CHANGE, EventListener(self.on_screen_state_change, self))

	 
