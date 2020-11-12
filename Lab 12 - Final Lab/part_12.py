"""
Load a map stored in csv format, as exported by the program 'Tiled.'

Artwork from: http://kenney.nl
Tiled available from: http://www.mapeditor.org/
"""
import arcade

SPRITE_SCALING = 0.5
PLAYER_SPRITE_SCALING = 0.4

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
BOTTOM_MARGIN = 80
TOP_MARGIN = 25
RIGHT_MARGIN = 200
LEFT_MARGIN = 60

TILE_SIZE = 128
SCALED_TILE_SIZE = TILE_SIZE * SPRITE_SCALING
MAP_HEIGHT = 7

# Physics
MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 0.5


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

        # Set up the player
        self.player_sprite = None

        self.gem_sprite = None

        # Physics engine
        self.physics_engine = None

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

        # Set up the player
        self.player_sprite = arcade.Sprite("alienBlue_walk2.png", PLAYER_SPRITE_SCALING)

        # Starting position of the player
        self.player_sprite.center_x = 90
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        # Get a 2D array made of numbers based on the map
        map_array = get_map("my_map_Walls.csv")

        # Now that we've got the map, loop through and create the sprites
        for row_index in range(len(map_array)):
            for column_index in range(len(map_array[row_index])):

                item = map_array[row_index][column_index]

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
                if 0 <= item <= 12:
                    # Calculate where the sprite goes
                    wall.left = column_index * SCALED_TILE_SIZE
                    wall.top = (MAP_HEIGHT - row_index) * SCALED_TILE_SIZE

                    # Add the sprite
                    self.wall_list.append(wall)

        map_array = get_map("my_map_Walls.csv")

        # Create out platformer physics engine with gravity
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        self.gem_sprite = arcade.Sprite("gemBlue.png", PLAYER_SPRITE_SCALING)

        # Starting position of the player
        self.gem_sprite.center_x = 3100
        self.gem_sprite.center_y = 0
        self.gem_list.append(self.gem_sprite)

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

        if len(self.gem_list) == 0:
            arcade.draw_text("You win", 2800, 175, arcade.color.WHITE, 50)

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """

        if key == arcade.key.UP:
            # This line below is new. It checks to make sure there is a platform underneath
            # the player. Because you can't jump if there isn't ground beneath your feet.
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

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
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_MARGIN
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


def main():
    window = MyWindow()
    window.setup()

    arcade.run()


main()