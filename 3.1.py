import turtle
def draw_star():
    star = turtle.Turtle()
    star.speed(3)
    for _ in range(5):
        star.forward(100)
        star.right(144)
    turtle.done()