import arcade

TILE_SIZE = 64
MAP_WIDTH = 10
MAP_HEIGHT = 8

class MapView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player_x = 0
        self.player_y = 0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        # Draw grid
        for row in range(MAP_HEIGHT):
            for col in range(MAP_WIDTH):
                x = col * TILE_SIZE + TILE_SIZE // 2
                y = row * TILE_SIZE + TILE_SIZE // 2
                arcade.draw_rectangle_outline(
                    x, y, TILE_SIZE, TILE_SIZE, arcade.color.DARK_GRAY
                )
        # Draw player
        px = self.player_x * TILE_SIZE + TILE_SIZE // 2
        py = self.player_y * TILE_SIZE + TILE_SIZE // 2
        arcade.draw_circle_filled(px, py, TILE_SIZE // 3, arcade.color.RED)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W and self.player_y < MAP_HEIGHT - 1:
            self.player_y += 1
        elif key == arcade.key.S and self.player_y > 0:
            self.player_y -= 1
        elif key == arcade.key.A and self.player_x > 0:
            self.player_x -= 1
        elif key == arcade.key.D and self.player_x < MAP_WIDTH - 1:
            self.player_x += 1
