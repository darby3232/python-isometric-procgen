import toml

with open("./data/file_paths.toml") as file:
	file_paths = toml.load(file)

# file paths
graphics_data_path = file_paths["graphics_data_path"]
