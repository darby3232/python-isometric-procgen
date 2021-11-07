import json
from data.file_paths import graphics_data_path

from core.event_bus import event_bus 
from core.event_types import EventType, NoDataEvent 

class GraphicsData:

    def __init__(self):
        event_bus.add_listener(EventType.INITIAL_LOAD, self.load)

    def load(self, event: NoDataEvent) -> None:
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
