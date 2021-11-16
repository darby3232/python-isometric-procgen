from pyglet.libs.win32.constants import GA_MAC
from core import game_manager
from core.game_manager import GameManager 

def main() -> None:
	game_manager = GameManager()
	game_manager.start()

if __name__ == "__main__":
	main()
