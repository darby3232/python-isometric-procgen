from procgen_mod.entity_data import EntityData

import random

class EntityDataManager:
	"""
	Handles the entity data.
	"""
	def __init__(self):
		self.entities: list[EntityData] = []
		self.entity_id = 0

	def get_unique_entity_id(self) -> int:
		prev_id = self.entity_id
		self.entity_id += 1
		return prev_id

	def add_entity(self, entity_data: EntityData) -> None:
		self.entities.append(entity_data)

	def get_all_entities(self) -> list[EntityData]:
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