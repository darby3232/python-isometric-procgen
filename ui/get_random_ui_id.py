import random
import string

def get_random_id() -> str:
	letters = string.ascii_lowercase
	return ''.join(random.choice((letters)) for _ in range(3))
