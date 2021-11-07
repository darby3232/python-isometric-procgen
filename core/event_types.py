from enum import Enum

class EventType(Enum):
    # Core Events
    INITIAL_LOAD = 1

    # Game State Events
    GOTO_MAIN_MENU = 2 
    START_GAME = 3

    # Pyglet Events
    ON_MOUSE_MOVE = 4

class Event: 
	pass

class NoDataEvent(Event):
    pass

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