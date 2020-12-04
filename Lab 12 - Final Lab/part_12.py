"""
Aliens vs. Worms
"""
import arcade

SPRITE_SCALING = 0.5
PLAYER_SPRITE_SCALING = 0.4
LASER_SPRITE_SCALING = 0.25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
BOTTOM_MARGIN = 80
RIGHT_MARGIN = 200
LEFT_MARGIN = 60

TILE_SIZE = 128
SCALED_TILE_SIZE = TILE_SIZE * SPRITE_SCALING
MAP_HEIGHT = 7

# Physics
MOVEMENT_SPEED = 3
JUMP_SPEED = 10
GRAVITY = 0.5
LASER_SPEED = 20


def get_map(filename):
    """
    This function loads an array based on a map stored as a list of
    numbers separated by commas.
    """

    # Open the file
    map_file = open(filename)

    # Create an empty list of rows that will hold our map
    map_array = []

    # Read in a line from the file
    for line in map_file:

        # Strip the whitespace, and \n at the end
        line = line.strip()

        # This creates a list by splitting line everywhere there is a comma.
        map_row = line.split(",")

        # The list currently has all the numbers stored as text, and we want it
        # as a number. (e.g. We want 1 not "1"). So loop through and convert
        # to an integer.
        for index, item in enumerate(map_row):
            map_row[index] = int(item)

        # Now that we've completed processing the row, add it to our map array.
        map_array.append(map_row)

    # Done, return the map.
    return map_array


class MyWindow(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        # Call the parent class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.lava_list = None
        self.coin_list = None
        self.gem_list = None
        self.laser_list = None
        self.enemy_list = None

        # Set up the player
        self.player_sprite = None
        self.gem_sprite = None
        self.laser_sprite = None
        self.score = None
        self.player_lives = None

        # Physics engine
        self.physics_engine = None

        self.gem_sound = arcade.load_sound("coin1.wav")
        self.game_over_sound = arcade.load_sound("gameover3.wav")
        self.laser_sound = arcade.load_sound("laser2.wav")
        self.enemy_sound = arcade.load_sound("hurt5.wav")
        self.coin_sound = arcade.load_sound("coin5.wav")

        # Used for scrolling map
        self.view_left = 0
        self.view_bottom = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.lava_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.score = 0
        self.player_lives = 3

        # Set up the player
        self.player_sprite = arcade.Sprite("alienBlue_walk2.png", PLAYER_SPRITE_SCALING)

        # Starting position of the player
        self.player_sprite.center_x = 90
        self.player_sprite.center_y = -40
        self.player_list.append(self.player_sprite)

        # Get a 2D array made of numbers based on the map
        map_array = get_map("my_map.csv")

        # Now that we've got the map, loop through and create the sprites
        for row_index in range(len(map_array)):
            for column_index in range(len(map_array[row_index])):

                item = map_array[row_index][column_index]
                lava = None
                wall = None

                if item == 0:
                    wall = arcade.Sprite("grassHill_left.png", SPRITE_SCALING)
                elif item == 1:
                    wall = arcade.Sprite("grassHill_right.png", SPRITE_SCALING)
                elif item == 2:
                    wall = arcade.Sprite("grassLeft.png", SPRITE_SCALING)
                elif item == 3:
                    wall = arcade.Sprite("grassMid.png", SPRITE_SCALING)
                elif item == 4:
                    wall = arcade.Sprite("grassRight.png", SPRITE_SCALING)
                elif item == 5:
                    wall = arcade.Sprite("boxCrate.png", SPRITE_SCALING)
                elif item == 6:
                    wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
                elif item == 7:
                    wall = arcade.Sprite("grassCenter.png", SPRITE_SCALING)
                elif item == 8:
                    wall = arcade.Sprite("grassCorner_left.png", SPRITE_SCALING)
                elif item == 9:
                    wall = arcade.Sprite("grassCorner_right.png", SPRITE_SCALING)
                elif item == 10:
                    wall = arcade.Sprite("grassHalf_left.png", SPRITE_SCALING)
                elif item == 11:
                    wall = arcade.Sprite("grassHalf_mid.png", SPRITE_SCALING)
                elif item == 12:
                    wall = arcade.Sprite("grassHalf_right.png", SPRITE_SCALING)
                elif item == 13:
                    lava = arcade.Sprite("lavaTop_low.png", SPRITE_SCALING)
                elif item == 14:
                    lava = arcade.Sprite("lava.png", SPRITE_SCALING)
                elif item == 15:
                    lava = arcade.Sprite("lavaTop_high.png", SPRITE_SCALING)
                if 0 <= item <= 12:
                    # Calculate where the sprite goes
                    wall.left = column_index * SCALED_TILE_SIZE
                    wall.top = (MAP_HEIGHT - row_index) * SCALED_TILE_SIZE

                    # Add the sprite
                    self.wall_list.append(wall)

                elif 13 <= item <= 15:
                    lava.left = column_index * SCALED_TILE_SIZE
                    lava.top = (MAP_HEIGHT - row_index) * SCALED_TILE_SIZE

                    self.lava_list.append(lava)

        # Create out platformer physics engine with gravity
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        self.gem_sprite = arcade.Sprite("gemBlue.png", PLAYER_SPRITE_SCALING)

        # Starting position of the player
        self.gem_sprite.center_x = 3100
        self.gem_sprite.center_y = -128
        self.gem_list.append(self.gem_sprite)

        enemy = arcade.Sprite("wormPink.png", SPRITE_SCALING)
        enemy.center_x = 1375
        enemy.center_y = 0

        self.enemy_list.append(enemy)

        enemy = arcade.Sprite("wormPink.png", SPRITE_SCALING)
        enemy.center_x = 2400
        enemy.center_y = 130

        self.enemy_list.append(enemy)

        enemy = arcade.Sprite("wormPink.png", SPRITE_SCALING)
        enemy.center_x = 2940
        enemy.center_y = 60

        self.enemy_list.append(enemy)

        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
        coin.center_x = 540
        coin.center_y = 35

        self.coin_list.append(coin)

        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
        coin.center_x = 790
        coin.center_y = -160

        self.coin_list.append(coin)

        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
        coin.center_x = 1375
        coin.center_y = 180

        self.coin_list.append(coin)

        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
        coin.center_x = 1693
        coin.center_y = -100

        self.coin_list.append(coin)

        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
        coin.center_x = 1693
        coin.center_y = -37

        self.coin_list.append(coin)

        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
        coin.center_x = 1693
        coin.center_y = 30

        self.coin_list.append(coin)

        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
        coin.center_x = 1821
        coin.center_y = -37

        self.coin_list.append(coin)

        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
        coin.center_x = 1821
        coin.center_y = 30

        self.coin_list.append(coin)

        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
        coin.center_x = 1952
        coin.center_y = 30

        self.coin_list.append(coin)

        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
        coin.center_x = 2400
        coin.center_y = 210

        self.coin_list.append(coin)

        for x in range(3100, 3102, 1):
            for y in range(0, 250, 50):
                coin = arcade.Sprite("coinGold.png", SPRITE_SCALING)
                coin.center_x = x
                coin.center_y = y
                self.coin_list.append(coin)

        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Set the view port boundaries
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
        self.gem_list.draw()
        self.lava_list.draw()
        self.laser_list.draw()
        self.enemy_list.draw()
        self.coin_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20, arcade.color.BLACK, 14)

        arcade.draw_text(f"Lives left: {self.player_lives}", self.view_left + 10, self.view_bottom + 50,
                         arcade.color.BLACK, 14)

        if len(self.gem_list) == 0:
            arcade.draw_text("You Win", 325 + self.view_left, 125, arcade.color.BLACK, 75)
        if self.player_lives == 0:
            arcade.draw_text("Game Over", 250 + self.view_left, 125,
                             arcade.color.BLACK, 75)
        if self.player_sprite.center_x <= 130 and self.player_lives != 0:
            arcade.draw_text(f"Move to Start. \nCollect as many coins \nas possible and avoid \nthe lava and worms."
                             f"\nTo win, collect the gem \nat end of the map."
                             f"\nYou have {self.player_lives} left.",
                             100 + self.view_left, 0, arcade.color.BLACK, 40)

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if self.player_lives != 0 and len(self.gem_list) != 0:
            if key == arcade.key.UP:
                # This line below is new. It checks to make sure there is a platform underneath
                # the player. Because you can't jump if there isn't ground beneath your feet.
                if self.physics_engine.can_jump():
                    self.player_sprite.change_y = JUMP_SPEED
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = MOVEMENT_SPEED
            if key == arcade.key.SPACE:
                arcade.play_sound(self.laser_sound)
                self.laser_sprite = arcade.Sprite("slimeGreen.png", LASER_SPRITE_SCALING)
                # The image points to the right, and we want it to point up. So
                # rotate it.

                # Position the bullet
                self.laser_sprite.center_x = self.player_sprite.center_x + 20
                self.laser_sprite.center_y = self.player_sprite.center_y
                self.laser_sprite.change_x = LASER_SPEED

                # Add the bullet to the appropriate lists
                self.laser_list.append(self.laser_sprite)

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the view port

        changed = False

        # Scroll left
        left_boundary = self.view_left + LEFT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        self.gem_list.update()

        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)

        for self.gem_sprite in gem_hit_list:
            self.gem_sprite.remove_from_sprite_lists()
            arcade.play_sound(self.gem_sound)

        self.player_list.update()

        for self.player_sprite in self.player_list:
            lava_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.lava_list)

            for lava_hit in lava_hit_list:
                self.player_sprite.remove_from_sprite_lists()
                arcade.play_sound(self.game_over_sound)
                self.player_lives -= 1
                self.player_sprite.center_x = 90
                self.player_sprite.center_y = -40
                self.player_list.append(self.player_sprite)

        for self.player_sprite in self.player_list:
            player_enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)

            for enemy_hit in player_enemy_hit_list:
                self.player_sprite.remove_from_sprite_lists()
                arcade.play_sound(self.game_over_sound)
                self.player_lives -= 1

                self.player_sprite.center_x = 90
                self.player_sprite.center_y = -40
                self.player_list.append(self.player_sprite)

        self.enemy_list.update()
        self.laser_list.update()

        for enemy in self.enemy_list:
            laser_hit_list = arcade.check_for_collision_with_list(enemy, self.laser_list)

            for laser_hit in laser_hit_list:
                laser_hit.remove_from_sprite_lists()
                enemy.remove_from_sprite_lists()
                arcade.play_sound(self.enemy_sound)

        for laser in self.laser_list:
            wall_hit_list = arcade.check_for_collision_with_list(laser, self.wall_list)

            for laser_hit in wall_hit_list:
                laser.remove_from_sprite_lists()

        self.coin_list.update()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)


def main():
    window = MyWindow()
    window.setup()
    arcade.run()


main()
