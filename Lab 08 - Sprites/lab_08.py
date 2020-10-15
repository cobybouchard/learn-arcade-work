import arcade
import random

SPRITE_SCALING_PLAYER = 0.33
SPRITE_SCALING_COIN = 0.33
SPRITE_SCALING_ROCK = 0.33
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites"
COIN_COUNT = 50
ROCK_COUNT = 30
MOVEMENT_SPEED = 5


class Coin(arcade.Sprite):
    """
    This class represents the coins on our screen
    """

    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.bottom = SCREEN_HEIGHT
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # Reset the coins to the top after they reach the bottom.
        if self.top < 0:
            self.reset_pos()


class Rock(arcade.Sprite):
    """
    This class represents the rocks on our screen
    """

    def reset_pos(self):
        # Reset the rock to a random spot above the screen
        self.bottom = random.randrange(SCREEN_HEIGHT)
        self.center_x = SCREEN_WIDTH

    def update(self):
        # Move the rock
        self.center_x -= 1

        # Reset the rock to the top after they reach the bottom.
        if self.right < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Lab")

        # Sprite lists
        self.coin_list = None
        self.player_list = None
        self.rock_list = None

        # Set up the player
        self.player_sprite = None
        self.score = 0

        # Make mouse invisible
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.RED)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("alienBlue_walk1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Make coins
        for i in range(COIN_COUNT):
            # Coin image from kenney.nl
            coin = Coin("coinGold.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Make rocks
        for i in range(ROCK_COUNT):
            # Rock image from kenney.nl
            rock = Rock("rock.png", SPRITE_SCALING_ROCK)

            # Position the rock
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the rock to the lists
            self.rock_list.append(rock)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()
        self.coin_list.draw()
        self.rock_list.draw()

        # Put the score on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        # Move the Sprite
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        self.coin_list.update()
        # Check to see if the character hit the coin
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Adding when getting coins
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        self.rock_list.update()
        # Check to see if the character hit the rock
        rock_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.rock_list)

        # Adding when getting coins
        for rock in rock_hit_list:
            rock.remove_from_sprite_lists()
            self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
