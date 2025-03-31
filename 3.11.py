import math
def find_quadrant(x, y):
    if math.isclose(x, 0) and math.isclose(y, 0):
        return "Origin"
    elif x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    elif math.isclose(x, 0) and y != 0:
        return "On Y-axis"
    elif x != 0 and math.isclose(y, 0):
        return "On X-axis"
x, y = 3, -4
print(f"The point ({x}, {y}) lies in {find_quadrant(x, y)}")
