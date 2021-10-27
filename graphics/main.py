import pyglet

from game import resources 
from game import resources
from game.Room import Room

window = pyglet.window.Window()
	
image_top_width = 42
image_top_height = 24

world_x_size = 5
world_y_size = 5

world_origin_x_s = (window.width // 2) #- (image_top_width // 2) 
world_origin_y_s = (window.height // 2) #- (image_top_height // 2)

inner_pixel_label = pyglet.text.Label(f'Inner Pixel [x: 0, y: 0]', x=0, y=window.height-20)

color = (200, 30, 30)

rectangle = pyglet.shapes.Rectangle(x=0, y=0, width=image_top_width, height=image_top_height, color=color)
rectangle.anchor_x = 0 
rectangle.anchor_y = 0 #image_top_height 

def to_screen_space(world_coords: tuple[int, int]) -> tuple[int, int]:

	x_change = (world_coords[0] - world_coords[1]) * (image_top_width // 2)
	y_change = (world_coords[0] + world_coords[1]) * (image_top_height // 2)

	return world_origin_x_s + x_change, world_origin_y_s + y_change

def to_world_space(screen_coords: tuple[int, int]) -> tuple[int, int]:

	# get the area
	to_origin_x_s = screen_coords[0] - world_origin_x_s
	to_origin_y_s = screen_coords[1] - world_origin_y_s

	to_origin_x_w = to_origin_x_s // image_top_width
	to_origin_y_w = to_origin_y_s // image_top_height

	isometric_x_w = to_origin_x_w + to_origin_y_w 
	#isometric_y_w = abs(to_origin_x_w - to_origin_y_w) 
	isometric_y_w = to_origin_y_w - to_origin_x_w 

	final_x_w = isometric_x_w
	final_y_w = isometric_y_w

	# get the line
	inner_x_pixel = to_origin_x_s % image_top_width
	inner_y_pixel = to_origin_y_s % image_top_height

	"""
	d=(x−x1)(y2−y1)−(y−y1)(x2−x1) 
	If d<0 then the point lies on one side of the line, 
	and if d>0 then it lies on the other side. 
	If d=0 then the point lies exactly line.
	"""	

	# points
	middle_x = image_top_width // 2
	left_x = 0
	right_x = image_top_width

	middle_y = image_top_height // 2
	bottom_y = 0
	top_y = image_top_height

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

	inner_pixel_label.text = f'Inner Pixel [x: {inner_x_pixel}, y: {inner_y_pixel}]' 

	return final_x_w, final_y_w 

ground_batch = pyglet.graphics.Batch()
wall_batch = pyglet.graphics.Batch()

# create spirtes array
"""
ground_sprites = [[pyglet.sprite.Sprite(img=resources.grass_image, batch=ground_batch) for _ in range(world_y_size)] for _ in range(world_x_size)]

ground_sprites.reverse()

# move the sprites into screen space
for x, col in enumerate(ground_sprites):
	col.reverse()
	for y, sprite in enumerate(col):
		# put the world space into screen space
		sprite.x, sprite.y = to_screen_space((x, y))	
"""

def create_room(map_file_path: str) -> Room:
	with open(map_file_path) as file:
		lines: list[str] = file.readlines()

	for y_index, line in enumerate(lines):
		y_w_pos: int = (len(lines) - 1) - y_index # since we start at the max y

		if y_index == 0:
			room: Room = Room(len(line), len(lines))

		for x_w_pos, char in enumerate(line):
			if char == 'X':
				screen_x, screen_y = to_screen_space((x_w_pos, y_w_pos))
				room.add_floor_sprite(x_w_pos, y_w_pos, screen_x, screen_y)

	return room

my_room = create_room('../maps/map.txt')

label = pyglet.text.Label(f'Screen Space [x: 0, y: 0] | World Origin [x:0, y:0] | World Space [x: 0, y:0]')

@window.event
def on_mouse_motion(x, y, dx, dy):

	# check if we are interacting with UI currently

	# check if we are interacting with the game currently

	world_x, world_y = to_world_space((x, y))

	wx_s, wy_s = to_screen_space((world_x, world_y))

	rectangle.x = wx_s 
	rectangle.y = wy_s 
	
	if my_room.check_floor_tile_is_active(world_x, world_y):
		my_room.change_floor_sprite_image(world_x, world_y, resources.weird_image)
	
	label.text = f'Screen Space [{x}, {y}] | World Origin [{world_origin_x_s}, {world_origin_y_s}] | World Space [{world_x}, {world_y}]'

"""
one_x_s, one_y_s = to_screen_space((1,1))
box_x_pos = one_x_s + (image_top_width - resources.box_image.width) // 2
box_y_pos = one_y_s + (image_top_height - resources.box_image.height) // 2

box_sprite = pyglet.sprite.Sprite(img=resources.box_image, x=box_x_pos, y=box_y_pos)

one_x_s, one_y_s = to_screen_space((3,3))
wall_x_pos = one_x_s
wall_y_pos = one_y_s # + resources.wall_image.height

wall_sprite = pyglet.sprite.Sprite(img=resources.wall_image, x=wall_x_pos, y=wall_y_pos)

"""

@window.event
def on_draw():
	window.clear()

	my_room.draw()

	label.draw()
	inner_pixel_label.draw()


pyglet.app.run()