from typing import Iterable

import random

from procgen_mod.entity_data import EntityData
from procgen_mod.history_event import SpellCreationEvent
from procgen_mod.history_event import HistoryEvent

class HistoryEventManager:

	def __init__(self):
		self.all_events = []
		self.spell_creation_events = []

	def register_spell_creation_event(self, spell_creation_event: SpellCreationEvent) -> None:
		self.all_events.append(spell_creation_event)
		self.spell_creation_events.append(spell_creation_event)

	def get_all_spell_creation_events(self) -> Iterable[SpellCreationEvent]:
		return self.all_events
