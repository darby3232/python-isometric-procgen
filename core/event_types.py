from enum import Enum, auto

class EventType(Enum):
    # Core Events
    # INITIAL_LOAD = auto()
    # MAIN_LOAD = auto()

    # Game State Events
    GOTO_MAIN_MENU = auto() 
    START_GAME = auto()

    # Pyglet Events
    ON_MOUSE_MOVE = auto()
    ON_DRAW_FRAME = auto()

class Event: 
	pass

class NoDataEvent(Event):
    pass

no_data_event_instance = NoDataEvent()

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