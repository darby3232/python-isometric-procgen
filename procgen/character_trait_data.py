import json
import random
from typing import Iterable
from dataclasses import dataclass

import file_paths

@dataclass
class TraitData:
	name: str 
	strength: int 
	dexterity: int 
	intelligence: int
	wisdom: int
	charisma: int
	action_likelihood_modifier: int
		

with open(file_paths.character_traits_path) as f:
	trait_raw_data = json.loads(f.read())

trait_datas = []

for key, value in trait_raw_data.items():
	name = key
	strength = value["str"]
	dexterity = value["dex"]
	intelligence = value["int"]
	wisdom = value["wis"]
	charisma = value["cha"]
	action_mod = value["action_likelihood_mod"]

	new_trait_data = TraitData(
		name=name,
		strength=strength, 
		dexterity=dexterity, 
		intelligence=intelligence, 
		wisdom=wisdom, 
		charisma=charisma, 
		action_mod=action_mod
	)
	
	trait_datas.append(new_trait_data)

def get_random_trait() -> TraitData:
	return random.choice(trait_datas)