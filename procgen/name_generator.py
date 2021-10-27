from typing import Tuple

import random
import json

import file_paths

with open(file_paths.names_path) as f:
	name_data = json.loads(f.read())

def get_random_first_name() -> str:
	prefix = random.choice(name_data["first_name_prefix"])
	suffix = random.choice(name_data["first_name_suffix"])

	return prefix + suffix

def get_random_last_name() -> str:
	prefix = random.choice(name_data["last_name_prefix"])
	suffix = random.choice(name_data["last_name_suffix"])

	return prefix + suffix

def generate_faction_name() -> str:
	prefix = random.choices(name_data["faction_first_name"])
	suffix = random.choices(name_data["faction_last_name"])

	return prefix + " " + suffix

