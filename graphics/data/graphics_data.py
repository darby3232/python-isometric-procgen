import json
from data.file_paths import graphics_data_path

from core.event_bus import event_bus

class GraphicsData:

    # should there just be a master python object?
    # why not?

    def __init__(self):
        event_bus.add("load", self.load)


    def load(self, ) -> None:
        with open(graphics_data_path) as file:
            self.graphics_data = json.load(file) 

    def update(self, setting_name: str, new_value: any) -> None:
        # here we can mess with the graphics settings
        with open(graphics_data_path, "a+") as file:
            existing_data = json.load(file)
            
            existing_data[setting_name] = new_value
            
            file.seek(0)
            json.dump(file)
            file.truncate()
