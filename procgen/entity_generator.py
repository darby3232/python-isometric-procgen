from procgen_mod.character_trait_data import get_random_trait
from color_data_manager import get_random_color_name

from procgen_mod.species_data import get_random_creature 
from procgen_mod.adjective_data import get_random_adjective
from procgen_mod.name_generator import get_random_first_name, get_random_last_name 
from procgen_mod.entity_data import EntityData

def generate_arch_wizard() -> EntityData:
	first_name, last_name = get_random_first_name(), get_random_last_name() 
	adjective = get_random_adjective()

	favorite_color = get_random_color_name()
	favorite_creature = get_random_creature() 

	entity_data = EntityData(
		first_name=first_name,
		last_name=last_name,
		title="archwizard",
		epithet="",
		adjective=adjective,
		favorite_creature=favorite_creature,
		favorite_color=favorite_color,
		is_alive=False
	)

	return entity_data


def generate_random_entity_base() -> EntityData:

	first_name, last_name = get_random_first_name(), get_random_last_name() 
	species = get_random_creature() 
	character_trait = get_random_trait()

	favorite_color = get_random_color_name()

	entity_data = EntityData(
		first_name=first_name,
		last_name=last_name,
		species=species,
		initial_character_trait=character_trait,
		favorite_color=favorite_color,
	)

	return entity_data