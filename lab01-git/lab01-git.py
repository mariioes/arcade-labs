import arcade

WIDTH = 1000
HEIGHT = 800

arcade.open_window(WIDTH, HEIGHT, "Example")

arcade.start_render()
arcade.draw_text("Mario Esteban", 200, 200, arcade.color.WHITE)
arcade.finish_render()

arcade.run()