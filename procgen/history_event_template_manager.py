import json
import file_paths
from dataclasses import dataclass

@dataclass
class HistoryEventTemplate:

	event_name: str
	actor_keys: list[str]
	description: str


with open(file_paths.event_template_path) as f:
	event_raw_data = json.loads(f.read())

event_datas: dict[str, HistoryEventTemplate] = {}

for key, value in event_raw_data.items():
	event_name = key

	actor_keys = value["actor_keys"]

	description = value["description"]

	event_data = HistoryEventTemplate(
		event_name=event_name, 
		actor_keys=actor_keys, 
		description=description
	)
	
	event_datas[key] = event_data


def get_history_event_template(event_name: str) -> HistoryEventTemplate:
	return event_datas[event_name] 