from typing import Callable
from enum import Enum
from core import event_types

from core.event_types import EventType, Event

class EventBus:
	def __init__(self):
		self.listeners: dict[EventType, list[Callable[[Event], None]]] = dict()
	
	def add_listener(self, event_type: EventType, listener: Callable[[Event], None]) -> None:
		if not self.listeners.get(event_type, None):
			self.listeners[event_type] = list()
			self.listeners[event_type].append(listener)
		else:
			self.listeners[event_type].append(listener)

	def remove_listener(self, event_type: EventType, listener: Callable[[Event], None]) -> None:
		self.listeners[event_type].remove(listener)
		if len(self.listeners[event_type]) == 0:
			del self.listeners[event_type]

	def emit(self, event_type: EventType, event: Event) -> None:
		if event_type not in self.listeners:
			return

		event_listeners: list[Callable[[Event], None]] = self.listeners[event_type]
		for listener in event_listeners:
			listener(event)


event_bus = EventBus()