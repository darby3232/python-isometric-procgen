import json

with open("./file_paths.json") as file:
	file_paths = json.load(file)

# file paths
graphics_data_path = file_paths["graphics_data_path"]
