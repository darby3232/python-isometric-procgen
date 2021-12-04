from typing import Annotated, Callable, Optional
from enum import Enum
from core import event_types

from core.event_types import EventType, Event

class ListenerContext:
	pass

class EventListener:

	callback: Callable[[Event, Optional[ListenerContext]], None]
	context: Optional[ListenerContext] 

	def __init__(self, callback: Callable[[Event, Optional[ListenerContext]], None], context: Optional[ListenerContext]):
		self.callback = callback
		self.context = context

	

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


"""
class EventBus:
	def __init__(self):
		self.listeners: dict[EventType, EventListener] = dict()
	
	def add_listener(self, event_type: EventType, listener: EventListener) -> None:
		if not self.listeners.get(event_type, None):
			self.listeners[event_type] = list()
			self.listeners[event_type].append(listener)
		else:
			self.listeners[event_type].append(listener)

	def remove_listener(self, event_type: EventType, listener: EventListener) -> None:
		self.listeners[event_type].remove(listener)
		if len(self.listeners[event_type]) == 0:
			del self.listeners[event_type]

	def emit(self, event_type: EventType, event: Event) -> None:
		if event_type not in self.listeners:
			return

		event_listeners: list[EventListener] = self.listeners[event_type]
		for listener in event_listeners:
			callback: Callable[[Event, Optional[ListenerContext]], None] = listener.callback
			callback(event, listener.context)	
"""

event_bus = EventBus()