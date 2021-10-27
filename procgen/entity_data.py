from procgen_mod.spell_data import SpellData
from typing import Iterable, Match

import random

from procgen_mod.species_data import SpeciesData
from procgen_mod.character_trait_data import TraitData

import string_functions


class EntityData:
	
	def __init__(
		self, 
		first_name: str, 
		last_name: str, 
		species: SpeciesData,
		initial_character_trait: TraitData,
		favorite_color: str,
	):
		self.first_name = first_name 
		self.last_name = last_name 
		self.title = "" 
		self.epithet = "" 

		self.species = species

		self.character_traits: Iterable[TraitData] = []
		self.character_traits.append(initial_character_trait)

		self.favorite_color = favorite_color

		self.is_alive = True 

	# Could be set later in the process ??
	def set_epithet(self, epithet: str) -> None:
		self.epithet = epithet

	def set_title(self, title: str) -> None:
		self.title = title

	def get_full_name(self) -> str:
		name = ""
		if self.title is not "":
			name += f"{self.title} " 

		name += f"{self.first_name} {self.last_name}"

		if self.epithet is not "":
			name += f" {self.epithet}"	

		return name

	def get_first_name(self) -> str:
		return self.first_name


	def get_species(self) -> SpeciesData:
		return self.species

	def get_action_modifier(self) -> float:
		modifier = 1

		for trait in self.character_traits:
			modifier *= (trait.action_likelihood_modifier / 100)

		return modifier

	def get_strength_score(self) -> int:
		score = 0

		for trait in self.character_traits:
			score += trait.strength

		score += self.species.strength

		return score 
	
	def get_dexterity_score(self) -> int:
		score = 0

		for trait in self.character_traits:
			score += trait.dexterity

		score += self.species.dexterity

		return score 


	def get_intelligence_score(self) -> int:
		score = 0

		for trait in self.character_traits:
			score += trait.intelligence

		score += self.species.intelligence
		
		return score 

	def get_wisdom_score(self) -> int:
		score = 0

		for trait in self.character_traits:
			score += trait.wisdom

		score += self.species.wisdom

		return score 

	def get_charisma_score(self) -> int:
		score = 0

		for trait in self.character_traits:
			score += trait.charisma

		score += self.species.charisma

		return score 

	def get_test_description(self) -> str:
		desc = f"Full name: {string_functions.capitalize_title(self.get_full_name())} \n"
		desc += "Character Traits: \n"

		for trait in self.character_traits:
			desc += f"\t{trait.name}\n"	
		
		desc += f"Favorite color: {self.favorite_color} \n"
		desc += f"Is Alive?: {str(self.is_alive)} \n"
	
		return desc


class EntityDataManager:
	"""
	Handles the entity data.
	"""

	def __init__(self):
		self.entities: Iterable[EntityData] = []
		self.entity_id = 0

	def get_unique_entity_id(self) -> int:
		prev_id = self.entity_id
		self.entity_id += 1
		return prev_id

	def add_entity(self, entity_data: EntityData) -> None:
		self.entities.append(entity_data)

	def get_all_entities(self) -> Iterable[EntityData]:
		return self.entities

	def get_entity_relationship_with_key(self, main_entity: EntityData, key: str) -> EntityData:
		
		if key == "any":
			# get any entity that is not the main entity
			without_main = list(self.entities)
			without_main.remove(main_entity)

			return random.choice(without_main)
		elif key == "alive":
			# get any entity that is alive and not the main entity
			all_alive_except_main = []
			for entity in self.entities:
				if entity.is_alive and entity != main_entity:
					all_alive_except_main.append(entity)

			return random.choice(all_alive_except_main)