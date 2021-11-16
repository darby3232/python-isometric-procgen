import json
from enum import Enum

from data.file_paths import graphics_data_path
from core.event_bus import event_bus 
from core.event_types import EventType, NoDataEvent 
from core.extended_enum import ExtendedEnum

class GraphicsUpdateType(Enum):
    WINDOW_SIZE_CHANGE = "window_size_change"

class GraphicsData:

    window_x_size: int
    window_y_size: int

    tile_image_region_x_start: int 
    tile_image_region_x_end: int 
    tile_image_region_y_start: int 
    tile_image_region_y_end: int
    
    tile_image_top_pixel_width: int 
    tile_image_top_pixel_height: int  

    image_paths: dict[str, str]

    has_loaded: bool = False

    def __init__(self) -> None:
        # event_bus.add_listener(EventType.INITIAL_LOAD, self.load)
        pass

    def load(self, event: NoDataEvent) -> None:
        print("Loading the graphics data")

        with open(graphics_data_path) as file:
            graphics_data = json.load(file) 
            self.window_x_size = graphics_data["window_x_size"]
            self.window_y_size = graphics_data["window_y_size"]

            self.tile_image_region_x_start = graphics_data["tile_image_region_x_start"]
            self.tile_image_region_x_end = graphics_data["tile_image_region_x_end"]
            self.tile_image_region_y_start = graphics_data["tile_image_region_y_start"]
            self.tile_image_region_y_end = graphics_data["tile_image_region_y_end"]

            self.tile_image_top_pixel_width = graphics_data["tile_image_top_pixel_width"]
            self.tile_image_top_pixel_height = graphics_data["tile_image_top_pixel_height"]

            # load the all the images
            self.image_paths = {} 

            # get the path data object
            image_path_data: any = graphics_data["image_paths"]

            # cycle through our expected data image keys
            for image_name in GraphicsImages.list():
                self.image_paths[image_name] = image_path_data[image_name]

        self.has_loaded = True

        print(json.dumps(self.image_paths))

    def update(self, update_type: GraphicsUpdateType, new_value: any) -> None:
        # here we can mess with the graphics settings
        with open(graphics_data_path, "a+") as file:
            existing_data = json.load(file)
            
            existing_data[update_type.value] = new_value
            
            file.seek(0)
            json.dump(file)
            file.truncate()
