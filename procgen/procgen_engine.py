from procgen_mod.character_trait_data import TraitManager
from color_data_manager import ColorManager

from name_generator import NameGenerator
from adjective_data import AdjectiveManager
from entity_data import EntityDataManager 
from history_event_data import HistoryEventManager 
from faction_data import FactionManager
from spell_data import SpellDataManager

from procgen_mod import entity_generator

import string_functions

class ProcgenEngine:

	def __init__(self):
		self.entity_manager = EntityDataManager()
		self.faction_manager = FactionManager()
		self.history_event_manager = HistoryEventManager()
		
	def generate_history(self) -> None:
		# Create Factions
		
		# Create Entities
		arch_wizard_one = entity_generator.generate_arch_wizard(self.name_generator, self.adjective_manager, self.color_manager, self.creature_data_manager)
		self.entity_manager.add_entity(arch_wizard_one)
		arch_wizard_two = entity_generator.generate_arch_wizard(self.name_generator, self.adjective_manager, self.color_manager, self.creature_data_manager)
		self.entity_manager.add_entity(arch_wizard_two)
		arch_wizard_three = entity_generator.generate_arch_wizard(self.name_generator, self.adjective_manager, self.color_manager, self.creature_data_manager)
		self.entity_manager.add_entity(arch_wizard_three)

		# Spells ?
		for i in range(4):
			self.spell_manager.generate_spell(arch_wizard_one, i)
			self.spell_manager.generate_spell(arch_wizard_two, i)
			self.spell_manager.generate_spell(arch_wizard_three, i)	

		
	def test_gen_dump(self) -> str:
		gen_str = ""

		# entity manager
		all_entities = self.entity_manager.get_all_entities()

		gen_str += "ENTITIES \n"

		for entity in all_entities:
			gen_str += entity.get_test_description()

		# spell manager
		all_spell_datas = self.spell_manager.get_all_spell_datas()

		gen_str += "SPELLS \n"
		
		for spell_data in all_spell_datas:
			gen_str +=  spell_data.get_test_description()

		# history event manager

		gen_str += "SPELL CREATION EVENTS \n"

		for spell_event in self.history_event_manager.get_all_spell_creation_events():
			gen_str += spell_event.get_spell_creation_exposition() + "\n"

		print(gen_str)