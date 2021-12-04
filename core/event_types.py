from enum import Enum, auto
from typing import NewType

from game.screen_state_enum import ScreenState

class EventType(Enum):
    # Core Events
    # INITIAL_LOAD = auto()
    # MAIN_LOAD = auto()

    # Game State Events
    ON_SCREEN_STATE_CHANGE = auto()

    # Pyglet Events
    ON_MOUSE_MOVE = auto()
    ON_DRAW_FRAME = auto()

class Event: 
	pass

class NoDataEvent(Event):
    pass

no_data_event_instance = NoDataEvent()

class OnDrawEvent(Event):  
    pass

class OnChangeScreenStateEvent(Event):

    new_state: ScreenState

    def __init__(self, screen_state: ScreenState) -> None:
        self.new_state = screen_state

class OnMouseMoveEvent(Event):
   
    x: int
    y: int
    dx: int
    dy: int

    def __init__(self, x: int, y: int, dx: int, dy: int) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy