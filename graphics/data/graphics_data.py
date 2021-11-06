import json
from data.file_paths import graphics_data_path

class GraphicsData:

    def __init__(self):
        pass

    def load(self):
        with open(graphics_data_path) as file:
            graphics_data = json.load(file) 
            self.