import json
from enum import Enum

from data.file_paths import graphics_data_path
from core.event_bus import event_bus 
from core.event_types import EventType, NoDataEvent 

class GraphicsUpdateType(Enum):
    WINDOW_SIZE_CHANGE = "window_size_change"


class GraphicsData:

    window_x_size: int
    window_y_size: int

    has_loaded: bool = False

    def __init__(self) -> None:
        event_bus.add_listener(EventType.INITIAL_LOAD, self.load)

    def load(self, event: NoDataEvent) -> None:
        with open(graphics_data_path) as file:
            graphics_data = json.load(file) 
            self.window_x_size = graphics_data["window_x_size"]
            self.window_y_size = graphics_data["window_y_size"]

        self.has_loaded = True

    def update(self, update_type: GraphicsUpdateType, new_value: any) -> None:
        # here we can mess with the graphics settings
        with open(graphics_data_path, "a+") as file:
            existing_data = json.load(file)
            
            existing_data[update_type.value] = new_value
            
            file.seek(0)
            json.dump(file)
            file.truncate()