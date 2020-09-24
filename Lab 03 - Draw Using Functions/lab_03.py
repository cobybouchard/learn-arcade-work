# Import arcade
import arcade

screen_width = 600
screen_height = 600


def draw_grass():
    """ Draw Grass """
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)


def draw_house():
    """ Draw House """
    arcade.draw_lrtb_rectangle_filled(100, 300, 400, 200, arcade.csscolor.BEIGE)
    arcade.draw_triangle_filled(75, 400, 325, 400, 200, 525, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(175, 225, 275, 200, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(215, 235, 5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(250, 350, 25, arcade.csscolor.LIGHT_BLUE)


def draw_bush(x, y):
    """ Draw Bush """
    arcade.draw_circle_filled(270 + x, 210 + y, 25, arcade.csscolor.DARK_GREEN)


def draw_sidewalk():
    """ Draw sidewalk """
    arcade.draw_lrtb_rectangle_filled(160, 240, 199, 100, arcade.csscolor.GREY)
    arcade.draw_triangle_filled(240, 100, 160, 100, 160, 20, arcade.csscolor.GREY)
    arcade.draw_lrtb_rectangle_filled(0, 160, 100, 20, arcade.csscolor.GREY)
    arcade.draw_triangle_filled(160, 100, 120, 100, 160, 140, arcade.csscolor.GREY)


def draw_tree(x, y):
    """ Draw Tree """
    arcade.draw_lrtb_rectangle_filled(400 + x, 450 + x, 450 + y, 250 + y, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(425 + x, 450 + y, 75, arcade.csscolor.DARK_GREEN)


def main():
    # Open Window
    arcade.open_window(screen_width, screen_height, "lab 3")

    # Set background color
    arcade.set_background_color(arcade.csscolor.BLUE)

    # Start Render
    arcade.start_render()

    draw_grass()
    draw_tree(-360, 20)
    draw_tree(100, 35)
    draw_tree(-80, 20)
    draw_tree(0, 0)
    draw_bush(58, 35)
    draw_bush(55, 65)
    draw_bush(-198, 35)
    draw_bush(-195, 65)
    draw_house()
    draw_sidewalk()
    draw_bush(20, 0)
    draw_bush(60, 0)
    draw_bush(-20, 0)
    draw_bush(-120, 0)
    draw_bush(-160, 0)
    draw_bush(-200, 0)


    # Finish Render
    arcade.finish_render()

    # Keep window open
    arcade.run()


# Call main function
main()
