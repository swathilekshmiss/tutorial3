import turtle
def draw_radial_hexagons():
    for _ in range(10):
        for _ in range(6):
            turtle.forward(50)
            turtle.right(60)
        turtle.right(36)
    turtle.done()
