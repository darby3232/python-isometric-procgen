from procgen_mod.entity_data import EntityDataManager
from procgen_mod.history_event_data import EntityData 
from procgen_mod.history_event_template_manager import HistoryEventTemplate, get_history_event_template

from __future__ import annotations

from typing import Tuple
import string_functions
import re
import random


def execute_duel(actor_roles: dict[str, str], event_actors: dict[str, EntityData], year: int, entity_manager: EntityDataManager) -> list[HistoryEvent]:

	resulting_events: list[HistoryEvent] = []

	# get the challenger actor
	challenger : EntityData = event_actors[actor_roles["challenger"]]
	challengee : EntityData = event_actors[actor_roles["challengee"]]

	# outcomes: both hit, both miss, one hits, the other hits
	challenger_prowess = challenger.get_dexterity_score() + challenger.get_strength_score()
	challengee_prowess = challengee.get_dexterity_score() + challengee.get_strength_score()
	combined_prowess = challenger_prowess + challengee_prowess


	both_hit_weight = (1 - abs(challengee_prowess - challenger_prowess))
	both_miss_weight = .5
	challenger_wins_weight = (1 * (challenger_prowess / combined_prowess))
	challengee_wins_weight = (1 * (challengee_prowess / combined_prowess))

	potential_outcomes = ["both_hit", "both_miss", "challenger_wins", "challengee_wins"]
	outcome_weights = [both_hit_weight, both_miss_weight, challenger_wins_weight, challengee_wins_weight]

	outcome = random.choices(potential_outcomes, outcome_weights)

	challenger_hit_event = HistoryEvent("wounded", year, entity_manager, preset_entities=[""])

	if outcome is "both_hit":

	elif outcome is "both_miss":
		pass
	elif outcome is "challenger_wins":
		pass
	elif outcome is "challengee_wins":
		pass



history_event_functions: dict[str, function] = {

	"duel": execute_duel,

}

class HistoryEvent:
	"""
	Creates then holds the relevent data to a historical event.
	"""
	def __init__(self, event_name: str, year: int, entity_manager: EntityDataManager, preset_entities: list[tuple[str, EntityData]] = []):

		self.year = year
		self.template = get_history_event_template(event_name)

		self.event_actors: dict[str, EntityData] = {}
		self.execute_function = history_event_functions[event_name]
		self.entity_manager = entity_manager

		actor_keys_to_find: list[str] = self.template.actor_keys

		# Remove all the actors that have been predetermined
		for preset in preset_entities:
			actor_key = preset[0]
			entity = preset[1]

			actor_keys_to_find.remove(entity)

			self.event_actors[actor_key] = entity	

		# Find any actors that have not been pre-determined
		for actor_key in actor_keys_to_find:	
			# find an actor relating to the key
			self.event_actors[actor_key] = entity_manager.get_entity_relationship_with_key(main_entity, actor_key)



	def get_description(self) -> str:

		tokenized = re.split('{}', self.template.description)

		tokenized_length = len(tokenized)

		new_desc = ""

		for i in range(tokenized_length):
			# check if even :)
			if i & 0:
				new_desc += tokenized[i]
			else:
				key = tokenized[i]
				sub_tokens = re.split('?', key)
				actor_key = sub_tokens[0]
				query_key = sub_tokens[1]

				actor = self.event_actors[actor_key]
				
				if query_key is "first_name":
					new_desc += actor.first_name
				elif query_key is "last_name":
					new_desc += actor.last_name
				elif query_key is "name" or query_key is "full_name":
					new_desc += actor.get_full_name
				elif query_key is "species_name":
					new_desc += actor.species.name

		return new_desc 

	def execute(self) -> list[HistoryEvent]:
		
		return self.execute_function(self.actor_roles, self.event_actors, self.year, self.entity)