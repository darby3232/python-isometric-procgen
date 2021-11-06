from typing import Callable

class Event: 
	pass

class EventBus:

	def __init__(self):
		self.listeners: dict[str, list[Callable[[Event], None]]] = dict()
	
	def add_listener(self, event_name: str, listener: Callable[[Event], None]) -> None:
		if not self.listeners.get(event_name, None):
			self.listeners[event_name] = list()
			self.listeners[event_name].append(listener)
		else:
			self.listeners[event_name].append(listener)

	def remove_listener(self, event_name: str, listener: Callable[[Event], None]) -> None:
		self.listeners[event_name].remove(listener)
		if len(self.listeners[event_name]) == 0:
			del self.listeners[event_name]

	def emit(self, event_name: str, event: Event) -> None:
		event_listeners: list[Callable[[Event], None]] = self.listeners[event_name]
		for listener in event_listeners:
			listener(event)


event_bus = EventBus()