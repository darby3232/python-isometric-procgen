from enum import Enum

class EventType(Enum):
    # Core Events
    INITIAL_LOAD = 1

    # Game State Events
    GOTO_MAIN_MENU = 2 
    START_GAME = 3

class Event: 
	pass

class NoDataEvent(Event):
    pass