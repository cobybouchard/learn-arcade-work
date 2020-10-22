import arcade

WIDTH = 20
HEIGHT = 20
MARGIN = 5
ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_HEIGHT = (HEIGHT * ROW_COUNT) + (MARGIN + 1) * ROW_COUNT
SCREEN_WIDTH = (WIDTH * ROW_COUNT) + (MARGIN + 1) * COLUMN_COUNT


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        for column in range(COLUMN_COUNT):
            arcade.draw_rectangle_filled((WIDTH / 2) + (column * (WIDTH + MARGIN)) + MARGIN,
                                         HEIGHT / 2, WIDTH, HEIGHT, arcade.color.TEAL)
            for row in range(ROW_COUNT):
                arcade.draw_rectangle_filled(WIDTH / 2,(HEIGHT / 2) + (row * (HEIGHT + MARGIN)) + MARGIN, WIDTH, HEIGHT, arcade.color.TEAL)


def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
