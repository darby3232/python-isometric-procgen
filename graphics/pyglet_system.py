import pyglet

class PygletSystem(pyglet.window.Window):

	draw_debug: bool = True

	# the dimensions of the tile images	
	self.image_top_width = 42
	self.image_top_height = 24

	def draw(self):
		pass

	def __init__(self):
		# create all the pyglet objects
		self.window = pyglet.window.Window()
		self.self.world_origin_x_s = (self.window.width // 2) 
		self.self.world_origin_y_s = (self.window.height // 2)

	def start():
		pyglet.app.run()

	def render(self):
		pass

	def on_draw(self):
		self.render()

	def on_mouse_motion(self, x, y, dx, dy):
		pass

	def to_screen_space(self, world_coords: tuple[int, int]) -> tuple[int, int]:
		x_change = (world_coords[0] - world_coords[1]) * (self.self.image_top_width // 2)
		y_change = (world_coords[0] + world_coords[1]) * (self.self.image_top_height // 2)

		return self.self.world_origin_x_s + x_change, self.self.world_origin_y_s + y_change


	def to_world_space(self, screen_coords: tuple[int, int]) -> tuple[int, int]:

		# get the area
		to_origin_x_s = screen_coords[0] - self.world_origin_x_s
		to_origin_y_s = screen_coords[1] - self.world_origin_y_s

		to_origin_x_w = to_origin_x_s // self.image_top_width
		to_origin_y_w = to_origin_y_s // self.image_top_height

		isometric_x_w = to_origin_x_w + to_origin_y_w 
		#isometric_y_w = abs(to_origin_x_w - to_origin_y_w) 
		isometric_y_w = to_origin_y_w - to_origin_x_w 

		final_x_w = isometric_x_w
		final_y_w = isometric_y_w

		# get the line
		inner_x_pixel = to_origin_x_s % self.image_top_width
		inner_y_pixel = to_origin_y_s % self.image_top_height

		"""
		d=(x−x1)(y2−y1)−(y−y1)(x2−x1) 
		If d<0 then the point lies on one side of the line, 
		and if d>0 then it lies on the other side. 
		If d=0 then the point lies exactly line.
		"""	

		# points
		middle_x = self.image_top_width // 2
		left_x = 0
		right_x = self.image_top_width

		middle_y = self.image_top_height // 2
		bottom_y = 0
		top_y = self.image_top_height

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




