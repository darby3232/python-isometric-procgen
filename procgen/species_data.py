from typing import Tuple

import json
import random

from color_data_manager import get_color

from dataclasses import dataclass
import file_paths

@dataclass
class SpeciesData:

	name: str 
	oldest: int 
	strength: int 
	dexterity: int 
	intelligence: int 
	color_name: str 
	color: Tuple[int, int, int]


with open(file_paths.proc_species_path) as file:
	creature_raw_data = json.loads(file.read())

creature_data = {}
for key, value in creature_raw_data.items():
	oldest = int(value["oldest"])
	strength = int(value["strength"])
	dexterity = int(value["dexterity"])
	intelligence = int(value["intelligence"])
	creature_color_name = value["color_name"]
	color = get_color(creature_color_name)
	
	new_creature = SpeciesData(
		key=key, 
		oldest=oldest, 
		strength=strength, 
		dexterity=dexterity, 
		intelligence=intelligence, 
		creature_color_name=creature_color_name, 
		color=color
	)
	
	creature_data[key] = new_creature

# Gets a random creature from the list of creatures
def get_random_creature() -> SpeciesData:
	return random.choice(list(creature_data.values()))