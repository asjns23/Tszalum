import arcade
from scenes.MenuView import MenuView

# Window constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Ascension Prototype"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, resizable=False)
        arcade.set_background_color(arcade.color.BLACK)

def main():
    window = GameWindow()
    menu = MenuView()
    window.show_view(menu)
    arcade.run()

if __name__ == "__main__":
    main()
