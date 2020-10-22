"""
Use sprites to scroll around a large screen.

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade
import os


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
PLAYER_SPRITE_SCALING = 0.25
WALL_SPRITE_SCALING = 0.5
COIN_SPRITE_SCALING = 0.25
GEM_SPRITE_SCALING = 0.25
# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 200

MOVEMENT_SPEED = 5

COIN_COUNT = 25
GEM_COUNT = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None
        self.gem_list = None

        # Set up the player
        self.player_sprite = None
        self.score = 0

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        self.coin_sound = arcade.load_sound("coin5.wav")
        self.gem_sound = arcade.load_sound("coin1.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("alienBlue_walk2.png", PLAYER_SPRITE_SCALING)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 250
        self.player_list.append(self.player_sprite)

        # -- Set up border walls
        for x in range(50, 1459, 1408):
            for y in range(50, 1050, 64):
                wall = arcade.Sprite("boxCrate.png", WALL_SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for y in range(50, 1025, 960):
            for x in range(114, 1408, 64):
                wall = arcade.Sprite("boxCrate.png", WALL_SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for y in range(560, 561, 1):
            for x in range(114, 1200, 64):
                wall = arcade.Sprite("boxCrate.png", WALL_SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for x in range(275, 1126, 125):
            for y in range(114, 561, 64):
                if random.randrange(4) > 1:
                    wall = arcade.Sprite("boxCrate.png", WALL_SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
        for x in range(275, 1126, 125):
            for y in range(625, 1003, 64):
                if random.randrange(4) > 1:
                    wall = arcade.Sprite("boxCrate.png", WALL_SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coinGold.png", COIN_SPRITE_SCALING)

            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(50, 1408)
                coin.center_y = random.randrange(50, 1000)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(GEM_COUNT):
            gem = arcade.Sprite("gemBlue.png", GEM_SPRITE_SCALING)
            gem_placed_successfully = False

            # Keep trying until success
            while not gem_placed_successfully:
                gem.center_x = random.randrange(50, 1408)
                gem.center_y = random.randrange(50, 1000)

                gem_wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)

                gem_gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                gem_coin_hit_list = arcade.check_for_collision_with_list(gem, self.coin_list)

                if len(gem_wall_hit_list) == 0 and len(gem_gem_hit_list) == 0 and len(gem_coin_hit_list) == 0:
                    gem_placed_successfully = True

            self.gem_list.append(gem)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.gem_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20, arcade.color.WHITE, 14)

        if len(self.coin_list) == 0 and len(self.gem_list) == 0:
            arcade.draw_text("Game Over", self.view_left + 250, self.view_bottom + 300,
                             arcade.color.WHITE, 50)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        if len(self.coin_list) != 0 or len(self.gem_list) != 0:
            self.physics_engine.update()

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)
        self.coin_list.update()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

        self.gem_list.update()

        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.gem_list)

        for gem in gem_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 5
            arcade.play_sound(self.gem_sound)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()