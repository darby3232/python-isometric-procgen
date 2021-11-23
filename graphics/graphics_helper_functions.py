import pyglet
from pyglet.window import Window

from graphics.data.graphics_data import GraphicsData 

def start_pyglet() -> None:
	pyglet.app.run()

def set_pyglet_resource_paths(path: list[str]) -> None:
	pyglet.resource.path = path
	pyglet.resource.reindex()

def get_world_origin_screen_space(window: Window) -> tuple[int, int]:
	origin_x_s = window.width // 2
	origin_y_s = window.height // 2

	return origin_x_s, origin_y_s

def to_screen_space(world_coords: tuple[int, int], window: Window, graphics_data: GraphicsData) -> tuple[int, int]:

	world_origin_x_s, world_origin_y_s = get_world_origin_screen_space(window)

	x_change = (world_coords[0] - world_coords[1]) * (graphics_data.tile_image_top_pixel_width // 2)
	y_change = (world_coords[0] + world_coords[1]) * (graphics_data.tile_image_top_pixel_height // 2)

	return world_origin_x_s + x_change, world_origin_y_s + y_change

def to_world_space(screen_coords: tuple[int, int], window: Window, graphics_data: GraphicsData) -> tuple[int, int]:

	world_origin_x_s, world_origin_y_s = get_world_origin_screen_space(window)
	
	# get the area
	to_origin_x_s = screen_coords[0] - world_origin_x_s
	to_origin_y_s = screen_coords[1] - world_origin_y_s

	to_origin_x_w = to_origin_x_s // graphics_data.tile_image_top_pixel_width 
	to_origin_y_w = to_origin_y_s // graphics_data.tile_image_top_pixel_height 

	isometric_x_w = to_origin_x_w + to_origin_y_w 
	# isometric_y_w = abs(to_origin_x_w - to_origin_y_w) 
	isometric_y_w = to_origin_y_w - to_origin_x_w 

	final_x_w = isometric_x_w
	final_y_w = isometric_y_w

	# get the line
	inner_x_pixel = to_origin_x_s % graphics_data.tile_image_top_pixel_width 
	inner_y_pixel = to_origin_y_s % graphics_data.tile_image_top_pixel_height

	"""
	d=(x−x1)(y2−y1)−(y−y1)(x2−x1) 
	If d<0 then the point lies on one side of the line, 
	and if d>0 then it lies on the other side. 
	If d=0 then the point lies exactly line.
	"""	

	# points
	middle_x = graphics_data.tile_image_top_pixel_width // 2
	left_x = 0
	right_x = graphics_data.tile_image_top_pixel_width 

	middle_y = graphics_data.tile_image_top_pixel_height // 2
	bottom_y = 0
	top_y = graphics_data.tile_image_top_pixel_height 

	# bottom left (mid left to bottom middle)
	b_left_d = (inner_x_pixel-left_x)*(bottom_y-middle_y) - (inner_y_pixel-middle_y)*(middle_x-left_x)
	if b_left_d > 0:
		final_x_w -= 1

	# upper left
	u_left_d = (inner_x_pixel-left_x)*(top_y-middle_y) - (inner_y_pixel-middle_y)*(middle_x-left_x)
	if u_left_d < 0:
		final_y_w += 1

	# upper right 
	u_right_d = (inner_x_pixel-right_x)*(top_y-middle_y) - (inner_y_pixel-middle_y)*(middle_x-right_x)
	if u_right_d > 0:
		final_x_w += 1

	# bottom right 
	b_right_d = (inner_x_pixel-right_x)*(bottom_y-middle_y) - (inner_y_pixel-middle_y)*(middle_x-right_x)
	if b_right_d < 0:
		final_y_w -= 1

	return final_x_w, final_y_w 

def anchor_image_top_left(image: any) -> None:
	image.anchor_y = image.height

def anchor_tile(image: any, graphics_data: GraphicsData) -> None:
	image.anchor_y = image.height - graphics_data.tile_image_top_pixel_height


def create_modded_tile_image(image_path: str, graphics_data: GraphicsData) -> any:
	image = pyglet.resource.image(image_path)

	# grab all bounds more cleanly -> cuts off excess for clean anchoring operations, etc.
	x_lower, x_upper = graphics_data.tile_image_region_x_start, graphics_data.tile_image_region_x_end
	y_lower, y_upper = graphics_data.tile_image_region_y_start, graphics_data.tile_image_region_y_end

	sub_image = image.get_region(x_lower, y_lower, x_upper, y_upper)
	anchor_tile(sub_image, graphics_data)
	return sub_image

def create_modded_wall_image(image_path: str, graphics_data: GraphicsData) -> any:
	image = pyglet.resource.image(image_path)

	# grab all bounds more cleanly -> cuts off excess for clean anchoring operations, etc.
	x_lower, x_upper = graphics_data.tile_image_region_x_start, graphics_data.tile_image_region_x_end
	y_lower, y_upper = graphics_data.tile_image_region_y_start, graphics_data.tile_image_region_y_end

	sub_image = image.get_region(x_lower, y_lower, x_upper, y_upper)
	return sub_image