import pyglet

pyglet.resource.path = ['../assets']
pyglet.resource.reindex()

def anchor_top_left(image):
	image.anchor_y = image.height

def anchor_tile(image):
	image.anchor_y = image.height - 24

def get_modded_tile_image(image_path: str) -> any:
	image = pyglet.resource.image(image_path)
	sub_image = image.get_region(4, 0, 42, 49)
	anchor_tile(sub_image)
	return sub_image


def get_modded_wall_image(image_path: str) -> any:
	image = pyglet.resource.image(image_path)
	sub_image = image.get_region(4, 0, 42, 49)
	return sub_image

grass_image = get_modded_tile_image('isometric_pixel_0014.png')
weird_image = get_modded_tile_image('isometric_pixel_0174.png')
wall_image = get_modded_wall_image('isometric_pixel_0052.png')

box_image = pyglet.resource.image('box.png')
# anchor_top_left(box_image) # why would i do this anymore?