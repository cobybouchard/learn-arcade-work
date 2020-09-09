# Import arcade
import arcade

# Open Window
arcade.open_window(600, 600, "lab 2")

# Set background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Start Render
arcade.start_render()

# Make Grass
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Make House
arcade.draw_lrtb_rectangle_filled(100, 300, 400, 200, arcade.csscolor.BEIGE)

# Make Roof
arcade.draw_triangle_filled(75, 400, 325, 400, 200, 525, arcade.csscolor.BLACK)

# Make Bush
arcade.draw_circle_filled(270, 210, 25, arcade.csscolor.FOREST_GREEN)

# Make Door
arcade.draw_lrtb_rectangle_filled(175, 225, 275, 200, arcade.csscolor.BROWN)

# Make Door Handle
arcade.draw_circle_filled(215, 235, 5, arcade.csscolor.BLACK)

# Make Window
arcade.draw_circle_filled(250, 350, 25, arcade.csscolor.LIGHT_BLUE)

# Sidewalk
arcade.draw_lrtb_rectangle_filled(160, 240, 199, 100, arcade.csscolor.GREY)

arcade.draw_triangle_filled(240, 100, 160, 100, 160, 20, arcade.csscolor.GREY)

arcade.draw_lrtb_rectangle_filled(0, 160, 100, 20, arcade.csscolor.GREY)

arcade.draw_triangle_filled(160, 100, 120, 100, 160, 140, arcade.csscolor.GREY)

# Draw a tree
arcade.draw_lrtb_rectangle_filled(400, 450, 450, 250, arcade.csscolor.BROWN)

arcade.draw_circle_filled(425, 450, 75, arcade.csscolor.FOREST_GREEN)

# Finish Render
arcade.finish_render()

# Keep window open
arcade.run()