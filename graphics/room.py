import pyglet

class RoomTile:
	is_active: bool = False
	sprite: pyglet.sprite.Sprite = None

class RoomGraphics:

	# probably can't use batches effectively in isometric render, so just draw the sprites individually | not that costly anyways
	floor_tiles : list[list[RoomTile]]
	wall_tiles : list[list[RoomTile]]

	room_x_limit: int
	room_y_limit: int

	def __init__(self, room_x_limit, room_y_limit) -> None:
		self.floor_tiles = [[RoomTile() for _ in range(room_y_limit)] for _ in range(room_x_limit)]

		self.room_x_limit = room_x_limit
		self.room_y_limit = room_y_limit

	def add_floor_sprite(self, world_x: int, world_y: int, screen_x: int, screen_y: int) -> None:
		# add groups for each y level
		sprite = pyglet.sprite.Sprite(img=resources.grass_image, x=screen_x, y=screen_y)
		self.floor_tiles[world_x][world_y].is_active = True
		self.floor_tiles[world_x][world_y].sprite = sprite 

	def add_wall_sprite(self, x: int, y: int) -> None:
		sprite = pyglet.sprite.Sprite(img=resources.wall_image, x=x, y=y)
		self.wall_sprites.append(sprite)

	def check_floor_tile_is_active(self, x: int, y: int) -> bool:
		if 0 <= x < self.room_x_limit and 0 <= y < self.room_y_limit:
			tile: RoomTile = self.floor_tiles[x][y]
			return tile.is_active
		else: 
			return False

	def change_floor_sprite_image(self, x: int, y: int, image: any) -> None:
		self.floor_tiles[x][y].sprite.image = image

	def draw(self) -> None:
		# start in the back, and move forward
		for y_col in reversed(self.floor_tiles):
			for tile in reversed(y_col):
				if tile.is_active:
					tile.sprite.draw()