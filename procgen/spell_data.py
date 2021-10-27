from procgen_mod.history_event_data import HistoryEventManager
from typing import Iterable

from procgen_mod.history_event import SpellCreationEvent
from procgen_mod.entity_data import EntityData

import string_functions

import json
import random

class SpellData:
	def __init__(self, name: str, creator: EntityData, element: str, level: int, _id: int):	
		self.name = name
		self.creator = creator
		self.element = element
		self.level = level
		self._id = _id

	def get_test_description(self) -> str:
		desc = "Name: " + self.name + "\n"
		desc += "Creator name: " + self.creator.get_full_name() + "\n"
		desc += "Element: " + self.element + "\n"
		desc += "level: " + str(self.level) + "\n"
		desc += "id: " + str(self._id) + "\n"
		return desc

class SpellDataManager:
	def __init__(self, file_path: str, history_event_manager: HistoryEventManager):
		self.history_event_manager = history_event_manager 
		self.spell_datas = []

		self.id_tracker = 0
		
		with open(file_path) as f:
			self.raw_spell_data = json.loads(f.read())


	def generate_spell(self, arch_wizard: EntityData, level: int) -> None:
		# create spell's data
		spell_element = arch_wizard.adjective.element_name
		element_data = self.raw_spell_data[spell_element]
		spell_first_name: str = random.choice(element_data["first_name"])
		spell_last_name: str = random.choice(element_data["last_name"])
		spell_impetus: str = random.choice(element_data["impetus"])

		spell_name = arch_wizard.first_name + "'s " + spell_first_name + " " + spell_last_name + " " + str(level)
		spell_name = string_functions.capitalize_title(spell_name)

		new_spell_data = SpellData(spell_name, arch_wizard, spell_element, level, self.id_tracker)
		self.id_tracker += 1

		self.spell_datas.append(new_spell_data)

		# Add event to event manager
		spell_creation_history_event = SpellCreationEvent(arch_wizard, spell_impetus, spell_name)

		self.history_event_manager.register_spell_creation_event(spell_creation_history_event)		

	def get_all_spell_datas(self) -> Iterable[SpellData]:
		return self.spell_datas
