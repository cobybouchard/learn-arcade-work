# Import arcade
import arcade

screen_width = 600
screen_height = 600


def draw_grass():
    """ Draw Grass """
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

def draw_sun(x, y):
    """ Draw Sun """
    arcade.draw_circle_filled(600 + x - 600, 600+ x -600, 60, arcade.csscolor.YELLOW)

def draw_house():
    """ Draw House """
    arcade.draw_lrtb_rectangle_filled(100, 300, 400, 200, arcade.csscolor.BEIGE)
    arcade.draw_triangle_filled(75, 400, 325, 400, 200, 525, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(175, 225, 275, 200, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(215, 235, 5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(250, 350, 25, arcade.csscolor.LIGHT_BLUE)


def draw_bush(x, y):
    """ Draw Bush """
    arcade.draw_circle_filled(270 + x - 270, 210 + y - 210, 25, arcade.csscolor.DARK_GREEN)

def draw_sidewalk():
    """ Draw sidewalk """
    arcade.draw_lrtb_rectangle_filled(160, 240, 199, 100, arcade.csscolor.GREY)
    arcade.draw_triangle_filled(240, 100, 160, 100, 160, 20, arcade.csscolor.GREY)
    arcade.draw_lrtb_rectangle_filled(0, 160, 100, 20, arcade.csscolor.GREY)
    arcade.draw_triangle_filled(160, 100, 120, 100, 160, 140, arcade.csscolor.GREY)


def draw_tree(x, y):
    """ Draw Tree """
    arcade.draw_lrtb_rectangle_filled(400 + x - 425, 450 + x - 425, 450 + y - 250, 250 + y - 250, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(425 + x - 425, 450 + y - 250, 75, arcade.csscolor.DARK_GREEN)

def main():
    # Open Window
    arcade.open_window(screen_width, screen_height, "lab 3")

    # Set background color
    arcade.set_background_color(arcade.csscolor.BLUE)

    # Start Render
    arcade.start_render()

    draw_grass()
    draw_tree(40, 270)
    draw_tree(500, 285)
    draw_tree(320, 270)
    draw_tree(400, 250)
    draw_bush(328, 245)
    draw_bush(325, 275)
    draw_bush(72, 245)
    draw_bush(75, 275)
    draw_house()
    draw_sidewalk()
    draw_bush(290, 210)
    draw_bush(330, 210)
    draw_bush(250, 210)
    draw_bush(150, 210)
    draw_bush(110, 210)
    draw_bush(70, 210)
    draw_sun(600, 600)

    # Finish Render
    arcade.finish_render()

    # Keep window open
    arcade.run()


# Call main function
main()
