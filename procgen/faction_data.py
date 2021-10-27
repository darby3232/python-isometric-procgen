from typing import Iterable

class FactionOpinion:
	def __init__(self, entity_id: int, original_opinion: int):
		self.entity_id = entity_id
		self.opinion_number = original_opinion

	def change_opinion(self, delta: int) -> None:
		self.opinion_number += delta

class Faction:
	"""
	A faction is a group of creatures. They work together, have a leader(?) and share opinions on creatures.
	"""

	def __init__(self, name: str):
		self.name = name 
		self.members: Iterable[int] = []
		self.opinions: Iterable[FactionOpinion]  = [] # those opinions not listed are assumed neutral

	def affect_opinion(self, entity_id: int, delta: int) -> int:
		"""
		Returns the new opinion
		"""
		for opinion in self.opinions:
			if opinion.entity_id == entity_id:
				opinion.opinion_number += delta


class FactionManager:
	"""
	This manages factions.
	"""
	
	def __init__(self):
		self.factions: Iterable[Faction] = []

	def add_faction(self, faction: Faction) -> None:
		self.factions.append(faction)
