import arcade
from scenes.MapView import MapView  # you'll make this next

class MenuView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

    def on_draw(self):
        self.clear()
        arcade.draw_text(
            "Press ENTER to start",
            self.window.width // 2,
            self.window.height // 2,
            arcade.color.WHITE,
            font_size=24,
            anchor_x="center"
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            game_view = MapView()
            self.window.show_view(game_view)